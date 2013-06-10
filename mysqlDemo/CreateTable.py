#coding:utf-8
'''
Created on 2011-10-25

@author: ke
'''
import MySQLdb
conn = MySQLdb.connect(host="localhost", user="root", passwd="123123")
#---------选择要操作的数据库------------------
conn.select_db("python")
#------------获取指针------------------
cursor = conn.cursor()
#------建表----------
cursor.execute("create table test11(id int,info varchar(100))")
#--------------------
#------删表-----------
#cursor.execute("drop table test11")
#--------------------
cursor.close()
conn.close()
