% ssh用法及命令
<h6>2017-07-21</h6>

 http://blog.csdn.net/pipisorry/article/details/52269785

## 什么是SSH？

简单说，SSH是一种网络协议，用于计算机之间的加密登录。如果一个用户从本地计算机，使用SSH协议登录另一台远程计算机，我们就可以认为，这种登录是安全的，即使被中途截获，密码也不会泄露。最早的时候，互联网通信都是明文通信，一旦被截获，内容就暴露无疑。1995年，芬兰学者Tatu Ylonen设计了SSH协议，将登录信息全部加密，成为互联网安全的一个基本解决方案，迅速在全世界获得推广，目前已经成为Linux系统的标准配置。

SSH只是一种协议，存在多种实现，既有商业实现，也有开源实现。本文针对的实现是OpenSSH，它是自由软件，应用非常广泛。这里只讨论SSH在Linux Shell中的用法。如果要在Windows系统中使用SSH，会用到另一种软件PuTTY，这需要另文介绍。

## 中间人攻击

SSH之所以能够保证安全，原因在于它采用了公钥加密。

整个过程是这样的：（1）远程主机收到用户的登录请求，把自己的公钥发给用户。（2）用户使用这个公钥，将登录密码加密后，发送回来。（3）远程主机用自己的私钥，解密登录密码，如果密码正确，就同意用户登录。

这个过程本身是安全的，但是实施的时候存在一个风险：如果有人截获了登录请求，然后冒充远程主机，将伪造的公钥发给用户，那么用户很难辨别真伪。因为不像https协议，SSH协议的公钥是没有证书中心（CA）公证的，也就是说，都是自己签发的。

可以设想，如果攻击者插在用户与远程主机之间（比如在公共的wifi区域），用伪造的公钥，获取用户的登录密码。再用这个密码登录远程主机，那么SSH的安全机制就荡然无存了。这种风险就是著名的"中间人攻击"（Man-in-the-middle attack）。

## ssh的安装

### SSH分客户端openssh-client和openssh-server

如果你只是想登陆别的机器的SSH只需要安装openssh-client（ubuntu有默认安装，如果没有则sudoapt-get install openssh-client），如果要使本机开放SSH服务就需要安装openssh-server。

Ubuntu缺省已经安装了ssh client。

#配置ssh#

    echo -e "\033[31;1m ******************************* \033[0m"
    echo -e "\033[31;1m ************安装和配置ssh************ \033[0m"
    sudo apt-get install -y openssh-server 1> /dev/null
    sudo sed -i 's/UsePAM no/UsePAM yes/g' /etc/ssh/sshd_config
    sudo sed -i '8a /etc/init.d/ssh start' /etc/profile
    sudo /etc/init.d/ssh start
    ps -e | grep ssh

    echo -e "\033[31;1m ssh授权 \033[0m"
    cd ~/.ssh/
    ssh-keygen -t rsa
    cat ./id_rsa.pub >> ./authorized_keys

    $ ps -e|grep ssh
    2151 ?        00:00:00 ssh-agent

    5313 ?        00:00:00 sshd

ssh-agent表示ssh-client启动，sshd表示ssh-server启动了。

如果缺少sshd，说明ssh服务没有启动或者没有安装。

## SSH基本用法

### SSH远程登录

#### 口令登录

假定你要以用户名user，登录远程主机host，只要一条简单命令就可以了。

    　　$ ssh user@host  如：ssh pika@192.168.0.111

如果本地用户名与远程用户名一致，登录时可以省略用户名。

    　　$ ssh host

SSH的默认端口是22，也就是说，你的登录请求会送进远程主机的22端口。使用p参数，可以修改这个端口。

    　　$ ssh -p 2222 user@host

上面这条命令表示，ssh直接连接远程主机的2222端口。

如果你是第一次登录对方主机，系统会出现下面的提示：

    　　$ ssh user@host
    　　The authenticity of host 'host (12.18.429.21)' can't be established.
    　　RSA key fingerprint is 98:2e:d7:e0:de:9f:ac:67:28:c2:42:2d:37:16:58:4d.
    　　Are you sure you want to continue connecting (yes/no)?

这段话的意思是，无法确认host主机的真实性，只知道它的公钥指纹，问你还想继续连接吗？

所谓"公钥指纹"，是指公钥长度较长（这里采用RSA算法，长达1024位），很难比对，所以对其进行MD5计算，将它变成一个128位的指纹。上例中是98:2e:d7:e0:de:9f:ac:67:28:c2:42:2d:37:16:58:4d，再进行比较，就容易多了。

很自然的一个问题就是，用户怎么知道远程主机的公钥指纹应该是多少？回答是没有好办法，远程主机必须在自己的网站上贴出公钥指纹，以便用户自行核对。

假定经过风险衡量以后，用户决定接受这个远程主机的公钥。

    　　Are you sure you want to continue connecting (yes/no)? yes

系统会出现一句提示，表示host主机已经得到认可。

    　　Warning: Permanently added 'host,12.18.429.21' (RSA) to the list of known hosts.

然后，会要求输入密码。

    　　Password: (enter password)

如果密码正确，就可以登录了。

当远程主机的公钥被接受以后，它就会被保存在文件$HOME/.ssh/known_hosts之中。下次再连接这台主机，系统就会认出它的公钥已经保存在本地了，从而跳过警告部分，直接提示输入密码。

每个SSH用户都有自己的known_hosts文件，此外系统也有一个这样的文件，通常是/etc/ssh/ssh_known_hosts，保存一些对所有用户都可信赖的远程主机的公钥。

#### 公钥登录

使用密码登录，每次都必须输入密码，非常麻烦。好在SSH还提供了公钥登录，可以省去输入密码的步骤。

所谓"公钥登录"，原理很简单，就是用户将自己的公钥储存在远程主机上。登录的时候，远程主机会向用户发送一段随机字符串，用户用自己的私钥加密后，再发回来。远程主机用事先储存的公钥进行解密，如果成功，就证明用户是可信的，直接允许登录shell，不再要求密码。

这种方法要求用户必须提供自己的公钥。如果没有现成的，可以直接用ssh-keygen生成一个：

    　　$ ssh-keygen

运行上面的命令以后，系统会出现一系列提示，可以一路回车。其中有一个问题是，要不要对私钥设置口令（passphrase），如果担心私钥的安全，这里可以设置一个。

运行结束以后，在$HOME/.ssh/目录下，会新生成两个文件：id_rsa.pub和id_rsa。前者是你的公钥，后者是你的私钥。

这时再输入下面的命令，将公钥传送到远程主机host上面：

    　　$ ssh-copy-id user@host

好了，从此你再登录，就不需要输入密码了。

如果还是不行，就打开远程主机的/etc/ssh/sshd_config这个文件，检查下面几行前面"#"注释是否取掉。

    　　RSAAuthentication yes
    　　PubkeyAuthentication yes
    　　AuthorizedKeysFile .ssh/authorized_keys

然后，重启远程主机的ssh服务。

    　　// ubuntu系统
    　　service ssh restart
    　　// debian系统
    　　/etc/init.d/ssh restart

authorized_keys文件

远程主机将用户的公钥，保存在登录后的用户主目录的$HOME/.ssh/authorized_keys文件中。公钥就是一段字符串，只要把它追加在authorized_keys文件的末尾就行了。

这里不使用上面的ssh-copy-id命令，改用下面的命令，解释公钥的保存过程：

    　　$ ssh user@host 'mkdir -p .ssh && cat >> .ssh/authorized_keys' < ~/.ssh/id_rsa.pub

这条命令由多个语句组成，依次分解开来看：（1）"$ ssh user@host"，表示登录远程主机；（2）单引号中的mkdir .ssh && cat >> .ssh/authorized_keys，表示登录后在远程shell上执行的命令：（3）"$ mkdir -p .ssh"的作用是，如果用户主目录中的.ssh目录不存在，就创建一个；（4）'cat >> .ssh/authorized_keys' < ~/.ssh/id_rsa.pub的作用是，将本地的公钥文件~/.ssh/id_rsa.pub，重定向追加到远程文件authorized_keys的末尾。

写入authorized_keys文件后，公钥登录的设置就完成了。

[SSH原理与运用（一）：远程登录](http://www.ruanyifeng.com/blog/2011/12/ssh_remote_login.html)

使用ssh在远程后台不中断地跑程序

Linux关闭ssh（关闭终端等）后运行的程序或者服务自动停止，如python3 a.py &。

解决：使用nohup命令让程序在关闭窗口（切换SSH连接）的时候程序还能继续在后台运行。

    nohup python3 a.py &

### SSH远程操作

#### SSH数据传输

SSH不仅可以用于远程主机登录，还可以直接在远程主机上执行操作。

    　　$ ssh user@host 'mkdir -p .ssh && cat >> .ssh/authorized_keys' < ~/.ssh/id_rsa.pub

单引号中间的部分，表示在远程主机上执行的操作；后面的输入重定向，表示数据通过SSH传向远程主机。

这就是说，SSH可以在用户和远程主机之间，建立命令和数据的传输通道，因此很多事情都可以通过SSH来完成。

下面看几个例子。

【例1】

将$HOME/src/目录下面的所有文件，复制到远程主机的$HOME/src/目录。

    　　$ cd && tar czv src | ssh user@host 'tar xz'

【例2】

将远程主机$HOME/src/目录下面的所有文件，复制到用户的当前目录。

    　　$ ssh user@host 'tar cz src' | tar xzv

【例3】

查看远程主机是否运行进程httpd。

    　　$ ssh user@host 'ps ax | grep [h]ttpd'

lz建议使用scp进行远程copy：

#### scp 跨机远程拷贝

scp是secure copy的简写，用于在Linux下进行远程拷贝文件的命令，和它类似的命令有cp，不过cp只是在本机进行拷贝不能跨服务器，而且scp传输是加密的。可能会稍微影响一下速度。两台主机之间复制文件必需得同时有两台主机的复制执行帐号和操作权限。

scp命令参数

    -1 强制scp命令使用协议ssh1
    -2 强制scp命令使用协议ssh2
    -4 强制scp命令只使用IPv4寻址
    -6 强制scp命令只使用IPv6寻址
    -B 使用批处理模式（传输过程中不询问传输口令或短语）
    -C 允许压缩。（将-C标志传递给ssh，从而打开压缩功能）
    -p 留原文件的修改时间，访问时间和访问权限。
    -q 不显示传输进度条。
    -r 递归复制整个目录。
    -v 详细方式显示输出。scp和ssh(1)会显示出整个过程的调试信息。这些信息用于调试连接，验证和配置问题。
    -c cipher 以cipher将数据传输进行加密，这个选项将直接传递给ssh。
    -F ssh_config 指定一个替代的ssh配置文件，此参数直接传递给ssh。
    -i identity_file 从指定文件中读取传输时使用的密钥文件，此参数直接传递给ssh。
    -l limit 限定用户所能使用的带宽，以Kbit/s为单位。
    -o ssh_option 如果习惯于使用ssh_config(5)中的参数传递方式，
    -P port 注意是大写的P, port是指定数据传输用到的端口号
    -S program 指定加密传输时所使用的程序。此程序必须能够理解ssh(1)的选项。

#### scp一般有六种使用方法

本地复制远程文件：（把远程的文件复制到本地）

    scp root@www.test.com:/val/test/test.tar.gz /val/test/test.tar.gz

远程复制本地文件：（把本地的文件复制到远程主机上）

    scp /val/test.tar.gz root@www.test.com:/val/test.tar.gz

本地复制远程目录：（把远程的目录复制到本地）

    scp -r root@www.test.com:/val/test/ /val/test/

远程复制本地目录：（把本地的目录复制到远程主机上）

    scp -r ./ubuntu_env/ root@192.168.0.111:/home/pipi

    pika:/media/pika/files/machine_learning/datasets$scp -r SocialNetworks/ piting@192.168.0.172:/media/data/pipi/datasets

本地复制远程文件到指定目录：（把远程的文件复制到本地）

    scp root@www.test.com:/val/test/test.tar.gz /val/test/

远程复制本地文件到指定目录：（把本地的文件复制到远程主机上）

      scp /val/test.tar.gz root@www.test.com:/val/

ps: scp复制文件时只指定服务器地址不加路径默认复制到哪里???

 [12个scp传输文件的命令栗子](http://www.cnblogs.com/voidy/p/4215891.html)

 [scp 跨机远程拷贝](http://linuxtools-rst.readthedocs.io/zh_CN/latest/tool/scp.html)

#### 绑定本地端口

既然SSH可以传送数据，那么我们可以让那些不加密的网络连接，全部改走SSH连接，从而提高安全性。

假定我们要让8080端口的数据，都通过SSH传向远程主机，命令就这样写：

    　　$ ssh -D 8080 user@host

SSH会建立一个socket，去监听本地的8080端口。一旦有数据传向那个端口，就自动把它转移到SSH连接上面，发往远程主机。可以想象，如果8080端口原来是一个不加密端口，现在将变成一个加密端口。

#### 本地端口转发

有时，绑定本地端口还不够，还必须指定数据传送的目标主机，从而形成点对点的"端口转发"。为了区别后文的"远程端口转发"，我们把这种情况称为"本地端口转发"（Local forwarding）。

假定host1是本地主机，host2是远程主机。由于种种原因，这两台主机之间无法连通。但是，另外还有一台host3，可以同时连通前面两台主机。因此，很自然的想法就是，通过host3，将host1连上host2。

我们在host1执行下面的命令：

    　　$ ssh -L 2121:host2:21 host3

命令中的L参数一共接受三个值，分别是"本地端口:目标主机:目标主机端口"，它们之间用冒号分隔。这条命令的意思，就是指定SSH绑定本地端口2121，然后指定host3将所有的数据，转发到目标主机host2的21端口（假定host2运行FTP，默认端口为21）。
这样一来，我们只要连接host1的2121端口，就等于连上了host2的21端口。

    　　$ ftp localhost:2121

"本地端口转发"使得host1和host3之间仿佛形成一个数据传输的秘密隧道，因此又被称为"SSH隧道"。

下面是一个比较有趣的例子。

    　　$ ssh -L 5900:localhost:5900 host3

它表示将本机的5900端口绑定host3的5900端口（这里的localhost指的是host3，因为目标主机是相对host3而言的）。
另一个例子是通过host3的端口转发，ssh登录host2。

    　　$ ssh -L 9001:host2:22 host3

这时，只要ssh登录本机的9001端口，就相当于登录host2了。

    　　$ ssh -p 9001 localhost

上面的-p参数表示指定登录端口。

#### 远程端口转发

既然"本地端口转发"是指绑定本地端口的转发，那么"远程端口转发"（remote forwarding）当然是指绑定远程端口的转发。

还是接着看上面那个例子，host1与host2之间无法连通，必须借助host3转发。但是，特殊情况出现了，host3是一台内网机器，它可以连接外网的host1，但是反过来就不行，外网的host1连不上内网的host3。这时，"本地端口转发"就不能用了，怎么办？

解决办法是，既然host3可以连host1，那么就从host3上建立与host1的SSH连接，然后在host1上使用这条连接就可以了。

我们在host3执行下面的命令：

    　　$ ssh -R 2121:host2:21 host1

R参数也是接受三个值，分别是"远程主机端口:目标主机:目标主机端口"。这条命令的意思，就是让host1监听它自己的2121端口，然后将所有数据经由host3，转发到host2的21端口。由于对于host3来说，host1是远程主机，所以这种情况就被称为"远程端口绑定"。
绑定之后，我们在host1就可以连接host2了：

    　　$ ftp localhost:2121

这里必须指出，"远程端口转发"的前提条件是，host1和host3两台主机都有sshD和ssh客户端。

#### SSH的其他参数

SSH还有一些别的参数，也值得介绍。

N参数，表示只连接远程主机，不打开远程shell；T参数，表示不为这个连接分配TTY。这个两个参数可以放在一起用，代表这个SSH连接只用来传数据，不执行远程操作。

    　　$ ssh -NT -D 8080 host

f参数，表示SSH连接成功后，转入后台运行。这样一来，你就可以在不中断SSH连接的情况下，在本地shell中执行其他操作。

    　　$ ssh -f -D 8080 host

要关闭这个后台连接，就只有用kill命令去杀掉进程。

[SSH原理与运用（二）：远程操作与端口转发]

from: http://blog.csdn.net/pipisorry/article/details/52269785

 [Ubuntu环境下SSH的安装及使用](http://blog.csdn.net/netwalk/article/details/12952051)

[25个必须记住的SSH命令](http://www.cnblogs.com/weafer/archive/2011/06/10/2077852.html)

[Linux 下 SSH 命令实例指南](https://linux.cn/article-3858-1.html)

[数字签名是什么？](http://www.ruanyifeng.com/blog/2011/08/what_is_a_digital_signature.html)

      [　　* SSH, The Secure Shell: The Definitive Guide: 2.4. Authentication by Cryptographic Key, O'reilly

	* SSH, The Secure Shell: The Definitive Guide: 9.2. Port Forwarding, O'reilly

	* Shebang: Tips for Remote Unix Work (SSH, screen, and VNC)

	* brihatch: SSH Host Key Protection

	* brihatch: SSH User Identities

	* IBM developerWorks: 实战 SSH 端口转发

	* Jianing YANG：ssh隧道技术简介

	* WikiBooks: Internet Technologies/SSH

	* Buddhika Chamith: SSH Tunneling Explained
      ]

## 25个必须记住的SSH命令

OpenSSH是SSH连接工具的免费版本。telnet，rlogin和ftp用户可能还没意识到他们在互联网上传输的密码是未加密的，但SSH是加密的，OpenSSH加密所有通信（包括密码），有效消除了窃听，连接劫持和其它攻击。此外，OpenSSH提供了安全隧道功能和多种身份验证方法，支持SSH协议的所有版本。

SSH是一个非常伟大的工具，如果你要在互联网上远程连接到服务器，那么SSH无疑是最佳的候选。下面是通过网络投票选出的25个最佳SSH命令，你必须牢记于心。

（注：有些内容较长的命令，在本文中会显示为截断的状态。如果你需要阅读完整的命令，可以把整行复制到您的记事本当中阅读。）

1、复制SSH密钥到目标主机，开启无密码SSH登录

    ssh-copy-id user@host

如果还没有密钥，请使用ssh-keygen命令生成。

2、从某主机的80端口开启到本地主机2001端口的隧道

    ssh -N -L2001:localhost:80 somemachine

现在你可以直接在浏览器中输入http://localhost:2001访问这个网站。

3、将你的麦克风输出到远程计算机的扬声器

    dd if=/dev/dsp | ssh -c arcfour -C username@host dd of=/dev/dsp

这样来自你麦克风端口的声音将在SSH目标计算机的扬声器端口输出，但遗憾的是，声音质量很差，你会听到很多嘶嘶声。

4、比较远程和本地文件

    ssh user@host cat /path/to/remotefile | diff /path/to/localfile –

在比较本地文件和远程文件是否有差异时这个命令很管用。

5、通过SSH挂载目录/文件系统

    sshfs name@server:/path/to/folder /path/to/mount/point

从http://fuse.sourceforge.net/sshfs.html下载sshfs，它允许你跨网络安全挂载一个目录。

6、通过中间主机建立SSH连接

    ssh -t reachable_host ssh unreachable_host

Unreachable_host表示从本地网络无法直接访问的主机，但可以从reachable_host所在网络访问，这个命令通过到reachable_host的“隐藏”连接，创建起到unreachable_host的连接。

7、将你的SSH公钥复制到远程主机，开启无密码登录 – 简单的方法

    ssh-copy-id username@hostname

8、直接连接到只能通过主机B连接的主机A

    ssh -t hostA ssh hostB		

当然，你要能访问主机A才行。

9、创建到目标主机的持久化连接

    ssh -MNf <user>@<host>

在后台创建到目标主机的持久化连接，将这个命令和你~/.ssh/config中的配置结合使用：

    Host host
    ControlPath ~/.ssh/master-%r@%h:%p
    ControlMaster no

所有到目标主机的SSH连接都将使用持久化SSH套接字，如果你使用SSH定期同步文件（使用rsync/sftp/cvs/svn），这个命令将非常有用，因为每次打开一个SSH连接时不会创建新的套接字。

10、通过SSH连接屏幕

    ssh -t remote_host screen –r

直接连接到远程屏幕会话（节省了无用的父bash进程）。

11、端口检测（敲门）

    knock <host> 3000 4000 5000 && ssh -p <port> user@host && knock <host> 5000 4000 3000

在一个端口上敲一下打开某个服务的端口（如SSH），再敲一下关闭该端口，需要先安装knockd，下面是一个配置文件示例。

    [options]
    logfile = /var/log/knockd.log
    [openSSH]
    sequence = 3000,4000,5000
    seq_timeout = 5
    command = /sbin/iptables -A INPUT -i eth0 -s %IP% -p tcp –dport 22 -j ACCEPT
    tcpflags = syn
    [closeSSH]
    sequence = 5000,4000,3000
    seq_timeout = 5
    command = /sbin/iptables -D INPUT -i eth0 -s %IP% -p tcp –dport 22 -j ACCEPT
    tcpflags = syn

12、删除文本文件中的一行内容，有用的修复

    ssh-keygen -R <the_offending_host>

在这种情况下，最好使用专业的工具。

13、通过SSH运行复杂的远程shell命令

    ssh host -l user $(<cmd.txt)

更具移植性的版本：

    ssh host -l user “`cat cmd.txt`”

14、通过SSH将MySQL数据库复制到新服务器

    mysqldump –add-drop-table –extended-insert –force –log-error=error.log -uUSER -pPASS OLD_DB_NAME | ssh -C user@newhost “mysql -uUSER -pPASS NEW_DB_NAME”

通过压缩的SSH隧道Dump一个MySQL数据库，将其作为输入传递给mysql命令，我认为这是迁移数据库到新服务器最快最好的方法。

15、删除文本文件中的一行，修复“SSH主机密钥更改”的警告

    sed -i 8d ~/.ssh/known_hosts

16、从一台没有SSH-COPY-ID命令的主机将你的SSH公钥复制到服务器

    cat ~/.ssh/id_rsa.pub | ssh user@machine “mkdir ~/.ssh; cat >> ~/.ssh/authorized_keys”

如果你使用Mac OS X或其它没有ssh-copy-id命令的*nix变种，这个命令可以将你的公钥复制到远程主机，因此你照样可以实现无密码SSH登录。

17、实时SSH网络吞吐量测试

    yes | pv | ssh $host “cat > /dev/null”

通过SSH连接到主机，显示实时的传输速度，将所有传输数据指向/dev/null，需要先安装pv。

如果是Debian：

    apt-get install pv

如果是Fedora：

    yum install pv

（可能需要启用额外的软件仓库）。

18、如果建立一个可以重新连接的远程GNU screen

    ssh -t user@some.domain.com /usr/bin/screen –xRR

人们总是喜欢在一个文本终端中打开许多shell，如果会话突然中断，或你按下了“Ctrl-a d”，远程主机上的shell不会受到丝毫影响，你可以重新连接，其它有用的screen命令有“Ctrl-a c”（打开新的shell）和“Ctrl-a a”（在shell之间来回切换），请访问http://aperiodic.net/screen/quick_reference阅读更多关于screen命令的快速参考。

19、继续SCP大文件

    rsync –partial –progress –rsh=ssh $file_source $user@$host:$destination_file

它可以恢复失败的rsync命令，当你通过VPN传输大文件，如备份的数据库时这个命令非常有用，需要在两边的主机上安装rsync。

    rsync –partial –progress –rsh=ssh $file_source $user@$host:$destination_file local -> remote

或

    rsync –partial –progress –rsh=ssh $user@$host:$remote_file $destination_file remote -> local

20、通过SSH W/ WIRESHARK分析流量

    ssh root@server.com ‘tshark -f “port !22″ -w -' | wireshark -k -i –

使用tshark捕捉远程主机上的网络通信，通过SSH连接发送原始pcap数据，并在wireshark中显示，按下Ctrl+C将停止捕捉，但也会关闭wireshark窗口，可以传递一个“-c #”参数给tshark，让它只捕捉“#”指定的数据包类型，或通过命名管道重定向数据，而不是直接通过SSH传输给wireshark，我建议你过滤数据包，以节约带宽，tshark可以使用tcpdump替代：

    ssh root@example.com tcpdump -w – ‘port !22′ | wireshark -k -i –

21、保持SSH会话永久打开

    autossh -M50000 -t server.example.com ‘screen -raAd mysession’

打开一个SSH会话后，让其保持永久打开，对于使用笔记本电脑的用户，如果需要在Wi-Fi热点之间切换，可以保证切换后不会丢失连接。

22、更稳定，更快，更强的SSH客户端

    ssh -4 -C -c blowfish-cbc

强制使用IPv4，压缩数据流，使用Blowfish加密。

23、使用cstream控制带宽

    tar -cj /backup | cstream -t 777k | ssh host ‘tar -xj -C /backup’

使用bzip压缩文件夹，然后以777k bit/s速率向远程主机传输。Cstream还有更多的功能，请访问http://www.cons.org/cracauer/cstream.html#usage了解详情，例如：

    echo w00t, i’m 733+ | cstream -b1 -t2

24、一步将SSH公钥传输到另一台机器

    ssh-keygen; ssh-copy-id user@host; ssh user@host

这个命令组合允许你无密码SSH登录，注意，如果在本地机器的~/.ssh目录下已经有一个SSH密钥对，ssh-keygen命令生成的新密钥可能会覆盖它们，ssh-copy-id将密钥复制到远程主机，并追加到远程账号的~/.ssh/authorized_keys文件中，使用SSH连接时，如果你没有使用密钥口令，调用ssh user@host后不久就会显示远程shell。

25、将标准输入（stdin）复制到你的X11缓冲区

    ssh user@host cat /path/to/some/file | xclip

你是否使用scp将文件复制到工作用电脑上，以便复制其内容到电子邮件中？xclip可以帮到你，它可以将标准输入复制到X11缓冲区，你需要做的就是点击鼠标中键粘贴缓冲区中的内容。

