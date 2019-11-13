from tqdm import tqdm
import argparse
import os
from os.path import join, isdir


parser = argparse.ArgumentParser()
parser.add_argument('--dataset_dir', type=str, help='dataset directory')
parser.add_argument('--dataset', type=str, choices=['BOP', 'Pascal3D', 'ShapeNet'], help='dataset format')
parser.add_argument('--input', type=str, help='subdirectory containing obj files in the dataset directory')
parser.add_argument('--filter', type=str, default='downsample.mlx', help='downsample filter used in meshlab')
args = parser.parse_args()

input_dir = join(args.dataset_dir, args.input)
output_dir = join(args.dataset_dir, 'mesh')

if args.dataset == 'BOP':
    model_files = sorted(os.listdir(input_dir))
    for model_file in tqdm(model_files):
        model_path = join(input_dir, model_file)
        example_dir = join(output_dir, model_file.split(".")[0])
        mesh_path = join(example_dir, 'compressed.obj')
        os.system('meshlabserver -i {} -o {} -s {}'.format(model_path, mesh_path, args.filter))

elif args.dataset in ['Pascal3D', 'ShapeNet']:
    categories = sorted(os.listdir(input_dir))
    for cat in tqdm(categories, desc='Generating point cloud for {}'.format(args.dataset)):
        cat_in = join(input_dir, cat)
        cat_out = join(output_dir, cat)
        model_files = sorted(os.listdir(cat_in))

        for model_file in tqdm(model_files, desc='Generating point cloud for {} class'.format(cat)):
            if args.dataset == 'Pascal3D':
                model_path = join(cat_in, model_file)
                model_name = model_file.split(".")[0]
            elif args.dataset == 'ShapeNet':
                model_path = join(cat_in, model_file, 'models', 'model_normalized.obj')
                model_name = model_file
            else:
                model_path = join(cat_in, model_file, 'model.obj')
                model_name = model_file

            example_dir = join(cat_out, model_name)
            if not isdir(example_dir):
                os.makedirs(example_dir)

            mesh_path = join(example_dir, 'compressed.obj')
            os.system('meshlabserver -i {} -o {} -s {}'.format(model_path, mesh_path, args.filter))
else:
    sys.exit(0)
