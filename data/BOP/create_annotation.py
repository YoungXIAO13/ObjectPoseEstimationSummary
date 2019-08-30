import json
import os
from tqdm import tqdm

dataset = 'LINEMOD-Occlusion'
test_dir = '/home/xiao/Datasets/{}/test'.format(dataset)
scenes = os.listdir(test_dir)
scenes.sort()

annot = {}
idx = 0

for scene_id in tqdm(range(len(scenes))):
    scene_dir = os.path.join(test_dir, scenes[scene_id])
    scene_gt = json.load(open(os.path.join(scene_dir, 'scene_gt.json')))
    scene_gt_info = json.load(open(os.path.join(scene_dir, 'scene_gt_info.json')))
    scene_camera = json.load(open(os.path.join(scene_dir, 'scene_camera.json')))

    for image_id in tqdm(range(len(scene_gt))):

        # Loop on obj ids of one image
        for n in range(len(scene_gt["{}".format(image_id)])):
            sample_frame = {}
            sample_frame["scene_id"] = int(scenes[scene_id])
            sample_frame["image_id"] = image_id
            sample_frame["instance_id"] = n

            # get annotation from scene_gt
            sample_frame["obj_id"] = scene_gt["{}".format(image_id)][n]["obj_id"]
            sample_frame["cam_R_m2c"] = scene_gt["{}".format(image_id)][n]["cam_R_m2c"]
            T = scene_gt["{}".format(image_id)][0]["cam_t_m2c"]
            sample_frame["cam_t_m2c"] = T
            cam_K = scene_camera["{}".format(image_id)]["cam_K"]
            fx, fy, px, py = cam_K[0], cam_K[4], cam_K[2], cam_K[5]
            cx = int(fx * T[0] / T[2] + px)
            cy = int(fy * T[1] / T[2] + py)
            sample_frame["obj_center"] = [cx, cy]

            # get annotation from scene_gt_info
            sample_frame["bbox_obj"] = scene_gt_info["{}".format(image_id)][n]["bbox_obj"]
            sample_frame["bbox_visib"] = scene_gt_info["{}".format(image_id)][n]["bbox_visib"]
            sample_frame["px_count_visib"] = scene_gt_info["{}".format(image_id)][n]["px_count_visib"]
            sample_frame["visib_fract"] = scene_gt_info["{}".format(image_id)][n]["visib_fract"]

            annot['{}'.format(idx)] = sample_frame
            idx += 1

annotation_file = '/home/xiao/Datasets/{}/{}.json'.format(dataset, dataset)
with open(annotation_file, 'w') as f:
    json.dump(annot, f, indent=4)


