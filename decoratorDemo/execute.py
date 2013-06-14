#coding:utf-8
#'''
#Created on 2013-1-5
#
#@author: k0000010359
#'''
import timeit
import functools

def foo1():
    print(223)

def timeiw(bb):
    @functools.wraps(bb)
    def aa():
        start = timeit.default_timer()
        bb()
        print(timeit.default_timer() - start)
    return aa

######写法1##########
@timeiw
def foo():
    print(123)
#####################
########写法2##########
#def foo():
#    print 123
#
#foo = timeiw(foo)
##################

foo()

#class Rabbit(object):
#
#    def __init__(self, name):
#        self._name = name
#
#    @staticmethod # 静态方法
#    def newRabbit(name):
#        return Rabbit(name)
#
#    @classmethod # 类方法
#    def newRabbit2(cls):
#        return Rabbit('')
#
#    @property # 类方法转成    属性
#    def name(self):
#        return self._name
#
#a = Rabbit.newRabbit2('aa').name
#print a
