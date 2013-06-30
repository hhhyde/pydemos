#coding=utf-8  
'''
Created on 2013-6-12

@author: Matthew
'''
import re  
import urllib  
import urllib2  
import cookielib  
import urllib,urllib2,cookielib  
import re  
class xiaobai:  
    post_data=""#登陆提交的参数  
    def __init__(self):  
        '''''初始化类，并建立cookies值'''  
        cj = cookielib.CookieJar()  
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))  
#        opener.addheaders = [('User-agent', 'Opera/9.23')]  
        urllib2.install_opener(opener)  
  
    def login(self,loginurl,bianma):  
        '''''模拟登陆'''  
        req = urllib2.Request(loginurl,self.post_data)  
        _response = urllib2.urlopen(req)  
        _d=_response.read()  
        _d =_d.decode(bianma)  
        return _d  
  
    def getpagehtml(self,pageurl,bianma):  
        '''''获取目标网站任意一个页面的html代码'''  
        req2=urllib2.Request(pageurl)  
        _response2=urllib2.urlopen(req2)  
        _d2=_response2.read()  
        _d2 =_d2.decode(bianma)  
        return _d2  
if __name__=="__main__":  
        x=xiaobai()  
        #参递一个post参数  
        x.post_data=urllib.urlencode({'account':'123123','passwd':'123123456','op':'login'})  
        y=x.login("http://localhost:8080/webDemo/login.jsp","utf-8")#登陆
        print y
        #获取一个页面的html并输出  
#        print x.getpagehtml("http://www.lvye.org/userinfo.php?uid=111111","utf-8")  