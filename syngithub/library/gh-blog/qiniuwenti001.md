% 使用七牛云做图床快速获取外链方法有哪里些?
打开空间,选择复制外链，就不用多说了．

先自己摸索的使用七牛云做图床方法：

1.	用qshell qupload将本地图片(/images文件夹)上传至空间(images)
2. 	用qshell listbucket提取外链(然后qshell batchsign生成私有外链)
3.	用sed生成md文件,用pandoc将md转化成html(附图１)
4.	复制网页上的链接
5.	发布html网页到github:[https://synbe.github.io/](https://synbe.github.io/)

脚本:

    #!/bin/bash  

    ./qshell qupload config
    #上传图片

    ./qshell listbucket images ./list/list.txt
    #提取空间文件列表

    # 获取images空间域名:
    #qshell domains images　
    #oop2y.bkt.clouddn.com

    sed  '/directory/d;s/^/http:\/\/oop2y.bkt.clouddn.com\//g;s/[[:space:]][[:space:]]*/\nLOG::/1'  ./list/list.txt > ./list/list001.txt
    #list.txt文件:
    #删除directory行;行首添加http://．．．;第１个空格符替换成换行符\n和LOG:: 
    #生成图片链接列表

    #sed '1~2!d' ./list/list001.txt > ./list/list002.txt
    #删除偶数行
    sed '/LOG/d' ./list/list001.txt > ./list/list002.txt
    #删除LOG（偶数）行

    echo ------------------列出图片链接-------------------------
    cat ./list/list002.txt
    #列出图片链接

    ./qshell batchsign ./list/list002.txt  > ./list/list003.txt
    #批量根据资源的公开外链生成资源的私有外链

    sed 's/^/![](/g;s/$/)/g' ./list/list003.txt > ./list/list004.txt
    #行首添加![](;行尾添加)

    sed 's/.*/&\n\nURL:\n\n\t&\n\n---\n\n/g;1i  %Qiniu images buckets\n\n---\n\n'  ./list/list004.txt  > ./list/list.md 
    #复制链接到下一行::sed 's/.*/&\n&/' filename
    #所复制的行,换行\n并行首添加tab符\t;第一行前添加标题Qiniu images buckets

    cp ./list/list.md  /home/user/git/bitbucket.org/synbe.bitbucket.io/drafts/posts/md/posts-drafts/imageslist.md
    #复制到...

    cd /home/user/git/bitbucket.org/synbe.bitbucket.io/sh

    sh ./m2drafts.sh
    #运行pandoc生成html

config 文件:

    {
    "src_dir"       :   "./images",
    "bucket"        :   "images",
    "access_key"    :   "FSeqnwxxxxxxxeVKKxBxxLDl5U",
    "secret_key"    :   "B2UuomPATpxxxxxx7kjxxxiT",
    "rescan_local"       :    true
    }

------------

生成的网页截图:附图1:

![](http://oop2yvbin.bkt.clouddn.com/002/948585.png?e=1524370212&token=FSeqnwREGiD86fOBBAr7GreFNeVKKxBCFyULDl5U:oczLgIr7LssPwoyt7Xrr5yzoC7M=)
－－－－－－－－－－－－－－－－－

遇到的问题：

1. 用qshell qupload将本地图片上传为什么不成功？

问题描述:

本地图片保存在~/images/目录下,

images/下还有多个子目录,如001, 00２

用shell qupload将图片上传至七牛空间(如images)

首次上传图片可成功，但此后再往本地目录images添加图片，再次运行qupload，新添加的图片都无法上传到七牛空间中.

详细见:

https://segmentfault.com/q/1010000009156103

**[已解决]:** config 添加:rescan_local设置为true

<!-- 网易云跟帖评论框 start -->
<div id="cloud-tie-wrapper" class="cloud-tie-wrapper"></div>
<script>
  var cloudTieConfig = {
url: document.location.href, 
sourceId: "",
productKey: "da5442dadc4c4813a81c796605822cc0",
target: "cloud-tie-wrapper"
  };
</script>
<script src="https://img1.cache.netease.com/f2e/tie/yun/sdk/loader.js"></script>
<!-- 网易云跟帖评论框 end -->

