'''
Created on 2013-6-12

@author: Matthew
'''
import urllib, urllib2, cookielib

cookie = {"t": "cfa92393bd91a458dcb31689e35d9d2e3"}
# Get this session ID in Chrome: Right click page -> Inspect elements -> Resources
cookie = "".join(x + "=" + cookie[x] + ";" for x in cookie)

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
urllib2.install_opener(opener)
req = urllib2.Request("http://www.renren.com/123456789/profile")
req.add_header('Cookie', cookie)
content = urllib2.urlopen(req).read()

with open("page.htm", "w") as f:
    f.write(content)