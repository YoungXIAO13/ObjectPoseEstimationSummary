import os, sys
import bpy
from mathutils import Matrix, Vector
import numpy as np
import random
import json
import ipdb

cur_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(cur_dir)
from render_utils import *
from annotation_utils import *


# Define pose grid for 20 vertex on the regular dodecahedron
phi = (1. + np.sqrt(5) / 2)
dodecahedron_vertex_coord = np.array(
    [[-1, -1, -1], [-1, -1, 1], [-1, 1, -1], [-1, 1, 1],
     [1, -1, -1], [1, -1, 1], [1, 1, -1], [1, 1, 1],
     [0, -phi, -1/phi], [0, -phi, 1/phi], [0, phi, -1/phi], [0, phi, 1/phi],
     [-1/phi, 0, -phi], [-1/phi, 0, phi], [1/phi, 0, -phi], [1/phi, 0, phi],
     [-phi, -1/phi, 0], [-phi, 1/phi, 0], [phi, -1/phi, 0], [phi, 1/phi, 0]]
)


# Add constraint to the camera
def parent_obj_to_camera(b_camera):
    # set the parenting to the origin
    origin = (0, 0, 0)
    b_empty = bpy.data.objects.new("Empty", None)
    b_empty.location = origin
    b_camera.parent = b_empty

    scn = bpy.context.scene
    scn.objects.link(b_empty)
    scn.objects.active = b_empty
    return b_empty


# Setup the camera
def setup_camera(scene):
    cam = scene.objects['Camera']
    cam_constraint = cam.constraints.new(type='TRACK_TO')
    cam_constraint.track_axis = 'TRACK_NEGATIVE_Z'
    cam_constraint.up_axis = 'UP_Y'
    b_empty = parent_obj_to_camera(cam)
    cam_constraint.target = b_empty
    return cam


# Import 3D model from .obj files
def import_model(model_file, axis_forward=None, axis_up=None):
    if axis_forward is not None and axis_up is not None:
        bpy.ops.import_scene.obj(filepath=model_file, axis_forward=axis_forward, axis_up=axis_up)
    else:
        bpy.ops.import_scene.obj(filepath=model_file)
    model_name = model_file.split('/')[-1].split('.')[0]
    return model_name


# Normalize the 3D model
def normalize_model(obj):
    bpy.context.scene.objects.active = obj
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')
    obj.location = (0, 0, 0)
    max_dim = max(obj.dimensions)
    obj.dimensions = obj.dimensions / max_dim


# Create normalized coordinate map as a color map
def create_coord_map(obj):
    mesh = obj.data
    vert_list = mesh.vertices
    vcos = [obj.matrix_world * v.co for v in vert_list]
    x, y, z = [[v[i] for v in vcos] for i in range(3)]
    min_x, min_y, min_z = min(x), min(y), min(z)
    size_x, size_y, size_z = max(x) - min(x), max(y) - min(y), max(z) - min(z)

    # get the color map to create as coordinate map
    if mesh.vertex_colors:
        color_map = mesh.vertex_colors.active
    else:
        color_map = mesh.vertex_colors.new()

    # apply the corresponding color to each vertex
    i = 0
    for poly in mesh.polygons:
        for idx in poly.loop_indices:
            loop = mesh.loops[idx]
            v = vert_list[loop.vertex_index]
            r = (v.co.x - min_x) / size_x if size_x != 0 else 1
            g = (v.co.y - min_y) / size_y if size_y != 0 else 1
            b = (v.co.z - min_z) / size_z if size_z != 0 else 1
            color_map.data[i].color = (r, g, b)
            i += 1

    mat = bpy.data.materials.new('vertex_material')
    mat.use_shadeless = True
    mat.use_vertex_color_paint = True
    if mesh.materials:
        mesh.materials[0] = mat
    else:
        mesh.materials.append(mat)


class RenderMachine:
    """Creates a python blender render machine.

    model_files: a list containing all the obj files
    out_dir: where to save the render results
    rad: lamp radiance to adjust the lightness
    clip_end: rendering range in mm
    """
    def __init__(self,
                 model_file, out_dir, rad=3000, clip_end=100, height=128, width=128):
        # Setting up the environment
        remove_obj_lamp_and_mesh(bpy.context)
        self.scene = bpy.context.scene
        self.depthFileOutput, self.normalFileOutput = setup_env(self.scene, True, True, height, width, clip_end)
        self.camera = setup_camera(self.scene)
        self.lamp = make_lamp(rad)
        self.height, self.width = height, width

        # Import 3D models and create the normalized object coordinate space as material
        self.model = import_model(model_file, axis_forward='Y', axis_up='Z')
        normalize_model(bpy.data.objects[self.model])
        create_coord_map(bpy.data.objects[self.model])

        # Output setting
        self.out_dir = os.path.join(out_dir, self.model, 'nocs')
        self.depthFileOutput.base_path = os.path.join(out_dir, self.model, 'depth')
        self.normalFileOutput.base_path = os.path.join(out_dir, self.model, 'normal')
        self.scene.render.image_settings.file_format = 'PNG'
        # self.depthFileOutput.format.file_format = 'OPEN_EXR'

    def render_grid_pose(self, pose_grid):
        for i in range(pose_grid.shape[0]):
            self.camera.location = pose_grid[i]
            self.lamp.location = pose_grid[i]

            self.scene.render.filepath = os.path.join(self.out_dir, '{:04d}'.format(i))
            self.depthFileOutput.file_slots[0].path = '{:04d}_'.format(i)
            self.normalFileOutput.file_slots[0].path = '{:04d}_'.format(i)
            render_without_output(use_antialiasing=True)

            # Crop and resize the rendering results
            img_path = '{}.png'.format(self.scene.render.filepath)
            depth_path = os.path.join(self.depthFileOutput.base_path, '{:04d}_0001.png'.format(i))
            normal_path = os.path.join(self.normalFileOutput.base_path, '{:04d}_0001.png'.format(i))
            clean_rendering_results(img_path, depth_path, normal_path)


if __name__ == '__main__':
    dataset_dir = '/media/xiao/newhd/XiaoDatasets/ABC'
    model_dir = os.path.join(dataset_dir, 'abc_0000_obj_v00')
    out_dir = os.path.join(dataset_dir, 'multiviews')
    model_files = [name for name in os.listdir(model_dir) if
                   os.path.getsize(os.path.join(model_dir, name)) / (2 ** 20) < 10]

    # dataset_dir = '/media/xiao/newhd/XiaoDatasets/LINEMOD-Occlusion'
    # model_dir = os.path.join(dataset_dir, 'models_obj')
    # out_dir = os.path.join(dataset_dir, 'multiviews')
    # model_files = os.listdir(model_dir)

    model_files.sort()

    for model_file in model_files:
        model_path = os.path.join(model_dir, model_file)
        model_name = model_file.split(".")[0]

        if os.path.isdir(os.path.join(out_dir, model_name)):
            continue

        render_machine = RenderMachine(model_path, out_dir, rad=30, height=224, width=224)
        render_machine.render_grid_pose(dodecahedron_vertex_coord)

    os.system('rm blender_render.log')
