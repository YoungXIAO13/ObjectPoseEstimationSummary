import os
from os.path import join, getsize
from PIL import Image
from tqdm import tqdm
import numpy as np


obj_dir = 'abc_0000'
view_dir = 'multiviews'
model_names = sorted(os.listdir(view_dir))

csv_file = 'abc_0000.txt'
with open(csv_file, 'w') as f:
    f.write('model_name,size,ratio_min,ratio_max\n')

for model_name in tqdm(model_names):
    size = int(os.path.getsize(join(obj_dir, '{}.obj'.format(model_name))) / (2 ** 20))
    img_dir = join(view_dir, model_name, 'nocs')
    images = os.listdir(img_dir)
    ratio = []
    for img in images:
        try:
            left, upper, right, lower = Image.open(join(img_dir, img)).getbbox()
            ratio.append((lower - upper) / (right - left))
        except TypeError:
            ratio.append(0)
    with open(csv_file, 'a') as f:
        f.write(model_name + ',' + str(size) + ',' + str(np.min(ratio)) + ',' + str(np.max(ratio)) + '\n')
