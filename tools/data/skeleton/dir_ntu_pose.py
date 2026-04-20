import os
import argparse
parser = argparse.ArgumentParser(
        description='Generate Pose Annotation for a single NTURGB-D video')
parser.add_argument('video_dir', type=str, help='source video')
args = parser.parse_args()
video_dir = args.video_dir
output_dir = '/root/autodl-tmp/action_output_dit'
action_list = next(os.walk(video_dir))[1]
for action in action_list:
        action_dir = os.path.join(video_dir, action)
        action_output_path = os.path.join(output_dir, action)
        for video in os.listdir(action_dir):
                output = video.split('.')[0] + '.pkl'
                video_path = os.path.join(action_dir, video)
                pkl_output_path = os.path.join(action_output_path, output)
                print('video_path: {}'.format(video_path))
                print('pkl_output_path: {}'.format(pkl_output_path))
                os.system('python ntu_pose_extraction.py {} {}'.format(video_path, pkl_output_path))