 #!/bin/zsh
echo 将剪切板内URL,单个网页,转化为ｐｄｆ．微信公众号网页不建议使用！
echo ------------------------------------
URL=$(xclip -o)  #读取剪切板内容
./phantomjs rasterize4url2pdf.js $URL
cp ./src/pdf/* ~/sources/websrc/pdf/phantomjs/
