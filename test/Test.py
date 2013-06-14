# _*_ coding: utf-8 _*_
'''
题目一:编写一个脚本main.py，使用方式如下：
main.py -u http://www.sohu.com -d 'a=1,b=2,c=3' -o /tmp/index.html
功能要求：打开-u指定的页面，将页面中所有的链接后面增加参数a=1&b=2&c=3
(需要考虑链接中已经存在指定的参数的问题), 然后保存到-o指定的文件中。
'''
import urllib2
import re
import sys, getopt
opts, args=getopt.getopt(sys.argv[1:], 'u:d:o:')

def execute(pairs = None):
    content=urllib2.urlopen('http://blog.csdn.net/jhonguy/article/details/7576155')
    return content.read()

def main():
    pairs={}
    for item in opts:
        pairs[item[0][1:]]=item[1]
    return execute(pairs)

if __name__=='__main__':
    execute()
