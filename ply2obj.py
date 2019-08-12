import os
from tqdm import tqdm

# where contains the original ply files
ply_dir = "models"

# where to save the converted obj files
obj_dir = "models_obj"
os.mkdir(obj_dir)

plys = [name for name in os.listdir(ply_dir) if name.endswith(".ply")]

for ply in tqdm(plys):
    os.system("meshlabserver -i %s -o %s" % (os.path.join(ply_dir, ply), os.path.join(obj_dir, ply.replace(".ply", ".obj")[-6:])))