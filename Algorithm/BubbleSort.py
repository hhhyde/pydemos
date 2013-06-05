#coding:utf8
'''
Created on 2013-5-30

@author: Matthew
'''
a=[1,23,4,2134,45,15,213,21,412,3,12,3124,424]

for i in xrange(len(a)-2):
    for j in xrange(i,len(a)-1):#从i开始到数组最后一位
        if a[i]>a[j+1]:
            a[i],a[j+1]=a[j+1],a[i]
            
print a