import yaml
import numpy as np
import os
from scipy.linalg import expm, norm, logm
import math
from tqdm import tqdm


def compute_rotation_from_vertex(vertex):
    """Compute rotation matrix from viewpoint vertex """
    up = [0, 0, 1]
    if vertex[0] == 0 and vertex[1] == 0 and vertex[2] != 0:
        up = [-1, 0, 0]
    rot = np.zeros((3, 3))
    rot[:, 2] = -vertex / norm(vertex)  # View direction towards origin
    rot[:, 0] = np.cross(rot[:, 2], up)
    rot[:, 0] /= norm(rot[:, 0])
    rot[:, 1] = np.cross(rot[:, 0], -rot[:, 2])
    return rot.T


def create_pose(vertex, scale=0, angle_deg=0):
    """Compute rotation matrix from viewpoint vertex and inplane rotation """
    rot = compute_rotation_from_vertex(vertex)
    transform = np.eye(4)
    rodriguez = np.asarray([0, 0, 1]) * (angle_deg * math.pi / 180.0)
    angle_axis = expm(np.cross(np.eye(3), rodriguez))
    transform[0:3, 0:3] = np.matmul(angle_axis, rot)
    transform[0:3, 3] = [0, 0, scale]
    return transform


def compute_inplane_from_rotation(R, vertex):
    rot = compute_rotation_from_vertex(vertex)
    angle_axis = logm(np.matmul(R, rot.T))
    return angle_axis[1, 0]


def compute_viewpoint_from_camera(c):
    # compute the viewpoint according to the camera position
    elevation = np.arctan(c[2] / np.sqrt(c[0] **2 + c[2] ** 2))
    azimuth = np.arctan(c[1] / c[0])
    if c[0] < 0 and c[1] < 0:
        azimuth -= np.pi
    if c[0] < 0 and c[1] > 0:
        azimuth += np.pi
    return azimuth[0] * 180./ np.pi, elevation[0] * 180./ np.pi


def compute_angles_from_pose(R, t):
    #c = - np.dot(np.transpose(R), t)
    direction = -np.dot(np.transpose(R), np.array([0., 0., 1.]).reshape(3, 1))
    azimuth = np.arctan2(direction[0], direction[1])[0] * 180./ np.pi
    elevation = np.arcsin(direction[-1])[0] * 180./ np.pi
    inplane = compute_inplane_from_rotation(R, direction.reshape(-1)) * 180./ np.pi
    return azimuth, elevation, inplane


LINEMOD_dir = '/media/xiao/newhd/XiaoDatasets/LineMod'
with open(os.path.join(LINEMOD_dir, 'test', '02', 'gt.yml'), 'r') as stream:
    data = yaml.load(stream)

outfile = 'table_poses.npz'
Rotations = np.zeros((1214, 9))
Translations = np.zeros((1214, 3))
Elevations = np.zeros(1214)

for i in tqdm(range(0, len(data))):
    for j in range(0, len(data[i])):
        obj_id = data[i][j]['obj_id']
        if obj_id != 2:
            continue
        x, y, w, h = data[i][j]['obj_bb']
        R = np.array(data[i][j]['cam_R_m2c']).reshape(-1)
        t = np.array(data[i][j]['cam_t_m2c']).reshape(-1)
        Rotations[i, :] = R
        Translations[i, :] = t
        azimuth, elevation, inplane = compute_angles_from_pose(R.reshape(3, 3), t.reshape(3, 1))
        Elevations[i] = elevation

np.savez(outfile, R=Rotations, T=Translations, Ele=Elevations)
