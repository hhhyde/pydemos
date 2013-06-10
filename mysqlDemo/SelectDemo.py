# coding:utf-8
'''
Created on 2011-11-1

@author: ke
'''
import MySQLdb
conn = MySQLdb.connect(host='localhost', user='root', passwd='123123')
conn.select_db('python')
cur = conn.cursor()
cur.execute('select * from test;')
# cur.execute('show tables;')
# 。description=get column name
for de in cur.description:
    print de[0] + '\t',
print ''
for data in cur.fetchall():
    for d in data:
        print '%s\t' % d,
    print ''
cur.close()
conn.close()

