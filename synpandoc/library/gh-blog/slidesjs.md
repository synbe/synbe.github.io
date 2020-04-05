% SlidesJS基本使用方法和官方文档解释
 Jquery幻灯片插件 Jquery相册插件】 

 Slides – 是一个简单的，容易定制和风格化，的jQuery幻灯片插件。

Slides提供褪色或幻灯片过渡效果，图像淡入淡出，图像预压，自动生成分页，循环，自动播放的自定义等很多选项。

用Slides插件，你可以随机播放幻灯片，设定那一套您想要开始幻灯片。它附带充分的说明和示例。

DEMO地址：http://slidesjs.com/

官网地址：http://slidesjs.com/

下载地址：http://slidesjs.com/downloads/slides.zip

#### 基本的HTML结构

```html
<div id="slides">
  <div class="slides_container">
    <div>
      <h1>Slide 1</h1>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
    </div>
    <div>
      <h1>Slide 2</h1>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
    </div>
    <div>
      <h1>Slide 3</h1>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
    </div>
    <div>
      <h1>Slide 4</h1>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
    </div>
  </div>
</div>
```

#### 基本CSS代码

```css
<style type="text/css" media="screen">
  .slides_container {
    width:470px;
    height:170px;
  }
  .slides_container div {
    width:470px;
    height:170px;
    display:block;
  }
</style>    
```

#### 基本的初始化JavaScript代码

```js
<script>  
  $(function(){  
    $("#slides").slides();  
  });  
</script> 
```

#### 使用步骤

1、引用以下的js和css文件

```
<link rel="stylesheet" type="text/css" href="css/wowwindow.css">
<script type="text/javascript" src="js/jquery.min.js"></script>
<script type="text/javascript" src="js/jquery.wowwindow.min.js"></script>
```

2、加入以下JS代码

```
$(function(){
    $(/’#slides/’).slides({
    preload: true,
    preloadImage: /’img/loading.gif/’,
    play: 5000,
    pause: 2500,
    hoverPause: true
    });
});
```

    参数配置

```
参数名 参数说明 可选值 默认值
preload 在幻灯片播放中是否预加载指定图片 true或false false
preloadImage 预加载图片的路径 路径字符串 /img/loading.gif
container 幻灯片容器的ID ID字符串 slides_container
generateNextPrev 是否自动生成 next/prev 按钮 true或false false
next next 按钮的样式名 字符串 next
prev prev 按钮的样式名 字符串 prev
pagination 如果你不使用分页，可以设置为flase，但不是必须的 true或false
generatePagination 是否自动生成分页 true或false true
paginationClass 分页的样式名 字符串 pagination
currentClass 当前页码的样式名 字符串 current
fadeSpeed 淡入淡出动画的速度 整数，单位为毫秒 350
fadeEasing 淡入淡出的效果 字符串，必须要包含 Easing plugin
slideSpeed 设置幻灯片滑动的毫秒时间 整数 350
slideEasing 滑动的效果 字符串，必须要包含 Easing plugin
start 设置从第几张幻灯片开始 整数 1
effect 设置幻灯片next/prev切换和分页切换方式的效果 字符串 slide
crossfade Crossfade images in a image based slideshow true或false false
randomize 是否随机切换效果 true或false false
play 自动播放切换幻灯的时间间隔 整数 0不自动切换
pause 当点击 next/prev或分页按钮后暂停多少毫秒才切换图片 整数
hoverPause 当鼠标移动到图片上的时候，幻灯片切换是否暂停 true或false false
autoHeight 是否自动调整高度 true或false false
autoHeightSpeed 设置自动调整高度的时间毫秒数 整数 350
bigTarget Set to true and the whole slide will link to next slide on click true或false false
animationStart 当动画开始时调用的函数 函数
animationComplete 当动画结束时调用的函数 函数
```

#### 使用示例：

```
<!doctype html>
<head>
  <style>
    /* Prevents slides from flashing */
    #slides {
      display:none;
    }
  </style>

  <script src="http://code.jquery.com/jquery-latest.min.js"></script>
  <script src="jquery.slides.min.js"></script>

  <script>
    $(function(){
      $("#slides").slidesjs({
        width: 940,
        height: 528
      });
    });
  </script>
</head>
<body>
  <div id="slides">
    <img src="http://placehold.it/940x528">
    <img src="http://placehold.it/940x528">
    <img src="http://placehold.it/940x528">
    <img src="http://placehold.it/940x528">
    <img src="http://placehold.it/940x528">
  </div>
</body>
```