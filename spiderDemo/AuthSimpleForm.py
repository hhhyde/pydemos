# coding:utf8
'''
Created on 2013-6-14

@author: Matthew
'''
import urllib2, urllib, cookielib
from urllib2 import HTTPCookieProcessor
from spiderDemo.cookieDemo import cookieFile
# cookie 保存路径
cookieFile = 'd:/webDemo.cok'
# 访问路径(这里不是说的登陆页面，而是登陆后进行处理的页面,这里的Login是login.jsp提交之后后台处理的action)
des_url = r'http://localhost:8080/webDemo/Login'
# 初始化cookie
ath_cookie = cookielib.LWPCookieJar()
# 加装cookie支持(插件)
urllib2.install_opener(urllib2.build_opener(HTTPCookieProcessor(ath_cookie)))
# post 表单数据
data = urllib.urlencode({'account':'hhhyde',
                      'passwd':'hhhyde'})
# 这里的Requst是专门为post请求加上的，如果不是post则不需要
req = urllib2.Request(des_url, data)
# 请求目标页面
result = urllib2.urlopen(req)
print result.read()
print ath_cookie
# 保存cookie到指定路径
ath_cookie.save(cookieFile)
