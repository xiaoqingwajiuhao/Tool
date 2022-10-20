#返回其不带后缀的文件名
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def get_file_name_from_pth(fpth: str):
    filename_list = []
    for root, dirs, files in os.walk(fpth):  # 每次遍历的对象都是返回的是一个三元组(root,dirs,files)
        for filename in files:
                filename_list.append(os.path.splitext(filename)[0])  # 获取不带后缀文件名
    return filename_list
dirPath = r"D:/StudyFile/1014"
print(get_file_name_from_pth(dirPath))