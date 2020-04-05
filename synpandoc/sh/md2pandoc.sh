#!/bin/zsh
start=`date +%s`
now=`date +%Y年%m月%d日`
cd ..
###########################################
#find ./library/md -name '*.md' -exec  pandoc {} -f markdown+smart -t html+smart -s --toc -H ./src/assets/header_index.html -A ./src/assets/footer_index.html -o {}.html \;

#find ./library/md -name '*.md' -exec pandoc {} -f markdown+smart -t html+smart -s --toc -H ./src/assets/header_single_green.html -A ./src/assets/footer_single.html -o {}.html \;
find ./library/md -name '*.md' -exec pandoc {} -f markdown+smart -t html+smart -s --toc -H ./src/assets/header_single_blue.html -A ./src/assets/footer_single.html -o {}.html \;

###########################
echo finish::++++++++++++++++++++
end=`date +%s`
dif=$(($end - $start))
echo 完成时间:$now,   总共耗时$dif秒 运行此脚本需要 $SECONDS 秒  
