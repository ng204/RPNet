# RPNet: RGB-Pose Network for Action Recognition

An RGB-Pose fusion network based on MMAction2 framework for video action recognition.

## 🛠️ Installation

### Requirements

- Linux / Windows
- Python 3.8+
- PyTorch 1.3+
- CUDA 10.0+ (GPU recommended)

### Step 1: Create Virtual Environment

```bash
conda create --name rpnet python=3.8 -y
conda activate rpnet
```

### Step 2: Install PyTorch

```bash
# CUDA 11.3
conda install pytorch torchvision torchaudio pytorch-cuda=11.3 -c pytorch -c nvidia

# Or CUDA 11.8
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia

# CPU version
conda install pytorch torchvision torchaudio cpuonly -c pytorch
```

### Step 3: Install MMEngine and MMCV

```bash
pip install -U openmim
mim install mmengine
mim install mmcv
```

### Step 4: Install MMAction2 and Dependencies

```bash
# Clone the project (if not already done)
git clone https://github.com/ng204/RPNet.git
cd RPNet

# Install MMAction2
pip install -v -e .

# Install other dependencies
pip install -r requirements.txt
```

### Verify Installation

```python
import torch
import mmaction
import mmcv
import mmengine

print(f"PyTorch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"MMAction2 version: {mmaction.__version__}")
print(f"MMCV version: {mmcv.__version__}")
print(f"MMEngine version: {mmengine.__version__}")
```

## 🚀 Quick Start

### Train Model

```bash
# Single GPU training
python tools/train.py configs/skeleton/posec3d/rgbpose_conv3d/RPNet.py

# Multi-GPU training (using 4 GPUs)
bash tools/dist_train.sh configs/skeleton/posec3d/rgbpose_conv3d/RPNet.py 4
```

### Test Model

```bash
# Single GPU testing
python tools/test.py configs/skeleton/posec3d/rgbpose_conv3d/RPNet.py \
    work_dirs/RPNet/best_acc_top1_epoch_XX.pth

# Multi-GPU testing
bash tools/dist_test.sh configs/skeleton/posec3d/rgbpose_conv3d/RPNet.py \
    work_dirs/RPNet/best_acc_top1_epoch_XX.pth 4
```

### Video Inference

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
