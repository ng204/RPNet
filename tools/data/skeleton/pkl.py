#/root/mmaction2/tools/data/skeleton/my_train.pkl
import pickle

# 加载 .pkl 文件
with open('/root/mmaction2/tools/data/skeleton/my_train.pkl', 'rb') as f:
    data = pickle.load(f)

# 查看 annotations 内容
annotations = data['annotations']

# 打印第一个样本的关键信息
first_annotation = annotations[0]
keypoints = first_annotation['keypoint']
keypoint_scores = first_annotation['keypoint_score']

# 打印关键点的形状，应该是 (num_person, num_frames, num_keypoints, 2)
print(f"关键点数据形状: {keypoints.shape}")

# 打印关键点数量
num_keypoints = keypoints.shape[2]
print(f"关键点数量: {num_keypoints}")

# 打印置信度分数
print(f"关键点置信度分数形状: {keypoint_scores.shape}")

# 打印总帧数
total_frames = first_annotation['total_frames']
print(f"总帧数: {total_frames}")

# 打印帧中的图像尺寸
img_shape = first_annotation['img_shape']
print(f"图像尺寸: {img_shape}")
