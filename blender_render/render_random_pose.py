import os, sys
import bpy
from mathutils import Matrix, Vector
from PIL import Image
from math import radians, sin, cos
import numpy as np
import random
import json
import ipdb

cur_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(cur_dir)
from annotation_utils import obtain_obj_region, obtain_obj_center
from render_utils import *


# Transform the R and T from numpy array to Matrix
def convert_pose_array_to_matrix(R, T):
    mat = Matrix(R.reshape(3, 3)).to_4x4()
    mat.col[3][:3] = T
    return mat


# Setup the camera
def setup_camera(scene, fx=572, fy=574, cx=325, cy=242):
    cam = scene.objects['Camera']
    width = scene.render.resolution_x
    height = scene.render.resolution_y
    cam.data.sensor_height = cam.data.sensor_width * height / width
    cam.data.lens = (fx + fy) / 2 * cam.data.sensor_width / width
    cam.data.shift_x = (width / 2 - cx) / width
    cam.data.shift_y = (cy - height / 2) / width
    # change to OpenCV camera coordinate system
    cam.matrix_world = Matrix(((1.0, 0.0, 0.0, 0.0),
                               (0.0, -1.0, 0.0, 0.0),
                               (0.0, 0.0, -1.0, 0.0),
                               (0.0, 0.0, 0.0, 1.0)))
    return cam


# Add material to object
def add_color(obj, color=(1., 0., 0.), shadeless=True):
    mat = bpy.data.materials.new(name='Material')
    mat.use_shadeless = shadeless
    mat.diffuse_color = color
    if obj.data.materials:
        obj.data.materials[0] = mat
    else:
        obj.data.materials.append(mat)


# Add texture map to object
def add_texture_map(obj, texture_img):
    mat = bpy.data.materials.new(name='Material')
    tex = bpy.data.textures.new('UVMapping', 'IMAGE')
    tex.image = bpy.data.images.load(texture_img)
    slot = mat.texture_slots.add()
    slot.texture = tex
    if obj.data.materials:
        obj.data.materials[0] = mat
    else:
        obj.data.materials.append(mat)


# Import 3D models from .obj files
def import_models(model_files, use_defalut_texture=False):
    models = {}
    textures = {}
    repeat_count = {}
    for i in range(len(model_files)):
        models[i] = {}
        model_file = model_files[i]
        bpy.ops.import_scene.obj(filepath=model_file)
        model_name = model_file.split('/')[-1].split('.')[0]
        models[i]['model_name'] = model_name

        if model_name not in repeat_count.keys():
            repeat_count[model_name] = 0
        else:
            repeat_count[model_name] += 1

        models[i]['object_name'] = model_name if repeat_count[model_name] == 0 else '{}.{:03d}'.format(model_name, repeat_count[model_name])

        if use_defalut_texture:
            textures[model_name] = model_file.replace('.obj', '.png')
    return models, textures


# Create random rotation matrix
def rand_rotation():
    # from http://www.realtimerendering.com/resources/GraphicsGems/gemsiii/rand_rotation.c

    theta, phi, z = np.random.uniform(size=(3,))
    theta = theta * 2.0 * np.pi  # Rotation about the pole (Z).
    phi = phi * 2.0 * np.pi  # For direction of pole deflection.
    z = z * 2.0  # For magnitude of pole deflection.

    # Compute a vector V used for distributing points over the sphere
    # via the reflection I - V Transpose(V).  This formulation of V
    # will guarantee that if x[1] and x[2] are uniformly distributed,
    # the reflected points will be uniform on the sphere.  Note that V
    # has length sqrt(2) to eliminate the 2 in the Householder matrix.

    r = np.sqrt(z)
    V = (
        np.sin(phi) * r,
        np.cos(phi) * r,
        np.sqrt(2.0 - z)
    )

    st = np.sin(theta)
    ct = np.cos(theta)

    R = np.array(((ct, st, 0), (-st, ct, 0), (0, 0, 1)))

    # Construct the rotation matrix  ( V Transpose(V) - I ) R.

    M = (np.outer(V, V) - np.eye(3)).dot(R)
    return M


class RenderMachine:
    """Creates a python blender render machine.

    model_files: a list containing all the obj files
    out_dir: where to save the render results
    table_file: 3D model of the table on which all objects could be placed
    hide_table: use the table model only when this arg is False
    texture_dir: directory containing the texture map images
    bg_dir: directory containing the background images
    dim_min: the minimum model dimension in mm
    dim_max: the maximum model dimension in mm
    grid: the distance between object models on the table
    rad: lamp radiance to adjust the lightness
    clip_end: rendering range in mm
    """
    def __init__(self,
                 model_files, out_dir, table_file='Platte.obj', hide_table=False, texture_dir=None, bg_dir=None,
                 dim_min=50, dim_max=150, grid=150, rad=3000, clip_end=2000,
                 fx=572, fy=574, cx=325, cy=242, height=480, width=640):
        # Setting up the environment
        remove_obj_lamp_and_mesh(bpy.context)
        self.scene = bpy.context.scene
        self.objs = bpy.data.objects
        self.depthFileOutput = setup_env(self.scene, True, False, height, width, clip_end)
        self.camera = setup_camera(self.scene, fx, fy, cx, cy)
        self.lamp = make_lamp(rad)
        self.rad = rad
        self.height, self.width = height, width
        self.fx, self.fy, self.cx, self.cy = fx, fy, cx, cy

        # Import table model and align it with camera frame
        bpy.ops.import_scene.obj(filepath=table_file)
        self.table = bpy.data.objects[table_file.split('.')[0]]
        self.offset = [0, -grid, grid, -2 * grid, 2 * grid, -3 * grid, 3 * grid]
        self.hide_table = hide_table

        # Import 3D models and register dimension range
        model_files = random.choices(model_files, k=30) if len(model_files) > 30 else model_files
        self.models, self.textures = import_models(model_files)
        self.dim_min, self.dim_max = dim_min, dim_max

        # Read texture maps and the background images
        self.texture_dir = texture_dir
        self.textures = os.listdir(texture_dir)
        self.bg_dir = bg_dir
        self.bg_imgs = os.listdir(bg_dir)

        # Output setting
        self.out_dir = out_dir
        self.scene.render.image_settings.file_format = 'PNG'
        self.depthFileOutput.base_path = out_dir
        self.depthFileOutput.format.file_format = 'OPEN_EXR'

    # TODO: to modify in order to be complied with T-LESS where multiple objects are present
    def render_pose_from_annotation(self, idx, R, T):
        self.table.hide_render = True

        # Render object masks
        for i in range(len(self.models)):
            model = self.models[i]['object_name']
            if model in R:
                self.objs[model].hide_render = False
                self.objs[model].matrix_world = convert_pose_array_to_matrix(R[model], T[model])
                add_color(self.objs[model], color=((i + 1) * 0.01, (i + 1) * 0.01, (i + 1) * 0.01), shadeless=True)
            else:
                self.objs[model].hide_render = True

        self.scene.render.filepath = os.path.join(self.out_dir, '{:04d}_mask'.format(idx))
        self.depthFileOutput.file_slots[0].path = '{:04d}_depth_'.format(idx)
        render_without_output(use_antialiasing=False)

        # Render textured image and depth map
        for i in range(len(self.models)):
            model = self.models[i]['object_name']
            if model in R:
                add_texture_map(self.objs[model], self.textures[model])

        self.depthFileOutput.file_slots[0].path = '{:04d}_depth_'.format(idx)
        self.scene.render.filepath = os.path.join(self.out_dir, '{:04d}_image'.format(idx))
        render_without_output(use_antialiasing=True)

    def render_random_pose(self, annot, start_idx, scene_id, image_id, R, T, ele):
        self.table.matrix_world = convert_pose_array_to_matrix(
            R, T + np.array([0, 200 * sin(radians(ele)), 200 * cos(radians(ele))])
        )
        self.table.scale = 6, 6, 6
        self.table.hide_render = self.hide_table

        # Randomize the lamp energy
        self.lamp.data.energy = np.random.uniform(self.rad * 0.5, self.rad * 1.5) / 30

        Rotations, Translations, Scales = {}, {}, {}
        # Render object masks
        for i in range(len(self.models)):
            model = self.models[i]['object_name']
            R_model = rand_rotation()
            T_model = T + np.array(
                [self.offset[i % 5], sin(radians(ele)) * self.offset[i // 5], -cos(radians(ele)) * self.offset[i // 5]]
            )
            self.objs[model].matrix_world = convert_pose_array_to_matrix(R_model, T_model)
            add_color(self.objs[model], color=((i + 1) * 0.01, (i + 1) * 0.01, (i + 1) * 0.01), shadeless=True)
            scale = np.random.uniform(self.dim_min, self.dim_max) / max(self.objs[model].dimensions)
            self.objs[model].scale = scale, scale, scale
            Rotations[i], Translations[i], Scales[i] = R_model, T_model, scale

        add_color(self.table, color=(0, 0, 0), shadeless=True)
        self.scene.render.filepath = os.path.join(self.out_dir, '{:04d}_mask'.format(image_id))
        self.depthFileOutput.file_slots[0].path = '{:04d}_depth_'.format(image_id)
        render_without_output(use_antialiasing=False)

        # Save mask as uint8 image
        mask = Image.open(os.path.join(self.out_dir, '{:04d}_mask.png'.format(image_id))).convert('L')
        mask.save(os.path.join(self.out_dir, '{:04d}_mask.png'.format(image_id)))

        # Render textured image and depth map
        for i in range(len(self.models)):
            model = self.models[i]['object_name']
            add_texture_map(self.objs[model], os.path.join(self.texture_dir, random.choice(self.textures)))
            # Generate the sample annotation
            sample_frame = {}
            sample_frame["scene_id"] = scene_id
            sample_frame["image_id"] = image_id
            sample_frame["obj_id"] = i

            sample_frame["model_path"] = self.models[i]['model_name']
            sample_frame["scale"] = Scales[i]
            sample_frame["cam_R_m2c"] = list(Rotations[i].reshape(-1))
            sample_frame["cam_t_m2c"] = list(Translations[i])
            cx, cy, outside = obtain_obj_center(Translations[i], self.fx, self.fy, self.cx, self.cy, self.height, self.width)
            sample_frame["obj_center"] = [cx, cy]
            sample_frame["obj_outside"] = outside
            bbox, px_visib, occupy_fract = obtain_obj_region(os.path.join(self.out_dir, '{:04d}_mask.png'.format(image_id)), i)
            sample_frame["bbox"] = bbox
            sample_frame["px_visib"] = px_visib
            sample_frame["occupy_fract"] = occupy_fract
            annot['{}'.format(start_idx + i)] = sample_frame

        add_texture_map(self.table, os.path.join(self.bg_dir, random.choice(self.bg_imgs)))
        self.scene.render.filepath = os.path.join(self.out_dir, '{:04d}_image'.format(image_id))
        render_without_output(use_antialiasing=True)


if __name__ == '__main__':
    # input and output directory
    model_dir = '/media/xiao/newhd/XiaoDatasets/ABC/abc_0000'
    out_dir = '/media/xiao/newhd/XiaoDatasets/ABC/synthetic_data_0000'
    scene_id = len(os.listdir(out_dir))
    out_dir = os.path.join(out_dir, '{:06d}'.format(scene_id))
    images_per_scene = 100

    # textures and backgrounds directory
    texture_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'textures')
    bg_dir = '/media/xiao/newhd/XiaoDatasets/PascalVOC/VOC2012/JPEGImages'

    # TODO: consider mutilple instances of the same shape
    model_files = [name for name in os.listdir(model_dir) if os.path.getsize(os.path.join(model_dir, name)) / (2 ** 20) < 10]
    model_number = np.random.randint(5, 25)
    model_files = random.choices(model_files, k=model_number)
    model_files = [os.path.join(model_dir, name) for name in model_files]

    render_machine = RenderMachine(model_files, out_dir, texture_dir=texture_dir, bg_dir=bg_dir, rad=3000)

    # Load table poses from the LINEMOD-OCCLUSION dataset
    table_poses = np.load('table_poses.npz')
    R = table_poses['R']
    T = table_poses['T']
    Ele = table_poses['Ele']
    idx = np.random.randint(0, R.shape[0], size=(images_per_scene,))

    # Read in annotation json file
    annotation_file = '/media/xiao/newhd/XiaoDatasets/ABC/annotation_0000.json'
    if os.path.isfile(annotation_file):
        annot = json.load(open(annotation_file))
        start_idx = len(annot)
    else:
        annot = {}
        start_idx = 0

    for i in range(len(idx)):
        render_machine.render_random_pose(
            annot, start_idx + i * model_number, scene_id, i, R[idx[i], :], T[idx[i], :], Ele[idx[i]])

    with open(annotation_file, 'w') as f:
        json.dump(annot, f, indent=4)

    os.system('rm blender_render.log')

    # model_dir = '/media/xiao/newhd/XiaoDatasets/LineMod/models_obj'
    # model_files = [os.path.join(model_dir, name) for name in os.listdir(model_dir) if name.endswith(".obj")]
    # out_dir = '/media/xiao/newhd/XiaoDatasets/LineMod/render_test'
    #
    # R, T = {}, {}
    # R['01'] = np.array([0.79796083, 0.60237870, -0.02630684, 0.38035542, -0.53676251, -0.75330230, -0.46784284, 0.59102839, -0.65733923])
    # T['01'] = np.array([183.63633301, -131.49685045, 1147.30061109])
    # R['02'] = np.array([-0.06894210, 0.99749202, -0.01604350, 0.69675398, 0.03663440, -0.71637398, -0.71398997, -0.06056670, -0.69753200])
    # T['02'] = np.array([16.07958566, -104.70886953, 1030.66843587])
    # R['05'] = np.array([0.89421800, 0.44575600, -0.04179340, 0.29321500, -0.65362400, -0.69775200, -0.33833500, 0.61166600, -0.71515800])
    # T['05'] = np.array([127.17500000, -25.73520000, 963.62800000])
    # R['06'] = np.array([0.43767701, -0.87971467, -0.18618649, -0.80190140, -0.28815846, -0.52350261, 0.40687085, 0.37841553, -0.83149655])
    # T['06'] = np.array([171.35228541, -296.82250528, 1308.65669015])
    # R['08'] = np.array([0.29412883, 0.95668816, -0.01349529, 0.67531949, -0.21756661, -0.70606017, -0.67776532, 0.19826147, -0.70939544])
    # T['08'] = np.array([117.81909817, -138.15322076, 1069.60944685])
    # R['09'] = np.array([-0.92941300, -0.36763500, -0.03276400, -0.24574300, 0.68259900, -0.68826000, 0.27538900, -0.63161500, -0.72474700])
    # T['09'] = np.array([50.68630000, 55.12450000, 963.16400000])
    # R['10'] = np.array([-0.16336268, 0.98598792, 0.03377058, 0.71096248, 0.14138866, -0.68887090, -0.68399406, -0.08852691, -0.72409719])
    # T['10'] = np.array([410.59555153, -135.18710539, 1175.12857344])
    # R['11'] = np.array([0.09409818, 0.99560544, 0.01487168, 0.67635234, -0.05295173, -0.73480894, -0.73071022, 0.07918466, -0.67822741])
    # T['11'] = np.array([20.06463127, -185.24679628, 1157.90564027])
    # R['12'] = np.array([-0.58295700, 0.81247100, -0.00921610, 0.60303800, 0.42503300, -0.67507200, -0.54454800, -0.39908800, -0.73771500])
    # T['12'] = np.array([-73.78200000, 30.04900000, 993.20500000])
    #
    # render_machine = RenderMachine(model_files, out_dir)
    # render_machine.render_pose_from_annotation(0, R, T)
