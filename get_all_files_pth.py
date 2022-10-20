#返回指定文件夹下（含子目录）以指定后缀结尾的文件路径列表
import os

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

dirPath = r"D:/StudyFile/1007"
fileSuffix = 'png'
Filelist = get_all_files_pth(dirPath + '/',fileSuffix)
print(len(Filelist))
for file in  Filelist :
    print(file)