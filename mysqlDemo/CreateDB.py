#coding=utf-8
'''
Created on 2011-10-23

@author: ke
'''
import MySQLdb
#建立连接和数据库系统的连接
conn = MySQLdb.connect(host="localhost", user="root", passwd="123123")
#获取操作游标
cursor = conn.cursor()
#执行SQL，创建一个数据库
cursor.execute("create database if not exists books")
#cursor.execute('drop database if exists djangotest')
cursor.close()
