import glob
import logging
import os
import time
from os.path import splitext
from tqdm import tqdm
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

def create_file(path):
    #os.path.exists(path)判断一个目录是否存在
    #os.mkdir(path)创建目录
    isExists=os.path.exists(path)
    if not isExists:
        os.mkdir(path)
        # print(path+'创建成功') #尽量避免在轮子库中打印输出
        return True
    else:
        # print(path+'文件夹已存在,创建文件夹失败')
        return False
    
def get_all_files_pth(dir:str,suffix:str = '*'):
    Filelist = []
    for root, dirs, files in os.walk(dir):   #每次遍历的对象都是返回的是一个三元组(root,dirs,files)
        # root 所指的是当前正在遍历的这个文件夹的本身的地址
        # dirs 是一个 list ，保存了文件夹下的所有子文件夹的目录名（只有一层）
        # files 同样是 list , 则是一个保存了文件夹下的所有文件的文件名，并保存到list中
        for filename in files:
            # 文件名列表，包含完整路径
            if filename.endswith(suffix):
                Filelist.append(os.path.join(root + '/', filename))
    return Filelist

def get_file_name_from_pth(fpth: str):
    filename_list = []
    for root, dirs, files in os.walk(fpth):  # 每次遍历的对象都是返回的是一个三元组(root,dirs,files)
        for filename in files:
                filename_list.append(os.path.splitext(filename)[0])  # 获取不带后缀文件名
    return filename_list

def get_fpths_from_dir(dir:str,suffix:str = '*'):
        for fileName in os.listdir(dir): #获取文件名
            if fileName.endswith(suffix):  #判断后缀
                 print(os.path.join(dir, fileName))


'''
下方是部分用于文件操作的代码，仅供参考~
你可以改一改，改成自己的。
'''
def auto_make_directory(dir_pth: str):
    '''
    自动检查dir_pth是否存在，若存在，返回真，若不存在创建该路径，并返回假
    :param dir_pth: 路径
    :return: bool
    '''
    if os.path.exists(dir_pth):  ##目录存在，返回为真
        return True
    else:
        os.makedirs(dir_pth)
        return False
def get_dirs_pth(dir_pth: str):
    '''
    返回返回dir_pth下文件夹路径
    :param dir_pth:
    :return: 文件夹绝对路径list
    '''
    rst = []
    for item in os.listdir(dir_pth):
        temp = os.path.join(dir_pth, item)
        if os.path.isdir(temp):
            rst.append(str(temp))
    return rst


def get_dirs_name(dir_pth: str):
    rst = []
    for item in os.listdir(dir_pth):
        temp = os.path.join(dir_pth, item)
        if os.path.isdir(temp):
            rst.append(str(item))
    return rst
def get_filename_from_pth(file_pth: str, suffix: bool = True):
    '''
    根据文件路径获取文件名
    :param file_pth:文件路径
    :return:文件名
    '''
    fname_list = os.path.split(file_pth)[1].split('.')
    if suffix: #如果保留后缀

        rst = '.'.join(fname_list)
    else:#如果不保留后缀
        rst = '.'.join(fname_list[:-1])
    return rst

def get_files_pth(dir_pth: str, suffix: str = '*'):
    '''
    返回dir_pth下以后缀名suffix结尾的文件绝对路径list
    :param dir_pth:文件夹路径
    :param suffix:限定的文件后缀
    :return: 文件绝对路径list
    '''
    rst = []
    glob_pth = os.path.join(dir_pth, f'*.{suffix}')
    for filename in glob.glob(glob_pth):
        rst.append(filename)
    return rst
def get_all_files_pth(dir_pth: str, suffix: str = None):
    '''
    获取指定文件夹下（含子目录）以指定后缀结尾的文件路径列表
    :param dir_pth: 指定文件夹路径
    :param suffix: 指定后缀
    :return:
    '''
    rst = []
    for root, dirs, files in os.walk(dir_pth):
        if len(files) > 0:
            for file_name in files:
                file_pth = os.path.join(root, file_name)
                if not suffix:
                    rst.append(file_pth)
                elif file_pth.endswith(f'.{suffix}'):
                    rst.append(file_pth)
    return rst


def get_files_name(dir_path: str, suffix: str = '*'):
    '''
    返回指定文件夹内的文件名（不带后缀）列表
    :param dir_path: 文件夹路径
    :param suffix:限定的文件后缀
    :return:文件名（不带后缀）列表
    '''
    if suffix == '*':
        ids = [splitext(file)[0] for file in os.listdir(dir_path) if not file.startswith('.')]
        return ids
    else:
        ids = [splitext(file)[0] for file in os.listdir(dir_path) if file.endswith(f'.{suffix}')]  # 获取图片名称，ids是一个列表
        return ids


def get_filename_from_pth(file_pth: str, suffix: bool = True):
    '''
    根据文件路径获取文件名
    :param file_pth:文件路径
    :return:文件名
    '''
    fname_list = os.path.split(file_pth)[1].split('.')
    if suffix: #如果保留后缀

        rst = '.'.join(fname_list)
    else:#如果不保留后缀
        rst = '.'.join(fname_list[:-1])
    return rst


def get_suffix_from_pth(file_pth: str):
    '''
    根据文件路径获取后缀
    :param file_pth:文件路径
    :return:后缀
    '''
    return os.path.split(file_pth)[1].split('.')[-1]
