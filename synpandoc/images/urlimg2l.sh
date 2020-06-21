#!/bin/zsh
echo 从互联网上抓取一个资源并保存
IMGNAME=urlimg`date +%Y%m%d%H%M%S` 
IMGURL=$(xclip -o)  #读取剪切板内容
wget -O $IMGNAME.png $IMGURL
mv ./$IMGNAME.png ./images/urlimg/
feh ./images/urlimg/$IMGNAME.png 
sh ./gen2index.sh
