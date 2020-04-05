% OpenWrt完美教程
### 从零开始学习OpenWrt完美教程

从零开始学习OpenWrt完美教程

现在有越来越多的Maker开始折腾OpenWrt，但作为一个Maker新手来讲，在网上还是很难找到一份系统的入门级资料。查找资料很辛苦，而且OpenWrt的门槛相对较高，希望这篇文章所提供的从零开始学OpenWrt编译

OpenWRT

Cisco/Linksys在2003年发布了WRT54G这款无线路由器，同年有人发现它的IOS是基于Linux的，然而Linux是基于GPL许可证发布的，按照该许可证Cisco应该把WRT54G 的IOS的源代码公开。2003年3月， Cisco迫于公众压力公开了WRT54G的源代码。此后就有了一些基于Cisco源码的第三方路由器固件，OpenWrt就是其中的一个。

OpenWrt的特点：

    可扩展性好，可以在线安装您所需要的功能，目前有1000多个功能包可选；
    是一台完整的Linux工作站，文件系统可读可写，便于开发者学习和实践；

现在有越来越多的Maker开始折腾OpenWrt，但作为一个Maker新手来讲，在网上还是很难找到一份系统的入门级资料。查找资料很辛苦，而且OpenWrt的门槛相对较高，希望这篇文章所提供的从零开始学OpenWrt编译 + 刷机 + 使用教程能降低新手们的入门难度，当然，编译过程非必须，一般的路由都可找到可用的稳定固件直接刷机。

#### 第一部分：搭建编译环境

1、安装Ubuntu（编译需要Linux环境），到其官网下载，版本根据自己所需选择即可。可以选择安装到虚拟机或者物理机，图形化安装而且是中文版，连安装都搞不定的，可以关闭本页面了；

2、切记不要改动软件源，同时按住Ctrl + Alt + T，调出终端；

3、逐条输入下列命令（及时验证是否安装成功）：

    sudo apt-get install g++
    sudo apt-get install libncurses5-dev
    sudo apt-get install zlib1g-dev
    sudo apt-get install bison
    sudo apt-get install flex
    sudo apt-get install unzip
    sudo apt-get install autoconf
    sudo apt-get install gawk
    sudo apt-get install make
    sudo apt-get install gettext
    sudo apt-get install gcc
    sudo apt-get install binutils
    sudo apt-get install patch
    sudo apt-get install bzip2
    sudo apt-get install libz-dev
    sudo apt-get install asciidoc
    sudo apt-get install subversion
    sudo apt-get install sphinxsearch
    sudo apt-get install libtool
    sudo apt-get install sphinx-common

至此编译环境搭建完成。

#### 第二部分：下载OpenWrt源码并编译

OpenWrt源码分两种，一种是最新但不是最稳定的Trunk开发版，一种是最稳定的Backfire版，建议下载官方源码。下载前先在本地创建文件夹：

    mkdir openwrt
    sudo chmod 777 openwrt
    cd openwrt

选择你想要的版本然后执行下载命令，下载结束会显示版本号：

Trunk版下载命令：

    svn co svn://svn.openwrt.org/openwrt/trunk/

Backfire版下载命令：

    svn co svn://svn.openwrt.org/openwrt/branches/backfire/

添加软件扩展包，将feeds.conf.default修改为feeds.conf：

    cp feeds.conf.default feeds.conf

更新扩展，安装扩展：

    ./scripts/feeds update -a
    ./scripts/feeds install -a

注：如果不是刚下载的源码，为保持代码为最新状态，应定期运行svn update命令更新源码。

测试编译环境：

    make defconfig

到这里就可以开始编译自己的固件了。进入定制界面：

    make menuconfig

如果一切正常，会出现一个配置菜单，可以选择要编译的固件平台（芯片类型）、型号，还能选择固件中要添加的功能和组件，配置好后保存并退出菜单即可。

    openwrt-make

如果你想修改源码，应该在此步进行，如支持大容量Flash之类的修改，自己上网查到修改什么文件什么地方后，就在ubuntu图形界面上进去找到文件，双击打开文本编辑器修改保存。

开始编译：

    make

或者

    make  V=99

或者

make -j V=99

    make是编译命令，V=99表示输出debug信息，V一定要大写，如果要让CPU全速编译，就加上 -j 参数，第一次编译最好不带-j参数。

编译过程保持联网（会从网上下载一些源码包），所以断网可能造成编译中断，编译所需时间与电脑CPU及网络环境有很大关系，第一次编译时间较久，快则半小时长则2、3个小时，之后的编译所需时间较短。编译完成后会在源码文件目录出现bin文件夹（如trunk/bin/XXXX），如果你手里的路由是原版固件需要刷OpenWrt需要选用XXX-factory.bin固件，如果路由已经刷了OpenWrt，选用升级固件XXXX-sysupgrade.bin升级用的，在升级界面升级即可。进到文件夹找到你需要的固件传出（通过邮箱、网盘、U盘等），开始刷机吧。

#### 第三部分：将OpenWrt刷入路由器

要在路由器上使用OpenWrt，首先要将路由器固件刷新为OpenWrt，即相当于OpenWrt 系统的安装，不同型号的路由器的安装方法可能也会不一样，但一般常用的有三种方法：

    Web上传固件更新
    PFTP上传固件更新
    编程器写入固件

具体型号的路由器适用于哪种或哪几种方法，需自行尝试。

#### 第四部分：开始使用OpenWrt

要对OpenWrt进行配置，一般有两条途径：

    SSH登录通过命令行控制
    Web登录通过Web界面设置

首次安装OpenWrt后，需要设置密码才可以使用SSH登录，方法是使用telnet登录或者Web登录设置密码。在Windows下面telnet和SSH登录可以使用Putty，在Linux或Mac下可分别使用如下命令：

    ssh –l root 192.168.1.1 //Linux
    ssh root@192.168.1.1 //Mac
    openwrt-ssh

一般指令与常见Linux发行版相同，但是OpenWrt使用自己的包管理器：opkg，使用“opkg –help”查看帮助信息。以下是一些常用操作命令：

    opkg update //更新软件包列表
    opkg install  //在线安装软件包
    opkg remove  //移除软件包

登录Web管理界面，前提是该OpenWrt系统中要安装了Web界面，一般是Luci，登录方式与普通路由器无异，打开浏览器，输入路由器IP即可进入登录界面，OpenWrt的默认IP是192.168.1.1。

    openwrt-web

到此，OpenWrt的大门已为你敞开。接下来，开始尝试利用OpenWrt实现更多智能应用吧，比如单号多拨榨取运营商带宽、绑定域名远程控制、挂载大容量硬盘、搭建BT下载机、搭建网络摄像头、Samba/DLNA家庭NAS共享、私有云同步、FTP、个人网站/服务器… 
