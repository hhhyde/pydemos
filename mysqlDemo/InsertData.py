#coding=utf-8
'''
Created on 2011-10-25

@author: ke
'''
import MySQLdb  
  
#建立和数据库系统的连接  
conn = MySQLdb.connect(host='localhost', user='root', passwd='123123')  
#选择数据库  
conn.select_db('python');
#获取操作游标  
cursor = conn.cursor()
#value = [1, "inserted ?"];
#插入一条记录  
sql = "insert into test values(111,'aaa')"
#param = (1, "inserted")
n = cursor.execute(sql)
print n

#values = []  
#  
  
#生成插入参数值  
#for i in range(20):  
#    values.append((i, 'Hello mysqldb, I am recoder ' + str(i)))  
#插入多条记录  
  
#cursor.executemany("""insert into bb values(%s,%s) """, values);  
  
#关闭连接，释放资源  
conn.commit()
cursor.close(); 
conn.close()
