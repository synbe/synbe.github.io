% BuffaloWHR-G300NCHv2刷OpenWrt教程
##  OpenWrt　Buffalo WHR-G300N V2 官方链接

1. [wiki.openwrt.org](https://wiki.openwrt.org/)
1. [Installing OpenWrt](https://wiki.openwrt.org/doc/howto/generic.flashing)
1. [Buffalo WHR-G300N V2](https://wiki.openwrt.org/toh/buffalo/whr-g300nv2)
1. [Techdata: Buffalo WHR-G300N v2](https://wiki.openwrt.org/toh/hwdata/buffalo/buffalo_whr-g300n_v2)
1. [OpenWrt Downloads](https://downloads.openwrt.org/)
1. [Gargoyle](https://www.gargoyle-router.com/)

## 史上最全面的Buffalo WHR-G300N CH v2 刷OpenWrt教程

Buffalo WHR-G300N CH v2 刷OpenWrt、有两种办法、一种是Windows下刷、一种是在linux下使用tftp刷.

Buffalo WHR-G300N-CH v2的openwrt固件在这个地址下载：

http://downloads.openwrt.org/snapshots/trunk/ar71xx/

openwrt官方对G300N v2的支持时有时无、还没有正式支持

由于硬件一样、我们可以下载使用WHR-G301N或者WHR-HP-G300N的固件

而这两款路由也没有得到openwrt正式的支持

openwrt每次会发布G301N和HP-G300N的openwrt固件、而每次发布没几天、该固件就会被openwrt取消下载

所以http://downloads.openwrt.org/snapshots/trunk/ar71xx/这个链接里偶尔才会有对应的固件下载、

为了提供方便、在这里我提供下载:

squashfs-factory版

squashfs-sysupgrade版

squashfs-tftp版

内核3.2.6

提前说一下、这个路由是刷不死的、不管怎样都可以用linux下tftp刷回

#### Ⅰ.Windows下：

我们需要用到两个工具

1.hfs        （点此下载hfs）

2.Telnet

Windows7默认没有开启telnet功能、在此讲述一下telnet的开启方法:

控制面板-程序-程序和功能-打开或关闭Windows功能;

把telnet服务端和telnet客户端勾选、确定

下载上面提供的sysupgrade版固件

使用hfs挂载、挂载方法：

挂载方法：

①.打开hfs

menu-IP Adress、选择你的路由给你电脑分配的IP地址

（一般为192.168.1.？、图中我的即是192.168.36.2）

把固件包拖到左侧“Virtual File System”下、成为这样：

telnet或者ssh登录路由、输入以下命令：

    cd /tmp 
    wget http://192.168.1.109/openwrt-ar71xx-generic-whr-g301n-squashfs-sysupgrade.bin                    在这里提示一下、①.可把固件名改为“1.bin”再挂载、这里的命令就可以简写了、②.这里的192.168.1.109应改为本机IP、像如图、我就应该改为192.168.36.2、 
    mtd -e linux -r write openwrt-ar71xx-generic-whr-g301n-squashfs-sysupgrade.bin linux

（附固件改名后菜鸟命令：

    cd /tmp 
    wget http://192.168.1.109/1.bin 
    mtd -e linux -r write 1.bin linux

）

等待画面显示失去主机连接后

等待1分钟、待power和router亮起、说明刷机成功了、下面我来讲linux下刷路由教程、刷好后却不能打开配置页面我将在另一篇文章中详细描述

http://zzsjlove.diandian.com/2012/04/whr-g300n-v2-openwrt-luci/

#### Ⅱ.Linux下（以ubuntu为例）：

下载tftp版固件（上文有提供下载）、同样还是建议把固件名改为1.bin把固件放入ubuntu的主文件夹（home）、先把ubuntu联网、怎么联网我就不赘述了

安装tftp

在终端中输入:

    sudo apt-get update 
    sudo apt-get install tftp

在终端中输入

    ifconfig

查看你的网卡哪个是本地网卡、如果是虚拟机用户看清楚哪个是连接虚拟机与主机的网卡、哪个是直接连接路由器的网卡

用网线连接电脑网口与路由LAN口

在终端输入：

```bash
+------------
sudo service networking stop  #树莓派、Ubuntu 9.10用户用这个命令、 
sudo service network-manager stop  #Ubuntu 10.4或以上系统用这个命令、 
sudo rc-service NetworkManager restart   #gentoo
+------------
sudo ifconfig eth0 192.168.11.2    # 必须是这个IP段、即使你已经改了路由的IP、这里你还是必须要配置本地网卡为192.168.11.？
sudo ifconfig enp134s0　192.168.11.2  ＃ｇｅｎｔｏｏ
+------------
sudo ifconfig eth0 netmask 255.255.255.0    #(此步可以省略) 
+------------
sudo arp -s 192.168.11.1  AABBCCDDEE5F        #AABBCCDDEEFF改为你的路由器mac地址（在路由器背面有标签）、可加冒号也可不加、
+------------
```

拔掉路由电源

在终端输入

    tftp 
    tftp> verbose 
    提示Verbose mode on. 
    tftp> binary 
    提示 mode set to octet. 
    tftp> trace 
    提示 Packet tracing on. 
    tftp> rexmt 1 
    tftp> timeout 60 
    tftp> connect 192.168.11.1 
    tftp> put 1.bin

这时立即插上路由器电源、待ubuntu显示正在推送固件、然后推送完成、会等待输入

输入

    quit

退出tftp

输入

    exit

退出终端，等待路由重启完成、亮起power与router、刷机完成，刷机后在浏览器输入 192.168.1.1并不能正常打开、我会在另一篇文章中详细解说

http://zzsjlove.diandian.com/2012/04/whr-g300n-v2-openwrt-luci/

需设置初始密码才可登录web后台：

    telnet  192.168.1.1 

提示输入新密码.

PS：ubuntu下tftp刷路由的方法可以刷回官方固件

PS：openwrt下刷回官方只能用tftp的方法、而openwrt下刷回DD-wrt可以用这个固件：

whr-g300nv2-openwrt-to-dd.bin

用这个固件在op下页面升级到dd，刷到DD后建议reset一次、或者再刷DD的更新版本即可．

－－－－－－－－－－－－－－－－－－－

### ubuntu/gentoo下刷机脚本：

```bash
#!/bin/bash  

echo "方法:
下载tftp版固件,把固件名改为1.bin，把固件放入与该脚本同级文件夹下（如主文件夹home）
用网线连接电脑网口与路由LAN口,拔掉路由电源，运行该脚本。
然后，在终端输入：
-----------------
tftp 
tftp> verbose 
提示Verbose mode on. 
tftp> binary 
提示 mode set to octet. 
tftp> trace 
提示 Packet tracing on. 
tftp> rexmt 1 
tftp> timeout 60 
tftp> connect 192.168.11.1 
tftp> put 1.bin
-----------------
这时立即插上路由器电源、待ubuntu显示正在推送固件、然后推送完成、会等待输入
-----------------
完成后，输入quit 退出tftp，退出终端，等待路由重启完成、亮起power与router、刷机完成，刷机后在浏览器输入 192.168.1.1"
# -----------------

# # ubuntu:

# sudo service networking stop 

# sudo ifconfig eth0 192.168.11.2

# sudo ifconfig eth0 netmask 255.255.255.0

# sudo arp -s 192.168.11.1  106F3F389CC8

# # #ifconfig 

# tftp 192.168.11.1

# -----------------

# gentoo:

sudo rc-service NetworkManager stop 
sudo ifconfig enp134s0 192.168.11.2
sudo ifconfig enp134s0 netmask 255.255.255.0
sudo arp -s 192.168.11.1  106F3F389CC8
# ifconfig 

tnftp 192.168.11.1

```

## OpenWrt sysupgrade 命令行更新固件到最新版

下面我们要使用 sysupgrade 更新固件到trunk最新版。

要注意的是，trunk包含试验的功能，可能不稳定，刷机风险自己承担。

在浏览器里登陆 192.168.1.1（可通过ｗｅｂ或telent界面改成：192.168.1１.1） 进行固件升级是比较简单的。今天我们要尝试的的是命令行刷机升级。命令行的方式更强大。

### 1、SSH登录路由器

在Ubuntu里，按Ctrl+Alt+T打开命令行终端，输入：

    ssh root@192.168.１1.1

输入密码（必须先通过ｗｅｂ界面改密码），登录成功:

```bash
ssh root@192.168.11.1              
root@192.168.11.1's password: 
BusyBox v1.19.4 (2015-01-02 10:48:30 CST) built-in shell (ash)
Enter 'help' for a list of built-in commands.
------------------------------------------------------------------
|            _____                             _                 |
|           |  __ \                           | |                |
|           | |  \/ __ _ _ __ __ _  ___  _   _| | ___            |
|           | | __ / _` | '__/ _` |/ _ \| | | | |/ _ \           |
|           | |_\ \ (_| | | | (_| | (_) | |_| | |  __/           |
|            \____/\__,_|_|  \__, |\___/ \__, |_|\___|           |
|                             __/ |       __/ |                  |
|                            |___/       |___/                   |
|                                                                |
|----------------------------------------------------------------|
| Gargoyle version 1.6.2    | OpenWrt Attitude Adjustment branch |
| Gargoyle revision         | OpenWrt revision r42171            |
| Built January 02, 2015    | Target  ar71xx/custom              |
------------------------------------------------------------------
```

进入OpenWrt /tmp目录

    cd /tmp

检查OpenWrt路由器是否有足够的内存

    df -h

可以看出， /tmp 还有29.5MB可用空间，而升级固件在3MB左右，足够了。

### ２、下载OpenWrt最新trunk版本固件

#####　２．１　方法一：

在Ubuntu里浏览器打开 

    http://downloads.openwrt.org/snapshots/trunk/

TP-LINK WR2543N路由器的芯片类型是ar71xx，就点击 ar71xx 目录进入。要注意，路由器的芯片类型千万不能搞错，不同路由器很可能是不同的。

 按Ctrl+F查找自己的路由器型号。比如我输入的是 wr2543, 有两个固件，升级用的是 sysupgrade.bin文件。右键点击该链接，复制下载地址。

回到Ubuntu命令行终端， 下载固件到 /tmp 目录。TP-LINK wr2543路由器是这样的:

     root@OpenWrt:/tmp# wget http://downloads.openwrt.org/snapshots/trunk/ar71xx/openwrt-ar71xx-generic-tl-wr2543-v1-squashfs-sysupgrade.bin

固件名称较长，可改为如sysupgrade.bin 、1.bin等名称。

##### ２．２　方法二：

无网络情况下：须先将固件复制sysupgrade.bin到电脑

Buffalo WHR-G300N CH v2无USB接口，然后在ysupgrade.bin文件的同级目录下运行simpleHTTPServer，脚本如下：

    #!/bin/bash
    ifconfig　　　　　　　　　　　　　　　　　　　
    firefox http://192.168.11.120:8000/　　　＃＃打开firefox查看文件服务器文件
    python -m SimpleHTTPServer
    read -n1 -p "Press any key to continue..."

然后，ＳＳＨ进入路由器，下载固件sysupgrade.bin	：

    root@OpenWrt:/tmp# wget http://192.168.11.120:8000/sysupgrade.bin	
    ＃其中，192.168.11.120为电脑的ＩＰ，可通过ifconfig命令查看。

md5校验，确保下载的固件完整（可略）:

    root@OpenWrt:/tmp# wget http://downloads.openwrt.org/snapshots/trunk/ar71xx/md5sums  
    root@OpenWrt:/tmp# md5sum -c md5sums 2> /dev/null | grep OK  
    openwrt-ar71xx-generic-tl-wr2543-v1-squashfs-sysupgrade.bin: OK        

输出结尾是OK，说明固件是完整的。

### ３、升级OpenWrt固件

OpenWrt sysupgrade命令升级OpenWrt固件

    root@OpenWrt:/tmp# sysupgrade -v sysupgrade.bin 
    ... 
    Upgrade completed
    Rebooting system...

过约2分钟，等路由器重启成功，如果没有意外，会发现有线和无线上网都正常。但浏览器192.168.1１.1无法登陆，因为snapshots版本固件是不带LuCI网页管理界面的。没有也好，可以节省路由器的存储空间，也可以学习一下命令行管理OpenWrt路由器。
