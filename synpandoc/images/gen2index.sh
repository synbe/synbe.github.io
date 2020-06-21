#!/bin/bash  
GURL="../images/"
#上传图片
touch ./library/index.md
echo -e '# Index \n'  > ./library/index.md
ls ./images | while read FOLDER
do
echo -e '# Githubimgs of '$FOLDER '\n' > ./library/$FOLDER.md
echo '1. ['$FOLDER]'(./'$FOLDER'.md.html)' >> ./library/index.md
ls ./images/$FOLDER | while read FILE
do
echo -e '\n![]('$GURL$FOLDER'/'$FILE')' >> ./library/$FOLDER.md
echo -e '\n```![]('$GURL$FOLDER'/'$FILE')```' >> ./library/$FOLDER.md
echo -e '\n---\n' >> ./library/$FOLDER.md
done
#cat ./library/$FOLDER.md
done 

find ./library -name '*.md' -exec  pandoc {} -f markdown+smart -t html+smart -s -H ./src/header.html -o {}.html \;


#http://www.synbe.com/images/library/index.md.html

#firefox  ./library/index.md.html
