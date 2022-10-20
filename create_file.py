#创建文件夹
import os

def create_file(path):
    #os.path.exists(path)判断一个目录是否存在
    #os.mkdir(path)创建目录
    isExists=os.path.exists(path)
    if not isExists:
        os.mkdir(path)
        print(path+'创建成功')
        return True
    else:
        print(path+'文件夹已存在,创建文件夹失败')
        return False
