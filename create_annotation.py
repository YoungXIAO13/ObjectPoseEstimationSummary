import json
import os
from tqdm import tqdm

dataset = 'LINEMOD'
test_dir = '/home/xiao/Datasets/{}/test'.format(dataset)
scenes = os.listdir(test_dir)
scenes.sort()

annot = {}
idx = 0

for scene_id in tqdm(range(1, len(scenes) + 1)):
    scene_dir = os.path.join(test_dir, scenes[scene_id - 1])
    scene_gt = json.load(open(os.path.join(scene_dir, 'scene_gt.json')))
    scene_gt_info = json.load(open(os.path.join(scene_dir, 'scene_gt_info.json')))
    scene_camera = json.load(open(os.path.join(scene_dir, 'scene_camera.json')))

    for i in tqdm(range(len(scene_gt))):
        # more than one models can be present in an image
        for n in range(len(scene_gt["{}".format(i)])):
            sample_frame = {}
            sample_frame["scene_id"] = int(scenes[scene_id - 1])
            sample_frame["image_id"] = i

            # get annotation from scene_gt
            sample_frame["obj_id"] = scene_gt["{}".format(i)][n]["obj_id"]
            sample_frame["cam_R_m2c"] = scene_gt["{}".format(i)][n]["cam_R_m2c"]
            T = scene_gt["{}".format(i)][0]["cam_t_m2c"]
            sample_frame["cam_t_m2c"] = T
            cam_K = scene_camera["{}".format(i)]["cam_K"]
            fx, fy, px, py = cam_K[0], cam_K[4], cam_K[2], cam_K[5]
            cx = int(fx * T[0] / T[2] + px)
            cy = int(fy * T[1] / T[2] + py)
            sample_frame["obj_center"] = [cx, cy]

            # get annotation from scene_gt_info
            sample_frame["bbox"] = scene_gt_info["{}".format(i)][n]["bbox_obj"]
            sample_frame["bbox_visib"] = scene_gt_info["{}".format(i)][n]["bbox_visib"]
            sample_frame["px_count_visib"] = scene_gt_info["{}".format(i)][n]["px_count_visib"]
            sample_frame["visib_fract"] = scene_gt_info["{}".format(i)][n]["visib_fract"]

            annot['{}'.format(idx)] = sample_frame
            idx += 1

annotation_file = '/home/xiao/Datasets/{}/{}.json'.format(dataset, dataset)
with open(annotation_file, 'w') as f:
    json.dump(annot, f, indent=4)


