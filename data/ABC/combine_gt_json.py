import os
from os.path import join
import pandas as pd
import json
import argparse
from tqdm import tqdm


parser = argparse.ArgumentParser()
parser.add_argument('--dataset_dir', type=str, help='dataset directory')
parser.add_argument('--train_data', type=str, help='subdirectory containing train data in the dataset directory')
args = parser.parse_args()

scenes = sorted(os.listdir(join(args.dataset_dir, args.train_data)))
outfile = join(args.dataset_dir, '{}.txt'.format(args.train_data))

frames = []
for scene in tqdm(scenes):
    df = pd.read_json(join(args.dataset_dir, args.train_data, scene, 'scene_gt.json'), orient='index')
    frames.append(df)
result = pd.concat(frames)
result.to_csv(outfile)
