% 如何实现shell中使用sed，while循环等替换文件中的链接?
<h6>2017-05-14</h6>

假设

 file1文件中含有若张图片链接，每个图片链接独占一行

    #cat file1
    文字文字文字文字
    <img src="http://www.aaa.com/01.jpg"/>
    文字文字文字
    <img src="http://www.aaa.com/03.jpg"/>
    文字文字文字文字
    <img src="http://www.aaa.com/33.jpg"/>
    文字文字文字文字
    <img src="http://www.aaa.com/55.jpg"/>
    文字文字文字文字
    ．．．

 file２文件中含有同样数量图片链接列表,每个图片链接独占一行

    #cat file2 
    http://www.bbb.com/23.jpg
    http://www.bbb.com/34.jpg
    http://www.bbb.com/55.jpg
    http://www.bbb.com/78.jpg
    ．．．

将file1中所有图片链接，按files2顺序依次替换，结果如下file3:

    #cat file3
    文字文字文字文字
    <img src="http://www.bbb.com/23.jpg"/>
    文字文字文字
    <img src="http://www.bbb.com/34.jpg"/>
    文字文字文字文字
    <img src="http://www.bbb.com/55.jpg"/>
    文字文字文字文字
    <img src="http://www.bbb.com/78.jpg"/>
    文字文字文字文字
    ．．．

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

