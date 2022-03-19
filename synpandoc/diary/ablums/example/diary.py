import os,random,markdown,time
import pdfkit

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
/*    font-family: 'PingFang SC', 'Noto Sans CJK', 'Source Han Sans', 'Microsoft Yahei', source-han-sans-simplified-c, sans-serif;
font-size: 16px;*/
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
h1{
font-size: 1.8em !important;
color: #4c9ed9;
font-weight: bold;
text-shadow: 1px 1px 1px rgb(97, 172, 217);
}
h2{
font-size: 1.6em !important;
color: #4c9ed9;
font-weight: bold;
text-shadow: 1px 1px 1px rgb(97, 172, 217);
}
h3{
font-size: 1.4em !important;
color: #4c9ed9;
font-weight: bold;
text-shadow: 1px 1px 1px rgb(97, 172, 217);
}
h4{
font-size: 1.2em !important;
color: #4c9ed9;
font-weight: bold;
text-shadow: 1px 1px 1px rgb(97, 172, 217);
}
h5{
font-size: 1em !important;
color: #4c9ed9;
font-weight: bold;
text-shadow: 1px 1px 1px rgb(97, 172, 217);
}
h6 {
font-size: 0.9em !important;
color: #447171 !important;
border-bottom:#447171 solid 1px;
padding-bottom:1em;
font-weight: bold;
text-shadow: 1px 1px 1px rgb(97, 172, 217);
}
pre {

background-color: #d7e4ee;
color: rgb(4, 7, 34);
}
hr{
width:100%;
margin:0 auto;
border: 0;
height: 2px;
background: #333;
background-image: linear-gradient(to right, red, #333, rgb(9, 206, 91));
}
blockquote
{
padding: .5em;
color: #fff;
border: 2px solid #fff;
border-radius: 4px;
font-size:1em;
line-height:1.1em;
}
blockquote
{
margin: 10px;

background: #777;
}
blockquote blockquote
{
margin: -10px;

background: #337ab7;
}
blockquote blockquote  blockquote
{
margin: -10px;

background: #5cb85c;
}

blockquote blockquote  blockquote blockquote
{
margin: -10px;

background: #f0ad4e;
}

blockquote blockquote  blockquote blockquote blockquote
{
margin: -10px;

background: #f32721;
}

blockquote blockquote  blockquote blockquote blockquote blockquote
{
margin: -10px;

background: #5bc0de;
}
.div-a{ 
float:left;
width:49%;
} 
.div-b{ 
float:right;
width:49%;
} 
.div-c{ 
width:95%;
padding: 1em;
background:rgb(240, 242, 222);
border: rgb(170, 162, 44) 1px solid;
margin-bottom: 2em;
border-radius:5px;
box-shadow: 10px 10px 5px #888888;
position: relative;
} 
.div-c h1 {
color:#fff;
text-shadow: 1px 1px 2px rgb(16, 11, 75);
}
.div-c p {
text-shadow: 1px 1px 0px #fff;
}
.div-c-banner{ 
width: 101%;
margin-left: -32px;
padding-right: 10px;
font-weight: bold;
color: rgb(255, 255, 255);
line-height: 0px;
border-right-color: transparent !important;
box-shadow: -5px 11px 8px -5px #110f0f;
} 
.div-c-banner-tag{ 
margin-left: -32px;
width: 0;
border: #332317 8px solid;
border-left-color: transparent;
border-bottom-color: transparent;
} 
.div-c-content{
margin-top: -4em;
}
.div-c-date{ 
float: left;
width: 49%;
text-shadow: 1px 1px 0px #fff;
} 
.div-c-icon{ 
float: right;
text-align: right;
width: 49%;
text-shadow: 1px 1px 0px #fff;
} 
.div-c-footer{ 
border-top: rgb(170, 162, 44) 1px solid;
color:  rgb(170, 162, 44);
padding: 1em;
} 
/*以下为屏幕适应改变*/
@media screen and (max-width:767px)
{
#TOC
{
display: none;
}
#header
{
margin-bottom: 12px;

border-bottom: 0;
background-color: #fff;
}
h2.author,
h3.date
{
border-top: 0px solid #e1e1e1;
padding-top: 0em !important;
margin-bottom: 1em !important;
}
}
h1.title
{
font-weight: bold;

text-align: left;

color: #000;
}
.width50
{
width: 100%;
}
}
'''
        print('='*10 + 'Checking   ./input.md:'+ '='*10) 
        self.check4inputfileexist()
        print('='*10 + 'Checking ./index.html:'+ '='*10) 
        self.check4indexhtmlexist()
        
    def check4inputfileexist(self):
        if os.path.exists('input.md'):
            if os.path.getsize('input.md') == 0:
                print('Empty: ./input.md') 
            else:
                print('Exsited: ./input.md')
        else:
            self.creat4emptyinputfile()
            print('Created: ./input.md !') 

    def check4indexhtmlexist(self):
        if os.path.exists('index.html') and os.path.getsize('input.md') != 0:
            self.append2md2html()
            print("Added new diary ! ")  
        elif os.path.exists('index.html') and os.path.getsize('input.md') == 0:
            print("...")
        elif os.path.exists('index.html') ==False and os.path.getsize('input.md') == 0:
            self.creat4initindexhtml()
            print("Created: ./index.html")
        elif os.path.exists('index.html') ==False and os.path.getsize('input.md') != 0:
            self.creat4initindexhtml()
            print("Created: ./index.html")
            self.append2md2html()
            print("Added: new diary ! ")    

    def creat4emptyinputfile(self):
        open('input.md','w+').close()

    def creat4initindexhtml(self):
        try:
            self.init_content="# Hello World !\n\nStart your diary here..."
            self.creat4htmlhead()
            self.md2html(self.init_content)
            self.exporthtml2pdf()
        except:
            print('...')

    def md2html(self,content):
            self.currentime=time.strftime("%Y.%m.%d %H:%M:%S", time.localtime())
            try:
                with open('index.html','a+') as fl:
                    data = markdown.markdown(content,extensions=['markdown.extensions.extra'])
                    icon_ls= list("☺♡✿☂☻♞♨۞❉ஐ♠♣♥♦◕☃☎☏♧㍿☎㊝❃✎❂❁❀囍㊣☢✄☪☣♬♝☠☆☄★")
                    icon_num = random.randint(0,len(icon_ls)-1)
                    icon = icon_ls[icon_num]
                    bannercolor_ls= self.somecolors.split(",")
                    bannercolor_num = random.randint(0,len(bannercolor_ls)-1)
                    bannercolor = bannercolor_ls[bannercolor_num]
                    num_random = random.randint(1000000000,9999999999)
                    num_str = ' | No.'+ str(num_random)
                    separator_begin = '<!-- Begin' +'-'*20+ num_str+'-'*20 + ' -->'
                    separator_end = '<!-- End..' +'-'*20+ num_str+'-'*20 + ' -->'
                    div_content ='\n'+separator_begin+'\n'+\
                        '<div class="div-c">'+\
                        '<div class="div-c-banner" style="border:24px solid '+bannercolor+';"></div>'+\
                        '<div class="div-c-banner-tag"></div>'+\
                        '<div class="div-c-content">'+data+'</div>'+\
                        '<div class="div-c-footer">'+\
                        '<div class="div-c-date">'+ self.currentime+'</div>'+\
                        '<div class="div-c-icon">'+icon+num_str+'</div>'+\
                        '</div>'+\
                        '</div>\n'+separator_end+'\n'
                    fl.write(div_content)
                    print(num_str)
            except Exception as e:
                        print('详细错误信息：'+repr(e))

    def append2md2html(self):
        try:
            with open('input.md','r+') as fl:
                self.new_content = fl.read()
                self.md2html(self.new_content)
                self.creat4emptyinputfile()
                self.exporthtml2pdf()
        except:
            print('...')

    def creat4htmlhead(self):
        with open('index.html','w+') as fl:
            self.rawhtmlhead = self.htmlhead + self.css + '\n</style>\n</head>\n' 
            fl.write(self.rawhtmlhead)
            # absurl = os.path.abspath('index.html')

    def exporthtml2pdf(self):
        with open('index.html') as fl:
            options = {
            'margin-bottom': '0.75in',
            'footer-right': '[page]'
                }
            pdfkit.from_file(fl, 'index.pdf')

if __name__ == '__main__':
    app = Diary()