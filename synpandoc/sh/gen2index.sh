#!/bin/bash
##此脚本：生成目录及文章列表

start=`date +%s`
now=`date +%Y年%m月%d日`
time=更新时间：$(date +%Y年%m月%d日%H时%M分%S秒)'，按文件名排列'
cd ..
###########################################
echo -e '% CATEGORY\n\n###### '$time '\n' > ./library/posts-category/posts-category.md
ls -d ./library/* | sed 's/^.*\///g' | while read category
do
echo $category
echo '1. ['$category'](../posts-lists/'$category'.md.html)'  >> ./library/posts-category/posts-category.md
echo -e '% INDEX\n\n###### '$time '\n' > ./library/posts-lists/$category.md
ls ./library/$category/*.md.html | sed 's/^.*\///g'| while read htmlfiles
do
title=$(sed -n '/<title>/p' ./library/$category/$htmlfiles | sed 's/<title>//g;s/<\/title>//g' | sed 's/ //g')
echo $htmlfiles:$title
echo -e '1. ['$title'](../'$category/$htmlfiles')('$htmlfiles')' >> ./library/posts-lists/$category.md
done
done
###########################################
find ./library/posts-category -name '*.md' -exec  pandoc {} -f markdown+smart -t html+smart -s --toc -H ./src/assets/header_index.html -A ./src/assets/footer_index.html -o {}.html \;
find ./library/posts-lists -name '*.md' -exec  pandoc {} -f markdown+smart -t html+smart -s --toc -H ./src/assets/header_index.html -A ./src/assets/footer_index.html -o {}.html \;
###########################################
echo finish::++++++++++++++++++++
end=`date +%s`
dif=$(($end - $start))
echo 完成时间:$now,   总共耗时$dif秒 运行此脚本需要 $SECONDS 秒  
