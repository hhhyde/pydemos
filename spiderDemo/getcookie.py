'''
Created on 2013-6-12

@author: Matthew
'''
import urllib2  
import cookielib  
cookie = cookielib.CookieJar()  
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))  
response = opener.open('http://www.0618.tv')  
for item in cookie:  
    print 'Name = '+item.name  
    print 'Value = '+item.value  