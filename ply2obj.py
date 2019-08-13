import os
from tqdm import tqdm

dataset_dir = '/home/xiao/Datasets/T-LESS'

# where contains the original ply files
ply_dir = os.path.join(dataset_dir, "models_cad")

# where to save the converted obj files
obj_dir = os.path.join(dataset_dir, "models_obj")
if not os.path.isdir(obj_dir):
    os.mkdir(obj_dir)

plys = [name for name in os.listdir(ply_dir) if name.endswith(".ply")]

for ply in tqdm(plys):
    os.system("meshlabserver -i %s -o %s" % (os.path.join(ply_dir, ply), os.path.join(obj_dir, ply.replace(".ply", ".obj")[-6:])))