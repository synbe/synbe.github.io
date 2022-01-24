#!/bin/bash
#echo ========================Rsync Files 同步以下文件夹 [exclude '.git']==================  
#echo 同步:不删除目标目录中存在的文件,同名文件内容覆盖!          
#rsync -vzrtopg --progress --exclude '.git' /run/media/xun/45941f25-3467-41dc-991a-7b475e40750f/home2/xun/git/bitbucket.org/synbe.bitbucket.io/github.com/synbe.github.io/ \
#/run/media/xun/45941f25-3467-41dc-991a-7b475e40750f/home2/xun/git/.github.com/synbe.github.io/
#cd /run/media/xun/45941f25-3467-41dc-991a-7b475e40750f/home2/xun/git/.github.com/synbe.github.io/
echo ——————————准备push本目录下的所有文件—————————————————————————
git pull origin master
git checkout  master
git add --all
today=`date +%Y-%m-%d/%H:%M:%S`
git commit -a -m "提交时间:$today"
git push origin master
echo —————————————————————完毕！—————————————————————————————————
# read -n1 -p "Press any key to continue..."
