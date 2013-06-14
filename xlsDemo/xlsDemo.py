#coding:utf-8
'''
Created on 2012-12-27

@author: k0000010359
'''
#from openpyxl import load_workbook
#import xmllib
#filename = 'f:/uuu1.xls'
#if filename[-4:] == 'xlsx':
#    wb = load_workbook(filename)
#    print len(wb.get_active_sheet().columns())
#elif filename[-4:] == '.xls':
#    import
#else:
#    print 'other'
#print (dir())
#import xml.sax.xmlreader
#print (dir())


#指定单元格
#print a[0][1][(98, 1)] 
#deweishen=a[0][1]
#for k, v in deweishen.items():
#    if '柯江涛'==v:
##        print 'v1|v2|v3|v4|v5'%()
#        #格式化输出
#        print '%s|%s|%s|%s|%s'%(deweishen[(k[0], 0)], deweishen[(k[0], 1)], deweishen[(k[0], 2)], deweishen[(k[0], 3)], deweishen[(k[0], 4)])

def exec123(filepath, place, name):
    from pyExcelerator import parse_xls
    a=parse_xls(filepath)
    from datetime import timedelta
    worktime=timedelta(hours = int(0))
    onworkdays=None
    for temp_sheet in a:
        if place==temp_sheet[0]:
            deweisen_sheet=temp_sheet
            deweisen=deweisen_sheet[0]
            deweisen_data=deweisen_sheet[1]
    #        print(deweisen_data)
    #        print(type(deweisen_data))
            pos_signs=[]
            signs=[]
            for k, v in deweisen_data.items():
                if name==v:
    #                print k
                    pos_sign=k[0], k[1]+3
    #                print pos_sign
                    pos_signs.append(pos_sign)
    #        print(pos_signs)
            for k, v in deweisen_data.items():
                if k in pos_signs:
                    signs.append(v)
            onworkdays=len(signs)
            for sign in signs:
                print(sign)
                sign_points=sign.split(' ')
    #            print(sign_points[len(sign_points)-1])
                max=sign_points[len(sign_points)-1]
                max=max.split(':')
    #            print(type(max[0]))
                min=sign_points[0]
                min=min.split(':')
                print('---%s----'%exec_worktime(min, max))
                worktime+=exec_worktime(min, max)
                print('-----------------')
    onworkdays=timedelta(hours = onworkdays*9.5)
#    print('aaaaaa%saaaaa'%onworkdays)
    if onworkdays>worktime:
        return '欠工时--->%s'%(onworkdays-worktime)
    else:
        return '剩余工时--->%s'%(worktime-onworkdays)

def exec_worktime(min = None, max = None):
    from datetime import timedelta
    max=timedelta(hours = int(max[0]), minutes = int(max[1]))#最后打卡时间
    min=timedelta(hours = int(min[0]), minutes = int(min[1]))#第一次打卡时间
    eight=timedelta(hours = 8)#上班时间
    off=timedelta(hours = int(18))#18点
    nine=timedelta(hours = int(9))#9点
    workout=timedelta(hours = int(17), minutes = 30)#17:30
    worktime=timedelta(hours = int(0))#默认
    minus_wt=timedelta(hours = int(0))#负工时,默认
    positive_wt=timedelta(hours = 9, minutes = 30)#正工时,默认
#    #正常情况
#    if min<nine:
#        worktime=max-min
#    #17:30之前打卡
#    if min>workout:
#        #最后一次打卡在18:00之前打卡不算工时
#        if max<=off:
#            pass
#        #18:00之后打卡
#        else:
#            worktime=max-off

    #第一次打卡在8:00后超出时间计入负工时,9点后不计,使用忘打卡
    if min>eight and min<nine:
        minus_wt=min-eight
    #第一次打卡在8:00前,0工时
    else:
        pass
    #最后打卡时间在18点后剩余时间计入正工时
    if max>off:
        positive_wt+=max-off
    #否则不计入正工时
    else:
        pass
    print(minus_wt)
    print(positive_wt)
    worktime=positive_wt-minus_wt

    return worktime

if __name__=='__main__':
    print(exec123('F:/123.xls', '德维森', '夏伟'))
