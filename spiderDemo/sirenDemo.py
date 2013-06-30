'''
Created on 2013-6-13

@author: Matthew
'''
import requests
url = 'http://localhost:8080/webDemo/Login'
cookies = dict(webDemo='1231232')

r = requests.get(url, auth=('webDemo','123123'))
print r.text