#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from datetime import datetime


def timestamp():
    """返回当前时间戳字符串，格式为 YYYY/MM/DD HH:MM:SS"""
    return datetime.now().strftime("%Y/%m/%d %H:%M:%S")


def print_fake_log():
    """模拟日志输出"""
    print(f"{timestamp()} - mmengine - INFO - Distributed training is not used, all SyncBatchNorm (SyncBN) layers in the model will be automatically reverted to BatchNormXd layers if they are used.")
    print(f"{timestamp()} - mmengine - INFO - Hooks will be executed in the following order:")
    print("before_run:\n(VERY_HIGH   ) RuntimeInfoHook\n(BELOW_NORMAL) LoggerHook")
    print(" -------------------- ")
    print(f"{timestamp()} - mmengine - INFO - 172 videos remain after valid thresholding")
    print(f"{timestamp()} - mmengine - INFO - 44 videos remain after valid thresholding")
    print()
    time.sleep(0.3)
    print(f"{timestamp()} - mmengine - INFO - Model summary:")
    print(f"{timestamp()} - mmengine - INFO - Params(M)\tFLOPs(G)")
    print(f"{timestamp()} - mmengine - INFO - 3.95\t28.81")
    print()
    print(f"{timestamp()} - mmengine - INFO - Initialization finished.")
    print(f"{timestamp()} - mmengine - INFO - Start validation...")


def main():
    """主函数"""
    print_fake_log()


if __name__ == "__main__":
    main()
