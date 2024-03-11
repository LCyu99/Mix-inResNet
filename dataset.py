""" train and test dataset

author baiyu
"""
import os
import sys
import pickle
from scipy.io import loadmat
from PIL import Image
from skimage import io
import matplotlib.pyplot as plt
import numpy as np
import torch
from torch.utils.data import Dataset
from torchvision.transforms import ToTensor
class orthopedicsTrain(Dataset):

    def __init__(self, path, transform=True):
        self.path = path
        self.transform = transform

        # 加载图像文件和标签
        self.image_files = []
        self.labels = []

        # 遍历路径下的所有目录
        for label in os.listdir(self.path):
            # 检查是否为目录
            if not os.path.isdir(os.path.join(self.path, label)):
                continue

            # 获取目录中的所有图像文件
            image_dir = os.path.join(self.path, label)
            image_files = [os.path.join(image_dir, f) for f in os.listdir(image_dir) if f.endswith('.jpg')]

            # 追加图像文件和标签
            self.image_files.extend(image_files)
            self.labels.extend([int(label) - 1] * len(image_files))

        # 打印最大和最小标签值
        max_label = max(self.labels)
        min_label = min(self.labels)
        print("Max label value: ", max_label)
        print("Min label value: ", min_label)


    def __len__(self):
        return len(self.image_files)


    def __getitem__(self, index):
        image_path = self.image_files[index]
        label = self.labels[index]

        # 打开图像文件并应用转换
        with Image.open(image_path) as img:
            if self.transform:
                image = self.transform(img)
            else:
                image = ToTensor()(img)

        return image, label




class orthopedicsTest(Dataset):

    def __init__(self, path, transform=True):
        self.path = path
        self.transform = transform

        # 加载图像文件和标签
        self.image_files = []
        self.labels = []

        # 遍历路径下的所有目录
        for label in os.listdir(self.path):
            # 检查是否为目录
            if not os.path.isdir(os.path.join(self.path, label)):
                continue

            # 获取目录中的所有图像文件
            image_dir = os.path.join(self.path, label)
            image_files = [os.path.join(image_dir, f) for f in os.listdir(image_dir) if f.endswith('.jpg')]

            # 追加图像文件和标签
            self.image_files.extend(image_files)
            self.labels.extend([int(label) - 1] * len(image_files))

    def __len__(self):
        return len(self.image_files)

    def __getitem__(self, index):
        image_path = self.image_files[index]
        label = self.labels[index]

        # 打开图像文件并应用转换
        with Image.open(image_path) as img:
            if self.transform:
                image = self.transform(img)
            else:
                image = ToTensor()(img)
        return label, image


