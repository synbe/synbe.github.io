#!/bin/bash

######################################
cd ../library/md
find  -name "*.md" -print | xargs -i sed -i '/^#/G;s/^\s*$/\n\n/g' {} 
#将所有#其后添加空行#替换空行为\n\n
find  -name "*.md" -print | xargs -i sed -i '/^$/N;/^\n$/D' {} 
# 合并空行
find  -name "*.md" -print | xargs -i sed -i '1s/^#/%/;3s/^######/%/;2d' {}   | sed '1,3s/^%%/%/g' 
# read -n1 -p "Press any key to continue..."


# ######################################
# cd ./library/md 
# ls -d */ | sed 's/\///' | while read category
# do
# echo ++++++++++:$category
# find $category -name "*.md" -print | xargs -i sed -i '/^#/G;s/^\s*$/\n\n/g' {} 
# #将所有#其后添加空行#替换空行为\n\n
# find $category -name "*.md" -print | xargs -i sed -i '/^$/N;/^\n$/D' {} 
# # 合并空行
# find $category -name "*.md" -print | xargs -i sed -i '1s/^#/%/;3s/^######/%/;2d' {}   | sed '1,3s/^%%/%/g' 
# # read -n1 -p "Press any key to continue..."
# done
