# ssh tips


## 配置 Proxy

编辑 `~/.ssh/config` 添加


``` config
Host xcdl1902*
     ProxyJump  xcdl190074
     StrictHostKeyChecking no
     UserKnownHostsFile /dev/null
```

这样，就可以直接使用 `ssh xcdl190253` 。 在笔记本上，安装 WSL 后，我们
使用起来就很方便，类似 linux 。windows 自带的 OpenSSH 可能类似，但是配
置文件的位置可能有些不同。可能不支持 `ProxyJump` 的选项。


## 打洞

首先理解基本的打洞原理。

1. 从机器 A 上运行命令 `ssh -Lx.x.x.x:p1:y.y.y.y.y:p2 B`，那么就会从 A
   登陆到 B 上，与此同时，在 A 上建立一个监听端口 `p1` ，监听地址
   `x.x.x.x` （一般是 0.0.0.0 ）。任何人建立 tcp 连接 A 的 x.x.x.x:p1 的时
   候，就相当于在 B 上建立一个 TCP 连接到 y.y.y.y:p2

1. 从机器 A 上运行命令 `ssh -Rx.x.x.x:p1:y.y.y.y.y:p2 B`，那么就会从 A
   登陆到 B 上，与此同时，在 B 上建立一个监听端口 `p1` ，监听地址
   `x.x.x.x` （一般是 0.0.0.0 ）。任何人建立 tcp 连接 B 的 x.x.x.x:p1
   端口时候，就相当于在 B 上建立一个 TCP 连接到 y.y.y.y:p2


实例， 在跳板机上，

``` consle
% ssh xbjjmphost01
% ssh -L0.0.0.0:10216:xbjlabdpsvr16:22 -L0.0.0.0:18216:xbjlabdpsvr16:8888 -R0.0.0.0:10074:xcdl190074:22 -R0.0.0.0:10152:xsjsda153:22 -R0.0.0.0:10142:xcosda142:22 -R0.0.0.0:10261:gitenterprise.xilinx.com:22 -oStrictHostKeyChecking=no -oUserKnownHostsFile=/dev/null -oStreamLocalBindUnlink=yes xbjlabdpsvr16
```

然后配合上面的例子，在 `xbjlabdpsvr16` 上 `~/.ssh/config`

```
Host github.com
     ProxyJump localhost:10152

Host xsjsda153
     HostName localhost
     Port 10152

Host xcosda142
     HostName localhost
     Port 10142

Host xcdl190*
     ProxyJump localhost:10074


Host gitenterprise.xilinx.com
     HostName 127.0.0.1
     Port 10261

Host 10.*.*.*
     StrictHostKeyChecking no
     UserKnownHostsFile /dev/null
```

这样，在  `xbjlabdpsvr16` ，你就可以正常的使用下面的命令访问源代码了。

``` console
xbjlabdpsvr16% git clone gits@xcdl190260:aisw/vart
xbjlabdpsvr16% git clone git@github.com:Xilinx/XRT
xbjlabdpsvr16% git clone git@gitenterprise.xilinx.com:aisw/vart
```

启动应用程序代理。

在 `xbjlabdpsvr16` 上，因为上面的打洞，我们可以反向访问 `xsjsda153` ，这个机器有 internet 的访问。

``` console
xbjlabdpsvr16% ssh -D 10080 -p 10152 localhost
xsjsda153:~%
```

建立这个连接之后，在其他终端上，我们就可以访问网络了

```
xbjlabdpsvr16% export ALL_PROXY=socks5h://localhost:10080
xbjlabdpsvr16% curl -v www.google.com
```

不仅仅  curl 很多程序都是可以识别 `ALL_PROXY` 这个环境变量，例如 `pip`, `cargo`, `yum` 等等。

注意，上面打洞的端口是唯一，大家最好使用自己的端口，防止端口冲突。
