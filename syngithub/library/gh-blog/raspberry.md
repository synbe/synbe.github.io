% 树莓派
##     raspbian在Linux下烧录系统

下载完成后，我们打开终端，找到下载的文件。使用“unzip 2016-xx-xx-xxxxx.zip ”(替换为您自己的文件名)命令解压文件。然后得到2016-xx-xx-xxxxx.img文件，此文件就是我们要的镜像。

得到镜像文件后，我们要将此镜像文件写入事先准备的TF卡内。

将TF卡放入读卡器，然后接入电脑。使用"sudo fdisk -l"命令查看此设备的名称，在我的电脑上是/dev/sdc（因为我的电脑已经有两个硬盘了）。

写镜像到sd卡， if= 是你下载的镜像的文件（默认下载是zip文件，需要先解压出来）地址， of= 是你要写入的地址，就是一开始让你记录的sd卡的设备地址。一定要明确，是sd卡整个的地址，不是某个分区的地址。

    dd bs=4M if=2017-04-10-raspbian-jessie.img  of=/dev/sdc

块大小设置成 4M 一般没有问题，如果失败了，设置1M试试，当然会更慢。 

回车，执行命令等它执行完毕。这个步骤时间比较长，要耐心等待。

最后不要忘了运行 sync ，确保cache中的数据都被写到了sd卡上。

在使用dd命令时，不要中断，一定要等到如上图所显示的写入成功再拔出读卡器。

移除sd卡，插到pi.

## 1.  树莓派没有声音的解决方案

    pi@raspberrypi:~ $ sudo amixer cset numid=3 1

    pi@raspberrypi:~ $ sudo amixer cset numid=3 2

Raspberry Pi(树莓派)声音输出可以设置为自动，耳机输出，从HDMI输出三种，默认为自动
values取不同的值分别代表：
0=auto(自动), 1=headphones(耳机), 2=hdmi

        pi@raspberrypi:~ $ sudo amixer cset numid=3 1
        numid=3,iface=MIXER,name=PCM Playback Route
        ; type=INTEGER,access=rw------,values=1,min=0,max=2,step=0
        : values=1
        pi@raspberrypi:~ $

## 2. 树莓派 - 修改pi账号密码,开启root账号

1、修改PI账号的密码

view plain copy print?在CODE上查看代码片派生到我的代码片

    password pi 

2、开启root账号

树莓派使用的linux是debian系统，所以树莓派启用root和debian是相同的。

debian里root账户默认没有密码，但账户锁定。'

当需要root权限时，由默认账户经由sudo执行，Raspberry pi 系统中的Raspbian

默认用户是pi 密码为`raspberry`

重新开启root账号，可由pi用户登录后，在命令行下执行

view plain copy print?在CODE上查看代码片派生到我的

    sudo passwd root 

执行此命令后系统会提示输入两遍的root密码，输入你想设的密码即可，然后在执行 

 view plain copy print?在CODE上查看代码片派生到我的代码片

    sudo passwd --unlock root 

这样就可以解锁root账户了。

## 3. 手动来安装中文字体。

树莓派默认是采用英文字库的，而且系统里没有预装中文字库，所以即使你在locale中改成中文，也不会显示中文，只会显示一堆方块。因此需要我们手动来安装中文字体。

好在有一个中文字体是免费开源使用的。ssh中输入以下命令：

    sudo apt-get install ttf-wqy-zenhei

安装过程中如果碰到(Y/n)，都选择y
中文字库安装完成之后，还需要安装一个中文输入法。输入如下命令

    sudo apt-get install scim-pinyin
一样的安装过程，安装完毕后输入

    sudo raspi-config
然后选择change_locale，在Default locale for the system environment:中选择zh_CN.UTF-8,配置完成之后，输入命令

    sudo reboot
重启完成好就可以在VNC连接上去后使用中文显示和中文输入法了，切换中文输入法一样也是ctrl+space。

## LCD和HDMI相互切换

使用上面两种方法在正常使用LCD的情况下，外接HDMI是没有显示的，如需启用HDMI输出，需执行以下命令，树莓派会自动重启。再等待约30秒，HDMI显示屏开始显示。

    cd LCD-show/
    ./LCD-hdmi
如需切换回LCD显示方式，则需执行以下命令：

    cd LCD-show/
    ./LCD35-show

## 树莓派上安装ArchLinux

树莓派有2种含义：那块集成电路板（硬件），还有一种就是“树莓派”操作系统（软件，基于Linux内核）。

现在居于Linux 内核的系统很多，五花八门，各有侧重。

我挑了一种还算比较流行，精简的Linux： ArchLinux ARM版本

下载地址：http://archlinuxarm.org/os/ArchLinuxARM-rpi-2-latest.tar.gz

安装说明：http://archlinuxarm.org/platforms/armv7/broadcom/raspberry-pi-2

我把这2个打包放在： http://yunpan.cn/cVNnEqCA6EFft  访问密码 83d8

一般的树莓派系统都提供的是一个img文件（系统镜像文件），然后用Win32DiskImager软件烧录到TF卡上，再插到树莓派上，即可上电运行！

但是这个ArchLinuxARM-rpi-2-latest.tar.gz不是镜像文件，而是一个目录树的压缩包，

**安装说明是在Linux环境下进行的（TF卡的制作步骤）：**

将TF卡放入读卡器，然后接入电脑。使用"sudo fdisk -l"命令查看此设备的名称:比如sdc

SD Card Creation

Replace sdX in the following instructions with the device name for the SD card as it appears on your computer.

Start fdisk to partition the SD card:

    fdisk /dev/sdX

At the fdisk prompt, delete old partitions and create a new one:

Type o. This will clear out any partitions on the drive.

Type p to list partitions. There should be no partitions left.

Type n, then p for primary, 1 for the first partition on the drive, press ENTER to accept the default first sector, then type +100M for the last sector.

Type t, then c to set the first partition to type W95 FAT32 (LBA).

Type n, then p for primary, 2 for the second partition on the drive, and then press ENTER twice to accept the default first and last sector.

Write the partition table and exit by typing w.

Create and mount the FAT filesystem:

    sudo mkfs.vfat /dev/sdc1 
    mkdir boot 
     sudo mount /dev/sdc1 boot

Create and mount the ext4 filesystem:

    sudo mkfs.ext4 /dev/sdc2
    mkdir root 
    sudo mount /dev/sdc2 root

Download and extract the root filesystem (as root, not via sudo):

    wget http://archlinuxarm.org/os/ArchLinuxARM-rpi-2-latest.tar.gz 
    bsdtar -xpf ArchLinuxARM-rpi-2-latest.tar.gz -C root 
    sync

Move boot files to the first partition:  sudo mount /dev/sdc2 root

    mv root/boot/* boot

Unmount the two partitions:

    umount boot root

Insert the SD card into the Raspberry Pi, connect ethernet, and apply 5V power.

Use the serial console or SSH to the IP address given to the board by your router. The default root password is 'root'.

装完以后的系统的用户名、密码都是：root

##安装错误

##速度与激情

电影名：速度与激情8
观看链接：http://18x8.cn/x/8/cynew878/

电影名：速度与激情7
观看链接：http://18x8.cn/x/8/m%7CgqToZxH1R0r2SB/

电影名：速度与激情7 国语
观看链接：http://18x8.cn/x/8/m%7ChafiZhH2Q0X3SR/

电影名：速度与激情1
观看链接：http://18x8.cn/x/8/m%7CgqniZkj6Qnr3SB/

电影名：速度与激情6
观看链接：http://18x8.cn/x/8/m%7CgariY0f7R0X3Sh/

电影名：速度与激情5
观看链接：http://18x8.cn/x/8/m%7CfaflYUX6SHr1Tx/

电影名：速度与激情2
观看链接：http://18x8.cn/x/8/m%7CfaPqZkT5SHbAUB/

电影名：速度与激情4
观看链接：http://18x8.cn/x/8/m%7CgqLnZUT6Qnr1UB/

电影名：速度与激情3
观看链接：http://18x8.cn/x/8/m%7Cg6XnYUT6Qnr0Th/

## 树莓派上的软件安装和卸载命令汇总

###基础命令

        安装软件 apt-get install softname1 softname2 softname3……
        卸载软件 apt-get remove softname1 softname2 softname3……
        卸载并清除配置 apt-get remove –purge softname1
        更新软件信息数据库 apt-get update
        进行系统升级 apt-get upgrade
        搜索软件包 apt-cache search softname1 softname2 softname3……

如果使用 apt-get 遇到速度慢或者源不存在等错误，可能需要更换源，请参考此处。

        安装deb软件包 dpkg -i xxx.deb
        删除软件包 dpkg -r xxx.deb
        连同配置文件一起删除 dpkg -r –purge xxx.deb
        查看软件包信息 dpkg -info xxx.deb
        查看文件拷贝详情 dpkg -L xxx.deb
        查看系统中已安装软件包信息 dpkg -l
        重新配置软件包 dpkg-reconfigure xxx

清除所有已删除包的残馀配置文件

        dpkg -l |grep ^rc|awk '{print $2}' |sudo xargs dpkg -P
如果报如下错误，证明你的系统中没有残留配置文件了，无须担心。

        dpkg: –purge needs at least one package name argument

dpkg安裝的可以用apt卸載，反之亦可。

### aptitude 命令

aptitude 与 apt-get 一样，是 Debian 及其衍生系统中功能极其强大的包管理工具。与 apt-get 不同的是，aptitude 在处理依赖问题上更佳一些。举例来说，aptitude 在删除一个包时，会同时删除本身所依赖的包。这样，系统中不会残留无用的包，整个系统更为干净。以下是笔者总结的一些常用 aptitude 命令，仅供参考。

        aptitude update 更新可用的包列表
        aptitude upgrade 升级可用的包
        aptitude dist-upgrade 将系统升级到新的发行版
        aptitude install pkgname 安装包
        aptitude remove pkgname 删除包
        aptitude purge pkgname 删除包及其配置文件
        aptitude search string 搜索包
        aptitude show pkgname 显示包的详细信息
        aptitude clean 删除下载的包文件
        aptitude autoclean 仅删除过期的包文件

当然，你也可以在文本界面模式中使用 aptitude。

**常用apt命令列表**

        apt-cache search # ------(package 搜索包)
        apt-cache show #------(package 获取包的相关信息，如说明、大小、版本等)
        sudo apt-get install # ------(package 安装包)
        sudo apt-get install # -----(package - - reinstall 重新安装包)
        sudo apt-get -f install # -----(强制安装?#"-f = --fix-missing"当是修复安装吧...)
        sudo apt-get remove #-----(package 删除包)
        sudo apt-get remove - - purge # ------(package 删除包，包括删除配置文件等)
        sudo apt-get autoremove --purge # ----(package 删除包及其依赖的软件包+配置文件等（只对6.10有效，强烈推荐）)
        sudo apt-get update #------更新源
        sudo apt-get upgrade #------更新已安装的包
        sudo apt-get dist-upgrade # ---------升级系统
        sudo apt-get dselect-upgrade #------使用 dselect 升级
        apt-cache depends #-------(package 了解使用依赖)
        apt-cache rdepends # ------(package 了解某个具体的依赖?#当是查看该包被哪些包依赖吧...)
        sudo apt-get build-dep # ------(package 安装相关的编译环境)
        apt-get source #------(package 下载该包的源代码)
        sudo apt-get clean && sudo apt-get autoclean # --------清理下载文件的存档 && 只清理过时的包
        sudo apt-get check #-------检查是否有损坏的依赖

## 用树莓派搭建Git私有服务器

    sudo adduser --system --shell /bin/bash --gecos 'git version control by pi' --group --home /home/gitrep git

### passwd git

        raspberry

## 在树莓派安装ftp服务器

vsftpd是开源的轻量级的常用ftp服务器．

1,安装vsftpd服务器 (约400KB)

    sudo apt-get install vsftpd

2,启动ftp服务

    sudo service vsftpd start

3,编辑vsftdp的配置文件

    sudo nano /etc/vsftpd.conf

找到以下行，定义一下

    anonymous_enable=NO  

表示：不允许匿名访问

    local_enable=YES  

设定本地用户可以访问。

    write_enable=YES

设定可以进行写操作

    local_umask=022

设定上传后文件的权限掩码。

存盘退出

4, 重启vsftpd服务

    sudo service vsftpd restart

5, 测试一下, OK

通过ftp连接树莓派系统，
以用户名pi登录，密码是raspberry
ftp的根目录是/home/pi，即pi用户的HOME目录
可上传或下载文件了

## linux 下 apache启动、停止、重启命令

一、Start Apache 2 Server /启动apache服务

	sudo /etc/init.d/apache2 start

二、 Restart Apache 2 Server /重启apache服务

	sudo /etc/init.d/apache2 restart

三、Stop Apache 2 Server /停止apache服务

	sudo /etc/init.d/apache2 stop

## 用树莓派搭建Git私有服务器

话说当年linux内核开发者林纳斯·托瓦兹（Linus Torvalds）为了更好的管理Linux内核开发创下git以来，时至今日，当下最流行的『版本管理系统』已非git莫属了！ 笔者私下认为，git相比其他的版本管理系统（csv, svn等）来，最大的方便莫过于分支（branch）的操作十分便捷，但项目开发分支如何管理，萝卜白菜各有所爱，见仁见智。笔者因工作需要，经常要参与国际化团队的协作开发，git乃是必不可缺之利器之一。

最近我利用树莓派为我所有的Git仓库创建了一个Git私有服务器。我花费了一些时间来使每件事情正确工作，但现在它已经能跑起来了。

安装Git

首先你需要在树莓派上安装Git.

    sudo apt-get install wget git-core

这将会安装Git服务器和必要的客户端软件。

安装SSH

如果你还没有安装SSH，通过以下命令安装它：

    sudo apt-get install ssh
通过以下命令启动它：

    sudo /etc/init.d/ssh start

现在ssh已经运行起来了，但是一旦你重启树莓派，你还需要重新执行一遍上面命令。你可以通过执行一次下面的命令来解决这个问题：

    sudo update-rc.d ssh defaults

当你重启树莓派，SSH应该能够自动启动了。你可以看看能不能通过SSH连接到树莓派，在你的Windows机器上使用Putty(Mac用户需要寻找替代的SSH客户端)。

在HostName文本框里输入树莓派的IP地址。通过以下命令找到你的树莓派IP:

    /sbin/ifconfig
找到inet addr:后面的就是IP。

改变主机名

这步不是必须的，但是我强烈推荐如果你正在，计划使用多台树莓派设备。

    sudo leafpad /etc/hostname

输入你想要的主机名，然后保存文件。我的主机名是”gitpi”。
接着，输入下面的命令：

    sudo leafpad /etc/hosts

替换所有”raspberrypi”为你上一步输入的新主机名。然后，重启你的树莓派。

添加一个”Git”用户和组

接着我们来创建一个”Git”用户和用户组。注意/home/git是这个例子里我使用的文件夹。如果你想使用别的路径，替换下面命令里的”/home/git”。

    adduser --system --shell /bin/bash --gecos 'git version control by pi' --group --home /home/git git

接着是更改密码：

    passwd git

你的”git”用户现在有了一个新密码。现在尝试切换用户，你将会看到现在的终端提示用户名和主机为”git@gitpi”。你可以通过下面的命令切换用户：

    su git

增加一个空的Git仓库(Git Repository)

我们现在来增加一个空的Git仓库.
首先更改目录到你存储git的路径下。

    cd /home/git

为你的仓库创建一个文件夹，并移动进去，然后初始化并清空仓库。
注意我现在使用的是”git”用户。这个用户具有/home/git目录的控制权。

    mkdir test.git
    cd test.git
    git --bare init

Push你的代码到Pi上

最终，我们会把代码push到树莓派上。首先，更改路径到你之前初始化的git仓库(或初始化一个新的)。

加入一个新的远程主机(*你的IP地址没有中括号)

1
git remote add pi git@[your IP]:/home/git/test.git
现在你要做的就是add你的代码，commit然后push。

    git add .
    git commit -am "Initial"
    git push pi master

如果你得到了一个类似这样的消息”authenticity of host …”只需要输入”yes”然后继续就可以了。
理想情况下，如果一切正常，你的Git仓库已经搭建在你的树莓派上了。

如果你想要测试一下，试着clone你的仓库到你的Windows机器上。首先更改路径到你希望存储clone的地方(一个空文件夹)，然后通过命令行(或git bash)，运行：

    git clone git@[your IP]:/home/git/test.git

## 基于 Samba 实现 NAS 系统

摆弄了几天Raspberry Pi，在搞定了无线网络、FTP服务之后，打算更进一步，通过Samba实现NAS系统与PC共享文件。
需要安装的软件：

    sudo apt-get install samba samba-common-bin
    sudo apt-get install netatalk （可选，用于支持AFP）
    sudo apt-get install avahi-daemon（可选，用于支持网内的计算机自动发现）

接下来就是配置了：

[Samba 配置] 

/etc/samba/smb.conf 文件尾部增加/etc/samba/smb.conf 

    [public]
    comment = Public Storage
    path = /home/pi
    read only = no  #任何人都具有了访问修改的权限

因为是公共文件夹，所以给了所有用户全部权限，可以自定义

    create mask = 0777   #新创建文件的默认属性
    directory mask = 0777   #新创建文件夹的默认属性
    guest ok = yes   #默认的访问用户名为guest
    browseable = yes

然后就可以 **smbd restart **了。

这时候已经可以通过网上邻居看到共享文件目录，只是进不去。
提示需要输入口令，尝试用本地帐户也无法进入。

查了资料原来因为 Samba 使用了自己一套用户帐号资料库。要登录的话还需要向该库添加帐号信息，方法有两种：

1.直接用 mksmbpasswd.sh 将系统用户转换成 Samba 用户：

    cat /etc/passwd | mksmbpasswd.sh >/etc/samba/smbpasswd

2.用 smbpasswd 命令直接设置，需要首先要添加系统用户然后用 smbpasswd -a 用户名 添加 Samba 用户；smbpasswd -e 用户名 激活用户。

[Netatalk 配置] 

    /etc/netatalk/AppleVolumes.default 方法参考资料3。

最后就是挂载USB移动硬盘了：

    mount /dev/sda1 /home/shares/public/
有时候卸载USB移动硬盘的时候会提示设备忙(Device is busy)，只需要加上 –l 参数就行了：

## 在树莓派上安装firefox浏览器

在树莓派上Firefox浏览器叫作iceweasel，所以可以使用下面的命令在树莓派上安装Firefox

    sudo apt-get install iceweasel

## 树莓派安装xfce 桌面系统

lxde桌面用着很不爽，直接换xfce4

首先卸载lxde

    sudo apt-get autoremove --purge lxde lxde-common lxde-core lxde-icon-theme galculator leafpad lxappearance lxappearance-obconf lxrandr

安装xfce4

    sudo apt-get install xfce4 xfce4-goodies

查看默认的窗口管理器

    sudo update-alternatives --display x-window-manager

    x-window-manager - 自动模式 链接目前指向 /usr/bin/openbox
    /usr/bin/openbox - 优先级 90  次要 x-window-manager.1.gz：/usr/share/man/man1/openbox.1.gz
    /usr/bin/xfwm4 - 优先级 60  次要 x-window-manager.1.gz：/usr/share/man/man1/xfwm4.1.gz
    目前“最佳”的版本为 /usr/bin/openbox。

更改窗口管理器为xfwm4

    sudo update-alternatives --config x-window-manager

有 2 个候选项可用于替换 x-window-manager (提供 /usr/bin/x-window-manager)。

      选择       路径            优先级  状态
    ------------------------------------------------------------
    * 0            /usr/bin/openbox   90        自动模式
      1            /usr/bin/openbox   90        手动模式
      2            /usr/bin/xfwm4     60        手动模式

要维持当前值[*]请按回车键，或者键入选择的编号：2 #这里选择2 xfce的xfwm4

    update-alternatives: 使用 /usr/bin/xfwm4 来在手动模式中提供 /usr/bin/x-window-manager (x-window-manager)

vnc远程桌面改成xfce4， 修改当前vnc用户家目录的vnc文件

    vim ~/.vnc/xstartup

如下:

    #!/bin/sh
    xrdb $HOME/.Xresources
    xsetroot -solid grey
    #x-terminal-emulator -geometry 80x24+10+10 -ls -title "$VNCDESKTOP Desktop" &
    #x-window-manager &
    # Fix to make GNOME work
    #export XKL_XMODMAP_DISABLE=1
    #/etc/X11/Xsession
    #以下是启动xfce4桌面
    unset SESSION_MANAGER
    startxfce4 &

后面的自己配置的， 原来lxde的东西可以再删一些

下面介绍下怎么安装slim

    sudo apt-get install slim

然后打y，安装过程中会出现一个蓝底窗口，先回车，然后键盘按方向下，选择slim，回车

重启后，按f1选择startxfce4

## 树莓派设置键盘

    sudo raspi-config

%树莓派

> 不要使用没有电源供电的HDMI转VGA线！

## LCD 3.5驱动：

把树莓派驱动`3.5inch RPi LCD (A)` ，复制到/boot目录下， 执行以下操作：

	tar xzvf /boot/LCD-show-*.tar.gz 
	cd LCD-show/
	chmod +x LCD35-show
	./LCD35-show

LCD和HDMI相互切换

使用上面两种方法在正常使用LCD的情况下，外接HDMI是没有显示的，如需启用HDMI输出，需执行以下命令，树莓派会自动重启。再等待约30秒，HDMI显示屏开始显示。

	cd LCD-show/
	./LCD-hdmi
如需切换回LCD显示方式，则需执行以下命令：

	cd LCD-show/
	./LCD35-show

## 显示管理器（Display Manager）

* **slim**：SLiM 是一个独立的图形化X11登录管理器.它目标在于提供一个轻型、简洁但是可完全配置主题和文件的登录窗口管理器。可以替代GDM。它原本搭载在LXDE/openbox桌面环境上。
* **lightdm**：LightDM（Light Display Manager）是一个全新的轻量级 Linux 桌面显示管理器，而传统的 Ubuntu 是使用 GNOME 桌面标准的 GDM。LightDM 是一个跨桌面显示管理器，其目的是成为 X org 的 X Server 的标准显示管理器。是2010 年开始的新项目，且被设计为轻量、小巧、快速。相较于 GDM-GTK， KDM-Qt，LightDM 实际上与界面无关，它仅支持本地图形界面获得最好兼容性
* **kdm**
* **gdm**

几个设置文件：

	/etc/inittab
	/etc/init/slim.conf
	/etc/lightdm/lightdm.conf
	~/.xinitrc

## start lightdm

Enter console mode by press Ctrl-Alt-F3 (F2~F8 is also good), and login. Do NOT try to change display manager in GUI, as the behavior is unpredictable.

    sudo systemctl disable gdm
    sudo systemctl enable lightdm
    Stop gdm with sudo systemctl stop gdm
    Start lightdm with sudo systemctl start lightdm

## 中文支持

树莓派默认是采用英文字库的，而且系统里没有预装中文字库，所以即使你在locale中改成中文，也不会显示中文，只会显示一堆方块。因此需要我们手动来安装中文字体。

好在有一个中文字体是免费开源使用的。ssh中输入以下命令：

	sudo apt-get install ttf-wqy-zenhei

安装过程中如果碰到(Y/n)，都选择y
中文字库安装完成之后，还需要安装一个中文输入法。输入如下命令

	sudo apt-get install scim-pinyin

一样的安装过程，安装完毕后输入

	sudo raspi-config

然后选择change_locale，在Default locale for the system environment:中选择（空格键选择）zh_CN.UTF-8,配置完成之后，输入命令重启树莓派reboot

重启完成好就可以在VNC连接上去后使用中文显示和中文输入法了，切换中文输入法一样也是ctrl+space。

## startx

安装有图形界面的情况下，启动linux在终端下输入:
startx   即可进入X11的图形操作界面。
如果希望每次都自动进入xwindos。。 修改inittab文件。 vi /etc/inittab 找到id:3:initdefault:这行 按i进入编辑模式，将3改为5。 按esc退出编辑。 输入 ：qw ---输入包括“：”   如果希望每次都自动进入多用户模式

改为:

	id:3:initdefault:   

有下几种模式:

	#   0 - halt (Do NOT set initdefault to this)
	#   1 - Single user mode   //单用户模式
	#   2 - Multiuser, without NFS (The same as 3, if you do not have networking) //多用户模式,没有网络文件系统
	#   3 - Full multiuser mode /完全多用户模式
	#   4 - unused
	#   5 - X11        //窗口模式
	#   6 - reboot (Do NOT set initdefault to this)   

## windows下 通过SSH使用树莓派 

1. 打开树莓派，设置开启ssh 和 vnc。

2. 在window下载安装putty后，打开，只需输入树莓派的IP地址，默认端口号22，默认选择SSH,点击Open

3. 字符界面输入用户名和密码（一般用户名为Pi，密码raspberry），至此在Windows的PC端通过SSH连接到了树莓派。

## windows下 用VNC图形界面远程控制树莓派

1. 打开树莓派，设置开启ssh 和 vnc：

		sudo raspi-config

2. 树莓派安装tightvncserver

		sudo apt-get install tightvncserver

   	安装完成后，运行tightvncserver,提示输入密码.

		tightvncserver

  	 输入两个密码，一个控制桌面，一个view only,我一般都设置成一样，比如******。然后就会在当下目录生成一个.vnc的隐藏目录。ps.如果想重置密码，只需rm  .vnc -r 然后再次输入tightvncserver即可。

   	设置完密码之后，树莓派需要运行vnc服务：

		tightvncserver

3. windows端：

   	打开http://www.tightvnc.com/download.php下载windows需要安装的VNC-Viewer 解压之后一路next安装.

   	运行填写Remote Host:`192.168.11.7:1`（使用:ifconfig命令）点击connect，输入之前设置好的vcn密码，点击ok。

4. **注意事项**

   * 一定要在PC端vnc-viewer运行之前，在树莓派用tightvncserver启动服务。否则提示远端计算机积极拒绝
   * PC端vnc-viewer软件填写ip地址比如`192.168.1.1:1`后面的英文冒号和1一定不要忘记！
   * 键盘同时按组合键`Ctrl+Alt+Shift+F`即可退出全屏.

5. 设置开机自动启动

设置开机启动，需要在/etc/init.d/中创建一个文件。例如tightvncserver（建议养成启动脚本的名称和程序名一致的习惯）：

	sudo nano /etc/init.d/tightvncserver

内容如下（putty窗口中按右键=粘贴）：

	#!/bin/sh
	### BEGIN INIT INFO
	# Provides: tightvncserver
	# Required-Start: $local_fs
	# Required-Stop: $local_fs
	# Default-Start: 2 3 4 5
	# Default-Stop: 0 1 6
	# Short-Description: Start/stop tightvncserver
	### END INIT INFO

	# More details see:
	# http://www.penguintutor.com/linux/tightvnc

	### Customize this entry
	# Set the USER variable to the name of the user to start tightvncserver under
	export USER='pi'
	### End customization required

	eval cd ~$USER

	case "$1" in
	start)
	# 启动命令行。此处自定义分辨率、控制台号码或其它参数。
	su $USER -c '/usr/bin/tightvncserver -depth 16 -geometry 800x600 :1'
	echo "Starting TightVNC server for $USER "
	;;
	stop)
	# 终止命令行。此处控制台号码与启动一致。
	su $USER -c '/usr/bin/tightvncserver -kill :1'
	echo "Tightvncserver stopped"
	;;
	*)
	echo "Usage: /etc/init.d/tightvncserver {start|stop}"
	exit 1
	;;
	esac
	exit 0

注：少数玩家默认用户不是pi的请自行更改USER变量

按Ctrl+X，回答Y（存盘）退出nano编辑器。

然后给tightvncserver文件加执行权限，并更新开机启动列表:

	sudo chmod 755 /etc/init.d/tightvncserver sudo update-rc.d tightvncserver defaults

## realVNC、tightVNC、ultraVNC

VNC由Olivetti & Oracle研究室所開發，此研究室在1999年併入美國電話電報公司（AT&T）。AT&T於2002年中止了此研究室的運作，並把VNC以GPL釋出。

由於VNC以GPL授權，衍生出了幾個VNC軟體：

RealVNC：由VNC團隊部份成員開發，分為全功能商業版及免費版。 

TightVNC：強調節省頻寬使用。 

UltraVNC：加入了TightVNC的部份程式及加強效能的圖型映射驅動程式，並結合Active Directory及NTLM的帳號密碼認證，但僅有Windows版本。 

Vine Viewer：MacOSX的VNC用戶端。 

這些軟體各有所長，例如UltraVNC支援檔案傳輸以及全螢幕模式。而這些軟體間大多遵循基本的VNC協定，因此大多可互通使用。

		http://www.realvnc.com/   REALVNC

		http://www.tightvnc.com/   TIGHTVNC

		http://ultravnc.com/        ULTRAVNC

## VNC Comparison and Review: TightVNC Vs UltraVNC Vs RealVNC

> milly	9:51 pm on December 1, 2009 | Answers: 1     

Virtual Network Computing (VNC) requires a client (viewer) to connect to the remote computer. There are mainly three popular candidates for clients: RealVNC, TightVNC, and UltraVNC. We’ll do a simple comparison here and choose the best one.

RealVNC

* The original developers. Out in the market the longest.
* The free version lacks a lot of features which are included in other VNC clients and it not being actively developed. Not a good thing.

RealVNC provides remote control software which lets you see and interact with desktop applications across any network.

The software has a widespread user base from individuals to the largest multi-national companies. Founded by the original developers of VNC to promote, enhance and commercialise VNC.

TightVNC

Const Kaplinsky’s project to improve VNC’s compression between server and viewer. Good replacement for RealVNC, but graphic and performance is sluggish sometimes.
Does not allow remote copy and paste
The project is being actively maintain, which is a plus.

TightVNC is a free remote control software package. With TightVNC, you can see the desktop of a remote machine and control it with your local mouse and keyboard, just like you would do it sitting in the front of that computer. TightVNC is:

* free for both personal and commercial usage, with full source code available (GPL-licensed);
* useful in remote administration, remote customer support, education, and for many other purposes;
* cross-platform, available for Windows and Unix, compatible with other VNC software.

UltraVNC

* A project to add in file transfer, chat messaging and NTLM authentication to VNC.
* Based on experience, UltraVNC runs faster than the other two and has better graphics.
* Has file transfer, faster connections, chat interface, etc
* Allows you to copy and paste from your local computer to remote computer and vice versa

UltraVNC is a powerful, easy to use and free software that can display the screen of another computer (via internet or network) on your own screen. The program allows you to use your mouse and keyboard to control the other PC remotely. It means that you can work on a remote computer, as if you were sitting in front of it, right from your current location. If you provide computer support, you can quickly access your customer’s computers from anywhere in the world and resolve helpdesk issues remotely! With addons like SingleClick your customers don’t even have to pre-install software or execute complex procedures to get remote helpdesk support. 

My recommendation: UltraVNC
So far UltraVNC combines the best of both worlds. Speed, graphic, feature … you name it. It is a clear winner! However, things might be different in 5 years. We shall re-exam again at later time! :) 

## UltraVNC  介绍

UltraVNC 是客户端/服务器软件，允许你经由 TCP/IP 连线，控制远端的电脑。这个版本的开发以 RealVNC 为基础，加上了 TightVNC 的鼠标控制与编码，以及在 eSVNC 和 Vdacc-VNC 找到的特殊功能，以及更多。它是自由软件，可在 GNU General Public License 的条款下散布。

与 VNC 各版本不同的地方，还有:

1. 自动组态/快速选项。

2. 「工具列」显示，让你快速存取。无论是早期的 winvnc 或是后来的 RealVNC 都缺少这个东西。
3. 内建「图形介面」的「文件传送」功能。允许在客户端和服务器之间，做简易的文件复制。
4. 提供 Windows 2000 / XP 高速的「视讯挂钩驱动程序」 (核心模式) ，成功地改进效能，并降低网路连线时的 CPU 活动量。速度简直就是超快。只是「视讯挂钩驱动程序」并非 GPL 方式散布，但仍然是免费的就是了

UltraVNC既是一个客户端也是一个服务器，可以用TCP/IP连接来控制另一台电脑。它可以在W9x/NT/2K/XP在使用，拥有包括自动设置，友好用户界面，全局热键，内部文件传输等功能。除此之外，它还是免费的，速度也非常不错。UltraVNC可能是我见过的最快的远程控制软件。你可以在旅行的时候访问你家里的计算机，处理发现的故障或者一般的网络连接.

远程控制(Remote Control)是指在网络上由一台电脑（主控端Remote/客户端）远距离去控制另一台电脑（被控端Host/服务器端）的技术。大多数人平常接触最多的就是QQ的远程协助了，然后就是办公或黑客们必备的工具。

## 树莓派手动指定静态IP和DNS 终极解决大法

在把玩树莓派的过程中，往往需要手动给它设定一个静态的IP地址，一来可以防范DHCP自动分配的IP来回变动，导致远程SSH时常无法连接；二来还可以提高树莓派的网络连接速度。

对此菲菲君在网上查了很多资料，大多数方法都是修改 /etc/network/interfaces 配置文件，增加静态IP的设定。的确对于 Debian 系的 Linux 系统来说，不都是这样修改滴嘛？

不过马上就发现了一个问题，那就是通过修改 interfaces 设置静态IP的方法，并不完美，即便取得了静态IP，DHCP 服务依然会自动为树莓派分配动态 IP 和 DNS 地址，导致路由表默认网关出现冲突，以及手动给定的默认 DNS 不生效的情况。

解决树莓派静态IP和DNS难题的终极方法

其实解决起来特别简单，人家已经在 interfaces 文件的开头注释里告诉我们了要修改静态IP地址，需要修改的是 /etc/dhcpcd.conf 也就是 DHCP 的配置文件。

查看官方文档 man dhcpcd.conf 可知，需要配置 static IP 的话，只需修改以下参数：

		vi /etc/dhcpcd.conf
		# 使用 vi 编辑文件，增加下列配置项

如下：

		# 指定接口 eth0
		interface eth0
		# 指定静态IP，/24表示子网掩码为 255.255.255.0
		static ip_address=192.168.1.20/24
		# 路由器/网关IP地址
		static routers=192.168.1.1
		# 手动自定义DNS服务器
		static domain_name_servers=114.114.114.114

修改完成后，按esc键后输入 :wq 保存。重启树莓派就生效了

        重启电脑
		sudo reboot
        #或者重启网络
        sudo /etc/init.d/networking restart

另外注意配置时，你的静态IP一定要和你的路由器网段一致，比如：假设你的路由器的IP为 192.168.0.x 网段，则上面的 static ip_address 就要对应的修改为 192.168.0.x/24 。还有一点就是你的手动静态IP要注意不能跟路由器 DHCP 所自动分配的 IP 冲突，否则树莓派就有可能无法正常联网。

## 使用静态 IP 地址

		cd /etc/network
		sudo nano interfaces

把iface eth0 inet dhcp中的dhcp换成static也就是以下文本

		iface eth0 inet static
		address 192.168.1.10
		netmask 255.255.255.0
		gateway 192.168.1.1

最后重启一下就行了。

## 设置树莓派3 B+的静态IP

修改/etc/dhcpcd.conf 文件

		sudo vim /etc/dhcpcd.conf

如下：

		interface eth0
		static ip_address=192.168.0.10/24
		static routers=192.168.0.1
		static domain_name_servers=192.168.0.1
		interface wlan0	
		static ip_address=192.168.0.200/24
		static routers=192.168.0.1
		static domain_name_servers=192.168.0.1

上面的配置文件中 , eth0是有线的配置  , wlan0是无线配置

ip_address就是静态IP , 后面要接/24

routers是网关

static domain_name_servers是DNS

## 树莓派2——网线直连电脑SSH 

最近听说了好多不靠谱的言论，说是网线直连电脑不能动态分配IP地址，让我都想开喷了，但是为了共和国的团结和谐，今天就开一贴啪啪啪打脸那些所谓的技术达人。

首先，我们需要准备的是已经配好ssh开机自启动的树莓派和一根普通网线，然后把这两个连起来，但是问题又来了，ip地址从哪看？其实很简单：

右击这个“网络”图标，点开“打开网络和共享中心”

网络和共享中心

找到本地连接以后单击，本地连接

再点击详细信息，记下IPv4地址，我这里是 192.168.137.1

IPv4地址

打开命令行，输入arp -a查看与你电脑相关的连接

注意看192.168.137.97就是树莓派的IP地址，然后打开putty，输入就可以正常的连接了.

## 更简单的方法实现远程桌面

1.安装xdrp

	sudo apt-get install xdrp

2.使用window 程序附件的“远程桌面连接”，输入树莓派ip，以及用户密码，就OK！！！

##  树莓派 Raspberry Pi 设置无线上网

一、查看网卡状态是否正常

把无线网卡插到树莓派上，输入命令ifconfig -a查看是否有wlan0的信息，如果有说明网卡状态正常，可以跳过第二步，直接配置无线网络。如果查不到wlan0的信息，则需要安装无线网卡的驱动。

二、查看无线网卡的信息

输入命令dmesg | grep usb查看无线网卡的信息，主要是看制造厂家（Manufacturer）。比如，我的网卡信息是

usb 1-1.3: Manufacturer: Realtek

以Realtek为例，安装无线网卡驱动。
如果现在你的树莓派能联网，输入安装命令就可以安装Realtek的驱动了。

首先搜索Realtek驱动：

	apt-cache search realtek

看到下面信息：

firmware-realtek – Binary firmware for Realtek wired and wireless network adapters

安装Realtek驱动：

	sudo apt-get install firmware-realtek

如果你的树莓派现在不能上网，那么你可以去镜像站点中下载相关驱动。我推荐阿里云的镜像站点，速度比较快。http://mirrors.aliyun.com/raspbian/raspbian/pool/non-free/f/firmware-nonfree

下载firmware-realtek_0.43_all.deb，用winscp上传到树莓派的/tmp目录中。输入命令安装：

    sudo dpkg -i /tmp/firmware-realtek_0.43_all.deb
三、配置无线网络

用编辑器nano打开interfaces文件

    sudo nano /etc/network/interfaces

我的interfaces文件是这样的：

    auto lo

    iface lo inet loopback
    iface eth0 inet dhcp

    allow-hotplug wlan0
    iface wlan0 inet manual
    wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
    iface default inet dhcp

我们把无线网卡部分全部用#注释掉，然后添加自己的配置信息，最终结果如下：

    auto lo

    iface lo inet loopback
    iface eth0 inet dhcp

    auto wlan0
    #allow-hotplug wlan0
    #iface wlan0 inet manual
    iface wlan0 inet dhcp
    wpa-conf /etc/wpa.conf
    #wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
    iface default inet dhcp

使用nano编辑器，ctrl+o保存，ctrl+x退出。

用编辑器nano创建 /etc/wpa.conf 文件：

sudo nano /etc/wpa.conf

如果你的wifi没有密码

    network={
    [Tab] ssid="你的无线网络名称（ssid）"
    [Tab] key_mgmt=NONE
    }

如果你的wifi使用WEP加密

    network={
    [Tab] ssid="你的无线网络名称（ssid）"
    [Tab] key_mgmt=NONE
    [Tab] wep_key0="你的wifi密码"
    }

如果你的wifi使用WPA/WPA2加密

    network={
    [Tab] ssid="你的无线网络名称（ssid）"
    [Tab] key_mgmt=WPA-PSK
    [Tab] psk="你的wifi密码"
    }

注1：所有符号都是半角符号（英文状态下的符号），“[Tab]”表示按一次Tab键

注2：如果你不清楚wifi的加密模式，可以在安卓手机上用root explorer打开 /data/misc/wifi/wpa/wpa_supplicant.conf，查看wifi的信息。

比如，我的wpa.conf文件是这样的：

    network={
	ssid="1234"
	key_mgmt=WPA-PSK
	psk="MTIzNA1234"
    }

最后输入命令启用无线网卡：

    sudo ifup wlan0

可以连无线网了。

## 树莓派3如何使用蓝牙

一、升级安装蓝牙相关软件包

    sudo apt-get update
    sudo apt-get upgrade -y
    sudo apt-get dist-upgrade -y
    sudo apt-get install pi-bluetooth bluez bluez-firmware blueman

二、最关键一点：添加pi用户到蓝牙组

    sudo usermod -G bluetooth -a pi

三、重启

    sudo reboot

之后就可以按照各种教程正确使用蓝牙了

#  session setup failed: NT_STATUS_LOGON_FAILURE (

samba服务器出现“session setup failed: NT_STATUS_LOGON_FAILURE”的解决办法：

    $ smbclient -L \\127.0.0.1 -U wuhaoshu
    Enter berbiey's password:
    session setup failed: NT_STATUS_LOGON_FAILURE

wuhaoshu是fedora 13中的一个普通用户，启动smb服务后，在本机上测试，就出现了上面的错误。这是由于wuhaoshu仅仅只是系统用户，而没有将它加入到samba账户中来，换言之，用来登录samba服务器的账户，首先是一个系统账户，同时还应是samba账户。找到了问题的症结所在，解决就简单了。方法如下：

    # smbpasswd -a wuhaoshu

为安全起见，这个密码应与wuhaoshu作为系统账户登录系统时所用的密码不一样。

    $ smbclient -L \\127.0.0.1 -U wuhaoshu

现在就正常了。

### smbclient命令  网络服务器

《Linux就该这么学》是一本基于最新Linux系统编写的入门必读书籍，内容面向零基础读者，由浅入深渐进式教学，销量保持国内第一，年销售量超过10万本。点此免费在线阅读。

smbclient命令属于samba套件，它提供一种命令行使用交互式方式访问samba服务器的共享资源。

语法

    smbclient(选项)(参数)

选项

    -B<ip地址>：传送广播数据包时所用的IP地址；
    -d<排错层级>：指定记录文件所记载事件的详细程度；
    -E：将信息送到标准错误输出设备；
    -h：显示帮助；
    -i<范围>：设置NetBIOS名称范围；
    -I<IP地址>：指定服务器的IP地址；
    -l<记录文件>：指定记录文件的名称；
    -L：显示服务器端所分享出来的所有资源；
    -M<NetBIOS名称>：可利用WinPopup协议，将信息送给选项中所指定的主机；
    -n<NetBIOS名称>：指定用户端所要使用的NetBIOS名称；
    -N：不用询问密码；
    -O<连接槽选项>：设置用户端TCP连接槽的选项；
    -p<TCP连接端口>：指定服务器端TCP连接端口编号；
    -R<名称解析顺序>：设置NetBIOS名称解析的顺序；
    -s<目录>：指定smb.conf所在的目录；
    -t<服务器字码>：设置用何种字符码来解析服务器端的文件名称；
    -T<tar选项>：备份服务器端分享的全部文件，并打包成tar格式的文件；
    -U<用户名称>：指定用户名称；
    -w<工作群组>：指定工作群组名称。

参数

    smb服务器：指定要连接的smb服务器。

实例

列出某个IP地址所提供的共享文件夹

    smbclient -L 198.168.0.1 -U username%password

像ftp客户端一样使用smbclient

    smbclient //192.168.0.1/tmp  -U username%password

执行smbclient命令成功后，进入smbclient环境，出现提示符：smb:/>

这里有许多命令和ftp命令相似，如cd 、lcd、get、megt、put、mput等。通过这些命令，我们可以访问远程主机的共享资源。

直接一次性使用smbclient命令

    smbclient -c "ls"  //192.168.0.1/tmp  -U username%password

和

    smbclient //192.168.0.1/tmp  -U username%password
    smb:/>ls

功能一样的。

创建一个共享文件夹

    smbclient -c "mkdir share1" //192.168.0.1/tmp -U username%password

如果用户共享//192.168.0.1/tmp的方式是只读的，会提示NT_STATUS_ACCESS_DENIED making remote directory /share1

### smbclient使用方法及常见问题  

假如我现在在虚拟机中的linux中，使用smbclient连接windows中的共享文件夹。

windows的IP地址是192.168.0.4,登录的用户名叫Jack

在E盘下有个共享文件夹叫tmp,

    smbclient -U Jack  //192.168.0.4/tmp

然后会提示你输入密码：

    Enter Jack's password:

输入正确的密码后，如果成功就会看到提示符啦

    smb: \>

之后使用get，put，ls......就不说啦

还可以使用下面的命令列出共享的文件夹

    smbclient -U Jack -L 192.168.0.4

下面主要说一下失败的情况。

    1.tree connect failed: NT_STATUS_BAD_NETWORK_NAME

先检查指定的文件件是否共享了，然后检查共享目录的路径是否正确。

    2.session setup failed: NT_STATUS_LOGON_FAILURE

检查用-U指定的用户名是否正确；

在Windows的开始菜单中，运行secpol.msc，打开安全设置，本地策略-->安全选项-->网络访问：本地账户的共享和安全模型，选择“经典 - 对本地用户进行身份验证，不改变其本来身份”；

    3.session setup failed: NT_STATUS_LOGON_TYPE_NOT_GRANTED

在Windows的开始菜单中，运行secpol.msc，打开安全设置，本地策略-->用户权限分配-->

从网络访问此计算机，确认一下是否包含指定的用户；

### inux挂载samba文件系统的方法

1 手工挂载

 有两个命令可以用来手工挂载samba文件系统，一个是mount，一个是smbmount。

1.1 使用mount命令挂载

mount就是用于挂载文件系统的，SMB做为网络文件系统的一种，也能用mount挂载   一般挂载的用法为：

    mount -t smbfs -o codepage=cp936,username=用户名,password=密码 , -l //ip地址/共享文件夹名 挂载点

或

    mount -t smbfs -o codepage=cp936,username=用户名,password=密码 , -l //计算机名/共享文件夹名 挂载点

  若没有设置用户名和密码，则可以简化为:

      mount -t smbfs -o codepage=cp936 //ip地址或计算机名/共享文件夹名 挂载点

1.2 使用smbmount命令挂载

  smbmount说到底也是用mount的一个变种,因此，类似于mount命令，smbmount的用法为：

    smbmount -o username=用户名,password=密码 , -l //ip地址/共享文件夹名 挂载点
    smbmount -o username=用户名,password=密码 , -l //计算机名/共享文件夹名 挂载点
    smbmount //ip地址或计算机名/共享文件夹名 挂载点

 2 自动挂载

要让linux在启动时自动挂载samba文件系统，就需要用root用户编辑/etc/fstab文件，在其中加入一行

    //ip地址或计算机名/共享文件夹名 挂载点  smbfs   username=用户名,password=密码       0     0

### linux-mount: unknown filesystem type 'smbfs'解决方法记录

今天在使用CentOS release 5.2 (Final)，mount其它服务器的文件目录

    # mount -t smbfs -o username="administrator",password="" //192.168.1.100/cp /mnt/ntfs

提示出错：

    mount: unknown filesystem type 'smbfs'

查资料后，说smbfs改为cifs了，所以要用下面的方法：

    # mount -t cifs -o username="administrator",password="" //192.168.1.101/cp /mnt/ntfs

成功！！

## 网络文件系统 (NFS)

NFS 允许系统将其目录和文件共享给网络上的其他系统。通过 NFS，用户和应用程序可以访问远程系统上的文件，就象它们是本地文件一样。

NFS 最值得注意的优点有：

                本地工作站可以使用更少的磁盘空间，因为常用数据可以被保存在一台机器上，并让网络上的其他机器可以访问它。
                不需要为用户在每台网络机器上放一个用户目录。用户目录可以在 NFS 服务器上设置并使其在整个网络上可用。
                存储设备如软盘、光驱及 USB 设备可以被网络上其它机器使用。这可能可以减少网络上移动设备的数量。

4.6.1. 安装

在终端提示符后键入以下命令安装 NFS 服务器：

    sudo apt-get install nfs-kernel-server

4.6.2. 配置

您可以配置要输出的目录，您可以在 /etc/exports 文件中添加该目录。例如：

    /ubuntu *(ro,sync,no_root_squash)
    /home *(rw,sync,no_root_squash)

您可以用主机名来代替 *。尽量指定主机名以便使那些不想其访问的系统访问 NFS 挂载的资源。

您可以在终端提示符后运行以下命令来启动 NFS 服务器：

    sudo /etc/init.d/nfs-kernel-server start

4.6.3. NFS 客户端配置

使用 mount 命令来挂载其他机器共享的 NFS 目录。可以在终端提示符后输入以下类似的命令：

    sudo mount example.hostname.com:/ubuntu /local/ubuntu

挂载点 /local/ubuntu 目录必须已经存在。而且在 /local/ubuntu 目录中没有文件或子目录。

另一个挂载其他机器的 NFS 共享的方式就是在 /etc/fstab 文件中添加一行。该行必须指明 NFS 服务器的主机名、服务器输出的目录名以及挂载 NFS 共享的本机目录。

以下是在 /etc/fstab 中的常用语法：

    example.hostname.com:/ubuntu /local/ubuntu nfs rsize=8192,wsize=8192,timeo=14,intr