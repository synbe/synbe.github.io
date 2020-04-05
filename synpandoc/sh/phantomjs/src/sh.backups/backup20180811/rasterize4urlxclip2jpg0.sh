 #!/bin/zsh
echo 将剪切板内URL,单个网页,转化为jpg图片格式．微信公众号网页不建议使用！
echo ------------------------------------
URL=$(xclip -o)  #读取剪切板内容
./phantomjs rasterize4url2jpg.js $URL
cp ./src/jpg/* ~/sources/websrc/longimages/phantomjs/

