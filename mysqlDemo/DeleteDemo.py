#coding:utf-8
'''
Created on 2011-11-2

@author: ke
'''
import MySQLdb
conn = MySQLdb.Connect(host = 'localhost', user = 'root', passwd = '123123')
conn.select_db('python')
c = conn.cursor()
n = c.execute('delete from test where id=1')
print n
conn.commit()
c.close()
conn.close()
