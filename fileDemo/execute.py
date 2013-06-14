#coding:utf-8
'''
Created on 2013-1-6

@author: k0000010359
'''
import os, time
import stat
#拿目标文件属性
#a = os.stat('F:/11.txt')
#print time.ctime(a[stat.ST_ATIME])

def getStat(path):
    fileStat = os.stat(path)
    #一共10个原书，前7个可直接使用
    parseSet = fileStat[:7]

    return fileStat

print getStat('f:/11.txt')[-3:]
