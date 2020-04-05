% markdown +CSS转换html V2
    #1级标题

    ##2级标题

    ###3级标题

    ####4级标题

    #####5级标题　　

    ######6级标题　　**强调** *斜体* *`斜体em里的代码`* **`强调strong里的代码`** ~~删除线~~

    #######7级标题

    ########8级标题

    #########9级标题

**exam:**

#  1级标题

##  2级标题

###  3级标题

####  4级标题

#####  5级标题　　

######  6级标题　　**强调** *斜体* *`斜体em里的代码`* **`强调strong里的代码`**~~删除线~~

#######  7级标题

########  8级标题

######### 9级标题

## 代码

### 代码块pre `tab` 或者 `(````)`

    代码代码代码代码代码代码代码代码代码代码代码代码代码代码
    代码代码代码代码代码代码代码代码代码代码代码代码代码代码
    代码代码代码代码代码代码代码代码代码代码代码代码代码代码

### 行内代码code `行内代码(``)`

行内的代码`这是行内代码`  
行内的代码`这是行内代码 最好不超过1行`  

### 代码高亮

        ``` python
        @requires_authorization
        def somefunc(param1='', param2=0):
            '''A docstring'''
            if param1 > param2: # interesting
                print 'Greater'
            return (param2 - param1 + 1) or None
        class SomeClass:
            pass
        >>> message = '''interpreter
        ... prompt'''
        ```

``` python
@requires_authorization
def somefunc(param1='', param2=0):
    '''A docstring'''
    if param1 > param2: # interesting
        print 'Greater'
    return (param2 - param1 + 1) or None
class SomeClass:
    pass
>>> message = '''interpreter
... prompt'''
```

---

## 段落

`段落`段落样式`(:)`
 :   段落段落段落段落段落段落段落段落段落段落段落段落段落段落

     段落段落段落段落段落段落段落段落段落段落段落段落段落段落

     普通强调**段落段落段落段落段落段落段落段落段落段落段落**

     普通斜体*落段落段落段落段落段落段落段落段落段落段落段落*

     段落段落段落段落段落段落段落段落段落段落段落段落段落段落

`段落`段落样式`(~)`
~   段落段落段落段落段落段落段落段落段落段落段落段落段落段落
     段落段落段落段落段落段落段落段落段落段落段落段落段落段落
     段落段落段落段落段落段落段落段落段落段落段落段落段落段落
     段落段落段落段落段落段落段落段落段落段落段落段落段落段落
     段落段落段落段落段落段落段落段落段落段落段落段落段落段落

## 表格

    ------------
    两行表格行1
    两行表格行2
    --------

------------
两行表格行1
两行表格行2
--------

    |表格头   |第一列    |第二列
    ---------|--------|---------
    |行1        | 值1       |值2
    |行2         |值1       |值2
    |强调**         |**强调样式**       |strong
    |斜体*         |*斜体样式*       |em
    |强调内代码        |**`强调样式`**       |strongcode
    |斜体内代码       |*`斜体样式`*       |emcode

|表格头   |第一列    |第二列
---------|--------|---------
|行1        | 值1       |值2
|行2         |值1       |值2
|强调**         |**强调样式**       |strong
|斜体*         |*斜体样式*       |em
|强调内代码       |**`强调样式`**       |strongcode
|斜体内代码      |*`斜体样式`*       |emcode

## 引用

    > 引用引用引用引用引用引用引用引用引用引用引用引用引用1

    >> 引用引用引用引用引用引用引用引用引用引用引用引用引用2

    >>> 引用引用引用引用引用引用引用引用引用引用引用引用引用3

    >>>> 引用引用引用引用引用引用引用引用引用引用引用引用引用4

    >>>>> 引用引用引用引用引用引用引用引用引用引用引用引用引用5

    >>>>>> 引用引用引用引用引用引用引用引用引用引用引用引用引用6

    >>>>>>> 引用引用引用引用引用引用引用引用引用引用引用引用引用7

      >>>>>>>> 引用引用引用引用引用引用引用引用引用引用引用引用引用8

      >>>>>>>>> 引用引用引用引用引用引用引用引用引用引用引用引用引用9

效果:

> 引用引用引用引用引用引用引用引用引用引用引用引用引用引用引用引引用引用引用引用引用引用引用引用引用引用引用引引用引用引用引用引用引用引用引用引用引用引用引引用引用引用引用引用引用引用引用引用1

效果:

>> 引用引用引用引用引用引用引用引用引用引用引用引用引用引用引用引用引引用引用引用引用引用引用引用引用引用引用引用引引用引用引用引用引用引用引用引用引用引用引用引引用引用引用引用引用引用引用引用2

效果:

>>> 引用引用引用引用引用引用引用引用引用引用引用引用引用引用引用引用引引用引用引用引用引用引用引用引用引用引用引用引引用引用引用引用引用引用引用引用引用引用引用引引用引用引用引用引用引用引用引用引用引用引用引引用引用引用引用引用引用引用引用3

效果:

>>>> 引用引用引用引用引用引用引用引用引用引用引用引用引用引用引用引用引引用引用引用引用引用引用引用引用引用引用引用引引用引用引用引用引用引用引用引用引用引用引用引引用引用引用引用引用引用引用引用引用引用引用引引用引用引用引用引用引用引用引用4

效果:

>>>>> 引用引用引用引引用引用引用引用引用引用引用引用引用引用引用引引用引用引用引用引用引用引用引用引用引用引用引引用引用引用引用引用引用引用引用引用引用引用引引用引用引用引用引用引用引用引用引用引用引用引引用引用引用引用引用引用引用引用引用引用引用引用引用引用引用引用引用引用引用引用引用5

效果:

>>>>>> 引用引用引用引用引用引用引用引用引用引用引用引用引用引用引用引引用引用引用引用引用引用引用引用引用引用引用引引用引用引用引用引用引用引用引用引用引用引用引引用引用引用引用引用引用引用引用引用引用引用引引用引用引用引用引用引用引用引用引用6

效果:

>>>>>>> 引用引用引用引用引用引用引用引用引用引用引用引用引用引用引用引引用引用引用引用引用引用引用引用引用引用引用引引用引用引用引用引用引用引用引用引用引用引用引引用引用引用引用引用引用引用引用引用引用引用引引用引用引用引用引用引用引用引用引用7

效果:

>>>>>>>> 引用引用引用引用引用引用引用引用引用引用引用引用引用引用引用引引用引用引用引用引用引用引用引用引用引用引用引引用引用引用引用引用引用引用引用引用引用引用引引用引用引用引用引用引用引用引用引用引用引用引引用引用引用引用引用引用引用引用引用8

效果:

>>>>>>>>> 引用引用引用引用引引用引用引用引用引用引用引用引用引用引用引用引引用引用引用引用引用引用引用引用引用引用引用引引用引用引用引用引用引用引用引用引用引用引用引引用引用引用引用引用引用引用引用引用引用引用引用引用引用引用引用引用引用引用引用9

###  复选框：不支持

使用 `- [ ]` 和 `- [x]` 语法可以创建复选框，实现 todo-list 等功能。例如：

- [ ] 复选框
- [ ] 复选框
- [x] 复选框

## 列表

**无序列表**

**`代码`**

    * 无序列表
     + 无序列表
     + 无序列表
        - 无序列表
            - 无序列表
                - 无序列表
                    - 无序列表
                        - 无序列表
    * 无序列表
    * 无序列表
    + 无序列表
    - 无序列表
    - 无序列表

* 无序列表
 + 无序列表
 + 无序列表
    - 无序列表
        - 无序列表
            - 无序列表
                - 无序列表
                    - 无序列表
* 无序列表
* 无序列表
+ 无序列表
- 无序列表
- 无序列表

**有序列表**

*`代码`*

    1. 有序列表
    2. 有序列表 列表内的强调`(*)`: *列表内的斜体样式*
    8. 有序列表 列表内的强调`(**)`: **列表内的强调样式**
    #. 有序列表  内的引用
    #. 有序列表  内的引用

        >有序列表 内的引用
        >有序列表 内的引用

    9) 有序列表
    (8)有序列表
    (10) 有序列表

    9) 有序列表
    #. 有序列表

    (8)有序列表
    #. 有序列表

    (10)有序列表
    #. 有序列表

1. 有序列表
2. 有序列表 列表内的强调`(*)`: *列表内的斜体样式*
8. 有序列表 列表内的强调`(**)`: **列表内的强调样式**
# . 有序列表  内的引用

# . 有序列表  内的引用

    >有序列表 内的引用
    >有序列表 内的引用

9) 有序列表
(8)有序列表
(10) 有序列表

9) 有序列表
# . 有序列表

(8)有序列表
# . 有序列表

(10)有序列表
# . 有序列表

# CSS自定义

*`代码`*

````
<div class="warning">
## 警告帮助你不出错

如果不想出错，请注意这类消息
</div>

````

*`效果`*

<div class="warning">
###### 警告帮助你不出错

如果不想出错，请注意这类消息
</div>

```
<div class="menu">
[首页](../../../index.html)
[文章列表](./list.md.html)
[MarkdownEditor](../../../editor/index.html)
</div>
```

菜单效果:

<div class="menu">
[首页](../../../index.html)
[文章列表](./list.md.html)
[MarkdownEditor](../../../editor/index.html)
</div>

#### link/img

```
[![百度](./img/baidu3.gif)](http://www.baidu.com/)
```

--------------

## 通用字体格式

```
**强调** *斜体*  ***斜粗体***  ~~删除线del~~　　下标~下标sub~　 上标^上标sup^  --删除线--   -删除线-

~~^下划线del>sup^~~
```

*`效果`*

**强调** *斜体*  ***斜粗体***  ~~删除线del~~　　下标~下标sub~　 上标^上标sup^  --删除线--   -删除线-

~~^下划线del>sup^~~

*多了空格的错误*

```
**    强调**  *斜体   *  **  *斜粗体   ***  ~~删除线del ~  ~　　下标~下标sub     ~　 上标^上标sup  ^  --删除线--   -删除线-
```

*`效果`*

**    强调**  *斜体   *  **  *斜粗体   ***  ~~删除线del ~  ~　　下标~下标sub     ~　 上标^上标sup  ^  --删除线--   -删除线-

## 自定义字体格式

```
|    样式  |strong                        | em                  | sub                  |sup                   |code                   | del                        |
|---------|----------------------------|---------------------|--------------------|-------------------|---------------------|----------------------------|
||||||||
|原始|**strong**|*em*|下标~sub~|上标^sup^|`code`|~~del~~|
|strong** |        |  ***strong>em***     |   **~strong>sub~**    |   **^strong>sup^**   | **`strong>code`**     | **~~strong>del~~**      |
|em*      |  ***em>strong***         |      **em>em**              |   高亮*~em>sub~*        |  *^em>sup^*       | *`em>code`*            | *~~em>del~~*           |
|sub~     |     ~**sub>strong**~        |     ~*sub>em*~         |         ~~sub>sub~~                     |    ~^sub>sup^~       |     ~`sub>code`~      |  ~~~sub>del~~~         |       
|code   \`|     `**code>strong**`      |     `*code>em*`            |`~code>sub~`        |    `^code>sup^`      |     ``code>code``    |  `~~code>del~~`        |
|del ~~     |     ~~**del>strong**~~     |     ~~*del>em*~~         |~~~del>sub~~~             |   下划线~~^del>sup^~~       |     ~~`del>code`~~    |  ~~~~del>del~~~~   |

```

*`效果`*

|    样式  |strong                        | em                  | sub                  |sup                   |code                   | del                        |
|---------|----------------------------|---------------------|--------------------|-------------------|---------------------|----------------------------|
||||||||
|原始|**strong**|*em*|下标~sub~|上标^sup^|`code`|~~del~~|
|strong** |        |  ***strong>em***     |   **~strong>sub~**    |   **^strong>sup^**   | **`strong>code`**     | **~~strong>del~~**      |
|em*      |  ***em>strong***         |      **em>em**              |   高亮*~em>sub~*        |  *^em>sup^*       | *`em>code`*            | *~~em>del~~*           |
|sub~     |     ~**sub>strong**~        |     ~*sub>em*~         |         ~~sub>sub~~                     |    ~^sub>sup^~       |     ~`sub>code`~      |  ~~~sub>del~~~         |       
|code   \`|     `**code>strong**`      |     `*code>em*`            |`~code>sub~`        |    `^code>sup^`      |     ``code>code``    |  `~~code>del~~`        |
|del ~~     |     ~~**del>strong**~~     |     ~~*del>em*~~         |~~~del>sub~~~             |   下划线~~^del>sup^~~       |     ~~`del>code`~~    |  ~~~~del>del~~~~   |

### SUP类定义格式:

    ^**sup>strong**^      

*`效果`*

^**sup>strong**^      

    ^*sup>em*^  

*`效果`*

^*sup>em*^                 

    ^`sup>code`^    

  *`效果`*

  ^`sup>code`^    

     ^~sup>sub~^           

*`效果`*

^~sup>sub~^      

    ^^sup>sup^^    

*`效果`*

^^sup>sup^^    

## 内部链接

```

[::返回顶部][header]

[header]: #header

[::返回列表][toc]

[toc]: #TOC

[*`返回顶部`*](#header)

<p  align="right"><em><code><a href="#header">返回顶部</a></code></em></p>

```
*`效果`*

[***::返回顶部***][header]

[header]: #header

[*~::返回列表~*][toc]

[toc]: #TOC

[*`返回顶部`*](#header)

<p  align="right"><em><code><a href="#header">返回顶部</a></code></em></p>

---

###  label

``` css
.label {
    display: inline;
    padding: .2em .6em .3em;
    font-size: 75%;
    font-weight: 700;
    line-height: 1;
    color: #fff;
    text-align: center;
    white-space: nowrap;
    vertical-align: baseline;
    border-radius: .25em;
}
.label-default {
    background-color: #777;
}
.label-primary {
    background-color: #337ab7;
}
.label-success {
    background-color: #5cb85c;
}
.label-danger {
    background-color: #d9534f;
}
.label-warning {
    background-color: #f0ad4e;
}
.label-info {
    background-color: #5bc0de;
}
```

```html
<span class="label label-default">Default</span>
<span class="label label-primary">Primary</span>
<span class="label label-success">Success</span>
<span class="label label-warning">Warning</span>
<span class="label label-danger">Danger</span>
<span class="label label-info">Info</span>
```

效果：

<span class="label label-default">Default</span>
<span class="label label-primary">Primary</span>
<span class="label label-success">Success</span>
<span class="label label-warning">Warning</span>
<span class="label label-danger">Danger</span>
<span class="label label-info">Info</span>

###  字体颜色

更改代码颜色代码如下：

    Default Color
    <font color='red'>Red Color</font>
    <font color='blue'>Blue Color</font>
    <font color='green'>Green Color</font>
    <font color='yellow'>Yellow Color</font>
    <font color='pink'>Pink Color</font>
    <font color='purple'>Purple Color</font>
    <font color='orange'>Orange Color</font>

更改颜色：

Default Color
<font color='red'>Red Color</font>
<font color='blue'>Blue Color</font>
<font color='green'>Green Color</font>
<font color='yellow'>Yellow Color</font>
<font color='pink'>Pink Color</font>
<font color='purple'>Purple Color</font>
<font color='orange'>Orange Color</font>

###  显示换字号、字体功能。

代码：

    <font size='-2'>Small Size</font>
    Normal Size
    <font size='+2'>Big Size</font>
    <font size='+2' face='Times'>Time New Roman</font>

效果

<font size='-2'>Small Size</font>
Normal Size
<font size='+2'>Big Size</font>
<font size='+2' face='Times'>Time New Roman</font>

###  数学公式

明星组合：Markdown + MathJax。

这里（http://mathjax-chinese-doc.readthedocs.org/en/latest/start.html）有一个MathJax的汉化入门指南，感兴趣的同学可以看看。

例如，以下代码可以给出一个行间公式：

    $$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$$
    \\(x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}\\)

其输出为：

$$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$$
\\(x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}\\)

图片：

    ![](./library/help-code/001.jpg)	

效果：

![](./library/help-code/001.jpg)

--------------------

#### bs-callout bs

    <div class="bs-callout bs-callout-warning">
    <h4>链接的原始功能不受影响</h4>
    <p>上面提到的类只是通过设置 <code>pointer-events: none</code> 来禁止 <code>&lt;a&gt;</code> 元素作为链接的原始功能，但是，这一 CSS 属性并没有被标准化，并且 Opera 18 及更低版本的浏览器并没有完全支持这一属性，同样，Internet Explorer 11 也不支持。In addition, even in browsers that do support <code>pointer-events: none</code>, keyboard navigation remains unaffected, meaning that sighted keyboard users and users of assistive technologies will still be able to activate these links. 因此，为了安全起见，建议通过 JavaScript 代码来禁止链接的原始功能。</p>
    </div>

    <div class="bs-callout bs-callout-info">
    <h4>链接的原始功能不受影响</h4>
    <p>上面提到的类只是通过设置 <code>pointer-events: none</code> 来禁止 <code>&lt;a&gt;</code> 元素作为链接的原始功能，但是，这一 CSS 属性并没有被标准化，并且 Opera 18 及更低版本的浏览器并没有完全支持这一属性，同样，Internet Explorer 11 也不支持。In addition, even in browsers that do support <code>pointer-events: none</code>, keyboard navigation remains unaffected, meaning that sighted keyboard users and users of assistive technologies will still be able to activate these links. 因此，为了安全起见，建议通过 JavaScript 代码来禁止链接的原始功能。</p>
    </div>

    <div class="bs-callout bs-callout-danger">
    <h4>链接的原始功能不受影响</h4>
    <p>上面提到的类只是通过设置 <code>pointer-events: none</code> 来禁止 <code>&lt;a&gt;</code> 元素作为链接的原始功能，但是，这一 CSS 属性并没有被标准化，并且 Opera 18 及更低版本的浏览器并没有完全支持这一属性，同样，Internet Explorer 11 也不支持。In addition, even in browsers that do support <code>pointer-events: none</code>, keyboard navigation remains unaffected, meaning that sighted keyboard users and users of assistive technologies will still be able to activate these links. 因此，为了安全起见，建议通过 JavaScript 代码来禁止链接的原始功能。</p>
    </div>

<div class="bs-callout bs-callout-warning">
<h4>链接的原始功能不受影响</h4>
<p>上面提到的类只是通过设置 <code>pointer-events: none</code> 来禁止 <code>&lt;a&gt;</code> 元素作为链接的原始功能，但是，这一 CSS 属性并没有被标准化，并且 Opera 18 及更低版本的浏览器并没有完全支持这一属性，同样，Internet Explorer 11 也不支持。In addition, even in browsers that do support <code>pointer-events: none</code>, keyboard navigation remains unaffected, meaning that sighted keyboard users and users of assistive technologies will still be able to activate these links. 因此，为了安全起见，建议通过 JavaScript 代码来禁止链接的原始功能。</p>
</div>

<div class="bs-callout bs-callout-info">
<h4>链接的原始功能不受影响</h4>
<p>上面提到的类只是通过设置 <code>pointer-events: none</code> 来禁止 <code>&lt;a&gt;</code> 元素作为链接的原始功能，但是，这一 CSS 属性并没有被标准化，并且 Opera 18 及更低版本的浏览器并没有完全支持这一属性，同样，Internet Explorer 11 也不支持。In addition, even in browsers that do support <code>pointer-events: none</code>, keyboard navigation remains unaffected, meaning that sighted keyboard users and users of assistive technologies will still be able to activate these links. 因此，为了安全起见，建议通过 JavaScript 代码来禁止链接的原始功能。</p>
</div>

<div class="bs-callout bs-callout-danger">
<h4>链接的原始功能不受影响</h4>
<p>上面提到的类只是通过设置 <code>pointer-events: none</code> 来禁止 <code>&lt;a&gt;</code> 元素作为链接的原始功能，但是，这一 CSS 属性并没有被标准化，并且 Opera 18 及更低版本的浏览器并没有完全支持这一属性，同样，Internet Explorer 11 也不支持。In addition, even in browsers that do support <code>pointer-events: none</code>, keyboard navigation remains unaffected, meaning that sighted keyboard users and users of assistive technologies will still be able to activate these links. 因此，为了安全起见，建议通过 JavaScript 代码来禁止链接的原始功能。</p>
</div>