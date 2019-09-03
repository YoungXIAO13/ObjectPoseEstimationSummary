import os
from os.path import join, getsize
from PIL import Image
from tqdm import tqdm
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--dataset_dir', type=str, help='dataset directory')
parser.add_argument('--model', type=str, default='abc_0000', help='subdirectory containing obj files')
parser.add_argument('--views', type=str, default='multiviews', help='subdirectory containing multiviews')
args = parser.parse_args()

obj_dir = join(args.dataset_dir, args.model)
view_dir = join(args.dataset_dir, args.views)
model_names = sorted(os.listdir(view_dir))

csv_file = join(args.dataset_dir, '{}.txt'.format(args.model))
with open(csv_file, 'w') as f:
    f.write('model_name,size,ratio_min,ratio_max,occupy_min,occupy_max\n')

for model_name in tqdm(model_names):
    size = int(getsize(join(obj_dir, '{}.obj'.format(model_name))) / (2 ** 20))
    img_dir = join(view_dir, model_name, 'nocs')
    images = os.listdir(img_dir)
    ratio = []
    occupy = []
    for img in images:
        try:
            rgb = Image.open(join(img_dir, img))
            w, h = rgb.size
            left, upper, right, lower = rgb.getbbox()
            ratio.append((lower - upper) / (right - left))
            occupy.append(np.sum(np.array(rgb.convert('L')) != 0) / (w * h))
        except TypeError:
            ratio.append(0)
            occupy.append(0)
    with open(csv_file, 'a') as f:
        f.write(model_name + ',' + str(size) + ',' + str(np.min(ratio)) + ',' + str(np.max(ratio)) + ',' +
                str(np.min(occupy)) + ',' + str(np.max(occupy)) + '\n')
