import os.path as osp
import os
import pickle
from sklearn.model_selection import train_test_split

# 定义文件夹名称到label的映射
label_map = {
    'bo': 0,
    'run': 1,
    'stand': 2,
    'walk': 3
}

result = []
file_names = []  # 用于保存文件名
root_path = '/root/autodl-tmp/action_output_dit'

# 遍历根目录下的所有文件夹
for folder in os.listdir(root_path):
    folder_path = osp.join(root_path, folder)

    # 只处理文件夹
    if osp.isdir(folder_path):
        for file_name in os.listdir(folder_path):
            if file_name.endswith('.pkl'):
                file_path = osp.join(folder_path, file_name)
                with open(file_path, 'rb') as f:
                    content = pickle.load(f)

                # 修改label字段，确保content中有label
                if 'label' in content:
                    content['label'] = label_map.get(folder, content['label'])  # 根据父文件夹修改label

                result.append(content)

                # 保存文件名（去掉后缀.pkl）
                file_names.append(file_name[:-4])  # 去掉 ".pkl"

# 检查是否成功读取了数据
if len(result) == 0:
    raise ValueError("未找到任何.pkl文件，确保路径正确并包含.pkl文件。")

# 划分训练集和验证集，比例为8:2
xsub_train, xsub_val = train_test_split(file_names, test_size=0.2, random_state=42)

# 构造最终的数据结构
final_data = {
    'annotations': result,  # 合并后的所有数据
    'split': {
        'xsub_train': xsub_train,  # 训练集的文件名列表
        'xsub_val': xsub_val  # 验证集的文件名列表
    }
}

# 保存最终的pkl文件
with open('my_train.pkl', 'wb') as out:
    pickle.dump(final_data, out, protocol=pickle.HIGHEST_PROTOCOL)

print(f"总文件数: {len(file_names)}，训练集大小: {len(xsub_train)}，验证集大小: {len(xsub_val)}")
