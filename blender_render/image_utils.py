import numpy as np
from PIL import Image
import cv2
import os
from os.path import join, dirname, basename
import shutil


# Value list used to select object mask rendered by Blender
value_list = [25,  39,  48,  56,  63,  69,  75,  80,  85,  89,
              93,  97,  101, 105, 108, 111, 115, 118, 121, 124,
              126, 129, 132, 134, 137, 139, 142, 144, 147, 149]


# Transform the image containing all visible object masks into one mask per image
def one_mask_per_image(mask_path, image_id, model_number):
    mask = np.array(Image.open(mask_path).convert('L'))
    mask_dir = dirname(mask_path)
    bbox, px = [], []
    for i in range(model_number):
        obj_mask = (mask == value_list[i]).astype('uint8')
        bbox.append(cv2.boundingRect(obj_mask))
        px.append(int(np.sum(obj_mask)))
        cv2.imwrite(join(mask_dir, '{:06d}_{:06d}.png'.format(image_id, i)), obj_mask * 255)
    os.remove(mask_path)
    return bbox, px


# Transform the colored mask of Blender renderer into binary mask
def binary_mask(mask_path):
    mask = np.array(Image.open(mask_path).convert('L'))
    obj_mask = (mask != 0).astype('uint8')
    x, y, w, h = cv2.boundingRect(obj_mask)
    px = int(np.sum(obj_mask))
    truncated = x == 0 or x + w == mask.shape[1] or y == 0 or y + h == mask.shape[0]
    cv2.imwrite(mask_path, obj_mask * 255)
    return (x, y, w, h), px, truncated


# Obtain the object center from the translation vector
def obtain_obj_center(T, fx, fy, px, py, height, width):
    cx = int(fx * T[0] / T[2] + px)
    cy = int(fy * T[1] / T[2] + py)
    boarder = 0.1
    inside = True if boarder * width <= cx <= (1 - boarder) * width and boarder * height <= cy <= (
                1 - boarder) * height else False
    return cx, cy, inside


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

