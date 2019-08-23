import json
import numpy as np
from PIL import Image
import cv2
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

    im = im.resize(new_size, Image.BILINEAR)

    # create a new image and paste the resized on it
    new_im = Image.new("RGBA", (desired_size, desired_size))
    new_im.paste(im, ((desired_size - new_size[0]) // 2, (desired_size - new_size[1]) // 2))
    return new_im


def resize_padding_v2(im, desired_size_in, desired_size_out):
    # compute the new size
    old_size = im.size
    ratio = float(desired_size_in)/max(old_size)
    new_size = tuple([int(x*ratio) for x in old_size])

    im = im.resize(new_size, Image.ANTIALIAS)

    # create a new image and paste the resized on it
    new_im = Image.new("RGBA", (desired_size_out, desired_size_out))
    new_im.paste(im, ((desired_size_out - new_size[0]) // 2, (desired_size_out - new_size[1]) // 2))
    return new_im


# Crop and resize the rendering images
def clean_rendering_results(img_path, depth_path, normal_path, target_size=128):
    img = Image.open(img_path)
    depth = Image.open(depth_path)
    normal = Image.open(normal_path)
    bbox = img.getbbox()
    img, depth, normal = img.crop(bbox), depth.crop(bbox), normal.crop(bbox)
    img = resize_padding(img, target_size).convert('RGB')
    depth = resize_padding(depth, target_size).convert('L')
    normal = resize_padding(normal, target_size).convert('RGB')
    normal_array = np.array(normal)
    mask = np.array(depth) == 0
    normal_array[mask, :] = 0
    normal = Image.fromarray(normal_array)
    img.save(img_path)
    depth.save(depth_path)
    normal.save(normal_path)
