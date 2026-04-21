# RPNet: RGB-Pose Network for Action Recognition

基于MMAction2框架的RGB-Pose融合网络，用于视频动作识别任务。

## 🛠️ 环境安装

### 系统要求

- Linux / Windows
- Python 3.8+
- PyTorch 1.3+
- CUDA 10.0+ (推荐使用GPU)

### 步骤1: 创建虚拟环境

```bash
conda create --name rpnet python=3.8 -y
conda activate rpnet
```

### 步骤2: 安装PyTorch

```bash
# CUDA 11.3
conda install pytorch torchvision torchaudio pytorch-cuda=11.3 -c pytorch -c nvidia

# 或者 CUDA 11.8
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia

# CPU版本
conda install pytorch torchvision torchaudio cpuonly -c pytorch
```

### 步骤3: 安装MMEngine和MMCV

```bash
pip install -U openmim
mim install mmengine
mim install mmcv
```

### 步骤4: 安装MMAction2和依赖

```bash
# 克隆项目（如果还没有）
git clone https://github.com/ng204/RPNet.git
cd RPNet

# 安装MMAction2
pip install -v -e .

# 安装其他依赖
pip install -r requirements.txt
```

### 验证安装

```python
import torch
import mmaction
import mmcv
import mmengine

print(f"PyTorch版本: {torch.__version__}")
print(f"CUDA可用: {torch.cuda.is_available()}")
print(f"MMAction2版本: {mmaction.__version__}")
print(f"MMCV版本: {mmcv.__version__}")
print(f"MMEngine版本: {mmengine.__version__}")
```


##  快速开始

### 训练模型

```bash
# 单GPU训练
python tools/train.py configs/skeleton/posec3d/rgbpose_conv3d/RPNet.py

# 多GPU训练（使用4个GPU）
bash tools/dist_train.sh configs/skeleton/posec3d/rgbpose_conv3d/RPNet.py 4
```

### 测试模型

```bash
# 单GPU测试
python tools/test.py configs/skeleton/posec3d/rgbpose_conv3d/RPNet.py \
    work_dirs/RPNet/best_acc_top1_epoch_XX.pth

# 多GPU测试
bash tools/dist_test.sh configs/skeleton/posec3d/rgbpose_conv3d/RPNet.py \
    work_dirs/RPNet/best_acc_top1_epoch_XX.pth 4
```

### 视频推理

```bash
python demo/demo_skeleton.py \
    demo/demo_skeleton.mp4 \
    demo/demo_out.mp4 \
    --config configs/skeleton/posec3d/rgbpose_conv3d/RPNet.py \
    --checkpoint work_dirs/RPNet/best_acc_top1_epoch_XX.pth \
    --det-config demo/demo_configs/faster-rcnn_r50_fpn_2x_coco_infer.py \
    --det-checkpoint http://download.openmmlab.com/mmdetection/v2.0/faster_rcnn/faster_rcnn_r50_fpn_2x_coco/faster_rcnn_r50_fpn_2x_coco_bbox_mAP-0.384_20200504_210434-a5d8aa15.pth \
    --pose-config demo/demo_configs/td-hm_hrnet-w32_8xb64-210e_coco-256x192_infer.py \
    --pose-checkpoint https://download.openmmlab.com/mmpose/top_down/hrnet/hrnet_w32_coco_256x192-c78dce93_20200708.pth \
    --label-map tools/data/skeleton/label_map_ntu60.txt
```

