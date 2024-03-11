import numpy as np
from tqdm import tqdm
import math
import os
from PIL import Image
data_path = r"D:\模型-腰狭数据\总数据集\侧隐窝分级\所有数据"

# 设置批次大小
batch_size = 16

# 初始化列表存放所有PNG文件路径
image_files = []

# 获取所有0-3命名的文件夹
folders = [os.path.join(data_path, f) for f in os.listdir(data_path) if os.path.isdir(os.path.join(data_path, f))]

# 遍历每个文件夹获取所有png图片
for folder in folders:
    image_files.extend([os.path.join(folder, f) for f in os.listdir(folder) if f.endswith('.png')])


# 初始化均值和标准差变量
mean_channel_1 = 0.0
mean_channel_2 = 0.0
mean_channel_3 = 0.0

std_channel_1 = 0.0
std_channel_2 = 0.0
std_channel_3 = 0.0

# 遍历图像文件，逐批次提取像素值并计算均值和标准差
for i in tqdm(range(0, len(image_files), batch_size), desc="Processing images"):
    batch_files = image_files[i:i+batch_size]
    batch_pixels = []

    # 加载和处理当前批次的图像
    for image_file in batch_files:
        img = Image.open(image_file)
        img = img.resize((36, 36))  # 调整图像大小
        pixels = np.asarray(img)
        batch_pixels.append(pixels)

    # 计算各个通道的均值和标准差
    batch_pixels = np.array(batch_pixels)
    batch_mean = np.mean(batch_pixels, axis=(0, 1, 2))  # 计算当前批次的均值
    batch_std = np.std(batch_pixels, axis=(0, 1, 2))  # 计算当前批次的标准差

    # 更新累计的均值和标准差
    mean_channel_1 += batch_mean[0]
    mean_channel_2 += batch_mean[1]
    mean_channel_3 += batch_mean[2]

    std_channel_1 += batch_std[0]
    std_channel_2 += batch_std[1]
    std_channel_3 += batch_std[2]

    # 手动释放内存
    del batch_pixels
    del batch_mean
    del batch_std

# 计算总体均值和标准差
total_samples = len(image_files)
mean_channel_1 /= total_samples
mean_channel_2 /= total_samples
mean_channel_3 /= total_samples

std_channel_1 /= total_samples
std_channel_2 /= total_samples
std_channel_3 /= total_samples

# 更新 CIFAR100_TRAIN_MEAN 和 CIFAR100_TRAIN_STD 的值
CIFAR100_TRAIN_MEAN = (mean_channel_1, mean_channel_2, mean_channel_3)
CIFAR100_TRAIN_STD = (std_channel_1, std_channel_2, std_channel_3)

# 打印均值和标准差
print("CIFAR100_TRAIN_MEAN:", CIFAR100_TRAIN_MEAN)
print("CIFAR100_TRAIN_STD:", CIFAR100_TRAIN_STD)