#!/bin/bash  
#上传图片
TODAY=`date +%Y-%m-%d\ %H:%M:%S`
touch ./index.html
cat ../src/index_header.html > ./index.html
echo -e '\n<h1>Index</h1>'  >> ./index.html
echo -e '<p>'$TODAY'</p>'  >> ./index.html
echo -e '<hr>\n<ol>'  >> ./index.html

ls ./attachments | while read FILE
do
echo -e '<li><a href="./attachments/'$FILE'">'$FILE'</a></li>' >> ./index.html
done
echo -e '</ol>\n<hr>'  >> ./index.html