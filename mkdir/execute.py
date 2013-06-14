#coding:gbk
import os
file = open('F:/11.txt', 'r')
for f in file.readlines():
    os.mkdir('C:/12/' + f.rstrip()),
file.close()
