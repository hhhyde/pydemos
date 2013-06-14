#coding:utf8
import sgmllib
from sgmllib import SGMLParser
import urllib2

class ss(SGMLParser):
    def handle_a(self, tag, method, attrs):
        SGMLParser.handle_starttag(self, tag, method, attrs)
        print('a')
data = urllib2.urlopen('F:/54.htm').read()
#ss.feed(data)
#ss.close()
print(data)
