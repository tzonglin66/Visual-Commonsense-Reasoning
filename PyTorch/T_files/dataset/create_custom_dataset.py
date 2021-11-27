# 作 者：田宗林
# 时 间：2021/10/31
# Creating a Custom Dataset for your files
"""
A custom Dataset class must implement three functions:
__init__, __len__, and __getitem__.
Take a look at this implementation;
the FashionMNIST images are stored in a directory img_dir, and their labels are stored separately in a CSV file annotations_file.
Like:
    tshirt1.jpg, 0
    tshirt2.jpg, 0
    ......
    ankleboot999.jpg, 9
"""

from torch.utils.data import Dataset
import os
import pandas as pd
from torchvision.io import read_image


class CustomImageDataset(Dataset):
    def __init__(self, annotations_file, img_dir, transform=None, target_transform=None): # 图片、注释文件、两种变换

        self.img_labels = pd.read_csv(annotations_file)
        self.img_dir = img_dir
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self):  # returns the number of samples in our dataset.
        return len(self.img_labels)

    def __getitem__(self, idx):  # loads and returns a sample from the dataset at the given index idx.
        img_path = os.path.join(self.img_dir, self.img_labels.iloc[idx, 0])  # 图片名在第1列
        image = read_image(img_path)  # read a JPEG or PNG image into a 3 dimensional RGB Tensor
        label = self.img_labels.iloc[idx, 1]  # label 放在第2列
        if self.transform:
            image = self.transform(image)
        if self.target_transform:
            label = self.target_transform(label)
        return image, label