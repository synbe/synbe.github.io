 #!/bin/zsh
echo 将剪切板内URL,单个网页,转化为ｐｄｆ．微信公众号网页不建议使用！
echo ------------------------------------
URL=$(xclip -o)  #读取剪切板内容
URLPDF=$(echo $URL | sed 's/synbox\/index5.html/synbox\/index7pdf.html/')
./phantomjs rasterize4url2pdfa4.js $URLPDF
./phantomjs rasterize4url2pdf.js $URLPDF
cp ./src/pdf/* ~/sources/websrc/pdf/phantomjs/
URLJPG=$(echo $URL | sed 's/synbox\/index5.html/synbox\/index7jpg.html/')
./phantomjs rasterize4url2jpg.js $URLJPG
cp ./src/jpg/* ~/sources/websrc/longimages/phantomjs/
