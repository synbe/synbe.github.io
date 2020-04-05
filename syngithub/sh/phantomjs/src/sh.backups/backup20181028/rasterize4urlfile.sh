 #!/bin/zsh
COUNT=
cat ./src/urlfile | while read URL
do
COUNT=$[$COUNT+1]
./phantomjs rasterize4url2jpg.js $URL
./phantomjs rasterize4url2pdf.js $URL
echo $URL >> ./src/urlall
echo "___________________________"
done

