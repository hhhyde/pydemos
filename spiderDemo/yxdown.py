#coding:utf8
'''
        只抓取了仙剑5前传的攻略，一共有31个页面，命名格式都是/gonglue/82039_*.html这种
        只有第一个是/gonglue/82039.html
'''
import urllib2
content=urllib2.urlopen('http://www.yxdown.com/gonglue/82039.html').read()
content= content.decode('gbk').encode('utf8')
#print content
import re
#定制化的一个正则表达式
p=re.compile(r'gonglue/82039_?\d{0,}.html')
#在一个字符串中找到所有匹配的内容，以list形式返回全部
matchs=p.findall(content)
#print matchs
#给每个链接加上前缀，并且转成set去重
links=set(map(lambda x:'http://www.yxdown.com/'+x,matchs))
import urllib2
for link in links:
  #以每个链接的最后一个/后面的内容为文件名
  tempfile=open('e:/temp/yxdown/'+link.split('/')[-1],'w')
  content=urllib2.urlopen(link).read()
  tempfile.write(content)
  tempfile.close()