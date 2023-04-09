#!/bin/zsh

#  将该目录下所有的图片重命名，并生成各个ablums/folder/index.html
start=`date +%s`
now=`date +%Y年%m月%d日`
time=更新时间：$(date +%Y年%m月%d日%H时%M分%S秒)

echo "
<style type="text/css">
body {
margin:auto;
padding: 1em 0.5em 1em 0.5em;
border: 1px solid  #CED7EA;
width:800px;
}
img {
display: block;
margin: 0 auto;
float: center;
border: 1px solid #fff;
border-radius: 4px;
max-width: 100%;
}
h1,p{
margin:auto;
text-align:center;
}
</style>
" >  index.html

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

