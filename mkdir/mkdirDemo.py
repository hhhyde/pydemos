#coding:gbk
import os
ff = open('F:/11.txt', 'r')
for f in ff.readlines():
    os.mkdir('f:/321/' + f.replace('\t', '').strip()),
ff.close()
#s='F:/'
#f=u"%sdd"%s
#os.mkdir(f)

#for i in range(1, 38):
#    os.mkdir('f:/OCS R002C02LG0309/'+str(i))
