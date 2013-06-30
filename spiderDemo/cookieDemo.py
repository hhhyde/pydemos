# coding:utf8
'''
Created on 2013-6-10

@author: Matthew
'''
from urllib import urlencode 
import cookielib, urllib2 
# cookie 
cookieFile = 'd:/nimei.dat'
cj = cookielib.LWPCookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj)) 
urllib2.install_opener(opener) 
# Login 
user_data = {'account': '666666',
'passwd': '4599' ,
'submit': 'tijiao' ,
'action': 'http://localhost:8080/webDemo/Login' 
} 
url_data = urlencode(user_data)
print url_data
req = urllib2.Request("http://localhost:8080/webDemo/login.jsp", url_data)
login_r = urllib2.urlopen(req).read()
req = urllib2.urlopen("http://localhost:8080/webDemo/login.jsp", url_data)
cj.save(cookieFile, ignore_discard=True, ignore_expires=True)

# login_r2 = opener.open("http://localhost:8080/webDemo/private/pass.jsp", url_data)

print login_r
# print login_r2.read()
