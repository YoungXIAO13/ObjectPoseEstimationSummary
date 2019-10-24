from tqdm import tqdm
import argparse
import os
from os.path import join, isdir, basename, dirname, exists
import shutil
import pymesh
import numpy as np


def sample_point_cloud_from_obj(virtualscanner, obj, out):
    """
    :param virtualscanner: executable path of virtual scanner
    :param obj: obj file path
    :param out: output directory
    :return: destination path to save the generated point cloud
    """
    ply_dest = join(out, 'sampled.ply')
    if exists(ply_dest):
        return ply_dest
    command = '{} {} 10'.format(virtualscanner, obj)
    os.system(command)
    ply = obj.replace('.obj', '.ply')
    shutil.move(ply, ply_dest)
    return ply_dest


def downsample_pointcloud(pc_path, point_num):
    mesh_raw = pymesh.load_mesh(pc_path)
    points_raw = mesh_raw.vertices
    if points_raw.shape[0] > point_num:
        point_subset = np.random.choice(points_raw.shape[0], point_num, replace=False)
        points = points_raw[point_subset]
    else:
        points = points_raw
    mesh = pymesh.form_mesh(points, np.ones((0, 3)))
    pymesh.save_mesh(join(dirname(pc_path), 'compressed.ply'), mesh)


parser = argparse.ArgumentParser()
parser.add_argument('--dataset_dir', type=str, help='dataset directory')
parser.add_argument('--dataset_format', type=str, choices=['BOP', 'Pascal3D', 'ShapeNet'], help='dataset format')
parser.add_argument('--input', type=str, help='subdirectory containing obj files in the dataset directory')
parser.add_argument('--virtualscanner', type=str, help='executable path of virtual scanner')
parser.add_argument('--downsample', type=int, default=5000, help='downsampled points')
args = parser.parse_args()

input_dir = join(args.dataset_dir, args.input)
output_dir = join(args.dataset_dir, 'pointcloud')

if args.dataset_format == 'BOP':
    model_files = sorted(os.listdir(input_dir))
    for model_file in tqdm(model_files):
        model_path = join(input_dir, model_file)
        example_dir = join(output_dir, model_file.split(".")[0])
        if not isdir(example_dir):
            os.makedirs(example_dir)
        ply_path = sample_point_cloud_from_obj(args.virtualscanner, model_path, example_dir)
        downsample_pointcloud(ply_path, args.downsample)

elif args.dataset_format in ['Pascal3D', 'ShapeNet']:
    categories = sorted(os.listdir(input_dir))
    for cat in tqdm(categories):
        cat_in = join(input_dir, cat)
        cat_out = join(output_dir, cat)
        model_files = sorted(os.listdir(cat_in))
        if len(model_files) > 200:
            model_files = model_files[:200]
        for model_file in tqdm(model_files):
            if args.dataset_format == 'Pascal3D':
                model_path = join(cat_in, model_file)
                model_name = model_file.split(".")[0]
            else:
                model_path = join(cat_in, model_file, 'models', 'model_normalized.obj')
                model_name = model_file

            example_dir = join(cat_out, model_name)
            if not isdir(example_dir):
                os.makedirs(example_dir)

            ply_path = sample_point_cloud_from_obj(args.virtualscanner, model_path, example_dir)
            downsample_pointcloud(ply_path, args.downsample)
else:
    sys.exit(0)
