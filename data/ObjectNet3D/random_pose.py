import os
from os.path import join, realpath, exists
import random
import pandas as pd
import numpy as np
from tqdm import tqdm
import json
import argparse
import sys

sys.path.append('../..')
from blender_render.render_random_pose import RenderMachine


cats = ['aeroplane', 'ashtray', 'backpack', 'basket', 'bed', 'bench', 'bicycle', 'blackboard', 'boat', 'bottle', 'bus',
        'cabinet', 'camera', 'can', 'cap', 'car', 'chair', 'coffee_maker', 'cup', 'desk_lamp', 'diningtable',
        'eyeglasses', 'fan', 'faucet', 'fire_extinguisher', 'flashlight', 'guitar', 'hair_dryer', 'headphone', 'helmet',
        'iron', 'kettle', 'microphone', 'motorbike', 'mouse', 'piano', 'pot', 'rifle', 'satellite_dish', 'shoe',
        'skate', 'skateboard', 'slipper', 'sofa', 'stapler', 'teapot', 'toilet', 'trophy', 'tub', 'wheelchair']

parser = argparse.ArgumentParser()
parser.add_argument('--dataset_dir', type=str, help='dataset directory')
parser.add_argument('--input', type=str, help='subdirectory containing obj files in the dataset directory')
parser.add_argument('--output', type=str, help='subdirectory to save the generated data in the dataset directory')
parser.add_argument('--bg_dir', type=str, default='/home/xiao/Datasets/SUN',
                    help='directory containing the background images')
parser.add_argument('--images_per_scene', type=int, default=100, help='images generated for each scene')
parser.add_argument('--scenes', type=int, default=100, help='number of scenes to generate')
args = parser.parse_args()

# set related directories
model_dir = join(args.dataset_dir, args.input)
out_dir = join(args.dataset_dir, args.output)

root_dir = realpath('../..')
texture_dir = join(root_dir, 'blender_render', 'textures')
table_file = join(root_dir, 'blender_render', 'Platte.obj')
table_poses = np.load(join(root_dir, 'blender_render', 'table_poses.npz'))
R, T, Ele = table_poses['R'], table_poses['T'], table_poses['Ele']
with open(join(args.bg_dir, 'ClassName.txt'), "r") as f:
    bg_cats = f.read().splitlines()


# create the final csv file containing all the annotations
outfile = join(args.dataset_dir, '{}.txt'.format(args.output))
frames = []

for scene_id in range(args.scenes):
    scene_out = join(out_dir, '{:06d}'.format(scene_id))
    scene_file = join(scene_out, 'scene_gt.json')

    # randomly select a category in SUN397 for each scene
    bg_dir = join(args.bg_dir, 'SUN397_256', random.choice(bg_cats)[1:])

    # randomly select some categories in ObjectNet3D for each scene
    scene_cats = random.sample(cats, np.random.randint(5, 25))
    model_files = [join(model_dir, cat, random.choice(os.listdir(join(model_dir, cat)))) for cat in scene_cats]
    
    if not exists(scene_file):
        # Create one render machine for each scene
        render_machine = RenderMachine(model_files, scene_out, table_file=table_file, texture_dir=texture_dir,
                                       bg_dir=bg_dir, dim_min=100, dim_max=200, category=True)

        scene_annot = {}
        pose_idx = np.random.randint(0, R.shape[0], size=(args.images_per_scene,))
        for i in range(args.images_per_scene):
            start_idx = len(scene_annot)
            render_machine.render_random_pose(scene_annot, start_idx, scene_id, i,
                                              R[pose_idx[i], :], T[pose_idx[i], :], Ele[pose_idx[i]])

        with open(scene_file, 'w') as f:
            json.dump(scene_annot, f, indent=4)
    scene_df = pd.read_json(scene_file, orient='index')
    frames.append(scene_df)

result = pd.concat(frames)
result.to_csv(outfile)
