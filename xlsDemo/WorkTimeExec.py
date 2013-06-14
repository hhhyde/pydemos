#coding:utf-8
'''
Created on 2012-12-27

@author: hhhyde
'''
def exec123(filepath, place, name):
    '''
    filepath:待处理xls绝对路径
    palce:办公场地
    name:待处理对象的姓名
    '''
    from pyExcelerator import parse_xls
    #打开xls
    a=parse_xls(filepath)
    from datetime import timedelta
    worktime=timedelta(hours = int(0))
    stand_worktime=9.5
    pps={}#{日期:记录}
    for temp_sheet in a:
        if place==temp_sheet[0]:
            palce_sheet=temp_sheet
            palce_data=palce_sheet[1]
            #整理有效数据,取出日期和打卡记录
            for k, v in palce_data.items():
                if name==v:
                    #取出每条打卡记录的日期
                    sign_date=palce_data[(k[0], k[1]+2)]
                    #取出每条打卡记录
                    sign_sign=palce_data[(k[0], k[1]+3)]
                    #过滤掉无效数据(入周末加班不计入工时)
                    if NoWeekend(sign_date):
                        pps[sign_date]=sign_sign
            #处理数据
            for curdate, sign in pps.items():
                print('%s\n%s'%(curdate, sign))
                #sign_points=[8:01,8:04,9:22,18:22]类似这样的记录
                sign_points=sign.split(' ')
                #max='18:22',取最后一条记录
                max=sign_points[len(sign_points)-1]
                #max=(18,22),小时和分钟分离
                max=max.split(':')
                #min='8:01'
                min=sign_points[0]
                #min=(8,01)
                min=min.split(':')
                print('工时%s'%Exec_worktime(min, max))
                worktime+=Exec_worktime(min, max)
                print('-----------------')
    #根据打卡记录条数来决定工作天数
    onworkdays=len(pps)
    #正常工时(工时最低标准,必须达到)
    onworkdays=timedelta(hours = onworkdays*stand_worktime)
    #判断是否欠工时
    if onworkdays>worktime:
        return '欠工时--->%s'%(onworkdays-worktime)
    else:
        return '剩余工时--->%s'%(worktime-onworkdays)

def Exec_worktime(min = None, max = None):
    '''
    min:第一次打卡记录
    max:最后一次打卡记录
    '''
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
#    print(minus_wt)
#    print(positive_wt)
    worktime=positive_wt-minus_wt
    return worktime

def NoWeekend(date):
    '''
    date:传入时间,格式类似'2013-02-22'
    '''
    import datetime
    a=date.split('-')
    weekday=datetime.date(int(a[0]), int(a[1]), int(a[2]))
#    if weekday.isoweekday()<=5:
#        return True
#    else:
#        return False
#    
    return True if weekday.isoweekday()<=5 else False

if __name__=='__main__':
#    print(NoWeekend('2013-03-02'))
    print(exec123(u'F:/深圳0301-0322上班打卡记录.xls', u'岗头10、11楼', u'陈雨婷'))
   # print(exec123(u'F:/深圳0301-0322上班打卡记录.xls', u'德维森', u'柯江涛'))
    # print(exec123(u'F:/深圳0301-0322上班打卡记录.xls', u'德维森', u'张南'))
    # print(exec123(u'F:/深圳0301-0322上班打卡记录.xls', u'德维森', u'曾晶'))
