% Ftp服务器、Samba服务器、NFS服务器
根据使用的方式来看，可以分为3种类别的文件服务器：ftp服务器（ftp/tftp）、 Samba服务器、NFS服务器。ftp的客户可以是任意平台，samba是专门针对windows客户，而NFS则是面向linux/unix用户的。下面是三种服务器的对比情况：

服务器名称     用户客户端平台     使用范围     服务端口

--------
FTP           Windows/linux/unix/macOS等            发布网站，文件共享                     Tcp/21
Samba                    Windows                               文件共享（网上邻居）                  Tcp/445,tcp/139
NFS                    Linux/unix                                 网站发布，文件共享（mount）     Tcp/2049
-------------

简单的说一下个个服务器的配置

### NFS服务器

   NFS是SUN Microsystem公司开发的网络文件系统，它是一种基于远程过程调用（RPC）的分布式文件系统架构。与Samba相比较，NFS的数据吞吐能力更强。

1、     用命令 # rpm –qa | grep nfs检查软件包NFS是否安装 ,如果输出没有输出，表明没有被安装，请自行安装之。

2、     配置NFS服务器。用任何文本编辑器配置文件/etc/exports,来确定需要给客户共享的目录。

它的基本格式为 Directory   Host(options) # comments ,这3个字段/列要在一行，directory与host(options)之间要有间隙，# comments 可有可无。主机选项主要是给与挂接用户什么样的权限。目录directory表示要共享出去的目录，值得注意的是，在启用NFS服务以前，系统管理员应该仔细一些，比如不小心共享了根目录/，并且给与用户读写权限，这是十分糟糕的问题。因此，尽可能少的共享目录和赋予较小的访问权限。主机名host是一个很灵活的项目，可以是单个的主机名称（由/etc/hosts得到），主机ip地址，由域名服务器解析的主机名称，IP网络—网络号和子网掩码中间用 “/”连接，NIC等。下面列举一个例子。

    /home/sery     sery(rw) #把目录/home/sery共享给主机sery,并且主机对目录#/home/sery有读写权限

    /tmp       192.168.100.18(ro) #主机192.168.100.18对目录/tmp具备只读共#享权限

    /media/cdrom   192.168.100.0/255.255.255.0(ro) #整个网络有读取挂接在NFS

    #服务器上的光驱光盘的读取权限

3、     启用NFS服务。分两步：首先启用portmap,然后启用NFS服务。

    # service portmap start;
    # service nfs start。
    其中portmap的功能是启用远程过程调用，有时启用NFS不能成功，不妨检查一下portmap服务是否启动（# ps aux | grep portmap）。

4、     在客户端挂接NFS共享出来的目录。先在客户端创建一个挂接点，如 # mkdir /mnt/nfs ,而后使用命令把nfs服务器共享出来的目录挂接上，以第2步那个共享为例，我们挂接目录 /tmp ,

    # mount –t nfs 192.168.100.100:/tmp /mnt/nfs //假定nfs服务器的ip地址是192.168.100.100。

5、     访问NFS共享资源。接上步，改变文件目录 # cd /mnt/nfs就方便地实现了对nfs服务器目录/tmp的远程访问。

6、     卸载NFS文件系统。在客户端执行命令 # umount /mnt/nfs 就卸下了第4步挂接的NFS文件系统。

### Samba服务器

  这个世界既非只有linux/unix,也不是由microsoft windows 独霸天下的格局。也许出于linux/unix与windows既竞争又共存的事实，人们开发了 linux给windows用户提供文件共享的工具Samba，这应该算得上linux的开放精神吧！

1、     检查是否安装samba软件包。

    # rpm –qa | grep smb ，如果没有则自行安装samba。

2、     修改配置文件/etc/samba/smb.conf。早期的linux版本的配置文件smb.conf的安全选项“security=share”,这个默认值是个安全隐患，不过现在流行的linux版本的安全选项的默认值是“security=user”。如果只想用户对他的目录拥有只读权限，就把选项“writeable=yes”改成“read only=yes”。其他的选项根据自己的要求更改即可。对于一般的应用而言，基本上不用修改这个文件。

3、     添加系统账户。由于smb的访问是使用系统账号进行的，因此添加账号是必不可少的。这个比较简单，用命令 

    # useradd sery , 
    # passwd sery，就可以依次添加若干系统账号。

4、     建立Samba用户密码文件。虽然samba的用户是系统用户，但出于安全考虑，samba用户的密码并非创建系统用户时设定的用户密码。为了生成smb所需的密码，应该进行下面的操作：

    # smbpasswd  -a sery   //为系统用户设置smb口令

5、  启用Samba服务器。

    # service smb start

6、  windows客户端访问 Samba服务器共享目录。在windows环境下，右键点击“网上邻居”图标，然后左击“搜索计算机”，把Samba服务器的IP地址填写在“计算机名”搜索栏，点击立即搜索。找到后双击图标，然后输入在Samba服务器上预先设定的用户名和密码，就能合法访问Samba服务器设定的共享资源。为了方便使用，可以把Samba服务器提供的共享目录映射成本地驱动器。

7、     其他。上述配置的samba服务器，用户的访问共享目录是系统账号的主目录。要想把共享目录设置到其他位置，修改Samba 的配置文件/etc/samba/smb.conf文件即可。

### FTP服务器

  在linux 环境下，有三个主要的FTP服务器：vsftpd、proftpd和wu-ftpd。因为安全方面的原因，vsftpd目前已经牢牢的占据了主导地位。从字面上我们就可以理解vsftpd所具备的主要特征—very secure(非常安全之ftp)。资料表明：1、使用ASCII方式下载文件，在1G以太网上的下载速度可以达到86M/s。2、vsftpd可以支持 15000个并发用户的访问。

1、     检查是否安装vsftp包。

    # rpm –qa | grep vsftpd。如果没有则安装它。

2、     修改配置文件。Vsftpd的配置文件为/etc/vsftpd/vsftpd.conf,如果不打算提供匿名访问的话，需要修改配置文件 /etc/vsftpd/vsftpd.conf的项“anonymous_enable=Yes”为“anonymous_enable=No”。

3、     启用vsftpd服务。

    #service vsftpd start。

4、     客户端连接访问。可以是专用的ftp客户端工具，也可以使用浏览器。用工具访问vsftpd服务器的速度要比用浏览器快很多。

5、     vsftpd服务器的用户。Vsftpd服务器支持三种类型的拥护：本地用户（拥有系统账号）、虚拟用户（guest）、匿名账号；系统管理员应该根据安全需求来确定vsftpd服务器的用户访问策略

##  Raspberry Pi3 ~ 安装 nfs Server

安装必要服务： 

    sudo      apt-get install  portmap 

    sudo  apt-get install  nfs-kernel-server

编辑文件 

    sudo      vim /etc/exports  

添加：

    /home/pi/Myself      192.168.11.*(rw,sync,no_subtree_check)     

   * 表示最后一段任何IP都可以共享，如果你想限定个别IP，用IP替代

   注意要事先创建要共享的目录

**参数说明**

----
ro #只读访问
rw #读写访问
sync #所有数据在请求时写入共享
async #nfs在写入数据前可以响应请求
secure# nfs通过1024以下的安全TCP/IP端口发送
insecure# nfs通过1024以上的端口发送
wdelay# 如果多个用户要写入nfs目录，则归组写入（默认）
no_wdelay #如果多个用户要写入nfs目录，则立即写入，当使用async时，无需此设置
hide#在nfs共享目录中不共享其子目录
no_hide#共享nfs目录的子目录
subtree_check#如果共享/usr/bin之类的子目录时，强制nfs检查父目录的权限（默认）
no_subtree_check#不检查父目录权限
all_squash#共享文件的UID和GID映射匿名用户anonymous，适合公用目录
no_all_squash#保留共享文件的UID和GID（默认）
root_squash#root用户的所有请求映射成如anonymous用户一样的权限（默认）
no_root_squash#oot用户具有根目录的完全管理访问权限
anonuid=xxx#指定nfs服务器/etc/passwd文件中匿名用户的UID
anongid=xxx#指定nfs服务器/etc/passwd文件中匿名用户的GID
----

启动：

    /etc/init.d/nfs-kernel-server     start

检查是否启动 

    showmount      –e  localhost

发现启动不起来，卡主不动。解决方法：

在服务器上先停止rpcbind 和nfs在启动 注意顺序    

    sudo      /etc/init.d/rpcbind  stop                     停止rpcbind   
    sudo      /etc/init.d/nfs-kernel-server stop        停止nfs
    sudo      /etc/init.d/rpcbind start                      启动rpcbind   
    sudo     /etc/init.d/nfs-kernel-server start         启动nfs

查看nfs状态： 

    pi@raspberrypi:~ $ showmount  -e  localhost   
    Export     list for localhost:
    /home/pi/xun/nfs      192.168.11.*   

出现目录和访问地址即可

 客户端进行连接

    sudo mount  -t  nfs    -o  nolock  192.168.11.135:/home/pi/xun/nfs  /home/xun/server/nfspi

注意事先创建目录

##  Gentoo安装配置使用nfs

Gentoo安装配置使用nfs

在局域网中，充分使用NFS能大大提高开发工作环境方便快捷性。gentoo中使用NFS需要安装以下两个包:

先配置内核。

    nfs-utils
    portmap

emerge nfs-utils 时会自动把portmap安装，因为依赖关系，所以不必要emerge portmap。在不能自动解决软件包依赖关系的系统上下载源代码来装，还要下载安装以下三个包：tcp_wrapper, libevent, libnfsidmap

在NFS服务器（192.168.1.254）端，配置/etc/exports文件, 如：

    /home/clfs 192.168.1.2(rw,async,no_root_squash,no_subtree_check)

启动NFS服务：

    # /etc/init.d/portmap start
    # /etc/init.d/nfs start

为了方便，可以设NFS为自动启动服务：

    # rc-update add nfs default
    # rc-update add portmap defaul

在客户端，首先要启动portmap服务，再挂载NFS文件系统

    # rc-update add portmap default
    # mount -t nfs 192.168.1.254:/home/clfs /home/clfs

就可以通过/home/clfs在两台机器间共享文件了。

安全问题在更深入了解后再补充。

##  树莓派挂载U盘、挂载系统SD卡后面的分区、挂载光盘、挂载Windows的共享文件夹和Linux的共享文件夹（Linux）(挂载)

一.通过给linux下的设备管理服务udev添加规则配置文件，可以实现命令行下USB存储设备自动挂载

输入命令：

    sudo nano /etc/udev/rules.d/10-usbstorage.rules

 复制粘贴这个脚本到编辑窗口

    KERNEL!="sd*", GOTO="media_by_label_auto_mount_end"  
    SUBSYSTEM!="block",GOTO="media_by_label_auto_mount_end"
    IMPORT{program}="/sbin/blkid -o udev -p %N"  
    ENV{ID_FS_TYPE}=="", GOTO="media_by_label_auto_mount_end"
    ENV{ID_FS_LABEL}!="", ENV{dir_name}="%E{ID_FS_LABEL}"  
    ENV{ID_FS_LABEL}=="", ENV{dir_name}="Untitled-%k"  
    ACTION=="add", ENV{mount_options}="relatime,sync"  
    ACTION=="add", ENV{ID_FS_TYPE}=="vfat", ENV{mount_options}="iocharset=utf8,umask=000"  
    ACTION=="add", ENV{ID_FS_TYPE}=="ntfs", ENV{mount_options}="iocharset=utf8,umask=000"  
    ACTION=="add", RUN+="/bin/mkdir -p /media/%E{dir_name}", RUN+="/bin/mount -o $env{mount_options} /dev/%k /media/%E {dir_name}" 
    ACTION=="remove", ENV{dir_name}!="", RUN+="/bin/umount -l /media/%E{dir_name}", RUN+="/bin/rmdir /media/%E{dir_name}"  
    LABEL="media_by_label_auto_mount_end"  

保存退出，再次插入usb存储设备 会自动挂载到/media目录下面的目录 并且支持utf8格式的中文文件名。

说明：

    命令格式：mount [-t vfstype] [-o options] device dir 其中： 
    1.-t vfstype 指定文件系统的类型，通常不必指定。mount 会自动选择正确的类型。常用类型有： 
    光盘或光盘镜像：iso9660 
    DOS fat16文件系统：msdos 
    Windows 9x fat32文件系统：vfat 
    Windows NT ntfs文件系统：ntfs 
    Mount Windows文件网络共享：smbfs 
    UNIX(LINUX) 文件网络共享：nfs 
    2.-o options 主要用来描述设备或档案的挂载方式。常用的参数有： 
    loop：用来把一个文件当成硬盘分区挂载上系统 
    ro：采用只读方式挂载设备 
    rw：采用读写方式挂载设备 
    iocharset：指定访问文件系统所用字符集 
    3.device 要挂载(mount)的设备。 
    4.dir设备在系统上的挂载点(mount point)。
    umask=0000 0 0
    前面四个0就是对所有人,可读可写可执行,
    后面两个0,第一个代表dump,0是不备份
    第二个代表fsck检查的顺序,0表示不检查

二.通过/etc/fstab 自动挂载SD卡的第三个分区

    sudo mkdir /media/usb
    sudo nano /etc/fstab

添加

    /dev/mmcblk0p3 /media/usb   ext4    defaults     0      0

说明：

    第一项是您想要mount的储存装置的实体位置，如hdb或/dev/sda1。
    第二项就是您想要将其加入至哪个目录位置，如/home或/,这其实就是在安装时提示的挂入点。
    第三项就是所谓的local filesystem，其包含了以下格式：如ext、ext2、msdos、iso9660、nfs、swap等，或如ext2，可以参见/prco/filesystems说明。
    第四项就是您mount时，所要设定的状态，如ro（只读）或defaults（包括了其它参数如rw、suid、exec、auto、nouser、async），可以参见「mount nfs」。
    第五项是提供DUMP功能，在系统DUMP时是否需要BACKUP的标志位，其内定值是0。
    第六项是设定此filesystem是否要在开机时做check的动作，除了root的filesystem其必要的check为1之外，其它皆可视需要设定，内定值是0。

三.手动挂载U盘 (FAT32)

插入U盘之前，应先用fdisk –l 或 more /proc/partitions查看系统的硬盘和硬盘分区情况。 

      sudo fdisk -l

插入U盘后，再用fdisk –l 或 more /proc/partitions查看系统的硬盘和硬盘分区情况。 

      sudo fdisk -l

系统多了一个SCSI硬盘/dev/sda和一个磁盘分区/dev/sda1,/dev/sda1就是我们要挂载的U盘。 

    sudo mkdir -p /mnt/usb 

注：建立一个目录用来作挂载点(mount point) 

    sudo mount -t vfat /dev/sda1 /mnt/usb 

注：现在可以通过/mnt/usb来访问U盘了, 若汉字文件名显示为乱码或不显示，可以使用下面的命令。 

    sudo mount -t vfat -o iocharset=cp936 /dev/sda1 /mnt/usb 

注：对ntfs格式的磁盘分区应使用-t ntfs 参数，对fat32格式的磁盘分区应使用-t vfat参数

对于ext2、ext3、ext4格式,使用下面的命令直接挂载即可:

    sudo mount /dev/sda1 /mnt/usb

四.光盘镜像文件的挂载(mount) 

    sudo mkdir /mnt/vcdrom 

注：建立一个目录用来作挂载点(mount point) 

    sudo mount -o loop -t iso9660 ~/mydisk.iso /mnt/vcdrom 

注：使用/mnt/vcdrom就可以访问盘镜像文件mydisk.iso里的所有文件了。 

五.挂载Windows文件共享 

Windows网络共享的核心是SMB/CIFS，在linux下要挂载(mount)windows的磁盘共享，就必须安装cifs-utils软件包。

    sudo apt-get install cifs-utils

当windows系统共享设置好以后，就可以在linux客户端挂载(mount)了，具体操作如下： 

    sudo mkdir –p /mnt/samba 

注：建立一个目录用来作挂载点(mount point) 

      mount -t cifs -o codepage=cp936 //ip地址或计算机名/共享文件夹名 挂载点

    sudo  mount -t cifs -o username=administrator,password=xxx //192.168.1.100/gongxiang /mnt/samba 

注：administrator 和 xxx 是ip地址为192.168.1.100 windows计算机的一个用户名和密码，//192.168.1.100/gongxiang是这台计算机的一个共享文件夹的全路径,如此就可以在linux系统上通过/mnt/samba来访问windows系统磁盘上的文件了。

注：查看windows共享文件夹

打开命令提示符：开始→搜索框（运行）键入cmd，然后键入：net share

出现如下的提示，里面的第一列 gongxiang 或者 C$ 等就是共享文件夹的路径

 注：fatab挂载samba网络共享文件夹 ，在/etc/fstab中添加：

    //192.168.1.100/gongxiang /mnt/samba  cifs  username=administrator,password=xxx  0  0

六.挂载UNIX系统NFS文件共享 

类似于windows的网络共享，UNIX(Linux)系统也有自己的网络共享，那就是NFS(网络文件系统)。在linux客户端挂载(mount)NFS磁盘共享之前，必须先配置好NFS服务端。 

1、Ubuntu 12.04 系统NFS服务端配置方法如下： 

    sudo apt-get install nfs-kernel-server

打开/etc/exports文件，在末尾加入：

    /home/knat/nfs *(rw,sync,no_root_squash)

注：nfs允许挂载的目录及权限，在文件/etc/exports中进行定义，各字段含义如下：

/home/knat/nfs：要共享的目录

\* ：允许挂载此共享linux客户机的IP地址或主机名。*表示允许所有的网段访问

rw ：读写权限

sync：资料同步写入内在和硬盘

no_root_squash：nfs客户端共享目录使用者权限

重启服务：

    sudo /etc/init.d/portmap restart                  <---重启portmap，
    sudo /etc/init.d/nfs-kernel-server restart        <---重启nfs服务
    showmount -e                                       <---显示共享出的目录。 

2、linux客户端树莓派上挂载(mount)其他linux系统或UNIX系统的NFS共享 

    sudo  mkdir –p /mnt/nfs 

注：建立一个目录用来作挂载点(mount point) 

    sudo mount -t nfs -o nolock 192.168.1.166:/home/knat/nfs /mnt/nfs

注：这里192.168.1.166是NFS服务端(Ubuntu 12.04 )的主机IP地址(用ifconfig命令查看)，当然这里也可以使用主机名，但必须在本机/etc/hosts文件里增加服务端ip定义。/home/knat/nfs为服务端共享的目录。 

注：fatab挂载NFS网络共享文件夹 ，在/etc/fstab中添加：

    192.168.1.166:/home/knat/nfs /mnt/nfs nfs  nolock 0 0

## Gentoo Linux下配置Samba服务器文件共享

主机：Gentoo 11.2 with linux kernel 3.0.6

1、安装Samba服务器

使用默认的USE标记直接执行命令

    emerge samba  

2、配置/etc/samba/smb.conf

首先拷贝/etc/samba/smb.conf.default然后根据自己的需要修改

修改后的smb.conf文件如下

FILE /etc/samba/smb.confSamba configuration example

    [global]
    ## # Replace MYWORKGROUPNAME with the appropriate workgroup/domain
    workgroup = ## MYWORKGROUPNAME
    ## # Of course this has no REAL purpose other than letting
    # everyone knows it is not Windows!
    # %v prints the version of Samba being used.
    server string = Samba Server %v
    ## # CUPS will be used; it should be inserted here
    printcap name = cups
    printing = cups
    load printers = yes
    ## # This line enables the log file and limits its size to less than 50kb.
    log file = /var/log/samba/log.%m
    max log size = 50
    ## # We are going to set some options for our interfaces...
    socket options = TCP_NODELAY SO_RCVBUF=8192 SO_SNDBUF=8192
    ## # This is a good idea, what we are doing is binding the
    # samba server to our local network.
    # For example, if eth0 is the local network interface:
    interfaces = lo eth0
    bind interfaces only = yes
    ## # Specifies which IP address range is allowed to access Samba
    # (this is for added security since this configuration does
    # not use passwords):
    hosts allow = 127.0.0.1 192.168.1.0/24
    hosts deny = 0.0.0.0/0
    ## # Other options for this are USER, DOMAIN, ADS, and SERVER
    # The default is user
    security = share
    ## # No passwords will be used so a guest account should be enabled:
    guest ok = yes

    ## # Now set print drivers information:
    [print$]
    comment = Printer Drivers
    path = /etc/samba/printer ## # This path holds the driver structure
    guest ok = yes
    browseable = yes
    read only = yes
    ## # Modify the following to "<username>,root" to add a second printer admin:
    write list = root

    ## # Setup a printer to share. While the name is arbitrary it
    # should be consistent throughout Samba and CUPS:
    [HPDeskJet930C]
    comment = HP DeskJet 930C Network Printer
    printable = yes
    path = /var/spool/samba
    public = yes
    guest ok = yes
    ## # Modify the following to "<username>,root" to add a second printer admin:
    printer admin = root

    ## # Now set the printer share. This should be
    # browseable, printable, public, etc.:
    [printers]
    comment = All Printers
    browseable = no
    printable = yes
    writable = no
    public = yes
    guest ok = yes
    path = /var/spool/samba
    ## # Modify the following to "<username>,root" to add a second printer admin:
    printer admin = root

    ## # Create a new share that can read from or written to anywhere.
    # This is kind of like a temp public share; anyone can do what
    # they want here:
    [public]
    comment = Public Files
    browseable = yes
    public = yes
    create mode = 0766
    guest ok = yes
    path = /home/samba/public

3、创建文件夹

    sudo mkdir /home/samba  
    chmod 777 /home/samba  

4、重启samba服务

    sudo /etc/init.d/samba restart   

设置开机启动：OpenRC

    sudo rc-update add samba default

启动：

    sudo  /etc/init.d/samba start

5、在windows上访问samba  server：

* 【网上邻居】搜索计算机
* 网上邻居
* unc路径    \\对方地址或者名字\共享名字
* 映射网络驱动器
* net  use      net share

６。linux下客户端：

在Linux系统中访问Samba服务器中的共享目录需要使用smbclient命令，当然首先得在对应Linux系统主机中安装Samba服务的客户端软件smbclient。

smbclient    与samba服务器断开连接后需要重新连接

使用共享目录的命令格式为：

    smbclient  //IP地址或主机名/共享目录名  -U用户名。

比如：

    sudo smbclient -L //192.168.11.135/samba

在出现提示输入密码时，直接按Enter键（因为此处是匿名访问），结果会显示指定Samba服务器上当前全部的共享目录，其中：-L　列出目录。

若是匿名访问，无须加上"-U"选项来指定访问的用户名。如在此要匿名访问Sambaserver上的samba目录，则可以在终端提示符下输入以下命令：

	sudo smbclient  //192.168.11.135/samba

在出现输入密码的password提示符时，直接按Enter键，即进入到远程使用服务器上指定资源的提示符smb:\>，与FTP客户端相似，这时可以使用如cd、cat、get等命令对共享目录和文件进行操作了。注意，这个命令不仅可以访问Samba服务器上的共享资源，还可以访问网络中Windows主机上的共享资源。

也可以：

    smbmount    直接访问挂载点（分为手动挂载和自动挂载）

## linux客户端访问samba服务器的指令

linux客户端要连接samba/windows文件服务器时，需使用smbmount或mount指令：

    smbmount //sambaserver/d /mnt/d -o username=aaa,password=bbb

    smbmount //sambaserver/d /mnt/d -o username=aaa%bbb

    mount -t smbfs -o username=aaa,password=bbb //sambaserver/d /mnt/d

    mount -t smbfs -o username=aaa%bbb //sambaserver/d /mnt/d

    smbclient //sambaserver/d -U username%password

注意：

1. 指定uid或者gid参数，也可以指定用户的身份(uid=后面可接uid号或者用户名)，如：
smbmount //test/d /mnt/d -o uid=grind
2. smbmount也可以写作mount.smbfs，这是一个符号链接；
3. smbmount的参数必须写在最后，而mount的参数位置可以变化；
4. 由于//sambaserver/d格式可以表明是要mount上smbfs，所以mount的-t smbfs参数可以省掉；
5. 如果命令行中不加入密码，下一行中系统会提示你输入；
6. smbclient成功后，会出现ftp类似的界面，请仿照ftp进行。

## Mounting a Windows or Samba share in GNU/Linux

Then make the module/install it; insert it with:

    sudo modprobe cifs

Once the module is loaded, mounting a Windows or Samba share is possible. Use mount to accomplish this, as detailed below.

The syntax for mounting a Windows/Samba share is:

    sudo mount -t cifs [-o username=xxx,password=xxx] //server/share /mnt/point

You can drop the username and password options if no password is needed.

    sudo mount -t cifs //PrintServer/public /mnt/public

gentoo挂载pi上的samba目录：

    sudo mount -t cifs //192.168.11.135/samba ~/server/sambapi

After mounting the share, it can be accessed as if it were a local drive. 

##  ubuntu下设置开机自启动项

这里说明，Ubuntu 中系统没有了RH系统中的 chkconfig 命令 ！

可用一些小工具来管理 Ubuntu 的启动选项：

小工具 rcconf：

    #sudo apt-get rcconf

    #sudo apt-get install rcconf

root 下运行:

    #sudo rcconf
功能更全的工具：sysv-rc-conf

    #sudo apt-get update
    #sudo apt-get install sysv-rc-conf

运行：

    #sudo sysv-rc-conf

也可以直接加入启动程序，例如把 /etc/init.d/red5 加入到系统自动启动列表中：

    #sudo sysv-rc-conf red5 on

其他使用方法见: google::Ubuntu::sysv-rc-conf 命令用法

也可以直接修改

直接改 /etc/rc0.d ~ /etc/rc6.d 和 /etc/rcS.d 下的东西，S开头的表示启动，K开头的表示不启动，

例如：想关闭 Red5 的开机自动启动，只需 #sudo mv /etc/rc2.d/S20red5 /etc/rc2.d/K20red5 就可以了。

Ubuntu自动启动程序

首 先，linux随机启动的服务程序都在/etc/init.d这个文件夹里，里面的文件全部都是脚本文件（脚本程序简单的说就是把要运行的程序写 到一个 文件里让系统能够按顺序执行，类似windows下的autorun.dat文件），另外在/etc这个文件夹里还有诸如名为rc1.d, rc2.d一直到rc6.d的文件夹，这些都是linux不同的runlevel，我们一般进入的X windows多用户的运行级别是第5级，也就是rc5.d，在这个文件夹下的脚本文件就是运行第5级时要随机启动的服务程序。需要注意的是，在每个rc (1-6).d文件夹下的文件其实都是/etc/init.d文件夹下的文件的一个软连接（类似windows中的快捷方式），也就是说，在 /etc/init.d文件夹下是全部的服务程序，而每个rc(1-6).d只链接它自己启动需要的相应的服务程序！

要 启动scim (某一程序)，我们首先要知道scim程序在哪里，用locate命令可以找到，scim在/usr/bin/scim这里，其中usr表 示是 属于用户的，bin在linux里表示可以执行的程序。这样，我就可以编写一个脚本程序，把它放到/etc/init.d里，然后在rc5.d里做一个相 应的软链接就可以了。

这个脚本其实很简单，就两行：

    #!/bin/bash

    /usr/bin/scim

第一行是声明用什么终端运行这个脚本，第二行就是要运行的命令。

还 需要注意的一点是，在rc5.d里，每个链接的名字都是以S或者K开头的，S开头的表示是系统启动是要随机启动的，K开头的是不随机启动的。这 样，你就可以知道，如果我要哪个服务随机启动，就把它名字第一个字母K改成S就可以了，当然，把S改成K后，这个服务就不能随机启动了。因此，我这个链接 还要起名为SXXX，这样系统才能让它随机启动。

在RH下，rc.local是默认启动的最后一个脚本文件，所以，

如果你想要随机启动，还有一种方法就是在rc.local的尾部加入/usr/bin/scim，这样就可以了。

Linux 自动启动程序

1．开机启动时自动运行程序

Linux 加载后, 它将初始化硬件和设备驱动, 然后运行第一个进程init。init根据配置文件继续引导过程，启动其它进程。通常情况下，修改放置在 /etc/rc或 /etc/rc.d 或 /etc/rc?.d 目录下的脚本文件，可以使init自动启动其它程序。例如：编辑 /etc/rc.d/rc.local 文件(该文件通常是系统最后启动的脚本)，在文件最末加上一行“xinit”或“startx”，可以在开机启动后直接进入X－Window。

2．登录时自动运行程序

用 户登录时，bash首先自动执行系统管理员建立的全局登录script ：/ect/profile。然后bash在用户起始目录下按顺序查找三个特殊文件中的一个：/.bash_profile、/.bash_login、 /.profile，但只执行最先找到的一个。
因此，只需根据实际需要在上述文件中加入命令就可以实现用户登录时自动运行某些程序（类似于DOS下的Autoexec.bat）。

3．退出登录时自动运行程序

退出登录时，bash自动执行个人的退出登录脚本/.bash_logout。例如，在/.bash_logout中加入命令“tar －cvzf c.source.tgz ＊.c”，则在每次退出登录时自动执行 “tar” 命令备份 ＊.c 文件。

4．定期自动运行程序

Linux有一个称为crond的守护程序，主要功能是周期性地检查 /var/spool/cron目录下的一组命令文件的内容，并在设定的时间执行这些文件中的命令。用户可以通过crontab 命令来建立、修改、删除这些命令文件。

例如，建立文件crondFile，内容为“00 9 23 Jan ＊ HappyBirthday”，运行“crontab cronFile”命令后，每当元月23日上午9:00系统自动执行“HappyBirthday”的程序（“＊”表示不管当天是星期几）。

5．定时自动运行程序一次

定时执行命令at 与crond 类似（但它只执行一次）：命令在给定的时间执行，但不自动重复。at命令的一般格式为：at [ －f file ] time ，在指定的时间执行file文件中所给出的所有命令。也可直接从键盘输入命令：

    ＄ at 12:00
    at>mailto Roger －s ″Have a lunch″ < plan.txt
    at>Ctr－D
    Job 1 at 2000－11－09 12:00
    2000－11－09 12:00时候自动发一标题为“Have a lunch”，内容为plan.txt文件内容的邮件给Roger。?9 12:00
    2000－11－09 12:00时候自动发一标题为“Have a lunch”，内容为plan.txt文件内容的邮件给Roger。er。ger。er。

Ubuntu 开机自动挂载windows分区

要挂载NTFS格式分区，需要NTFS-3g这个软件。它短小精悍，而且功能强大。
NTFS-3g是一个开源软件，它支持在Windows下面读写NTFS格式的分区。它非常的快速，同时也很安全。它支持Windows 2000、XP和2003，并且支持所有的符合POSIX标准的磁盘操作。

首先要编辑sources.list

    #sudo gedit /etc/apt/sources.list

Ubuntu Drapper添加：

    deb http://givre.cabspace.com/ubuntu/ dapper main main-all
    deb http://ntfs-3g.sitesweetsite.info/ubuntu/ dapper main main-all
    deb http://flomertens.keo.in/ubuntu/ dapper main main-all

Ubuntu Edgy添加：

    deb http://givre.cabspace.com/ubuntu/ edgy main
    deb http://ntfs-3g.sitesweetsite.info/ubuntu/ edgy main
    deb http://flomertens.keo.in/ubuntu/ edgy main

 同时必须导入GPG-Key，可以这样：

    #wget http://flomertens.keo.in/ubuntu/givre_key.asc -O- | sudo apt-key add -
    #wget http://givre.cabspace.com/ubuntu/givre_key.asc -O- | sudo apt-key add -

现在更新一下源：

    #sudo aptitude update

正式安装

在“终端”下面运行：

    #sudo apt-get install ntfs-3g

配置NTFS-3g

首先看一些硬盘分区的分区类型

    #sudo fdisk -l

现在就可以修改 /etc/fstab，来让Ubuntu启动的时候自动挂载NTFS分区了。但是首先请备份一下这个文件：

    #sudo cp /etc/fstab /etc/fstab.bak

建立挂载点，譬如挂载在 /media/windows 下面

    #sudo mkdir /media/windows

现在可以在 /etc/fstab 的后面添加

    /dev/hda1 /media/ ntfs-3g defaults,locale=zh_CN.utf8 0 0

根据自己的情况进行修改。

一些示例

    挂载 /dev/hda3
    添加 /dev/hda3 /media/windows ntfs-3g ro,locale=zh_CN.utf8,uid=1000 0 0

关于自己的locale

可以用下面的命令查看所有的locale

    #locale -a

如果不想重新启动，就可以

    #sudo umount -a
    #sudo mount -a

最后一个挂载FAT分区的命令

    #sudo mount /dev/hda3 /media/windows/ -t vfat -o iocharset=utf8,umask=000

当然可以在/etc/fstab里面添加

    /dev/hda3 /media/windows vfat iocharset=utf8,umask=000 0 0

Openfire随着Ubuntu自动启动

openfire缺省情况下，是不随机启动的。为了解决每次都要手工启动的麻烦，我编写了一个脚本，放在/etc/init.d目录里面

    #sudo vim /etc/init.d/openfire

内容如下：

    #!/bin/sh

    openfire_start(){
    /etc/openfire/bin/openfire start
    }

    openfire_stop(){
    /etc/openfire/bin/openfire stop
    }

    case $1 in
    start)
    openfire_start
    ;;
    stop)
    openfrie_stop
    ;;
    *)
    echo ‘Usage:openfire start|stop’
    ;;
    esac

##  Ubuntu管理开机启动服务项 -- 图形界面的Boot-up Manager

有时学习时安装的服务太多，比如mysql、mongodb、redis、apache、nginx等等，它们都是默认开机启动的，如果不想让它们开机启动，用到时再自己手工启动怎么办呢？

使用sysv-rc-conf确实是一个不错的选择，但在暂时不了解服务启动的层级细节，又只需要一次过全关掉的情况下，用sysv-rc-conf未免过于繁琐。

好在我们还有图形界面下的工具Boot-up Manager，即bum

    sudo apt-get install bum

安装之后以root身份运行，就可以直接对特定的服务设置是否开机启动或不启动，十分方便。

