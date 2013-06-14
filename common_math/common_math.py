#coding:utf-8
'''
Created on 2013-2-4

@author: k0000010359
'''
'''
阶乘
'''
def factorial(n):
    if n<2:
        return n
    else:
        return n+factorial(n-1)

if __name__=='__main__':
    print factorial(4)
