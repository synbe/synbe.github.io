 #!/bin/zsh
#  DATE=`date +%Y%m%d%H%M%S`
  # read -p "请输入网址)：" URL
#URL=$(zenity --entry --title "请输入网址" --text "请输入网址URL(含文件后缀名如.jpg)" --width=400 --height=200)
# URL=$(whiptail --title "网址" --inputbox "请输入网址" 10 80 3>&1 1>&2 2>&3)
URL=$(xclip -o)  #读取剪切板内容
./phantomjs rasterize4url2pdfa4.js $URL


