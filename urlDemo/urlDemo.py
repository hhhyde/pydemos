#coding:utf8
'''
 题目三:
 有配置文件有类似下面的配置:
http://192.168.41.55/img/9981|11|200
http://192.168.41.55/img/9982|11|200
http://192.168.41.55/img/9983|11|200
http://192.168.41.55/img/9984|11|200
http://192.168.41.55/img/9985|11|200
 
 编写一个脚本，要求如下：
 1. 读取配置文件，对每一个url进行检查.
    例如http://192.168.41.55/img/9985|11|200, 这个url返回的结果应该包含"11"两个字，并且HTTP状态码是200, 否则报错。
 2. 需支持并行的检查多个链接 
'''
import re, urllib2
import threading
import time
index=0
rlock=threading.RLock()
class ExeThread(threading.Thread):
    def __init__(self, path):
        self.path=path
        super(ExeThread, self).__init__()
    def run(self):
        #同步锁
        rlock.acquire()
        global index
        temp=open(self.path)
        temp.seek(index)
        for i in range(100):
            cnt=temp.readline()
            exee(cnt)
            index+=len(cnt)+1
        #同步锁
        rlock.release()
def exee(cnt):
    if len(cnt)==0:
        return
    url, tag, code=cnt.split('|')
    a=urllib2.urlopen(url)
    content=a.read()
    if tag in content and int(code)==a.code:
        pass
    else:
        print('%serror'%cnt)
path='f:/temp/html.txt'
for i in range(100):
    exec('th=ExeThread(path);th.start()')
