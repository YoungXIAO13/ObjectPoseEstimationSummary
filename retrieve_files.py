import os
import shutil
from tqdm import tqdm

cur_dir = os.path.dirname(os.path.abspath(__file__))
input_dir = os.path.join(cur_dir, 'retrieve_FILES')
output_dir = os.path.join(cur_dir, 'abc_0000')

subdirs = os.listdir(input_dir)

for subdir in tqdm(subdirs):
    if len(os.listdir(os.path.join(input_dir, subdir))) == 0:
        continue
    file_name = os.listdir(os.path.join(input_dir, subdir))[0]
    ori_file_path = os.path.join(input_dir, subdir, file_name)
    new_file_path = os.path.join(output_dir, file_name)
    shutil.move(ori_file_path, new_file_path)
