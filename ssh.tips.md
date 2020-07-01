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

```

## On Windows
