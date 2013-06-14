#coding:utf-8
'''
Created on 2013-3-14

@author: k0000010359
'''
from xml.dom import minidom
import xml.etree.ElementTree as ET

def Xmlparse():
    a=ET.parse('f:/temp/busconfig.xml').getroot()
#    return a.getElementsByTagName('realtimeworkorderconfig')[0]
    return len(a.find('workorderinterface'))












if __name__=='__main__':
    print Xmlparse()
