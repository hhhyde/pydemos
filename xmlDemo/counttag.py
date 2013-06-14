'''
Created on 2013-4-10

@author: k0000010359
'''
from xml.sax.handler import ContentHandler
from xml import sax
import sys

class handclass(ContentHandler):
    def __init__(self):
        self.tags={}
    def startElement(self, name, attrs):
        self.tags[name]=self.tags.get(name, 0)+1

parser=sax.make_parser()
handler=handclass()
parser.setContentHandler(handler)
parser.parse('f:/temp/busconfig.xml')
for k, v in handler.tags.items():
    print '%40s:%4s'%(k, v)
