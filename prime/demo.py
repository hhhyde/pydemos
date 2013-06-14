'''
Created on 2013-3-4

@author: k0000010359
'''
def eratosthenes():
    import itertools
    D={}
    for q in itertools.count(2):
        p=D.pop(q, None)
        if p is None:
#            yield q
            D[q*q]=q
        else:
            x=p+q
            while x in D:
                x+=p
            D[x]=p
        if q>20:return D

if __name__=='__main__':
    print(eratosthenes())
