'''
Created on 2013-1-6

@author: k0000010359
'''
import urllib2
a=urllib2.urlopen('http://172.21.4.45:23006/pms_common/pms_blank.action').read()
print a
