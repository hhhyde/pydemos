'''
Created on 2013-6-13

@author: k0000010359
'''
import cookielib, urllib2, urllib
cj=cookielib.LWPCookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
data={'tbUserName':'hhhyde', 'tbPassword':'333333', 'btnLogin':'%E7%99%BB++%E5%BD%95', 'txtReturnUrl':'http%3A%2F%2Fpassport.cnblogs.com%2F'}
url=r'http://home.cnblogs.com/'
url_req=urllib2.Request(url, urllib.urlencode(data))
content=opener.open(url_req).read()
print(content)
cj.save('d:/somecookie')
