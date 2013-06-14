#coding:utf8
'''
Created on 2013-3-15

@author: k0000010359
'''
import os
def MkdirfromStr(path):
#    dirs=path.split('/')
#    return dirs[:-1]
#    os.mkdir(path)
#    print(rootpath+path)
        os.makedirs(path)

def getdirfromPathFile(filepath):
    '''
        未实现功能，不能建全部文件夹，从名字短的路径开始建，首先按照路径名字长短排序，试试lamda
    '''
    file=open(filepath, 'r')
    dirs=[]
    for line in file.readlines():
        line=line[:line.rfind('/')]
        if line in dirs:
            pass
        else:
            dirs.append(line)
    print(dirs)
    for path in dirs:
        print('f:/'+path)
        MkdirfromStr('f:/'+path)
    for dir in dirs:
        print(dir)


if __name__=='__main__':

#    path='com/huawei/bus/common/util'
#    os.mkdir('f:/com/huawei/bus/common/util')
#    print MkdirfromStr('f:/com/huawei/bus/common/util')
    getdirfromPathFile('F:\upgrade.txt')
