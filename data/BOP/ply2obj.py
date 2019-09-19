import os
from os.path import join
import argparse
from tqdm import tqdm


parser = argparse.ArgumentParser()
parser.add_argument('--dataset_dir', type=str, help='dataset directory')
parser.add_argument('--input', type=str, help='subdirectory containing obj files in the dataset directory')
args = parser.parse_args()

# where contains the original ply files
ply_dir = join(args.dataset_dir, args.input)

# where to save the converted obj files
obj_dir = join(args.dataset_dir, "models_obj")
if not os.path.isdir(obj_dir):
    os.mkdir(obj_dir)

plys = [name for name in os.listdir(ply_dir) if name.endswith(".ply")]

for ply in tqdm(plys):
    os.system("meshlabserver -i %s -o %s" % (os.path.join(ply_dir, ply), os.path.join(obj_dir, ply.replace(".ply", ".obj")[-6:])))
