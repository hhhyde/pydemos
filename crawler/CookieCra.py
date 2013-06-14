'''
Created on 2013-6-9

@author: k0000010359
'''
import cookielib, urllib2, urllib
import math
cj=cookielib.LWPCookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
data={"account":'acc', "passwd":'pass'}
print 'login to get cookies'
url1=r'http://localhost:8080/webDemo/login.jsp'
url2=r'http://localhost:8080/webDemo/pass.jsp'
data=urllib.urlencode(data)
content=urllib2.urlopen(url1, data)
content=opener.open(url2).read()
print(content)
cj.save('d:/somecookie')

def aa(x):
    return str(math.pow(x, 3))[:-2]+'|'

#print(aa(2))
ab=[4, 5, 2, 1, 6, 4]
v=''.join([aa(x) for x in ab])
print v
