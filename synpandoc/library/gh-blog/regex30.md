%正则表达式30分钟入门教程
href="http://www.unibetter.com/deerchao/zhengzhe-biaodashi-jiaocheng-se.htm#mission">跳过目录</A></P>
<OL>
  <LI><A 
  href="http://www.unibetter.com/deerchao/zhengzhe-biaodashi-jiaocheng-se.htm#mission">本文目标</A> 

  <LI><A 
  href="http://www.unibetter.com/deerchao/zhengzhe-biaodashi-jiaocheng-se.htm#howtouse">如何使用本教程</A> 

  <LI><A 
  href="http://www.unibetter.com/deerchao/zhengzhe-biaodashi-jiaocheng-se.htm#introduction">正则表达式到底是什么东西？</A> 

  <LI><A 
  href="http://www.unibetter.com/deerchao/zhengzhe-biaodashi-jiaocheng-se.htm#getstarted">入门</A> 

  <LI><A 
  href="http://www.unibetter.com/deerchao/zhengzhe-biaodashi-jiaocheng-se.htm#testing">测试正则表达式</A> 

  <LI><A 
  href="http://www.unibetter.com/deerchao/zhengzhe-biaodashi-jiaocheng-se.htm#metacode">元字符</A> 

  <LI><A 
  href="http://www.unibetter.com/deerchao/zhengzhe-biaodashi-jiaocheng-se.htm#escape">字符转义</A> 

  <LI><A 
  href="http://www.unibetter.com/deerchao/zhengzhe-biaodashi-jiaocheng-se.htm#repeat">重复</A> 

  <LI><A 
  href="http://www.unibetter.com/deerchao/zhengzhe-biaodashi-jiaocheng-se.htm#charclass">字符类</A> 

  <LI><A 
  href="http://www.unibetter.com/deerchao/zhengzhe-biaodashi-jiaocheng-se.htm#alternative">分枝条件</A> 

  <LI><A 
  href="http://www.unibetter.com/deerchao/zhengzhe-biaodashi-jiaocheng-se.htm#negation">反义</A> 

  <LI><A 
  href="http://www.unibetter.com/deerchao/zhengzhe-biaodashi-jiaocheng-se.htm#grouping">分组</A> 

  <LI><A 
  href="http://www.unibetter.com/deerchao/zhengzhe-biaodashi-jiaocheng-se.htm#backreference">后向引用</A> 

  <LI><A 
  href="http://www.unibetter.com/deerchao/zhengzhe-biaodashi-jiaocheng-se.htm#lookaround">零宽断言</A> 

  <LI><A 
  href="http://www.unibetter.com/deerchao/zhengzhe-biaodashi-jiaocheng-se.htm#negativelookaround">负向零宽断言</A> 

  <LI><A 
  href="http://www.unibetter.com/deerchao/zhengzhe-biaodashi-jiaocheng-se.htm#commenting">注释</A> 

  <LI><A 
  href="http://www.unibetter.com/deerchao/zhengzhe-biaodashi-jiaocheng-se.htm#greedyandlazy">贪婪与懒惰</A> 

  <LI><A 
  href="http://www.unibetter.com/deerchao/zhengzhe-biaodashi-jiaocheng-se.htm#regexoptions">处理选项</A> 

  <LI><A 
  href="http://www.unibetter.com/deerchao/zhengzhe-biaodashi-jiaocheng-se.htm#balancedgroup">平衡组/递归匹配</A> 

  <LI><A 
  href="http://www.unibetter.com/deerchao/zhengzhe-biaodashi-jiaocheng-se.htm#more">还有些什么东西没提到</A> 

  <LI><A 
  href="http://www.unibetter.com/deerchao/zhengzhe-biaodashi-jiaocheng-se.htm#contact">联系作者</A> 

  <LI><A 
  href="http://www.unibetter.com/deerchao/zhengzhe-biaodashi-jiaocheng-se.htm#ad">最后,来点广告...</A> 

  <LI><A 
  href="http://www.unibetter.com/deerchao/zhengzhe-biaodashi-jiaocheng-se.htm#resources">网上的资源及本文参考文献</A> 

  <LI><A 
  href="http://www.unibetter.com/deerchao/zhengzhe-biaodashi-jiaocheng-se.htm#updatelog">更新说明</A> 
  </LI></OL>
<H2 id=mission>本文目标</H2>
<P>30分钟内让你明白正则表达式是什么，并对它有一些基本的了解，让你可以在自己的程序或网页里使用它。</P>
<H2 id=howtouse>如何使用本教程</H2>
<P class="important note" 
id=giveMe30Minutes>最重要的是——请给我<EM>30分钟</EM>，如果你没有使用正则表达式的经验，请不要试图在30<EM>秒</EM>内入门——除非你是超人 
:)</P>
<P>别被下面那些复杂的表达式吓倒，只要跟着我一步一步来，你会发现正则表达式其实并<SPAN 
lang=zh-cn>没有</SPAN>你想像中的那么困难。当然，如果你看完了这篇教程之后，发现自己明白了很多，却又几乎什么都记不得，那也是很正常的——我认为，没接触过正则表达式的人在看完这篇教程后，能把提到过的语法记住80%以上的可能性为零。这里只是让你明白基本的原理，以后你还需要多练习，多使用，才能熟练掌握正则表达式。</P>
<P>除了作为入门教程之外，本文还试图成为可以在日常工作中使用的正则表达式语法参考手册。就作者本人的经历来说，这个目标还是完成得不错的——你看，我自己也没能把所有的东西记下来，不是吗？</P>
<P><A id=clearButton onClick="return clearFormats();" 
href="http://www.unibetter.com/deerchao/zhengzhe-biaodashi-jiaocheng-se.htm">清除格式</A>&nbsp;文本格式约定：<SPAN 
class=name>专业术语</SPAN>&nbsp;<SPAN class=code>元字符/语法格式</SPAN>&nbsp;<SPAN 
class=regex>正则表达式</SPAN>&nbsp;<SPAN 
class=part>正则表达式中的一部分(用于分析)</SPAN>&nbsp;<SPAN 
class=string>对其进行匹配的源字符串</SPAN>&nbsp;<SPAN class=desc>对正则表达式或其中一部分的说明</SPAN></P>
<P><A id=hideButton onClick="return hideNotes();" 
href="http://www.unibetter.com/deerchao/zhengzhe-biaodashi-jiaocheng-se.htm">隐藏边注</A>&nbsp;本文右边有一些注释，主要是用来提供一些相关信息，或者给没有程序员背景的读者解释一些基本概念，通常可以忽略。</P>
<H2 id=introduction>正则表达式到底是什么东西？</H2>
<P class=note><SPAN 
class=name>字符</SPAN>是计算机软件处理文字时最基本的单位，可能是字母，数字，标点符号，空格，换行符，汉字等等。<SPAN 
class=name>字符串</SPAN>是0个或更多个字符的序列。<SPAN 
class=name>文本</SPAN>也就是文字，字符串。说某个字符串<SPAN 
class=name>匹配</SPAN>某个正则表达式，通常是指这个字符串里有一部分（或几部分分别）能满足表达式给出的条件。</P>
<P>在编写处理字符串的程序或网页时，经常会有查找符合某些复杂规则的字符串的需要。<SPAN 
class=name>正则表达式</SPAN>就是用于描述这些规则的工具。换句话说，正则表达式就是记录文本规则的代码。</P>
<P>很可能你使用过Windows/Dos下用于文件查找的<SPAN class=name>通配符(wildcard)</SPAN>，也就是<SPAN 
class=code>*</SPAN>和<SPAN class=code>?</SPAN>。如果你想查找某个目录下的所有的Word文档的话，你会搜索<SPAN 
style="COLOR: red">*.doc</SPAN>。在这里，<SPAN 
class=code>*</SPAN>会被解释成任意的字符串。和通配符类似，正则表达式也是用来进行文本匹配的工具，只不过比起通配符，它能更精确地描述你的需求——当然，代价就是更复杂——比如你可以编写一个正则表达式，用来查找<SPAN 
class=desc>所有以0开头，后面跟着2-3个数字，然后是一个连字号“-”，最后是7或8位数字的字符串</SPAN>(像<SPAN 
class=string>010-12345678</SPAN>或<SPAN class=string>0376-7654321</SPAN>)。</P>
<H2 id=getstarted>入门</H2>
<P>学习正则表达式的最好方法是从例子开始，理解例子之后再自己对例子进行修改，实验。下面给出了不少简单的例子，并对它们作了详细的说明。</P>
<P>假设你在一篇英文小说里查找<SPAN class=desc>hi</SPAN>，你可以使用正则表达式<SPAN 
class=regex>hi</SPAN>。</P>
<P>这几乎是最简单的正则表达式了，它可以精确匹配这样的字符串：<SPAN 
class=desc>由两个字符组成，前一个字符是h,后一个是i</SPAN>。通常，处理正则表达式的工具会提供一个忽略大小写的选项，如果选中了这个选项，它可以匹配<SPAN 
class=string>hi</SPAN>,<SPAN class=string>HI</SPAN>,<SPAN 
class=string>Hi</SPAN>,<SPAN class=string>hI</SPAN>这四种情况中的任意一种。</P>
<P>不幸的是，很多单词里包含<SPAN class=string>hi</SPAN>这两个连续的字符，比如<SPAN 
class=string>him</SPAN>,<SPAN class=string>history</SPAN>,<SPAN 
class=string>high</SPAN>等等。用<SPAN class=regex>hi</SPAN>来查找的话，这里边的<SPAN 
class=string>hi</SPAN>也会被找出来。如果要<SPAN 
class=desc>精确地查找hi这个单词</SPAN>的话，我们应该使用<SPAN class=regex>\bhi\b</SPAN>。</P>
<P><SPAN class=part>\b</SPAN>是正则表达式规定的一个特殊代码（好吧，某些人叫它<SPAN 
class=name>元字符，metacharacter</SPAN>），代表着<SPAN 
class=desc>单词的开头或结尾，也就是单词的分界处</SPAN>。虽然通常英文的单词是由空格，标点符号或者换行来分隔的，但是<SPAN 
class=code>\b</SPAN>并不匹配这些单词分隔字符中的任何一个，它<STRONG>只匹配一个位置</STRONG>。</P>
<P class=note>如果需要更精确的说法，<SPAN 
class=code>\b</SPAN>匹配这样的位置：它的前一个字符和后一个字符不全是(一个是,一个不是或不存在)<SPAN 
class=code>\w</SPAN>。</P>
<P>假如你要找的是<SPAN class=desc>hi后面不远处跟着一个Lucy</SPAN>，你应该用<SPAN 
class=regex>\bhi\b.*\bLucy\b</SPAN>。</P>
<P>这里，<SPAN class=part>.</SPAN>是另一个元字符，匹配<SPAN 
class=desc>除了换行符以外的任意字符</SPAN>。<SPAN 
class=part>*</SPAN>同样是元字符，不过它代表的不是字符，也不是位置，而是数量——它指定*<SPAN 
class=desc>前边的内容可以连续重复出现任意次以使整个表达式得到匹配</SPAN>。因此，<SPAN 
class=part>.*</SPAN>连在一起就意味着<SPAN class=desc>任意数量的不包含换行的字符</SPAN>。现在<SPAN 
class=regex>\bhi\b.*\bLucy\b</SPAN>的意思就很明显了：<SPAN 
class=desc>先是一个单词hi,然后是任意个任意字符(但不能是换行)，最后是Lucy这个单词</SPAN>。</P>
<P class=note>换行符就是'\n',ASCII编码为10(十六进制0x0A)的字符。</P>
<P>如果同时使用其它元字符，我们就能构造出功能更强大的正则表达式。比如下面这个例子：</P>
<P><SPAN class=regex>0\d\d-\d\d\d\d\d\d\d\d</SPAN>匹配这样的字符串：<SPAN 
class=desc>以0开头，然后是两个数字，然后是一个连字号“-”，最后是8个数字</SPAN>(也就是中国的电话号码。当然，这个例子只能匹配区号为3位的情形)。</P>
<P>这里的<SPAN class=part>\d</SPAN>是个新的元字符，匹配<SPAN 
class=desc>一位数字(0，或1，或2，或……)</SPAN>。<SPAN 
class=part>-</SPAN>不是元字符，只匹配它本身——连字符或者减号。</P>
<P>为了避免那么多烦人的重复，我们也可以这样写这个表达式：<SPAN class=regex>0\d{2}-\d{8}</SPAN>。 这里<SPAN 
class=part>\d</SPAN>后面的<SPAN class=part>{2}</SPAN>(<SPAN 
class=part>{8}</SPAN>)的意思是前面<SPAN class=part>\d</SPAN><SPAN 
class=desc>必须连续重复匹配2次(8次)</SPAN>。</P>
<H2 id=testing>测试正则表达式</H2>
<DIV class=note>
<P>其它可用的测试工具:</P>
<UL>
  <LI><A href="http://www.regexbuddy.com/">RegexBuddy</A> 
  <LI><A href="http://regexpal.com/">Javascript正则表达式在线测试工具</A> </LI></UL></DIV>
<P>如果你不觉得正则表达式很难读写的话，要么你是一个天才，要么，你不是地球人。正则表达式的语法很令人头疼，即使对经常使用它的人来说也是如此。由于难于读写，容易出错，所以找一种工具对正则表达式进行测试是很有必要的。</P>
<P>由于在不同的环境下正则表达式的一些细节是不相同的，本教程介绍的是微软 .Net Framework 
2.0下正则表达式的行为，所以，我向你介绍一个.Net下的工具<A title=转到RegexTester的官方网站（英文） 
href="http://www.dotnet2themax.com/blogs/fbalena/PermaLink,guid,13bce26d-7755-441e-92b3-1eb5f9e859f9.aspx">Regex 
Tester</A>。首先你确保已经安装了<A title="转到下载.Net Framework 2.0的页面" 
href="http://www.microsoft.com/downloads/details.aspx?displaylang=zh-cn&amp;FamilyID=0856eacb-4362-4b0d-8edd-aab15c5e04f5">.Net 
Framework 2.0</A>，然后<A title="从www.unibetter.com下载Regex Tester, 75KB" 
href="http://www.unibetter.com/deerchao/downloads/RegexTester.zip">下载Regex 
Tester</A>。这是个绿色软件，下载完后打开压缩包,直接运行RegexTester.exe就可以了。</P>
<P>下面是Regex Tester运行时的截图：</P>
<P><IMG src="../Images/Document/RegexTester.jpg" alt="Regex Tester运行时的截图" width="446" height="414"></P>
<H2 id=metacode>元字符</H2>
<P>现在你已经知道几个很有用的元字符了，如<SPAN class=code>\b</SPAN>,<SPAN class=code>.</SPAN>,<SPAN 
class=code>*</SPAN>，还有<SPAN class=code>\d</SPAN>.正则表达式里还有更多的元字符，比如<SPAN 
class=code>\s</SPAN>匹配<SPAN 
class=desc>任意的空白符，包括空格，制表符(Tab)，换行符，中文全角空格等</SPAN>。<SPAN 
class=code>\w</SPAN>匹配<SPAN class=desc>字母或数字或下划线或汉字等</SPAN>。</P>
<P class=note>对中文/汉字的特殊处理是由.Net提供的正则表达式引擎支持的，其它环境下的具体情况请查看相关文档。</P>
<P>下面来看看更多的例子：</P>
<P><SPAN class=regex>\ba\w*\b</SPAN>匹配<SPAN class=desc>以字母<SPAN 
class=part>a</SPAN>开头的单词——先是某个单词开始处(<SPAN class=part>\b</SPAN>)，然后是字母<SPAN 
class=part>a</SPAN>,然后是任意数量的字母或数字(<SPAN class=part>\w*</SPAN>)，最后是单词结束处(<SPAN 
class=part>\b</SPAN>)</SPAN>。</P>
<P class=note>好吧，现在我们说说正则表达式里的单词是什么意思吧：就是多于一个的连续的<SPAN 
class=code>\w</SPAN>。不错，这与学习英文时要背的成千上万个同名的东西的确关系不大 :)</P>
<P><SPAN class=regex>\d+</SPAN>匹配<SPAN class=desc>1个或更多连续的数字</SPAN>。这里的<SPAN 
class=part>+</SPAN>是和<SPAN class=code>*</SPAN>类似的元字符，不同的是<SPAN 
class=code>*</SPAN>匹配<SPAN class=desc>重复任意次(可能是0次)</SPAN>，而<SPAN 
class=code>+</SPAN>则匹配<SPAN class=desc>重复1次或更多次</SPAN>。</P>
<P><SPAN class=regex>\b\w{6}\b</SPAN> 匹配<SPAN 
class=desc>刚好6个字母/数字的单词</SPAN>。</P>
<TABLE cellSpacing=0>
  <CAPTION>表1.常用的元字符</CAPTION>
  <THEAD>
  <TR>
    <TH scope=col>代码</TH>
    <TH scope=col>说明</TH></TR></THEAD>
  <TBODY>
  <TR>
    <TD><SPAN class=code>.</SPAN></TD>
    <TD><SPAN class=desc>匹配除换行符以外的任意字符</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>\w</SPAN></TD>
    <TD><SPAN class=desc>匹配字母或数字或下划线或汉字</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>\s</SPAN></TD>
    <TD><SPAN class=desc>匹配任意的空白符</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>\d</SPAN></TD>
    <TD><SPAN class=desc>匹配数字</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>\b</SPAN></TD>
    <TD><SPAN class=desc>匹配单词的开始或结束</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>^</SPAN></TD>
    <TD><SPAN class=desc>匹配字符串的开始</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>$</SPAN></TD>
    <TD><SPAN class=desc>匹配字符串的结束</SPAN></TD></TR></TBODY></TABLE>
<P>元字符<SPAN class=code>^</SPAN>（和数字6在同一个键位上的符号）和<SPAN 
class=code>$</SPAN>都匹配一个位置，这和<SPAN class=code>\b</SPAN>有点类似。<SPAN 
class=code>^</SPAN>匹配你要用来查找的字符串的开头，<SPAN 
class=code>$</SPAN>匹配结尾。这两个代码在验证输入的内容时非常有用，比如一个网站如果要求你填写的QQ号必须为5位到12位数字时，可以使用：<SPAN 
class=regex>^\d{5,12}$</SPAN>。</P>
<P>这里的<SPAN class=part>{5,12}</SPAN>和前面介绍过的<SPAN 
class=part>{2}</SPAN>是类似的，只不过<SPAN class=part>{2}</SPAN>匹配<SPAN 
class=desc>只能不多不少重复2次</SPAN>，<SPAN class=part>{5,12}</SPAN>则是<SPAN 
class=desc>重复的次数不能少于5次，不能多于12次</SPAN>，否则都不匹配。</P>
<P>因为使用了<SPAN class=part>^</SPAN>和<SPAN class=part>$</SPAN>，所以输入的整个字符串都要用来和<SPAN 
class=part>\d{5,12}</SPAN>来匹配，也就是说整个输入<SPAN 
class=desc>必须是5到12个数字</SPAN>，因此如果输入的QQ号能匹配这个正则表达式的话，那就符合要求了。</P>
<P>和忽略大小写的选项类似，有些正则表达式处理工具还有一个处理多行的选项。如果选中了这个选项，<SPAN class=code>^</SPAN>和<SPAN 
class=code>$</SPAN>的意义就变成了<SPAN class=desc>匹配行的开始处和结束处</SPAN>。</P>
<H2 id=escape>字符转义</H2>
<P>如果你想查找元字符本身的话，比如你查找<SPAN class=desc>.</SPAN>,或者<SPAN 
class=desc>*</SPAN>,就出现了问题：你没办法指定它们，因为它们会被解释成别的意思。这时你就得使用<SPAN 
class=code>\</SPAN>来取消这些字符的特殊意义。因此，你应该使用<SPAN class=regex>\.</SPAN>和<SPAN 
class=regex>\*</SPAN>。当然，要查找<SPAN class=desc>\</SPAN>本身，你也得用<SPAN 
class=regex>\\</SPAN>.</P>
<P>例如：<SPAN class=regex>unibetter\.com</SPAN>匹配<SPAN 
class=desc>unibetter.com</SPAN>，<SPAN class=regex>C:\\Windows</SPAN>匹配<SPAN 
class=desc>C:\Windows</SPAN>。</P>
<H2 id=repeat>重复</H2>
<P>你已经看过了前面的<SPAN class=code>*</SPAN>,<SPAN class=code>+</SPAN>,<SPAN 
class=code>{2}</SPAN>,<SPAN 
class=code>{5,12}</SPAN>这几个匹配重复的方式了。下面是正则表达式中所有的限定符(指定数量的代码，例如*,{5,12}等)：</P>
<TABLE cellSpacing=0>
  <CAPTION>表2.常用的限定符</CAPTION>
  <THEAD>
  <TR>
    <TH scope=col>代码/语法</TH>
    <TH scope=col>说明</TH></TR></THEAD>
  <TBODY>
  <TR>
    <TD><SPAN class=code>*</SPAN></TD>
    <TD><SPAN class=desc>重复零次或更多次</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>+</SPAN></TD>
    <TD><SPAN class=desc>重复一次或更多次</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>?</SPAN></TD>
    <TD><SPAN class=desc>重复零次或一次</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>{n}</SPAN></TD>
    <TD><SPAN class=desc>重复n次</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>{n,}</SPAN></TD>
    <TD><SPAN class=desc>重复n次或更多次</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>{n,m}</SPAN></TD>
    <TD><SPAN class=desc>重复n到m次</SPAN></TD></TR></TBODY></TABLE>
<P>下面是一些使用重复的例子：</P>
<P><SPAN class=regex>Windows\d+</SPAN>匹配<SPAN 
class=desc>Windows后面跟1个或更多数字</SPAN></P>
<P><SPAN class=regex>^\w+</SPAN>匹配<SPAN 
class=desc>一行的第一个单词(或整个字符串的第一个单词，具体匹配哪个意思得看选项设置)</SPAN></P>
<H2 id=charclass>字符类</H2>
<P>要想查找数字，字母或数字，空白是很简单的，因为已经有了对应这些字符集合的元字符，但是如果你想匹配没有预定义元字符的字符集合(比如元音字母a,e,i,o,u),应该怎么办？</P>
<P>很简单，你只需要在方括号里列出它们就行了，像<SPAN class=regex>[aeiou]</SPAN>就匹配<SPAN 
class=desc>任何一个英文元音字母</SPAN>，<SPAN class=regex>[.?!]</SPAN>匹配<SPAN 
class=desc>标点符号(.或?或!)</SPAN>。</P>
<P>我们也可以轻松地指定一个字符<SPAN class=name>范围</SPAN>，像<SPAN 
class=regex>[0-9]</SPAN>代表的含意与<SPAN class=regex>\d</SPAN>就是完全一致的：<SPAN 
class=desc>一位数字</SPAN>；同理<SPAN class=regex>[a-z0-9A-Z_]</SPAN>也完全等同于<SPAN 
class=code>\w</SPAN>（如果只考虑英文的话）。</P>
<P>下面是一个更复杂的表达式：<SPAN class=regex>\(?0\d{2}[) -]?\d{8}</SPAN>。</P>
<P class=note>“(”和“)”也是元字符，后面的<A 
href="http://www.unibetter.com/deerchao/zhengzhe-biaodashi-jiaocheng-se.htm#grouping">分组节</A>里会提到，所以在这里需要使用<A 
href="http://www.unibetter.com/deerchao/zhengzhe-biaodashi-jiaocheng-se.htm#escape">转义</A>。</P>
<P>这个表达式可以匹配<SPAN class=desc>几种格式的电话号码</SPAN>，像<SPAN 
class=string>(010)88886666</SPAN>，或<SPAN class=string>022-22334455</SPAN>，或<SPAN 
class=string>02912345678</SPAN>等。我们对它进行一些分析吧：首先是一个转义字符<SPAN 
class=part>\(</SPAN>,它能出现0次或1次(<SPAN class=part>?</SPAN>),然后是一个<SPAN 
class=part>0</SPAN>，后面跟着2个数字(<SPAN class=part>\d{2}</SPAN>)，然后是<SPAN 
class=part>)</SPAN>或<SPAN class=part>-</SPAN>或<SPAN 
class=part>空格</SPAN>中的一个，它出现1次或不出现(<SPAN class=part>?</SPAN>)，最后是8个数字(<SPAN 
class=part>\d{8}</SPAN>)。</P>
<H2 id=alternative>分枝条件</H2>
<P>不幸的是，刚才那个表达式也能匹配<SPAN class=string>010)12345678</SPAN>或<SPAN 
class=string>(022-87654321</SPAN>这样的“不正确”的格式。要解决这个问题，我们需要用到<SPAN 
class=name>分枝条件</SPAN>。正则表达式里的<SPAN 
class=name>分枝条件</SPAN>指的是有几种规则，如果满足其中任意一种规则都应该当成匹配，具体方法是用<SPAN 
class=code>|</SPAN>把不同的规则分隔开。听不明白？没关系，看例子：</P>
<P><SPAN class=regex>0\d{2}-\d{8}|0\d{3}-\d{7}</SPAN>这个表达式能<SPAN 
class=desc>匹配两种以连字号分隔的电话号码：一种是三位区号，8位本地号(如010-12345678)，一种是4位区号，7位本地号(0376-2233445)</SPAN>。</P>
<P><SPAN class=regex>\(0\d{2}\)[- ]?\d{8}|0\d{2}[- ]?\d{8}</SPAN>这个表达式<SPAN 
class=desc>匹配3位区号的电话号码，其中区号可以用小括号括起来，也可以不用，区号与本地号间可以用连字号或空格间隔，也可以没有间隔</SPAN>。你可以试试用分枝条件把这个表达式扩展成也支持4位区号的。</P>
<P><SPAN 
class=regex>\d{5}-\d{4}|\d{5}</SPAN>这个表达式用于匹配美国的邮政编码。美国邮编的规则是5位数字，或者用连字号间隔的9位数字。之所以要给出这个例子是因为它能说明一个问题：<STRONG>使用分枝条件时，要注意各个条件的顺序</STRONG>。如果你把它改成<SPAN 
class=regex>\d{5}|\d{5}-\d{4}</SPAN>的话，那么就只会匹配5位的邮编(以及9位邮编的前5位)。原因是匹配分枝条件时，将会从左到右地测试每个条件，如果满足了某个分枝的话，就不会去再管其它的条件了。</P>
<H2 id=grouping>分组</H2>
<P>我们已经提到了怎么重复单个字符（直接在字符后面加上限定符就行了）；但如果想要重复多个字符又该怎么办？你可以用小括号来指定<SPAN 
class=name>子表达式</SPAN>(也叫做<SPAN 
class=name>分组</SPAN>)，然后你就可以指定这个子表达式的重复次数了，你也可以对子表达式进行其它一些操作(后面会有介绍)。</P>
<P><SPAN class=regex>(\d{1,3}\.){3}\d{1,3}</SPAN>是一个<SPAN 
class=desc>简单的IP地址匹配</SPAN>表达式。要理解这个表达式，请按下列顺序分析它：<SPAN 
class=part>\d{1,3}</SPAN>匹配<SPAN class=desc>1到3位的数字</SPAN>，<SPAN 
class=part>(\d{1,3}\.){3}</SPAN>匹配<SPAN class=desc>三位数字加上一个英文句号(这个整体也就是这个<SPAN 
class=name>分组</SPAN>)重复3次</SPAN>，最后再加上<SPAN class=desc>一个一到三位的数字</SPAN>(<SPAN 
class=part>\d{1,3}</SPAN>)。</P>
<P class=note>IP地址中每个数字都不能大于255，大家千万不要被《24》第三季的编剧给忽悠了...</P>
<P>不幸的是，它也将匹配<SPAN 
class=string>256.300.888.999</SPAN>这种不可能存在的IP地址。如果能使用算术比较的话，或许能简单地解决这个问题，但是正则表达式中并不提供关于数学的任何功能，所以只能使用冗长的分组，选择，字符类来描述一个正确的IP地址：<SPAN 
class=regex>((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)</SPAN>。</P>
<P>理解这个表达式的关键是理解<SPAN 
class=part>2[0-4]\d|25[0-5]|[01]?\d\d?</SPAN>，这里我就不细说了，你自己应该能分析得出来它的意义。</P>
<H2 id=negation>反义</H2>
<P>有时需要查找不属于某个能简单定义的字符类的字符。比如想查找除了数字以外，其它任意字符都行的情况，这时需要用到<SPAN 
class=name>反义</SPAN>：</P>
<TABLE cellSpacing=0>
  <CAPTION>表3.常用的反义代码</CAPTION>
  <THEAD>
  <TR>
    <TH scope=col>代码/语法</TH>
    <TH scope=col>说明</TH></TR></THEAD>
  <TBODY>
  <TR>
    <TD><SPAN class=code>\W</SPAN></TD>
    <TD><SPAN class=desc>匹配任意不是字母，数字，下划线，汉字的字符</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>\S</SPAN></TD>
    <TD><SPAN class=desc>匹配任意不是空白符的字符</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>\D</SPAN></TD>
    <TD><SPAN class=desc>匹配任意非数字的字符</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>\B</SPAN></TD>
    <TD><SPAN class=desc>匹配不是单词开头或结束的位置</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>[^x]</SPAN></TD>
    <TD><SPAN class=desc>匹配除了x以外的任意字符</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>[^aeiou]</SPAN></TD>
    <TD><SPAN class=desc>匹配除了aeiou这几个字母以外的任意字符</SPAN></TD></TR></TBODY></TABLE>
<P>例子：<SPAN class=regex>\S+</SPAN>匹配<SPAN class=desc>不包含空白符的字符串</SPAN>。</P>
<P><SPAN class=regex>&lt;a[^&gt;]+&gt;</SPAN>匹配<SPAN 
class=desc>用尖括号括起来的以a开头的字符串</SPAN>。</P>
<H2 id=backreference>后向引用</H2>
<P>使用小括号指定一个子表达式后，<STRONG>匹配这个子表达式的文本</STRONG>(也就是此分组捕获的内容)可以在表达式或其它程序中作进一步的处理。默认情况下，每个分组会自动拥有一个<SPAN 
class=name>组号</SPAN>，规则是：从左向右，以分组的左括号为标志，第一个出现的分组的组号为1，第二个为2，以此类推。</P>
<P><SPAN class=name>后向引用</SPAN>用于重复搜索前面某个分组匹配的文本。例如，<SPAN 
class=part>\1</SPAN>代表<SPAN class=desc>分组1匹配的文本</SPAN>。难以理解？请看示例：</P>
<P><SPAN class=regex>\b(\w+)\b\s+\1\b</SPAN>可以用来匹配<SPAN 
class=desc>重复的单词</SPAN>，像<SPAN class=string>go go</SPAN>, 或者<SPAN 
class=string>kitty kitty</SPAN>。这个表达式首先是<SPAN class=desc>一个单词</SPAN>，也就是<SPAN 
class=desc>单词开始处和结束处之间的多于一个的字母或数字</SPAN>(<SPAN 
class=part>\b(\w+)\b</SPAN>)，这个单词会被捕获到编号为1的分组中，然后是<SPAN 
class=desc>1个或几个空白符</SPAN>(<SPAN class=part>\s+</SPAN>)，最后是<SPAN 
class=desc>分组1中捕获的内容（也就是前面匹配的那个单词）</SPAN>(<SPAN class=part>\1</SPAN>)。</P>
<P>你也可以自己指定子表达式的<SPAN class=name>组名</SPAN>。要指定一个子表达式的组名，请使用这样的语法：<SPAN 
class=code>(?&lt;Word&gt;\w+)</SPAN>(或者把尖括号换成<SPAN class=code>'</SPAN>也行：<SPAN 
class=code>(?'Word'\w+)</SPAN>),这样就把<SPAN class=part>\w+</SPAN>的组名指定为<SPAN 
class=part>Word</SPAN>了。要反向引用这个分组<SPAN class=name>捕获</SPAN>的内容，你可以使用<SPAN 
class=code>\k&lt;Word&gt;</SPAN>,所以上一个例子也可以写成这样：<SPAN 
class=regex>\b(?&lt;Word&gt;\w+)\b\s+\k&lt;Word&gt;\b</SPAN>。</P>
<P>使用小括号的时候，还有很多特定用途的语法。下面列出了最常用的一些：</P>
<TABLE cellSpacing=0>
  <CAPTION>表4.常用分组语法</CAPTION>
  <TBODY>
  <TR>
    <TH scope=col>分类</TH>
    <TH scope=col>代码/语法</TH>
    <TH scope=col>说明</TH></TR>
  <TR>
    <TH rowSpan=3>捕获</TH>
    <TD><SPAN class=code>(exp)</SPAN></TD>
    <TD><SPAN class=desc>匹配exp,并捕获文本到自动命名的组里</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>(?&lt;name&gt;exp)</SPAN></TD>
    <TD><SPAN class=desc>匹配exp,并捕获文本到名称为name的组里，也可以写成(?'name'exp)</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>(?:exp)</SPAN></TD>
    <TD><SPAN class=desc>匹配exp,不捕获匹配的文本，也不给此分组分配组号</SPAN></TD></TR>
  <TR>
    <TH rowSpan=4>零宽断言</TH>
    <TD><SPAN class=code>(?=exp)</SPAN></TD>
    <TD><SPAN class=desc>匹配exp前面的位置</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>(?&lt;=exp)</SPAN></TD>
    <TD><SPAN class=desc>匹配exp后面的位置</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>(?!exp)</SPAN></TD>
    <TD><SPAN class=desc>匹配后面跟的不是exp的位置</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>(?&lt;!exp)</SPAN></TD>
    <TD><SPAN class=desc>匹配前面不是exp的位置</SPAN></TD></TR>
  <TR>
    <TH>注释</TH>
    <TD><SPAN class=code>(?#comment)</SPAN></TD>
    <TD><SPAN 
  class=desc>这种类型的分组不对正则表达式的处理产生任何影响，用于提供注释让人阅读</SPAN></TD></TR></TBODY></TABLE>
<P>我们已经讨论了前两种语法。第三个<SPAN 
class=code>(?:exp)</SPAN>不会改变正则表达式的处理方式，只是这样的组匹配的内容<SPAN 
class=desc>不会像前两种那样被捕获到某个组里面，也不会拥有组号</SPAN>。</P>
<H2 id=lookaround>零宽断言</H2>
<P 
class=note>地球人，是不是觉得这些术语名称太复杂，太难记了？我也和你一样。知道有这么一种东西就行了，它叫什么，随它去吧！“无名，万物之始...”</P>
<P>接下来的四个用于查找在某些内容(但并不包括这些内容)之前或之后的东西，也就是说它们像<SPAN class=code>\b</SPAN>,<SPAN 
class=code>^</SPAN>,<SPAN 
class=code>$</SPAN>那样用于指定一个位置，这个位置应该满足一定的条件(即断言)，因此它们也被称为<SPAN 
class=name>零宽断言</SPAN>。最好还是拿例子来说明吧：</P>
<P class=note>断言用来声明一个应该为真的事实。正则表达式中只有当断言为真时才会继续进行匹配。</P>
<P><SPAN class=code>(?=exp)</SPAN>也叫<SPAN class=name>零宽度正预测先行断言</SPAN>，它<SPAN 
class=desc>断言自身出现的位置的后面能匹配表达式exp</SPAN>。比如<SPAN 
class=regex>\b\w+(?=ing\b)</SPAN>，匹配<SPAN 
class=desc>以ing结尾的单词的前面部分(除了ing以外的部分)</SPAN>，如查找<SPAN class=string>I'm singing 
while you're dancing.</SPAN>时，它会匹配<SPAN class=desc>sing</SPAN>和<SPAN 
class=desc>danc</SPAN>。</P>
<P><SPAN class=code>(?&lt;=exp)</SPAN>也叫<SPAN 
class=name>零宽度正回顾后发断言</SPAN>，它<SPAN 
class=desc>断言自身出现的位置的前面能匹配表达式exp</SPAN>。比如<SPAN 
class=regex>(?&lt;=\bre)\w+\b</SPAN>会匹配<SPAN 
class=desc>以re开头的单词的后半部分(除了re以外的部分)</SPAN>，例如在查找<SPAN class=string>reading a 
book</SPAN>时，它匹配<SPAN class=desc>ading</SPAN>。</P>
<P>假如你想要给一个很长的数字中每三位间加一个逗号(当然是从右边加起了)，你可以这样查找需要在前面和里面添加逗号的部分：<SPAN 
class=regex>((?&lt;=\d)\d{3})*\b</SPAN>，用它对<SPAN 
class=string>1234567890</SPAN>进行查找时结果是<SPAN class=desc>234567890</SPAN>。</P>
<P>下面这个例子同时使用了这两种断言：<SPAN class=regex>(?&lt;=\s)\d+(?=\s)</SPAN>匹配<SPAN 
class=desc>以空白符间隔的数字(再次强调，不包括这些空白符)</SPAN>。</P>
<H2 id=negativelookaround>负向零宽断言</H2>
<P>前面我们提到过怎么查找<STRONG>不是某个字符或不在某个字符类里</STRONG>的字符的方法(反义)。但是如果我们只是想要<STRONG>确保某个字符没有出现，但并不想去匹配它</STRONG>时怎么办？例如，如果我们想查找这样的单词--它里面出现了字母q,但是q后面跟的不是字母u,我们可以尝试这样：</P>
<P><SPAN class=regex>\b\w*q[^u]\w*\b</SPAN>匹配<SPAN 
class=desc>包含<STRONG>后面不是字母u的字母q</STRONG>的单词</SPAN>。但是如果多做测试(或者你思维足够敏锐，直接就观察出来了)，你会发现，如果q出现在单词的结尾的话，像<STRONG>Iraq</STRONG>,<STRONG>Benq</STRONG>，这个表达式就会出错。这是因为<SPAN 
class=part>[^u]</SPAN>总要匹配一个字符，所以如果q是单词的最后一个字符的话，后面的<SPAN 
class=part>[^u]</SPAN>将会匹配q后面的单词分隔符(可能是空格，或者是句号或其它的什么)，后面的<SPAN 
class=part>\w*\b</SPAN>将会匹配下一个单词，于是<SPAN 
class=regex>\b\w*q[^u]\w*\b</SPAN>就能匹配整个<SPAN class=string>Iraq 
fighting</SPAN>。<SPAN 
class=name>负向零宽断言</SPAN>能解决这样的问题，因为它只匹配一个位置，并不<STRONG>消费</STRONG>任何字符。现在，我们可以这样来解决这个问题：<SPAN 
class=regex>\b\w*q(?!u)\w*\b</SPAN>。</P>
<P><SPAN class=name>零宽度负预测先行断言</SPAN><SPAN class=code>(?!exp)</SPAN>，<SPAN 
class=desc>断言此位置的后面不能匹配表达式exp</SPAN>。例如：<SPAN 
class=regex>\d{3}(?!\d)</SPAN>匹配<SPAN 
class=desc>三位数字，而且这三位数字的后面不能是数字</SPAN>；<SPAN 
class=regex>\b((?!abc)\w)+\b</SPAN>匹配<SPAN class=desc>不包含连续字符串abc的单词</SPAN>。</P>
<P>同理，我们可以用<SPAN class=code>(?&lt;!exp)</SPAN>,<SPAN 
class=name>零宽度正回顾后发断言</SPAN>来<SPAN class=desc>断言此位置的前面不能匹配表达式exp</SPAN>：<SPAN 
class=regex>(?&lt;![a-z])\d{7}</SPAN>匹配<SPAN 
class=desc>前面不是小写字母的七位数字</SPAN>。</P>
<P class=note>请详细分析表达式<SPAN 
class=regex>(?&lt;=&lt;(\w+)&gt;).*(?=&lt;\/\1&gt;)</SPAN>，这个表达式最能表现零宽断言的真正用途。</P>
<P>一个更复杂的例子：<SPAN 
class=regex>(?&lt;=&lt;(\w+)&gt;).*(?=&lt;\/\1&gt;)</SPAN>匹配<SPAN 
class=desc>不包含属性的简单HTML标签内里的内容</SPAN>。<SPAN 
class=code>(&lt;?(\w+)&gt;)</SPAN>指定了这样的<SPAN class=name>前缀</SPAN>：<SPAN 
class=desc>被尖括号括起来的单词</SPAN>(比如可能是&lt;b&gt;)，然后是<SPAN 
class=part>.*</SPAN>(任意的字符串),最后是一个<SPAN class=name>后缀</SPAN><SPAN 
class=part>(?=&lt;\/\1&gt;)</SPAN>。注意后缀里的<SPAN 
class=part>\/</SPAN>，它用到了前面提过的字符转义；<SPAN class=part>\1</SPAN>则是一个反向引用，引用的正是<SPAN 
class=desc>捕获的第一组</SPAN>，前面的<SPAN 
class=part>(\w+)</SPAN>匹配的内容，这样如果前缀实际上是&lt;b&gt;的话，后缀就是&lt;/b&gt;了。整个表达式匹配的是&lt;b&gt;和&lt;/b&gt;之间的内容(再次提醒，不包括前缀和后缀本身)。</P>
<H2 id=commenting>注释</H2>
<P>小括号的另一种用途是通过语法<SPAN class=code>(?#comment)</SPAN>来包含注释。例如：<SPAN 
class=regex>2[0-4]\d(?#200-249)|25[0-5](?#250-255)|[01]?\d\d?(?#0-199)</SPAN>。</P>
<P>要包含注释的话，最好是启用“忽略模式里的空白符”选项，这样在编写表达式时能任意的添加空格，Tab，换行，而实际使用时这些都将被忽略。启用这个选项后，在#后面到这一行结束的所有文本都将被当成注释忽略掉。例如，我们可以前面的一个表达式写成这样：</P><PRE class=regex>      (?&lt;=    # 断言要匹配的文本的前缀
      &lt;(\w+)&gt; # 查找尖括号括起来的字母或数字(即HTML/XML标签)
      )       # 前缀结束
      .*      # 匹配任意文本
      (?=     # 断言要匹配的文本的后缀
      &lt;\/\1&gt;  # 查找尖括号括起来的内容：前面是一个"/"，后面是先前捕获的标签
      )       # 后缀结束</PRE>
<H2 id=greedyandlazy>贪婪与懒惰</H2>
<P>当正则表达式中包含能接受重复的限定符时，通常的行为是（在使整个表达式能得到匹配的前提下）匹配<STRONG>尽可能多</STRONG>的字符。考虑这个表达式：<SPAN 
class=regex>a.*b</SPAN>，它将会匹配<SPAN 
class=desc>最长的以a开始，以b结束的字符串</SPAN>。如果用它来搜索<SPAN 
class=string>aabab</SPAN>的话，它会匹配整个字符串<SPAN class=desc>aabab</SPAN>。这被称为<SPAN 
class=name>贪婪</SPAN>匹配。</P>
<P>有时，我们更需要<SPAN 
class=name>懒惰</SPAN>匹配，也就是匹配<STRONG>尽可能少</STRONG>的字符。前面给出的限定符都可以被转化为懒惰匹配模式，只要在它后面加上一个问号<SPAN 
class=code>?</SPAN>。这样<SPAN class=regex>.*?</SPAN>就意味着<SPAN 
class=desc>匹配任意数量的重复，但是在能使整个匹配成功的前提下使用最少的重复</SPAN>。现在看看懒惰版的例子吧：</P>
<P><SPAN class=regex>a.*?b</SPAN>匹配<SPAN 
class=desc>最短的，以a开始，以b结束的字符串</SPAN>。如果把它应用于<SPAN 
class=string>aabab</SPAN>的话，它会匹配<SPAN class=desc>aab（第一到第三个字符）</SPAN>和<SPAN 
class=desc>ab（第四到第五个字符）</SPAN>。</P>
<P 
class=note>为什么第一个匹配是aab（第一到第三个字符）而不是ab（第二到第三个字符）？简单地说，因为正则表达式有另一条规则，比懒惰／贪婪规则的优先级更高：最先开始的匹配拥有最高的优先权——The 
match that begins earliest wins。</P>
<TABLE cellSpacing=0>
  <CAPTION>表5.懒惰限定符</CAPTION>
  <THEAD>
  <TR>
    <TH scope=col>代码/语法</TH>
    <TH scope=col>说明</TH></TR></THEAD>
  <TBODY>
  <TR>
    <TD><SPAN class=code>*?</SPAN></TD>
    <TD><SPAN class=desc>重复任意次，但尽可能少重复</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>+?</SPAN></TD>
    <TD><SPAN class=desc>重复1次或更多次，但尽可能少重复</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>??</SPAN></TD>
    <TD><SPAN class=desc>重复0次或1次，但尽可能少重复</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>{n,m}?</SPAN></TD>
    <TD><SPAN class=desc>重复n到m次，但尽可能少重复</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>{n,}?</SPAN></TD>
    <TD><SPAN class=desc>重复n次以上，但尽可能少重复</SPAN></TD></TR></TBODY></TABLE>
<H2 id=regexoptions>处理选项</H2>
<P class=note>在C#中，你可以使用<A title="MSDN 相关文档" 
href="http://msdn2.microsoft.com/zh-cn/library/h5845fdz.aspx">Regex(String, 
RegexOptions)构造函数</A>来设置正则表达式的处理选项。如：Regex regex = new Regex("\ba\w{6}\b", 
RegexOptions.IgnoreCase);</P>
<P>上面介绍了几个选项如忽略大小写，处理多行等，这些选项能用来改变处理正则表达式的方式。下面是.Net中常用的正则表达式选项：</P>
<TABLE cellSpacing=0>
  <CAPTION>表6.常用的处理选项</CAPTION>
  <THEAD>
  <TR>
    <TH scope=col>名称</TH>
    <TH scope=col>说明</TH></TR></THEAD>
  <TBODY>
  <TR>
    <TD>IgnoreCase(忽略大小写)</TD>
    <TD>匹配时不区分大小写。</TD></TR>
  <TR>
    <TD>Multiline(多行模式)</TD>
    <TD>更改<SPAN class=code>^</SPAN>和<SPAN 
      class=code>$</SPAN>的含义，使它们分别在任意一行的行首和行尾匹配，而不仅仅在整个字符串的开头和结尾匹配。(在此模式下,<SPAN 
      class=code>$</SPAN>的精确含意是:匹配\n之前的位置以及字符串结束前的位置.) </TD></TR>
  <TR>
    <TD>Singleline(单行模式)</TD>
    <TD>更改<SPAN class=code>.</SPAN>的含义，使它与每一个字符匹配（包括换行符\n）。 </TD></TR>
  <TR>
    <TD>IgnorePatternWhitespace(忽略空白)</TD>
    <TD>忽略表达式中的非转义空白并启用由<SPAN class=code>#</SPAN>标记的注释。</TD></TR>
  <TR>
    <TD>RightToLeft(从右向左查找)</TD>
    <TD>匹配从右向左而不是从左向右进行。</TD></TR>
  <TR>
    <TD>ExplicitCapture(显式捕获)</TD>
    <TD>仅捕获已被显式命名的组。</TD></TR>
  <TR>
    <TD>ECMAScript(JavaScript兼容模式)</TD>
    <TD>使表达式的行为与它在JavaScript里的行为一致。</TD></TR></TBODY></TABLE>
<P>一个经常被问到的问题是：是不是只能同时使用多行模式和单行模式中的一种？答案是：不是。这两个选项之间没有任何关系，除了它们的名字比较相似（以至于让人感到疑惑）以外。</P>
<H2 id=balancedgroup>平衡组/递归匹配</H2>
<P class="important note">这里介绍的平衡组语法是由.Net 
Framework支持的；其它语言／库不一定支持这种功能，或者支持此功能但需要使用不同的语法。</P>
<P>有时我们需要匹配像<SPAN class=desc>( 100 * ( 50 + 15 ) 
)这样的可嵌套的层次性结构</SPAN>，这时简单地使用<SPAN 
class=code>\(.+\)</SPAN>则只会匹配到最左边的左括号和最右边的右括号之间的内容(这里我们讨论的是贪婪模式，懒惰模式也有下面的问题)。假如原来的字符串里的左括号和右括号出现的次数不相等，比如<SPAN 
class=string>( 5 / ( 3 + 2 ) ) 
)</SPAN>，那我们的匹配结果里两者的个数也不会相等。有没有办法在这样的字符串里匹配到最长的，配对的括号之间的内容呢？</P>
<P>为了避免<SPAN class=code>(</SPAN>和<SPAN 
class=code>\(</SPAN>把你的大脑彻底搞糊涂，我们还是用尖括号代替圆括号吧。现在我们的问题变成了如何把<SPAN class=string>xx 
&lt;aa &lt;bbb&gt; &lt;bbb&gt; aa&gt; yy</SPAN>这样的字符串里，最长的配对的尖括号内的内容捕获出来？</P>
<P>这里需要用到以下的语法构造：</P>
<UL>
  <LI><SPAN class=code>(?'group')</SPAN> 把捕获的内容命名为group,并压入<SPAN 
  class=name>堆栈(Stack)</SPAN> 
  <LI><SPAN class=code>(?'-group')</SPAN> 
  从堆栈上弹出最后压入堆栈的名为group的捕获内容，如果堆栈本来为空，则本分组的匹配失败 
  <LI><SPAN class=code>(?(group)yes|no)</SPAN> 
  如果堆栈上存在以名为group的捕获内容的话，继续匹配yes部分的表达式，否则继续匹配no部分 
  <LI><SPAN class=code>(?!)</SPAN> 零宽负向先行断言，由于没有后缀表达式，试图匹配总是失败 </LI></UL>
<P 
class=note>如果你不是一个程序员（或者你自称程序员但是不知道堆栈是什么东西），你就这样理解上面的三种语法吧：第一个就是在黑板上写一个"group"，第二个就是从黑板上擦掉一个"group"，第三个就是看黑板上写的还有没有"group"，如果有就继续匹配yes部分，否则就匹配no部分。</P>
<P>我们需要做的是每碰到了左括号，就在压入一个"Open",每碰到一个右括号，就弹出一个，到了最后就看看堆栈是否为空－－如果不为空那就证明左括号比右括号多，那匹配就应该失败。正则表达式引擎会进行回溯(放弃最前面或最后面的一些字符)，尽量使整个表达式得到匹配。</P><PRE class=regex>&lt;                         #最外层的左括号
    [^&lt;&gt;]*                #最外层的左括号后面的不是括号的内容
    (
        (
            (?'Open'&lt;)    #碰到了左括号，在黑板上写一个"Open"
            [^&lt;&gt;]*       #匹配左括号后面的不是括号的内容
        )+
        (
            (?'-Open'&gt;)   #碰到了右括号，擦掉一个"Open"
            [^&lt;&gt;]*        #匹配右括号后面不是括号的内容
        )+
    )*
    (?(Open)(?!))         #在遇到最外层的右括号前面，判断黑板上还有没有没擦掉的"Open"；如果还有，则匹配失败
&gt;                         #最外层的右括号</PRE>
<P>平衡组的一个最常见的应用就是匹配HTML,下面这个例子可以匹配<SPAN class=desc>嵌套的&lt;div&gt;标签</SPAN>：<SPAN 
class=regex>&lt;div[^&gt;]*&gt;[^&lt;&gt;]*(((?'Open'&lt;div[^&gt;]*&gt;)[^&lt;&gt;]*)+((?'-Open'&lt;/div&gt;)[^&lt;&gt;]*)+)*(?(Open)(?!))&lt;/div&gt;</SPAN>.</P>
<H2 id=more>还有些什么东西没提到</H2>
<P>我已经描述了构造正则表达式的大量元素，还有一些我没有提到的东西。下面是未提到的元素的列表，包含语法和简单的说明。你可以在网上找到更详细的参考资料来学习它们--当你需要用到它们的时候。如果你安装了MSDN 
Library,你也可以在里面找到关于.net下正则表达式详细的文档。</P>
<TABLE cellSpacing=0>
  <CAPTION>表7.尚未详细讨论的语法</CAPTION>
  <THEAD>
  <TR>
    <TH scope=col>代码/语法</TH>
    <TH scope=col>说明</TH></TR></THEAD>
  <TBODY>
  <TR>
    <TD><SPAN class=code>\a</SPAN></TD>
    <TD><SPAN class=desc>报警字符(打印它的效果是电脑嘀一声)</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>\b</SPAN></TD>
    <TD><SPAN class=desc>通常是单词分界位置，但如果在字符类里使用代表退格</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>\t</SPAN></TD>
    <TD><SPAN class=desc>制表符，Tab</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>\r</SPAN></TD>
    <TD><SPAN class=desc>回车</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>\v</SPAN></TD>
    <TD><SPAN class=desc>竖向制表符</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>\f</SPAN></TD>
    <TD><SPAN class=desc>换页符</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>\n</SPAN></TD>
    <TD><SPAN class=desc>换行符</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>\e</SPAN></TD>
    <TD><SPAN class=desc>Escape</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>\0nn</SPAN></TD>
    <TD><SPAN class=desc>ASCII代码中八进制代码为nn的字符</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>\xnn</SPAN></TD>
    <TD><SPAN class=desc>ASCII代码中十六进制代码为nn的字符</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>\unnnn</SPAN></TD>
    <TD><SPAN class=desc>Unicode代码中十六进制代码为nnnn的字符</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>\cN</SPAN></TD>
    <TD><SPAN class=desc>ASCII控制字符。比如\cC代表Ctrl+C</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>\A</SPAN></TD>
    <TD><SPAN class=desc>字符串开头(类似^，但不受处理多行选项的影响)</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>\Z</SPAN></TD>
    <TD><SPAN class=desc>字符串结尾或行尾(不受处理多行选项的影响)</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>\z</SPAN></TD>
    <TD><SPAN class=desc>字符串结尾(类似$，但不受处理多行选项的影响)</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>\G</SPAN></TD>
    <TD><SPAN class=desc>当前搜索的开头</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>\p{name}</SPAN></TD>
    <TD><SPAN class=desc>Unicode中命名为name的字符类，例如\p{IsGreek}</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>(?&gt;exp)</SPAN></TD>
    <TD><SPAN class=desc>贪婪子表达式</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>(?&lt;x&gt;-&lt;y&gt;exp)</SPAN></TD>
    <TD><SPAN class=desc>平衡组</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>(?im-nsx:exp)</SPAN></TD>
    <TD><SPAN class=desc>在子表达式exp中改变处理选项</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>(?im-nsx)</SPAN></TD>
    <TD><SPAN class=desc>为表达式后面的部分改变处理选项</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>(?(exp)yes|no)</SPAN></TD>
    <TD><SPAN 
    class=desc>把exp当作零宽正向先行断言，如果在这个位置能匹配，使用yes作为此组的表达式；否则使用no</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>(?(exp)yes)</SPAN></TD>
    <TD><SPAN class=desc>同上，只是使用空表达式作为no</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>(?(name)yes|no)</SPAN></TD>
    <TD><SPAN class=desc>如果命名为name的组捕获到了内容，使用yes作为表达式；否则使用no</SPAN></TD></TR>
  <TR>
    <TD><SPAN class=code>(?(name)yes)</SPAN></TD>
    <TD><SPAN class=desc>同上，只是使用空表达式作为no</SPAN></TD></TR></TBODY></TABLE>
<H2 id=contact>联系作者</H2>
<P>好吧,我承认,我骗了你,读到这里你肯定花了不止30分钟.相信我,这是我的错,而不是因为你太笨.我之所以说"30分钟",是为了让你有信心,有耐心继续下去.既然你看到了这里,那证明我的阴谋成功了.被忽悠的感觉很爽吧？</P>
<P>要投诉我,或者觉得我其实可以做得更好,或者有任何其它问题,欢迎来<A 
href="http://www.cnblogs.com/deerchao/archive/2006/08/24/zhengzhe30fengzhongjiaocheng.html">我的博客</A>让我知道.</P>
<H2 id=resources>网上的资源及本文参考文献</H2>
<UL>
  <LI><A 
  href="http://msdn.microsoft.com/library/chs/default.asp?url=/library/CHS/jscript7/html/jsreconintroductiontoregularexpressions.asp">微软的正则表达式教程</A> 

  <LI><A 
  href="http://msdn2.microsoft.com/zh-cn/library/system.text.regularexpressions.regex.aspx">System.Text.RegularExpressions.Regex类(MSDN)</A> 

  <LI><A href="http://www.regular-expressions.info/">专业的正则表达式教学网站(英文)</A> 
  <LI><A 
  href="http://weblogs.asp.net/whaggard/archive/2005/02/20/377025.aspx">关于.Net下的平衡组的详细讨论（英文）</A> 

  <LI><A href="http://www.oreilly.com/catalog/regex2/">Mastering Regular 
  Expressions (Second Edition)</A> </LI></UL>
<H2 id=updatelog>更新说明</H2>
<OL>
  <LI>2006-3-27 第一版 
  <LI>2006-10-12 第二版 
  <UL>
    <LI>修正了几个细节上的错误和不准确的地方 
    <LI>增加了对处理中文时的一些说明 
    <LI>更改了几个术语的翻译（采用了MSDN的翻译方式） 
    <LI>增加了平衡组的介绍 
    <LI>放弃了对The Regulator的介绍，改用Regex Tester </LI></UL>
  <LI>2007-3-12 V2.1 
  <UL>
    <LI>修正了几个小的错误 
    <LI>增加了对处理选项(RegexOptions)的介绍 </LI></UL>
  <LI>2007-5-28 V2.2 
  <UL>
    <LI>重新组织了对零宽断言的介绍 
    <LI>删除了几个不太合适的示例，添加了几个实用的示例 
    <LI>其它一些微小的更改 </LI></UL>
  <LI>2007-8-3 V2.21 
  <UL>
    <LI>修改了几处文字错误 
    <LI>修改/添加了对$,\b的精确说明 
    <LI>承认了作者是个骗子 
    <LI>给RegexTester添加了Singleline选项的相关功能 </LI></UL>
  <LI>2008-4-13 v2.3 
  <UL>
    <LI>调整了部分章节的次序 
    <LI>修改了页面布局，删除了专门的参考节 
<LI>针对读者的反馈，调整了部分内容 </LI></UL></LI></OL>
</BODY></HTML>

