import os
import re


def rename_videos(folder_path):
    # 遍历文件夹及其子目录
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 只处理.mp4文件
            if file.endswith(".mp4"):
                # 获取所在文件夹的名称
                parent_folder_name = os.path.basename(root)

                # 原有文件名
                old_file_path = os.path.join(root, file)

                # 使用正则表达式查找文件名中的数字部分
                match = re.search(r'(\d+)', file)
                if match:
                    number = match.group(1)
                    # 将数字部分补齐为三位
                    new_number = f"{int(number):03d}"
                    # 将文件名中的数字部分替换为补齐后的三位数
                    new_file_name = re.sub(r'\d+', new_number, file)
                else:
                    # 如果没有找到数字，保持原文件名不变
                    new_file_name = file

                # 新文件名: 所在文件夹名称 + A + 新的文件名
                new_file_name = f"{parent_folder_name}A{new_file_name}"
                new_file_name = new_file_name.split('.')[0] + '.mp4'
                new_file_path = os.path.join(root, new_file_name)

                # 重命名文件
                os.rename(old_file_path, new_file_path)
                print(f"已重命名: {old_file_path} -> {new_file_path}")


# 调用函数，传入需要遍历的文件夹路径
folder_path = "/root/autodl-tmp/action"
rename_videos(folder_path)
