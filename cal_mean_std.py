#返回所有图片整体的均值与标准差字典
import os
import cv2
import numpy as np
from PIL import Image, ImageStat

def cal_mean_std(images_dir:str):
    mean_sum = 0
    std_sum = 0
    num = 0
    Filelist = []
    #图片路径列表
    for root, dirs, files in os.walk(images_dir):  # 每次遍历的对象都是返回的是一个三元组(root,dirs,files)
        for filename in files:
            # 文件名列表，包含完整路径
            if filename.endswith('jpg'):
                Filelist.append(os.path.join(root + '/', filename))
    #计算平均值与标准差
    # ImageStat模块用于计算整个图像或者图像的一个区域的统计数据
        for i in range(len(Filelist)):
            img = Image.open(Filelist[i])   #plt函数读入的顺序为RGB,cv2.imshow()读入的顺序为BGR
            stat = ImageStat.Stat(img)
            mean_sum += stat.mean[0]       #属性mean为每个通道的像素值之和除以像素个数
            std_sum += stat.stddev[0]      #stddev获取图像中每个通道的像素值的标准差值
            num += 1  # 累加图片数
    mean = mean_sum / num   #整个数据集的均值
    std = std_sum / num
    return {'mean':mean,'std':std}

dirPath = r"D:/StudyData/dataset/train/image"
result = cal_mean_std(dirPath)
print( cal_mean_std(dirPath))
