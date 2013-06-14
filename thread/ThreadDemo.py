'''
Created on 2012-12-24

@author: k0000010359
'''
from dummy_thread import start_new_thread
def abc(a):
        print(a)
        IOError('unhandle')
        error()

def error():
    tup = (1, 2, 3)
    tup[0] = 0
    print(tup)

if __name__ == '__main__':
    print(start_new_thread(abc, ('234',)))
