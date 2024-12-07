#!/bin/bash  

TODAY=`date +%Y-%m-%d\ %H:%M:%S`
##  生成ablums index
touch ./index.html
cat ../src/index_header.html > ./index.html
echo -e '\n<h1>Index</h1>'  >> ./index.html
echo -e '<p>'$TODAY'</p>'  >> ./index.html
echo -e '<hr>\n<ol>'  >> ./index.html
ls ./ablums | while read FOLDER
do
echo -e '<li><a href="./ablums/'$FOLDER'/index.html">'$FOLDER'</a></li>' >> ./index.html
done
echo -e '</ol>\n<hr>'  >> ./index.html
