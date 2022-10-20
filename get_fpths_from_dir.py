import os

def get_fpths_from_dir(dir:str,suffix:str = '*'):
        for fileName in os.listdir(dir): #获取文件名
            if fileName.endswith(suffix):  #判断后缀
                 print(os.path.join(dir, fileName))

dirPath = r"D:/StudyImage/study-0930"
fileSuffix = 'jpg'
get_fpths_from_dir(dirPath,fileSuffix)