#!/bin/bash
#拿到当前日期 如20130819
declare today=`date +%Y%m%d`
declare todaydir=/home/hhhyde/huishouzhan/$today
#如果不存在今天的文件夹则新建一个
if [ ! -d $todaydir ];then
	mkdir $todaydir
fi
#移进去
mv `pwd`/$1 $todaydir
