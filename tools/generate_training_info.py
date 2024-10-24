import os
import json

from tqdm import tqdm

import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Process video data paths")
    
    parser.add_argument('--uid_info_dict_path', type=str, 
                        default=None,
                        required=True,
                        help="Path to the UID info dictionary JSON file")
    
    parser.add_argument('--output_path', type=str, 
                        default="data/vdm/meta/training_info.json",
                        help="Output path for processed data")
    
    parser.add_argument('--data_root', type=str, 
                        default=None,
                        required=True,
                        help="Root directory for the video data")

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    
    uid_info_dict_path = args.uid_info_dict_path
    output_path = args.output_path
    data_root = args.data_root
    view_groups = [
        [0, 4, 8, 12],
        [1, 5, 9, 13],
        [2, 6, 10, 14],
        [3, 7, 11, 15],
    ]

    with open(uid_info_dict_path, "r") as file_to_read:
        uid_info_dict = json.load(file_to_read)

    training_meta_info = []

    for key, val in tqdm(uid_info_dict.items(), desc="Processing UID"):
        anims = val["anim"]
        for anim_index, anim_meta in anims.items():
            for view_group in view_groups:
                sample = {}
                sample["data_path"] = [os.path.join(data_root, key, anim_index, f"view_{index}.mp4") for index in view_group]
                sample["angle"] = anim_meta["angle"]
                
                sample["text_prompt"] = anim_meta["text_prompt"]

                training_meta_info.append(sample)
            # check if video exist
            assert os.path.exists(training_meta_info[-1]["data_path"][-1]), "video path not exist!"

    print("len training meta info: ", len(training_meta_info))
    with open(output_path, "w+") as file_to_write:
        json.dump(training_meta_info, file_to_write, indent=2)