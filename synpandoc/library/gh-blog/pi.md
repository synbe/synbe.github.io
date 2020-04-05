% 树莓派LCD和HDMI相互切换
<h6> 不要使用没有电源供电的HDMI转VGA线！</h6>

##  LCD 3.5驱动：

把树莓派驱动3.5inch RPi LCD (A) ，复制到/boot目录下， 执行以下操作：

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

##  显示管理器（Display Manager）

* **slim**：SLiM 是一个独立的图形化X11登录管理器.它目标在于提供一个轻型、简洁但是可完全配置主题和文件的登录窗口管理器。可以替代GDM。它原本搭载在LXDE/openbox桌面环境上。
* **lightdm**：LightDM（Light Display Manager）是一个全新的轻量级 Linux 桌面显示管理器，而传统的 Ubuntu 是使用 GNOME 桌面标准的 GDM。LightDM 是一个跨桌面显示管理器，其目的是成为 X org 的 X Server 的标准显示管理器。是2010 年开始的新项目，且被设计为轻量、小巧、快速。相较于 GDM-GTK， KDM-Qt，LightDM 实际上与界面无关，它仅支持本地图形界面获得最好兼容性
* **kdm**
* **gdm**

几个设置文件：

	/etc/inittab
	/etc/init/slim.conf
	/etc/lightdm/lightdm.conf
	~/.xinitrc

##  start lightdm

Enter console mode by press Ctrl-Alt-F3 (F2~F8 is also good), and login. Do NOT try to change display manager in GUI, as the behavior is unpredictable.

    sudo systemctl disable gdm
    sudo systemctl enable lightdm
    Stop gdm with sudo systemctl stop gdm
    Start lightdm with sudo systemctl start lightdm

##  中文支持

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

##  startx

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

##  windows下 通过SSH使用树莓派 

1. 打开树莓派，设置开启ssh 和 vnc。

2. 在window下载安装putty后，打开，只需输入树莓派的IP地址，默认端口号22，默认选择SSH,点击Open

3. 字符界面输入用户名和密码（一般用户名为Pi，密码raspberry），至此在Windows的PC端通过SSH连接到了树莓派。

##  windows下 用VNC图形界面远程控制树莓派

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

   	运行填写Remote Host:192.168.11.7:1（使用:ifconfig命令）点击connect，输入之前设置好的vcn密码，点击ok。

4. **注意事项**

   * 一定要在PC端vnc-viewer运行之前，在树莓派用tightvncserver启动服务。否则提示远端计算机积极拒绝
   * PC端vnc-viewer软件填写ip地址比如192.168.1.1:1后面的英文冒号和1一定不要忘记！

