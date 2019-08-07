import json
import numpy as np
from PIL import Image
import cv2
import os
import ipdb

value_list = [25,  39,  48,  56,  63,  69,  75,  80,  85,  89,
              93,  97,  101, 105, 108, 111, 115, 118, 121, 124,
              126, 129, 132, 134, 137, 139, 142, 144, 147, 149]


# Obtain the bounding box from the mask
def obtain_obj_region(mask_path, idx):
    mask = cv2.imread(mask_path, -1)
    obj_mask = np.array(mask == value_list[idx]).astype('uint8')
    bbox = cv2.boundingRect(obj_mask)
    px_visible = int(np.sum(obj_mask))
    occupy_fract = px_visible / (bbox[2] * bbox[3]) if px_visible != 0 else 0
    return bbox, px_visible, occupy_fract


# Obtain the object center from the translation vector
def obtain_obj_center(T, fx, fy, px, py, height, width):
    cx = int(fx * T[0] / T[2] + px)
    cy = int(fy * T[1] / T[2] + py)
    outside = True if cx <= 0 or cy <= 0 or cx >= width or cy >= height else False
    return cx, cy, outside


# Crop and Resize the image without changing the aspect ratio
def resize_padding(im, desired_size):
    # compute the new size
    old_size = im.size
    ratio = float(desired_size) / max(old_size)
    new_size = tuple([int(x * ratio) for x in old_size])

    im = im.resize(new_size, Image.ANTIALIAS)

    # create a new image and paste the resized on it
    new_im = Image.new("RGBA", (desired_size, desired_size))
    new_im.paste(im, ((desired_size - new_size[0]) // 2, (desired_size - new_size[1]) // 2))
    return new_im


# Create directory if not existed
def create_dir(dir):
    if not os.path.isdir(dir):
        os.makedirs(dir)


if __name__ == '__main__':
    scene_id = '{:08d}'.format(0)
    sample_id = '{:04d}'.format(100)
    image_path = 'random_path.png'
    obj_id = str(10)
    model_path = 'random_path.obj'
    cam_R_m2c = list(np.array([0.89421800, 0.44575600, -0.04179340, 0.29321500, -0.65362400, -0.69775200, -0.33833500, 0.61166600, -0.71515800]))
    cam_t_m2c = list(np.array([127.17500000, -25.73520000, 963.62800000]))
    obj_center = (234, 124)
    bbox = (0, 0, 0, 0)
    occupy_fract = str(0.455)
    px_visible = str(100)

    annotation = {}
    idx = 0
    sample_frame = {}
    sample_frame["scene_id"] = 0
    sample_frame["sample_id"] = 0
    sample_frame["image_path"] = 'random.png'
    sample_frame["model_path"] = 'random.obj'
    sample_frame["obj_id"] = 0
    sample_frame["cam_R_m2c"] = cam_R_m2c
    sample_frame["cam_t_m2c"] = cam_t_m2c
    sample_frame["obj_center"] = obj_center
    sample_frame["bbox"] = bbox
    sample_frame["occupy_fract"] = 0.5
    sample_frame["px_visib"] = 100
    annotation['{}'.format(idx)] = sample_frame

    idx += 1
    sample_frame["scene_id"] = 0
    sample_frame["sample_id"] = 0
    sample_frame["image_path"] = 'random.png'
    sample_frame["model_path"] = 'random.obj'
    sample_frame["obj_id"] = 0
    sample_frame["cam_R_m2c"] = cam_R_m2c
    sample_frame["cam_t_m2c"] = cam_t_m2c
    sample_frame["obj_center"] = obj_center
    sample_frame["bbox"] = bbox
    sample_frame["occupy_fract"] = 0.5
    sample_frame["px_visib"] = 100
    annotation['{}'.format(idx)] = sample_frame

    with open('annotation.json', 'w') as f:
        json.dump(annotation, f, indent=4, separators=(',', ': '))
