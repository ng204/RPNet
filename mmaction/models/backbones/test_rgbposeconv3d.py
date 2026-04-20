# test_rgbposeconv3d.py

import torch
from rgbposeconv3d import RGBPoseConv3D

if __name__ == '__main__':
    # 实例化模型
    model = RGBPoseConv3D(pretrained=None)

    # 打印模型结构，确认 MSAA 模块已集成
    print(model)

    # 创建虚拟输入
    imgs = torch.randn(1, 3, 16, 224, 224)          # 示例 RGB 输入 (N, C, T, H, W)
    heatmap_imgs = torch.randn(1, 17, 16, 224, 224) # 示例 Pose 热图输入 (N, C, T, H, W)

    # 前向传播
    x_rgb, x_pose = model(imgs, heatmap_imgs)

    # 打印输出形状
    print(f'RGB 输出形状: {x_rgb.shape}')
    print(f'Pose 输出形状: {x_pose.shape}')
