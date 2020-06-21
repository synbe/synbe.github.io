#!/bin/zsh
echo 截图并保存
IMGNAME=scrot`date +%Y%m%d%H%M%S` 
#scrot -s ./images/scrot/$IMGNAME.png 
import ./images/scrot/$IMGNAME.png 
sh ./gen2index.sh
