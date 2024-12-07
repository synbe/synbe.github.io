#!/bin/zsh

#  将该目录下所有的图片重命名，并生成各个ablums/folder/index.html
start=`date +%s`
now=`date +%Y年%m月%d日`
time=更新时间：$(date +%Y年%m月%d日%H时%M分%S秒)

echo "
<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Transitional//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd\">
<html xmlns=\"http://www.w3.org/1999/xhtml\"><head>
<meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">
<meta name=\"viewport\" content=\"width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=0,viewport-fit=cover\">
<style>
html
{
margin: auto;
}
body
{
/* font-family: 'PingFang SC', 'Noto Sans CJK', 'Source Han Sans', 'Microsoft Yahei', source-han-sans-simplified-c, sans-serif; */
line-height: 140%;
max-width: 1024px;
margin: auto;
padding: 1em 0em;
font-size: 16px;
}
a 
{
color:#0f8050;
}
a:visited
{
color:#0f8050;
}
img
{
display: block;
max-width: 100%;
margin: auto;
padding: 0;
border-radius: 4px;
}

table
{
border: 1px solid #ccc;
margin:1em auto;
margin-left:0em;
}
table tr:nth-child(2n)
{
background-color: #d4d7d0;
}
thead tr th
{
background-color: #d4d7d0;
text-shadow: 1px 1px 0 #fff;
}
caption
{
color: #935417 !important;
border: 1px solid #f2e7ab;
background: #fcffcf ;
}
/*
table tr:nth-child(2n+1) {
background-color: #FFF8D4;
}
*/
pre {
font-size:90%;
background-color: #d9dee6;
color: rgb(4, 7, 34);
border: 1px solid #a5dba5;
border-radius: 4px;
white-space: normal; 
word-break: break-all;
}
code{
font-size:90%;
background-color: #f2f4f7;
color: rgb(4, 7, 34);
border: 1px solid #a5dba5;
border-radius: 4px;
}
blockquote
{
padding: .5em;
color: #fff;
border: 2px solid #fff;
border-radius: 4px;
font-size:1em;
line-height:1.2em;
}
blockquote
{
margin: 10px;
background: #777;
}
/*以下为屏幕适应改变*/
@media screen and (max-width:800px)
{
body
{
width: 100%;
}
}

</style>
</head>
">  index.html

echo "<h1>"$time"</h1>" >> index.html
# 插入图片
# find -name "*.jpg" -o -name '*.png' > listall.txt
find -name "*.jpg" -o -name '*.JPG' -o -name '*.jpeg' -o -name '*.PNG' -o -name '*.png' | sort -f | while read filename 
do 
echo "=:" $filename
# newfilename=${filename//\ /}
# newfilename=${newfilename//\[/}
# newfilename=${newfilename//\]/}
# newfilename=${newfilename//\(/}
# newfilename=${newfilename//\)/}
# newfilename=${newfilename//\【/}
# newfilename=${newfilename//\】/}
# newfilename=${newfilename//（/}
# newfilename=${newfilename//）/}
# newfilename=${newfilename//・/}
# newfilename=${newfilename//：/}
# newfilename=${newfilename//:/}
# newfilename=${newfilename//，/}
# newfilename=${newfilename//,/}
# newfilename=${newfilename//-/}
# newfilename=${newfilename//——/}
# newfilename=${newfilename//_/}
# newfilename=${newfilename//、/}
# newfilename=${newfilename//――/}
# echo "ADD=>" $newfilename
# mv "$filename" "$newfilename"   # 重命名
echo "<hr><img src=\""$filename"\">" >> index.html
done
# 插入MP4
find -name '*.mp4' | sort -f | while read filename 
do 
echo "=:" $filename
echo "<hr><video controls><source src=\""$filename"\"></video>" >> index.html
done
# 插入wmv
find -name '*.wmv'| sort -f | while read filename 
do 
echo "=:" $filename
echo "<hr><a href=\""$filename"\">视频:$filename</a>" >> index.html
done

