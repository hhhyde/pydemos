#coding:gbk
'''
Created on 2012-7-25

@author: kejiangtao
'''
import os
class Mkdir(object):
    def mkdirs(self, filepath, dirpath):
        files = open(filepath, 'r')
        for file in files.readlines():
            filevaild = file.replace('\t', '').strip()
            os.mkdir(dirpath + '/' + filevaild)
#            print(filevaild)
        files.close()
