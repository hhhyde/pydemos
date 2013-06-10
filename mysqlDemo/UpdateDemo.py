#coding:utf-8
'''
Created on 2011-11-2

@author: ke
'''
import MySQLdb
conn = MySQLdb.Connect(host='localhost', user='root', passwd='123123')
conn.select_db('python')
c = conn.cursor()
c.execute('update test set info="ke" where id=4')
conn.commit()
c.close()
conn.close()
