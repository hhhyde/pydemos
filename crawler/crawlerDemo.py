#coding:utf-8
'''
Created on 2012-12-21

@author: k0000010359
'''
import urllib2
pxy=urllib2.ProxyHandler({'http':'http://openproxy.huawei.com'})
bul=urllib2.build_opener(pxy, urllib2.HTTPHandler)
urllib2.install_opener(bul)
content=urllib2.urlopen('http://www.cnblogs.com/').read()
print(content)
