#coding:utf-8
from glob import glob

def checkxml(path):
    from xml.sax import make_parser
    parser=make_parser()
    parser.parse(path)

pathname='f:/temp/*.xml'
for case in glob(pathname):
    try:
        checkxml(case)
        print '%s is ok'%case
    except Exception, e:
        print e

