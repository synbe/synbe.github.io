 #!/bin/zsh
echo 将剪切板内URL,单个网页,转化为ｐｄｆ！
echo ------------------------------------
URL=$(xclip -o)  #读取剪切板内容
URLPDF=$(echo $URL | sed 's/synbox\/index5.html/synbox\/index7pdf.html/')
./phantomjs rasterize4url2pdfa4.js $URLPDF
cp ./src/pdf/* /home2/xun/sources/websrc/pdf/phantomjs/
