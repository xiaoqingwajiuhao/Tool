import os
import cv2
import numpy as np
import sys
from tqdm import tqdm


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

#现阶段不要混杂着使用PIL与OpenCV
def cal_mean_std(images_dir,is_normalized=False):
    """
    给定数据图片根目录,计算图片整体均值与方差
    :param images_dir:
    :return:
    """
    img_filenames = os.listdir(images_dir)
    m_list, s_list = [], []
    for img_filename in tqdm(img_filenames):
        img = cv2.imread(images_dir + '/' + img_filename)
        img = img / 255.0
        m, s = cv2.meanStdDev(img)

        m_list.append(m.reshape((3,)))
        s_list.append(s.reshape((3,)))
        print(m_list)
    m_array = np.array(m_list)
    s_array = np.array(s_list)
    m = m_array.mean(axis=0, keepdims=True)
    s = s_array.mean(axis=0, keepdims=True)

    mean = m[0][::-1] if is_normalized else m[0][::-1]*255
    std = s[0][::-1] if is_normalized else s[0][::-1]*255

    return {'mean':mean,'std':std}
def is_bin_bg_white(img):
    '''_summary_
    判断二值图背景是否为白色
    Args:
        img (_type_): _description_
    Returns:
        _type_: _description_
    '''
    if isinstance(img, str):
        img = cv2.imread(img)
    elif isinstance(img, np.ndarray):
        pass
    h,w,c = img.shape[:2]
    if c!=1:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # _, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    max_val = h*w*255
    current_val = np.sum(img)
    ratio = current_val/max_val

    if ratio > 0.5:
        return True
    return False
def get_hor_projection(img_bin):
    img_bin=img_bin
    # showim(img_bin)
    rst = np.sum(img_bin,axis=1)//255
    return rst.tolist()