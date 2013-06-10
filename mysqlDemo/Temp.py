#coding:utf-8
'''
Created on 2011-11-2

@author: ke
'''
import MySQLdb
conn = MySQLdb.Connect(host="localhost", user='root', passwd='123123')
conn.select_db('python2')
cur = conn.cursor()
#cur.execute('create table temp(id int ,name varchar(50))')
#cur.execute("insert into temp(id,name) values(22,'aa')")
#cur.execute("create database python2")
cur.execute('drop database python2')
conn.commit()  #必须啊   别忘了
cur.close()
conn.close()
