#coding:utf8
import urllib2
def getLnkByHTML(content):
    import re
    #定制化的一个正则表达式
    p=re.compile('.*.html')
    #在一个字符串中找到所有匹配的内容，以list形式返回全部
    matchs=p.findall(content)
    print matchs

def getContentbyurl(url,charset):
    return urllib2.urlopen(url).read().decode(charset,'ignore').encode('utf8')

def getLnkByUrl(url,charset='gbk'):
    return getContentbyurl(getLnkByHTML(url),charset)

if __name__=='__main__':
    print getLnkByUrl('http://club.jd.com/bbs/404379-3-1-4.html')