#!/bin/bash
declare date=`date +%Y%m%d%H%M`
declare path=/home/hhhyde/kk/gitbak/$date

wget -P $path/try_git https://github.com/hhhyde/try_git/archive/master.zip
wget -P $path/mysite https://github.com/hhhyde/mysite/archive/master.zip
wget -P $path/mysite https://github.com/hhhyde/mysite/archive/dev.zip
wget -P $path/pydemos https://github.com/hhhyde/pydemos/archive/master.zip
wget -P $path/pydemos https://github.com/hhhyde/pydemos/archive/dev.zip

cd $path
tar -cf $path.tar *
rm -r $path