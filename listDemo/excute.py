'''
Created on 2013-1-31

@author: k0000010359
'''
ser={'log':[{1:'a'}, {2:'b'}, {3:'c'}]}
l=ser['log']
b=l
l.insert(0, {0:'d'})
print 'old', ser
l=l[:3]
print 'new', ser
