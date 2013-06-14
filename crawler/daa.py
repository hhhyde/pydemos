'''
Created on 2013-6-13

@author: k0000010359
'''
import requests
r=requests.get('http://localhost:8080/webDemo/login.jsp', auth = ('user', 'pass'))
print r.status_code
print r.text
