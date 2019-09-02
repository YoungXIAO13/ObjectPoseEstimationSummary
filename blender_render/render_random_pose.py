import os, sys
from os.path import join, dirname, basename, exists
import shutil
import bpy
from mathutils import Matrix, Vector
from PIL import Image
from math import radians, sin, cos
import numpy as np
import random
import json

cur_dir = dirname(os.path.abspath(__file__))
sys.path.append(cur_dir)
from image_utils import obtain_obj_center, one_mask_per_image, binary_mask
from render_utils import remove_obj_lamp_and_mesh, setup_env, make_lamp, render_without_output


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
                 model_files, out_dir, table_file='Platte.obj', texture_dir=None, bg_dir=None,
                 dim_min=50, dim_max=150, grid=100, rad=3000, clip_end=2000,
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
        self.depthFileOutput.base_path = join(out_dir, 'depth')
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

        self.scene.render.filepath = join(self.out_dir, '{:04d}_mask'.format(idx))
        self.depthFileOutput.file_slots[0].path = '{:04d}_depth_'.format(idx)
        render_without_output(use_antialiasing=False)

        # Render textured image and depth map
        for i in range(len(self.models)):
            model = self.models[i]['object_name']
            if model in R:
                add_texture_map(self.objs[model], self.textures[model])

        self.depthFileOutput.file_slots[0].path = '{:04d}_depth_'.format(idx)
        self.scene.render.filepath = join(self.out_dir, '{:04d}_image'.format(idx))
        render_without_output(use_antialiasing=True)

    def render_random_pose(self, annot, start_idx, scene_id, image_id, R, T, ele):
        """
        Render objects under random poses
        :param annot: annotation dictionary
        :param start_idx:
        :param scene_id:
        :param image_id:
        :param R:
        :param T:
        :param ele:
        :return: annotation, rgb, mask, mask_visib, depth
        """
        self.table.matrix_world = convert_pose_array_to_matrix(
            R, T + np.array([0, 200 * sin(radians(ele)), 200 * cos(radians(ele))])
        )
        self.table.scale = 6, 6, 6
        self.depthFileOutput.file_slots[0].path = '{:06d}_'.format(image_id)

        # Randomize the lamp energy
        self.lamp.data.energy = np.random.uniform(self.rad * 0.5, self.rad * 1.5) / 30

        # Render visible object masks
        Rotations, Translations, Scales = {}, {}, {}
        for i in range(len(self.models)):
            object = self.models[i]['object_name']
            R_model = rand_rotation()
            T_model = T + np.array(
                [self.offset[i % 5], sin(radians(ele)) * self.offset[i // 5], -cos(radians(ele)) * self.offset[i // 5]]
            )
            self.objs[object].matrix_world = convert_pose_array_to_matrix(R_model, T_model)
            add_color(self.objs[object], color=((i + 1) * 0.01, (i + 1) * 0.01, (i + 1) * 0.01), shadeless=True)
            scale = np.random.uniform(self.dim_min, self.dim_max) / max(self.objs[object].dimensions)
            self.objs[object].scale = scale, scale, scale
            Rotations[i], Translations[i], Scales[i] = R_model, T_model, scale

        add_color(self.table, color=(0, 0, 0), shadeless=True)
        self.scene.render.filepath = join(self.out_dir, 'mask_visib', '{:06d}'.format(image_id))
        render_without_output(use_antialiasing=False)
        bbox_visib, px_visib = one_mask_per_image(join(self.out_dir, 'mask_visib', '{:06d}.png'.format(image_id)),
                                                  image_id, len(self.models))

        # Render amodal object masks
        bbox_amodal, px_amodal, truncated = [], [], []
        self.table.hide_render = True
        for i in range(len(self.models)):
            object = self.models[i]['object_name']
            self.objs[object].hide_render = True
        for i in range(len(self.models)):
            object = self.models[i]['object_name']
            self.objs[object].hide_render = False
            self.scene.render.filepath = join(self.out_dir, 'mask', '{:06d}_{:06d}'.format(image_id, i))
            render_without_output(use_antialiasing=False)
            bbox, px, trunc = binary_mask(join(self.out_dir, 'mask', '{:06d}_{:06d}.png'.format(image_id, i)))
            bbox_amodal.append(bbox)
            px_amodal.append(px)
            truncated.append(trunc)
            self.objs[object].hide_render = True

        # Render textured image and depth map
        self.table.hide_render = False
        for i in range(len(self.models)):
            object = self.models[i]['object_name']
            self.objs[object].hide_render = False
        for i in range(len(self.models)):
            object = self.models[i]['object_name']
            add_texture_map(self.objs[object], join(self.texture_dir, random.choice(self.textures)))

            # Generate the sample annotation
            if px_amodal[i] == 0 or px_visib[0] == 0:
                continue
            sample_frame = {}
            sample_frame["scene_id"] = scene_id
            sample_frame["image_id"] = image_id
            sample_frame["instance_id"] = i

            sample_frame["model_name"] = self.models[i]['model_name']
            sample_frame["scale"] = Scales[i]
            sample_frame["cam_R_m2c"] = list(Rotations[i].reshape(-1))
            sample_frame["cam_t_m2c"] = list(Translations[i])
            cx, cy, inside = obtain_obj_center(Translations[i], self.fx, self.fy, self.cx, self.cy, self.height,
                                               self.width)
            sample_frame["obj_center"] = [cx, cy]
            sample_frame["inside"] = inside
            sample_frame["truncated"] = truncated[i]
            sample_frame["bbox_obj"] = bbox_amodal[i]
            sample_frame["bbox_visib"] = bbox_visib[i]
            sample_frame["px_count_visib"] = px_visib[i]
            sample_frame["visib_fract"] = px_visib[i] / px_amodal[i]
            annot['{}'.format(start_idx + i)] = sample_frame

        add_texture_map(self.table, join(self.bg_dir, random.choice(self.bg_imgs)))
        self.scene.render.filepath = join(self.out_dir, 'rgb', '{:06d}'.format(image_id))
        render_without_output(use_antialiasing=True)

        # rename depth image
        shutil.move(join(self.depthFileOutput.base_path, '{:06d}_0001.exr'.format(image_id)),
                    join(self.depthFileOutput.base_path, '{:06d}.exr'.format(image_id)))


if __name__ == '__main__':
    import pandas as pd
    # input and output directory
    dataset_dir = '/home/xiao/Datasets/ABC'
    model_dir = join(dataset_dir, 'abc_0000')
    out_dir = join(dataset_dir, 'train_0000')
    scene_id = len(os.listdir(out_dir))
    out_dir = join(out_dir, '{:06d}'.format(scene_id))
    images_per_scene = 100

    # textures and backgrounds directory
    texture_dir = join(dirname(os.path.realpath(__file__)), 'textures')
    bg_dir = '/home/xiao/Datasets/PascalVOC/VOCdevkit/VOC2012/Images/JPEGImages'

    # TODO: consider mutilple instances of the same shape
    df = pd.read_csv(join(dataset_dir, 'abc_0000.txt'))
    df = df[df.ratio_max <= 5]
    df = df[df.ratio_min >= 0.2]
    model_number = np.random.randint(5, 25)
    idx = np.random.randint(0, len(df), size=(model_number,))
    model_files = [join(model_dir, '{}.obj'.format(df.iloc[i, 0])) for i in idx]

    render_machine = RenderMachine(model_files, out_dir, texture_dir=texture_dir, bg_dir=bg_dir, rad=3000)

    # Load table poses from the LINEMOD-OCCLUSION dataset
    table_poses = np.load('table_poses.npz')
    R = table_poses['R']
    T = table_poses['T']
    Ele = table_poses['Ele']
    idx = np.random.randint(0, R.shape[0], size=(images_per_scene,))

    # Read in annotation json file
    annotation_file = join(out_dir, 'scene_gt.json')
    annot = json.load(open(annotation_file)) if exists(annotation_file) else {}

    for i in range(len(idx)):
        start_idx = len(annot)
        render_machine.render_random_pose(annot, start_idx, scene_id, i, R[idx[i], :], T[idx[i], :], Ele[idx[i]])

    with open(annotation_file, 'w') as f:
        json.dump(annot, f, indent=4)

    os.system('rm blender_render.log')
