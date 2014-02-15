# coding:UTF8
'''
Created on 2014-1-18

@author: Matthew
'''
#import urllib, urllib2, cookielib
#class SIS(object):
#    def __init__(self):
#        pass;
#    def retrieve(self):
#        cj = cookielib.CookieJar()  
#        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
#        opener.addheaders=[('User-Agent','Chrome/32.0.1700.76')]
#        urllib2.install_opener(opener) 
#        loginUrl = 'http://67.220.90.30/bbs/logging.php?action=login&';
#        postdata = urllib.urlencode({'formhash': '29ceb510', 'referer': 'index.php', 'loginfield':
#                            'username', 'username': 'tiexueshitai', 'password': '333333', 'questionid': '0', 'answer': '', 'cookietime': '2592000', 'loginmode': '', 'styleid': '', 'loginsubmit': ''})
#        content = urllib2.urlopen(loginUrl,postdata).read()
#        print content.decode('gbk')
#
#        
##        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
##        urllib2.install_opener(opener)
##        req = urllib2.Request('http://67.220.90.30/bbs/index.php')
##        req.add_header('Cookie', '4wQYoE')
##        content = urllib2.urlopen(req).read()
#if __name__ == '__main__':
#    sis = SIS()
#    sis.retrieve()
from loginform import fill_login_form
import requests
url = "https://github.com/login"
r = requests.get(url)
fill_login_form(url, r.text, "hhhyde", "333333")
