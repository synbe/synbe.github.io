% linuxsed提取之间的字符
<h6>2009-10-12 17:02:05)</h6>

###  比如从第3行到第10行

    sed -n '3,10p' myfile > newfile

另外以行的内容输出，例如；

有一个文件，内容如下：

    WWW
    CTAAACCCTAAACCCTAAACCCTAAACCCTAAACCCTAAACCCTAAACCCTAAACCCTAA
    CCCTAAACCCTAACCCTAAACCCTAAACCCTAAACCCTAAACCCTAAACCCTAAACAGCT
    GACAGTACGATAGATCCACGCGAGAGGAACCGGAGAGACAACGGGATCCAGGCGCCAGCG
    MMM
    CTAAACCCTAAACCCTAAACCCTAAACCCTAAACCCTAAACCCTAAACCCTAAACCCTAA
    CCCTAAACCCTAACCCTAAACCCTAAACCCTAAACCCTAAACCCTAAACCCTAAACAGCT
    GACAGTACGATAGATCCACGCGAGAGGAACCGGAGAGACAACGGGATCCAGGCGCCAGCG
    KKK

想要输出WWW与>MMM这两行及其之间的行
命令如下：

    sed -n '/WWW/,/MMM/p' file 

注意逗号，如果行中出现逗号，前面一定要以反斜线

### sed之截取第一个和最后一个关键字之间的内容 2011-08-04 13:25:54

    123
    232
    313
    321

截取第一个2和最后一个2之间的内容(红色部分)：

    3
    232
    313
    3

    sed ':a;N;$!ba;s/[^2]*2\(.*\)2.*/\1/' file

[解析]

  当初看到这个题的时候无从下手，真没有想到可以用sed来完成，Tim大师的思路真的值得人五体投地的敬佩，向前辈们致敬。这些另辟蹊径的思路真的值得大家借鉴和积累。接着来分析，首先Tim大师的思路是把所有的行全读入pattern space中，来统一处理，所以有了“:a;N!ba;”这个命令，到了最后一行不执行跳转，那现在pattern space中的内容就成了“123\n232\n313\n321”，然后执行后面的替换语句，由于充分利用正则贪婪匹配的原理，它会匹配到最后一个2的，然后用小括号标记起来，最后打印。

### 如何用Sed和正则表达式提取子字符串

现在有如下一串字符串：

    "asdfkjasldjkf"shiner"df

需求：
     需要提取出shiner子字符串。

命令如下：

      echo "asdfkjasldjkf\"shiner\"df" | sed 's/\(.*\)"\(.*\)"\(.*\)/\2/g'

      shiner

命令解释

    s： 表示替换命令
    \(.*\)" : 表示第一个引号前的内容
    "\(.*\)"：表示两引号之间的内容
    )"\(.*\)：表示引号后的内容
    \2: 表示第二对括号里面的内容

括号里的表达式匹配的内容，可以用\1，\2等进行引用，第n个括号对内的内容，就用\n引用。

这个命令的意思是：

用\2代表的第二个括号的内容（shiner）去替换整个字符串，这样就得到了我们所需要的子字符串了。

###  sed 提取匹配的字符串内容 

    #STR="MAIL FROM(CCC) TO(DDD)"
    #echo $STR | sed -n 's/.*FROM([)]{1,}).*TO(.∗)/\1-\2/g'p

提取括号里面的内如
    STR="MAIL FROM(ABCD) BODY"
    echo $STR | sed 's/^.*FROM(.∗).*$/\1/g'      # ABCD

    STR="MAIL FROM(AB)CD) BODY"
    echo $STR | sed 's/^.*FROM([)]\+).*$/\1/g'        # AB

提取第一个括号和第二个括号里面的内如

    STR="MAIL FROM(ABCD) TO(EFGH) BODY"
    echo $STR | sed 's/^.*FROM([)]\+).*TO([)]\+).*$/\1-\2/g'         # ABCD-EFGH

### Linux中使用sed命令替换字符串小结

这篇文章主要介绍了Linux中使用sed命令替换字条串小结，纯属个人总结,需要的朋友可以参考下

最近写了几个小脚本用到了sed命令,学了一下,顺便记下

sed替换的基本语法为:

代码如下:

    sed 's/原字符串/替换字符串/'

单引号里面,s表示替换,三根斜线中间是替换的样式,特殊字符需要使用反斜线”\”进行转义,但是单引号”‘”是没有办法用反斜线”\”转义的,这时候只要把命令中的单引号改为双引号就行了,例如:

代码如下:

    sed "s/原字符串包含'/替换字符串包含'/" //要处理的字符包含单引号

命令中的三根斜线分隔符可以换成别的符号,这在要替换的内容有较多斜线是较为方便,只需要紧跟s定义即可,例如换成问号”?”:

代码如下:

    sed 's?原字符串?替换字符串?' //自定义分隔符为问号

可以在末尾加g替换每一个匹配的关键字,否则只替换每行的第一个,例如:

代码如下:

      sed 's/原字符串/替换字符串/' //替换所有匹配关键字

上箭头”^”表示行首,美元”$”符号如果在引号中表示行尾,但是在引号外却表示末行(最后一行),这里犯二了,搜了半天哪个符号表示首行,半天才想起来,首行就是数字”1″啊.那么在行首和行尾添加字符串就是把行尾和行首替换,例如:

代码如下:

    sed 's/^/添加的头部&/g' //在所有行首添加
    sed 's/$/&添加的尾部/g' //在所有行末添加
    sed '2s/原字符串/替换字符串/g' //替换第2行
    sed '$s/原字符串/替换字符串/g' //替换最后一行
    sed '2,5s/原字符串/替换字符串/g' //替换2到5行
    sed '2,$s/原字符串/替换字符串/g' //替换2到最后一行

替换样式可以多个在同一条命令中执行,用分号”;”分隔,例如:

代码如下:

    sed 's/^/添加的头部&/g；s/$/&添加的尾部/g' //同时执行两个替换规则

sed处理过的输出是直接输出到屏幕上的,要保存可以将输出重定向,或者使用参数”i”直接在文件中替换:

代码如下:

    sed -i 's/原字符串/替换字符串/g' filename //替换文件中的所有匹配项

写完晚上12点半了,困得不行,要是中间语言不连贯了出错了请见谅,欢迎指出.

sed如何替换每一行最后一个匹配的字符串
--------
    [root@rhel-oracle shell]# cat testfile
    abc 11 abc 11 abc 11 eee
    [root@rhel-oracle shell]# sed 's/\(.*\)11/\122/' testfile
    abc 11 abc 11 abc 22 eee
