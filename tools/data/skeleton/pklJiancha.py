

import pickle

# 替换为你的 pkl 文件路径
pkl_file_path = '/root/mmaction2/tools/data/skeleton/my_train.pkl'

# 加载 pkl 文件
with open(pkl_file_path, 'rb') as f:
    data = pickle.load(f)

# 查看数据的键
print(f"数据类型: {type(data)}")
print(f"数据键值: {data.keys()}")

# 访问 'annotations' 键中的数据
if 'annotations' in data:
    annotations = data['annotations']
    print(f"'annotations' 类型: {type(annotations)}")
    
    # 假设 annotations 是一个列表，查看第一个样本的信息
    if isinstance(annotations, list) and len(annotations) > 0:
        first_sample = annotations[0]
        print(f"第一个样本数据类型: {type(first_sample)}")

        # 如果是字典类型，列出所有键值
        if isinstance(first_sample, dict):
            print(f"第一个样本键值: {first_sample.keys()}")

            # 假设 'keypoint' 是关键点数据，查看关键点数据维度
            if 'keypoint' in first_sample:
                keypoints = first_sample['keypoint']
                print(f"关键点数据维度: {keypoints.shape}")
                print(f"关键点数据示例: {keypoints}")

            # 检查是否包含 'keypoint_score'
            if 'keypoint_score' in first_sample:
                keypoint_scores = first_sample['keypoint_score']
                print(f"关键点置信度维度: {keypoint_scores.shape}")
                print(f"关键点置信度示例: {keypoint_scores}")
