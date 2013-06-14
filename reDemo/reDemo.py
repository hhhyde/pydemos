'''
Created on 2013-5-8

@author: k0000010359
'''
import re
str1='2134213412'
str2='2gew2ada'
print re.match(r'^\d+$', str2).string
