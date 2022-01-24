#!/bin/bash  

TODAY=`date +%Y-%m-%d\ %H:%M:%S`
##  生成ablums index
touch ./index.html
cat ./header.html > ./index.html
echo -e '\n<h1>Index</h1>'  >> ./index.html
echo -e '<p>'$TODAY'</p>'  >> ./index.html
echo -e '<hr>\n<ol>'  >> ./index.html
ls ./ablums | while read FOLDER
do
echo -e '<li><a href="./ablums/'$FOLDER'/index.html">'$FOLDER'</a></li>' >> ./index.html
done
echo -e '</ol>\n<hr>'  >> ./index.html

##  生成files index
ls ./ablums | while read FOLDER
do
cat ./header.html > ./ablums/$FOLDER/index.html
echo -e '\n<h1>Index of '$FOLDER '</h1>' >> ./ablums/$FOLDER/index.html
echo -e '<p>'$TODAY'</p>\n<hr>'  >> ./ablums/$FOLDER/index.html
ls ./ablums/$FOLDER/images | while read FILE
	do
	echo -e '<img src="./images/'$FILE'">' >> ./ablums/$FOLDER/index.html
	done
done 