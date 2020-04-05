#!/bin/bash
#将library/所有目录下所有文章转为PDF
    ls -d ../../library/* | sed 's/^.*\///g' | while read DIR
    do
    # DIR=$(pwd |  sed 's/^.*\///')     #显示当前目录
    ls ../../library/$DIR/*.md  | sed 's/.md//g;s/^.*\///g' > ../../library/$DIR/filelist
    echo 1.==========当前library/$DIR目录下所有文章:
    cat  ../../library/$DIR/filelist
    echo 2.__________转为PDF,富含图片的内容建议转为PDF.
	    cat ../../library/$DIR/filelist | while read FILENAME
	    do
	    TITLE=$(sed -n '1p' ../../library/$DIR/$FILENAME.md | sed  's/[[:space:]]//g;s/\n//;s/^#//g;')
	    echo '文件名：'$DIR'/'$FILENAME'.md | 标题：'$TITLE
	    FILEPATH=file:///home/xun/git/bitbucket.org/synbe.bitbucket.io/synbox/index7.html?name=$DIR:$FILENAME
	    ../../sh/rasterize/phantomjs ../../sh/rasterize/rasterize4synbox2pdfa4.js $FILEPATH ~/sources/websrc/pdf/library/$DIR/$TITLE'_a4'.pdf
	    done

    done
