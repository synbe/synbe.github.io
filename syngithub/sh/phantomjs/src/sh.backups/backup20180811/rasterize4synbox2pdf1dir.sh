#!/bin/bash
# 将library/XXX目录下所有文章转为PDF,把此脚本放到library/XXX目录下
echo 1.同步建立pdf/library下的文件夹
echo ---------------------------------------------------------------------------------------
DIR_MD=$(ls ~/git/bitbucket.org/synbe.bitbucket.io/synbox/library/  -F | sed -n '/\/$/{s/\/$//;p}')
for MKDIR in $DIR_MD; do
if [ ! -d ~/sources/websrc/pdf/library/"$MKDIR" ]; then
mkdir ~/sources/websrc/pdf/library/"$MKDIR"
fi
done

echo 2.在批量将当期library/ｘｘｘ目录下所有文章转为PDF,富含图片的内容建议转为PDF.
echo ---------------------------------------------------------------------------------------
DATE=`date +%Y%m%d-%H%M%S`
DIR=$(pwd |  sed 's/^.*\///')     #显示当前目录
ls *.md  | sed 's/.md//g' > ./filelist
cat ./filelist | while read FILENAME
do
TITLE=$(sed -n '1p' ./$FILENAME.md | sed  's/[[:space:]]//g;s/\n//;s/^#//g;')
echo $FILENAME.md:$TITLE
FILEPATH=file:///home/xun/git/bitbucket.org/synbe.bitbucket.io/synbox/index7.html?name=$DIR:$FILENAME
../../sh/rasterize/phantomjs ../../sh/rasterize/rasterize4synbox2pdfa4.js $FILEPATH ~/sources/websrc/pdf/library/$DIR/$TITLE'_a4'.pdf
done

