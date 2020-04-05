% 精彩博文
# Markdown+Pandoc，打通写作界的任督二脉！

    Author Duqi
    Date : 2013.5.25

### 前言

Markdown+Pandoc，可以把自己的写作内容，变成世界上已有的任何格式的文件，包括很炫的slide，html5。没有人（或者我没看到）总结过这些内容，导致我走了很多弯路才最终打通任督二脉，特此纪念。

了解Markdwon以后，我的写作世界，只有它；看到Pandoc格式转换以后，对生成的slide和pdf羡慕的不行。那时，自己期望以后的写作是这样的：首先用Markdown把自己的想法写下来；其次，通过Pandoc，把写好的Markdown文件，转换成Slide或者PDF。如此而已。

但是，我一直对于pandoc不知道怎么去使用。问了一些人，查了很多网页，都没有写如何去使用pandoc，直到，我在github上搭建Blog，安装Ruby，以及安装了Jekyll，才最终发现我会使用Pandoc了。可见，机遇是给有准备的人。

这周准备R的分享，特意尝试用Markdown和Pandoc准备资料。用Markdown写了10分钟的内容，然后用Pandoc“秒杀”了一个Slide的Html的文件，效果不错。
鉴于个人对于过程和效果的喜欢，特别整理，分享给有缘人。 个人估计，有缘人看到以后，必定会引起写作界的一波学习热！

### 一、Markdown使用

Markdown，就像一个人的任脉。它简洁，方便，只要集中精力写文章就好，排版不用管。它的语法如此简单，简单的连一个初中生就可以10分钟学会去用，5分钟写一个例子，就会了。此言真不虚。比如，我要写一篇文章,可以这么写：

    ##我的工作
    - 工作在Etao
    我属于阿里妈妈，是的。你没看错，就是阿里妈妈。
    - 工作是BI
    我的工作是BI.BI？啥？就是。。。就是。。那个。
    `- 工作薪水
    薪水？老板不让说。不告诉你。

#### 展现的样式呢，是这样的：

## 我的工作

- 工作在Etao

我属于阿里妈妈，是的。你没看错，就是阿里妈妈。

- 工作是BI

我的工作是BI.BI？啥？就是。。。就是。。那个。

- 工作薪水

 薪水？老板不让说。不告诉你。 

哇，简单么？#就是标题的代表，一个#是一级标题，两个#是二级标题，以此类推。如果要引用，就使用>。多么简单的美好啊！其他的使用方法，大家可以去自己学习一下，你会体会到什么是简单的美好！Markdown的内容写好以后，保存成*.md文件。
### 二、Pandoc使用

Pandoc，这个不知道怎么发音，google也没找到。好吧，我就读做panda吧，谁让它是国宝。

Pandoc的运行，是在命令行里面。可是，没那么简单，不是任何一个cmd都可以。你必须要下载Pandoc，请参考这里.根据自己的os，选择Windows 或者其他。

安装以后，记得Pandoc的目录是啥，然后再到cmd里面去操作一些失传已久的doc命令，转换到pandoc的路径下。

我个人习惯，是把要转换的文件，比如test.md，放到pandoc的路径下，这样在使用pandoc转换的时候，不用输入太多的路径（尤其是我们很多路径是中文，怕可能有一些问题）。当然，也可以调用其他路径的文件，只要自己觉得舒服。

pandoc，就像linux下的iconv，可以把其他格式的文件，转化成自己想要的格式。具体的格式参考请看这里。

#### 个人常用的有两个格式转换：

        a>md文件转换成html5
        pandoc -s --mathml -i -t dzslides test.md -o test.html
        b>md文件转换成pdf
        pandoc -t beamer test.md -o test.pdf 

这里强调一点，如果想转成PDF文件，要安装LATEX。推荐安装MiKTex。但是，中文转PDF，因latex支持中文差，转换有问题。对于Latex熟悉的人，可以参考这个，看是否能解决中文转slide pdf的问题。

文件转换完成以后，如果有一些地方不合适，可以调整原始的md文件，再转换一次。等熟练以后，从写，到转换就非常迅速了。 当然，Pandoc还有很多的转换格式，大家可以自己去研究发觉。

记得有好的东西，要分享。

### 后记

虽然偶不美，但是，对于任何美的东西，尤其是设计或者排版，或者操作界面，自己还是很热衷的。使用Pandoc，自己当初只是喜欢Slide的样式，不用去辛辛苦苦的做PPT,就可以有超过PPT的效果，何乐而不为呢？还有Html5，哦，真的是很炫。

关于Pandoc的使用，我没有过多的去研究。只是把自己常用的几个功能熟悉了一下。时间，真的真的很宝贵，不知不觉就从指缝中溜走了。所以，我只能在满足自己需求情况下，去使用pandoc。
期待大家更多的分享！

# 神器Pandoc的安装与使用 

>21 October 2013

[神器Pandoc的安装与使用](http//zhouyichu.com/misc/Pandoc.html)

### 前言

其实很早就知道Pandoc这个东西了，只是一直没有什么需求促使我去使用它。平时写博客虽然也是用Markdown，但是由于Jekyll并不支持Pandoc，所以也没有特别去研究它(目前博客使用的是Kramdown渲染器，它在很多扩展语法都是借鉴Pandoc的。)。可是时过境迁，现在平时需要写一些非正式报告和总结，每次使用word的时候总觉得不舒服，有次为了调整一个段落的行距搞了1个多小时，虽然可以说是我自己没有学好word的基本操作，但是每次为了寻找一个功能”翻箱倒柜”地在网上找方法，彻底破坏了写作的情绪，这实在让我很难受。因此我选择markdown来进行平时的写作，为了达到这个目的，必须要选择一个markdown的渲染器，网上有着各式各样的渲染器，还有一些可以直接在线渲染的网站。但是平时在本地编辑的时候，总要开个浏览器，这实在让人接受不了。在众多渲染器中，最先映入眼帘的就是Pandoc了，号称为文本格式转换的瑞士军刀，既然有了这个称号，说明其功能是非常不错的。后来查了一下，发现果然是一个神器，它甚至可以生成pdf和docs！

Pandoc的官网在这里，网上有很多具体介绍Pandoc的文章，其中质量比较高的有

>Markdown写作进阶：Pandoc入门浅谈
>Markdown+Pandoc 最佳写作拍档
>轻量级文档写作

本文就不再赘述上面文章提到过的一些基本概念和操作了，如果读者还不知道Markdown和Pandoc是什么的话，请阅读上述文章。

### 配置

具体的安装过程上述文章和Pandoc的官网上都有，此处不再细说了，这里主要说明一些在安装过程遇到的问题和解决方法(以windows7为例)。

#### 系统路径

在Windows下Pandoc安装的时候，默认是安装在用户主目录下的，以win7为例，就是 C\Users\USERNAME\AppData\Local\Pandoc，照理来说安装程序是应该会把这个目录添加到Path中去的，但是我发现并没有自动添加，因此首先要将这个目录手动加入到Path中，这样才能在任何的目录下进行调用。

#### 生成HTML

就我自己而言，我使用Pandoc最主要的功能就是利用它来生成HTML和PDF文件，本节先讨论HTML的配置方法，下一节再来说明pdf的配置。

其实将markdown生成html，是Pandoc最基本的一个功能，使用起来也是非常简单的，打开cmd，切换到makrdown文本所在的目录，写入如下代码1

	pandoc in.md -o out.html

1如果发现没有pandoc命令，说明还没有将安装目录添加到系统Path中，请查看上一节内容。

程序运行之后，就会在当前目录下生成一个相应的out.html文件。

#### CSS样式

上面这是最基本的用法了，但是这还不能满足我的日常需求，单纯的html文件太过单调了，只有配上相应的CSS样式，才能使得文本以更加优美的方式展现出来。

可喜的是pandoc完全支持加入css一起渲染，利用如下的命令：

	pandoc in.md -c style.css out.html

其中style.css是为生成的html文件编写的样式文件，但是这个style.css应该放在哪呢？放在当前目录下，当然没问题，但是每次编写markdown的时候，都要将这个css文件复制到当前目录下，那岂不是很麻烦？因此我要想办法把它放在一个固定的地方，每次直接调用就可以了。

这就引出了pandoc的默认目录了，可以通过pandoc --version命令来查看pandoc当前的默认目录，还是以windows7为例，它的默认目录是C\Users\USERNAME\AppData\Roaming\pandoc ,只需要将这个style.css文件放入到这个目录下，那么在任意目录使用pandoc时，都能自动读取到这个文件，而且，如果需要一些特殊的css样式，可以在当前目录编写，pandoc会自动使用当前目录下的style.css替代默认目录中的style.css文件。

#### 生成独立HTML

通常来说，写作的目的是写给别人来看的，但是如果是使用html文件的格式的话，那么每次传输都需要传送整个目录文件，因为会有很多图片或css文件需要一起被传送，否则html会无法正确显示。这显然是很麻烦的，有没有办法让pandoc在生成的时候，自动把style.css中样式代码直接嵌入到html中呢？办法当然是有的，主要是参考了这篇文章。主要有两种方法：

第一种是使用方法是使用如下的命令

	pandoc -s -H style.css  in.md -o out.html

但是当我试用这种方式的时候，发现style.css文件必须放在当前目录下，这个命令才能正常执行，否则会报错说找不到style.css文件。

另外一种更加好的方式使用--self-contained参数

	pandoc -s --self-contianed -c style.css in.md -o out.html

这个命令不但会把css文件嵌入到html中，它会把所有外部文件全部压缩进单个html文件中，包括图片、视屏、音乐等。这是何等强大的功能！！

利用上述这个命令，就能将markdown文档轻易地生成一个真正独立的html文件，不需要任何其他外部文件支持，这就非常方便传递了。

#### 生成pdf

生成一个pdf文件也是pandoc的主要功能之一，但是它要依赖于latex，如果需要使用pandoc来生成pdf文件，那么需要另外安装Latex，pandoc官方推荐安装MiKTeX，具体安装过程也不说了，非常简单。安装好MikTex之后，可以利用如下的命令来生成pdf

	pandoc in.md -o out.pdf

但是这样命令会出现这样的错误

    ! Package inputenc Error Unicode char \u8:鍒?not set up for use with LaTex. pandoc: Error producing PDF from Tex source. See the inputsnc package documentation for explanation. …

原因是pandoc默认选择的pdf引擎是pdflatex，而pdflatex是不支持中文的，因此会发生上述错误。因此在使用pandoc的时候，可以手动指明Latex引擎为xelatex，这是完全支持中文显示的。这样我们的命令就变成了
````
	pandoc in.md -o out.pdf --latex-engine=xelatex
````
使用这个命令能够正常的编译出pdf文件，但是当你打开编译出来的pdf文件时，会发现其中的中文部分全是空白，这是字体的问题，因为Latex的默认字体是不支持中文的，因此我们可以继续修改命令：

	pandoc in.md -o out.pdf --latex-engine=xelatex -V mainfont=SimSun

其中mainfont参数是用来指明所使用的字体，SinSun表示的是宋体，你可以选择其他支持中文的字体。

但是这个命令还是有问题的，打开生成的pdf，你会发现其中的中文完全是没有断行的，这是因为pandoc本身对中文支持不够，但这不是说我们没有解决方案，解决方案是使用网友编辑好的latex模板来生成pdf，这里用到的是tzengyuxio提供的pm-template.latex4。 下载模板后将其中的LiHei Pro字体替换成系统中安装有的中文字体即可，然后编译命令改为

	pandoc in.md -o out.pdf --latex-engine=xelatex --template=pm-template.latex

这时就能生成一个比较完美的pdf文件了。

## Vim与Pandoc

既然现在有了panodc这个神器，那么大部分的文本编辑操作我就可以在Vim中进行了，而不需要去使用那个无比臃肿的word了，配合Vim强大的定制功能，我就能配置出一个功能完善的pandoc写作环境了。

这显然又是一个很深的话题，这里我只是稍微写一下配置过程，因为我自己本身也还在研究当中。

首先可以为markdown文件映射几个命令，使得可以快捷的生成html，在Vim的_vimrc文件中加入如下代码：

````
function! ToHtml()
	exec 'w'
	exec "!pandoc  -s -S --self-contained -c style.css % -o %<.html "
endfunction

function! ToPdf()
	exec 'w'
	exec "!pandoc  % -o %<.pdf --latex-engine=xelatex --template=pm-template.latex"
endfunction
:nmap <silent> <F5> :call ToHtml()<CR>
:nmap <silent> <F6> :call ToPdf()<CR>
````

上述的代码中，我首先定义了两个函数，分别是用来调用pandoc来生成html和pdf文件的，然后映射了两个快捷键<F5>和<F6>去调用这两个函数，这样就实现了直接在Vim中调用pandoc生成html或pdf，而不再需要通过命令行来调用。

最后推荐一个比较好的pandoc插件vim-pandoc，这个插件我也是刚刚开始使用，感觉还不错，值得推荐。
参考资料

> Markdown写作进阶：Pandoc入门浅谈
> Markdown+Pandoc 最佳写作拍档
>轻量级文档写作
> 利用Pandoc将markdown文件转化为pdf
> pandoc中文pdf转换攻略
> pandoc官方User Guide

字数4130 

## ubuntu默认打开方式的修改保留了linux特色。

ubuntu的全局默认打开方式保存在/etc/gnome/defaults.list

个人的打开方式保存在~/.local/share/applications/mimeapps.list

举例来讲，application/pdf=evince.desktop;Foxit-Reader.desktop;gimp.desktop;表示pdf的默认打开方式为evince，然后是foxit-reader和gimp（foxit需要自己装）。

如果想默认用foxit打开，就改成application/pdf=Foxit-Reader.desktop;evince.desktop;gimp.desktop;

个人感觉虽然比windows上设置麻烦得多，但比起在windows上默认打开方式设置出错之后，需要在注册表里翻来覆去找键值来修正要好得多了。而且这种问题在windows下不一定修改注册表就能搞定。。

# Ubuntu 14.0操作系统，修改默认打开方式的方法

[此博文包含图片] (2014-10-29 1117:27)

Ubuntu 14.0 有内置的视频播放器 Totem，但是使用起来不太习惯，所以在系统的软件中心 下载了gnome Mplayer和s Mplayer，都有打开上次播放的忆功能，只是gnome Mplayer在播放mkv时刚开始有点卡，播一会儿就好,s Mplayer总体还不错, 问题就是默认打开方式还是Totem，于是最初搜索了一通，看了很多长篇大论尝试修改了mimeapp.list 但是没生效。

       最后在其他地方发现某位前辈写的一句：“从总体上讲 /etc/gnome/defaults.list 保存了全局的打开方式，而~/.local/share/applications/mimeapps.list 保存了个人的打开方式，当两者不一致时，会优先采用局部的个人设置”，虽然和实际情况有些出入, 但瞬间领悟，再改一下全局设置就可以了~

       很简单的一条命令就可以实现，步骤如下：

       1、ctrl+atl+T 打开终端，输入命令 sudo gedit /etc/gnome/defaults.list，这样就用gedit打开了全局设置；
Ubuntu <wbr>14.0操作系统，修改默认打开方式的方法

        2、点击gedit菜单栏的“搜索”——“替换”，输入totem替换为gnome-mplayer或者smplayer，点击“替换”按钮接着ctrl+s保存，完成～！

Ubuntu <wbr>14.0操作系统，修改默认打开方式的方法
       另外，搜狗拼音出了linux版本，需要搭载于fcitx，比ibus的sunpinyin好用，词库丰富，使用习惯也很对味，据说是Ubuntu keylin的标配输入法，建议装上。

       如果安装过其他输入法，可以用下面这条命令设置默认输入法：
       $ im-switch -s fcitx
       设置好之后重启 x 即可。

# Tip using Pandoc to create truly standalone HTML files

A Labourer at the Bitface

Posted on 2012-07-02 by Martin McCallion	

If you’re using the excellent Pandoc to convert between different document formats, and you

  -  want your final output to be in HTML;
  -  want the HTML to be styled with CSS;
  - and want the HTML document to be truly standalone;

then read on.

The most common approach with Pandoc is, I think, to write in Markdown, and then convert the output to RTF, PDF or HTML. There are all sorts of more advanced options too; but here we are only concerned with HTML.

The pandoc command has an option which allows you to style the resulting HTML with CSS. Example 3 in the User’s Guide shows how you do this, with the -c option. The example also uses the -s option, which means that we are creating a standalone HTML document, as distinct from a fragment that is to be embedded in another document. The full command is

    pandoc -s -S --toc -c pandoc.css -A footer.html README -o example3.html

If you inspect the generated HTML file after running this, you will see it contains a line like this

    <link rel="stylesheet" href="pandoc.css" type="text/css" />

That links to the CSS stylesheet, keeping the formatting information separate from the content. Very good practice if you’re publishing a document on the web.

But what about that “standalone” idea that you expressed with the -s option? What that does is make sure that the HTML is a complete document, beginning with a DOCTYPE tag, an <html> tag, and so on. But if, for example, you have to email the document you just created, or upload it to your company’s document store, then things fall apart. When your reader opens it, they’ll see what you wrote, all right; but it won’t be styled the way you wanted it. Because that pandoc.css file with the styling is back on your machine, in the same directory as the original Markdown file.

What you really want is to use embedded CSS; you want the content of pandoc.css to be included along with the prose you wrote in your HTML file.

Luckily HTML supports that, and Pandoc provides a way to make it all happen the -H option, or using its long form, --include-in-header=FILE

**First you’ll have to make sure that your pandoc.css file1 starts and ends with HTML `<style> `, so it should look something like this**

    <style type="text/css">
    body {
    margin auto;
    padding-right 1em;
    padding-left 1em;
    max-width 44em;
    border-left 1px solid black;
    border-right 1px solid black;
    color black;
    font-family Verdana, sans-serif;
    font-size 100%;
    line-height 140%;
    color #333;
    }
    </style>

**Then run the pandoc command like this**

    pandoc -s -S --toc -H pandoc.css -A footer.html README -o example3.html

and you’re done. A fully standalone HTML document.

It doesn’t have to be called that, by the way.↩
