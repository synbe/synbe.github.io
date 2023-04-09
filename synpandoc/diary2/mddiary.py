# 写的md解释器，
# 输入md文字，转换成html网页，
# 2022-6-27

import os,time

class Diary(object):
    def  __init__(self):
        self.htmlhead ='''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel="stylesheet" href="css/style.css">
<style>'''
        self.somecolors="#F0F8FF,#FAEBD7,#00FFFF,#7FFFD4,#F0FFFF,#F5F5DC,#FFE4C4,#000000,#FFEBCD,#0000FF,\
#8A2BE2,#A52A2A,#DEB887,#5F9EA0,#7FFF00,#D2691E,#FF7F50,#6495ED,#FFF8DC,#DC143C,#00FFFF,#00008B,\
#008B8B,#B8860B,#A9A9A9,#006400,#BDB76B,#8B008B,#556B2F,#FF8C00,#9932CC,#8B0000,#E9967A,#8FBC8F,\
#483D8B,#2F4F4F,#00CED1,#9400D3,#FF1493,#00BFFF,#696969,#1E90FF,#D19275,#B22222,#FFFAF0,#228B22,\
#FF00FF,#DCDCDC,#F8F8FF,#FFD700,#DAA520,#808080,#008000,#ADFF2F,#F0FFF0,#FF69B4,#CD5C5C,#4B0082,\
##9ACD32,#F0E68C,#E6E6FA,#FFF0F5,#7CFC00,#FFFACD,#ADD8E6,#F08080,#E0FFFF,#FAFAD2,#D3D3D3,#90EE90,\
#FFB6C1,#FFA07A,#20B2AA,#87CEFA,#8470FF,#778899,#B0C4DE,#FFFFE0,#00FF00,#32CD32,#FAF0E6,#FF00FF,\
#800000,#66CDAA,#0000CD,#BA55D3,#9370D8,#3CB371,#7B68EE,#00FA9A,#48D1CC,#C71585,#191970,#F5FFFA,\
#FFE4E1,#FFE4B5,#FFDEAD,#000080,#FDF5E6,#808000,#6B8E23,#FFA500,#FF4500,#DA70D6,#EEE8AA,#98FB98,\
#AFEEEE,#D87093,#FFEFD5,#FFDAB9,#CD853F,#FFC0CB,#DDA0DD,#B0E0E6,#800080,#FF0000,#BC8F8F,#4169E1,\
#8B4513,#FA8072,#F4A460,#2E8B57,#FFF5EE,#A0522D,#C0C0C0,#87CEEB,#6A5ACD,#708090,#FFFAFA,#00FF7F,\
#4682B4,#D2B48C,#008080,#D8BFD8,#FF6347,#40E0D0,#EE82EE,#D02090,#F5DEB3,#FFFFFF,#F5F5F5,#FFFF00,"
        self.css='''
html
{
margin: auto;
}
body
{
/*ont-family: 'PingFang SC', 'Noto Sans CJK', 'Source Han Sans', 'Microsoft Yahei', source-han-sans-simplified-c, sans-serif;*/
line-height: 140%;
max-width: 1024px;
margin: auto;
padding: 1em .5em;
}
a 
{
color:#0f8050;
}
a:visited
{
color:#0f8050;
}
img
{
display: block;
max-width: 100%;
margin: auto;
padding-top: 0;
padding-left: 0;
border-radius: 4px;
}

table
{
border: 1px solid #ccc;
margin:1em auto;
margin-left:0em;
}
table tr:nth-child(2n)
{
background-color: #d4d7d0;
}
thead tr th
{
background-color: #d4d7d0;
text-shadow: 1px 1px 0 #fff;
}
caption
{
color: #935417 !important;
border: 1px solid #f2e7ab;
background: #fcffcf ;
}
/*
table tr:nth-child(2n+1) {
background-color: #FFF8D4;
}
*/
pre {
font-size:90%;
background-color: #d9dee6;
color: rgb(4, 7, 34);
border: 1px solid #a5dba5;
border-radius: 4px;
white-space: normal; 
word-break: break-all;
}
code{
font-size:90%;
background-color: #f2f4f7;
color: rgb(4, 7, 34);
border: 1px solid #a5dba5;
border-radius: 4px;
}
blockquote
{
padding: .5em;
color: gray;
border-left: 4px solid gray;
font-size: 1em;
line-height: 1.1em;
margin: 10px;
}
/*以下为屏幕适应改变*/
@media screen and (max-width:767px)
{
.width50
{
width: 100%;
}
}
'''

        self.newhtmlfilehead = self.htmlhead + self.css + '\n</style>\n</head>\n' 
        self.filepath = "./static/web/default/index.html"
        self.creatNewFileTF = False
        
        
        self.mddict = {
                    "@?":"TAG",                  #询问当前文件名
                    "@":"TAG",                     #文件名
                    "######":"\n<h6>TAG</h6>",
                    "#####":"\n<h5>TAG</h5>",
                    "####":"\n<h4>TAG</h4>",
                    "###":"\n<h3>TAG</h3>",
                    "##":"\n<h2>TAG</h2>",
                    "#":"\n<h1>TAG</h1>",
                    "=":"\n<p>TAG</p>",             #段落：=
                    "---":"\n<hr>",
                    "**":"TAG",
                    "*":"TAG",    
                    "```":"\nTAG",           
                    "`":"TAG",      
                    ". ":"\n<li>TAG</li>",          # . 后有空格
                    ">":"\n<p><blockquote>TAG</blockquote></p>",  
                    "![](":"\n<img src=\"TAG\"></img>",
                    "[](":"\n<a href=\"TAG\">链接</a>",
                    }
        self.tags = (">",". ","######","#####","####","###","##","#","=")
                            
        self.mddictkeys = self.mddict.keys()
        
        self.singnal = "continue"
        

    def creatNewFile(self,file,content):
        self.currentime=time.strftime("%Y%m%d %H:%M:%S", time.localtime())
        if os.path.exists(file) == True: 
            pass
        else:
            with open(file,'w+') as _file:
                _file.write(content +"\n<p><b>"+self.filepathlink+'</b></p>\n<p>'+self.currentime+"</p><hr>")
            with open("./static/web//index5.html","a+") as fl:
                fl.write("\n<li><a href=\""+self.filepathlink+"\">"+self.filepathlink+"</a></li>")   
        print("File:",file)  
            
    def creatNewFolder(self,folder):
        os.makedirs(folder, exist_ok=True)

    def md2Html(self,content):
        try:
            for i in self.mddictkeys:
                    if content.find(i) == 0 and i == "@?":                    #询问当前文件名
                        print("corrent:",self.filepath) 
                        self.creatNewFileTF == True
                        self.outcontent=""
                        break
                    elif content.find(i) == 0 and i == "@":                                              #适用：@
                        content = content.replace(i,"")
                        self.folderpath = "./static/web/"+self.mddict[i].replace("TAG",content)
                        self.folderpath2src = "./static/web/"+self.mddict[i].replace("TAG",content)+"/src"
                        self.filepath= self.folderpath+"/index.html"
                        self.filepathlink= self.mddict[i].replace("TAG",content)+"/index.html"
                        self.creatNewFolder(self.folderpath)
                        self.creatNewFolder(self.folderpath2src)
                        self.creatNewFile(self.filepath,self.newhtmlfilehead)
                        self.outcontent=""
                        self.creatNewFileTF = True            
                        break
                    elif content.find(i) == 0 and i in self.tags:
                        content = content.replace(i,"")                                              #适用：#>.=(段落：=)
                        self.outcontent = self.mddict[i].replace("TAG",content)
                        break
                    elif content.find(i) >=0 and i == "---":
                        self.outcontent = "\n<hr>"                                                             #适用：---
                        self.creatNewFileTF = True 
                        break
                    elif content.find(i) >= 0 and i == "![](":
                        content = content.replace(i,"")                                              #适用：![]()
                        self.outcontent = self.mddict[i].replace("TAG",content).replace(")","")
                        break
                    elif content.find(i) >= 0 and i == "[](":
                        content = content.replace(i,"")                                              #适用：[]()
                        self.outcontent = self.mddict[i].replace("TAG",content).replace(")","")
                        break
                    elif content.find(i) >=0 and i == "**":
                        self.outcontent = content.replace("**","<b>",1).replace("**","</b>",1)               #适用：**粗体**
                        break
                    elif content.find(i) >=0 and i == "*":
                        self.outcontent = content.replace("*","<i>",1).replace("*","</i>",1)                 #适用：*斜体*
                        break
                    elif content.find(i) >=0 and i == "```":
                        self.outcontent = content.replace("```","\n<pre>",1).replace("```","</pre>",1)           #适用：‘pre’
                        break
                    elif content.find(i) >=0 and i == "`":
                        self.outcontent = content.replace("`","<code>",1).replace("`","</code>",1)           #适用：‘code’
                        break
                    else:
                        self.outcontent = content
                        print(".",end="")
            return self.outcontent
        except Exception as e:
            print('\n详细错误信息1：'+repr(e))
                    
            
    def conmd2Html(self,content,file):
        try:
            i = 1
            for i in range(10):
                self.md2Html(content)
                content = self.outcontent
                i = i + 1
            print("\n",self.outcontent)
            self.append2File(self.outcontent,file)
            print("To File:",self.filepath)
        except Exception as e:
            print('\n详细错误信息4：'+repr(e))
            
            
    def append2File(self,content,file):
        self.currentfile = file
        if content.find("<")  != -1 and content.find("</") != -1  or self.creatNewFileTF == True:    # 判断是否语法错误：含有“<”
            try:
                with open(file,'a+') as _file:
                    _file.write(content)
            except Exception as e:
                print('\n详细错误信息2：'+repr(e))
            self.creatNewFileTF = False
        else:
            print('\n详细错误信息3：语法错误，无效！')

if __name__ == '__main__':
    app = Diary()
    while True:
        inputcontent = input()
        app.conmd2Html(inputcontent,app.filepath)
        print("="*20)
