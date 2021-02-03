# login to aws.

```console
% ssh -i ~/d/working/xlnx-deephi.pem -J xcoengvm229135 10.243.12.162
% ls
% exit
```

```console
# content of ~/.ssh/config
Host aws
     ProxyJump xcoengvm229135
     IdentityFile /mnt/c/Users/chunywan/AppData/Roaming/d/working/xlnx-deephi.pem
     User ubuntu
     HostName 10.243.12.162
```


# build from the open source repo


```console
% ssh aws
% sudo apt --fix-broken install
% sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com --verbose 5DE10266B40665E66D7301F660FC2865A39A32B2
% sudo add-apt-repository --enable-source ppa:alfonsosanchezbeato/arm64-vitis
% sudo apt build-dep -y vitis-ai
% apt source vitis-ai
% cd vitis-ai-1.3
% sudo apt-get install -y fakeroot
% sudo apt-get install -y pybind11-dev
% sudo apt-get install -y libpython3-dev
% dpkg-buildpackage -us -uc
```

# build from the private repo

```console
% sudo apt-get install -y emacs-gtk
% curl -sLo - https://github.com/wcy123/100ms_dot_emacs/releases/download/v1.0.14/100ms_dot_emacs.emacs.d.v1.0.14.tar.gz | tar -zxvf - -C ~/
% emacs -nw
```

```console
#  if the server is shutdown

% ssh xcoengvm229135
% /tools/batonroot/rodin/devkits/lnx64/aws/f1/aws-login.sh
% /tools/batonroot/rodin/devkits/lnx64/aws/f1/f1-instance.sh i-0386c279e375ce828 start


```

```console
% ssh -R:10020:xcdl190260:22 aws
% ssh-keygen
% # upload pub key to xcdl
% ssh -p 10020 -T gits@localhost
% # update .ssh/config
% cat ~/.ssh/config

Host xcdl190260
     User gits
     Port 10020
     HostName localhost

% ssh -T gits@xcdl190260
% git clone --depth 1 gits@xcdl190260:aisw/unilog
% git clone --depth 1 gits@xcdl190260:aisw/target_factory
% git clone --depth 1 gits@xcdl190260:aisw/xir
% git clone --depth 1 gits@xcdl190260:aisw/vart
```

# build unilog

``` console
% cd ~/unilog
% ./cmake.sh
% emacs -nw cmake.sh
% git remote add wcy gits@xcdl190260:wangchunye/unilog
% git checkout -b br-ubuntu-20.04 origin/dev
% git push -u wcy br-ubuntu-20.04
% emacs cmake.sh
% ./cmake.sh --pack=deb
```

# build  xir

```console
% # xir
% cd ~/xir
% sudo chmod o+w /usr/lib/python3/dist-packages/
% ./cmake.sh --build-python --pack=deb
```

# build target factory

```console
% # target_factory
% cd ~/target_factory
% ./cmake.sh --pack=deb
```

# build vart

``` console
% cd $HOME/vart
% ./cmake.sh --pack=deb --cmake-options=-DENABLE_DPU_RUNNER=ON --cmake-options=-DENABLE_SIM_RUNNER=OFF --cmake-options=-DENABLE_CPU_RUNNER=OFF --build-python
```

# build vitit-ai-library

```console
% git clone --depth 1 gits@xcdl190260:aisw/Vitis-AI-Library
% cd ~/Vitis-AI-Library
% ./cmake.sh --cmake-options='-DENABLE_OVERVIEW=ON -DBUILD_PYTHON=ON' --pack=deb
```


# copy them back

``` console
% for  i in /home/ubuntu/build/build.Ubuntu.20.04.aarch64.Debug/vart/libvart_1.3.1_arm64.deb \
            /home/ubuntu/build/build.Ubuntu.20.04.aarch64.Debug/target_factory/libtarget-factory_1.3.1_arm64.deb \
            /home/ubuntu/build/build.Ubuntu.20.04.aarch64.Debug/unilog/libunilog_1.3.1_arm64.deb \
            /home/ubuntu/build/build.Ubuntu.20.04.aarch64.Debug/Vitis-AI-Library/libvitis_ai_library_1.3.1_arm64.deb \
            /home/ubuntu/build/build.Ubuntu.20.04.aarch64.Debug/xir/libxir_1.3.1_arm64.deb; do \
        echo scp aws:$i /tmp/; \
done | sh;

% scp /tmp/*.deb xbjlabdpsvr16:/group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/xdock-vitis-ai-sw/workspace
```



# deploy it on board

``` console
% scp /workspace/*.deb b2:/tmp/
% ssh b2
```

``` console
% # vim /etc/apt/apt.conf.d/70debconf
% # to enable sock
% # Acquire::http::proxy "socks5h://10.176.178.16:10080";
% sudo apt-get install -y gnupg2
% sudo apt-get install -y tsocks
% # vim /etc/tsocks.conf
% /usr/bin/dirmngr & # gpg: no running Dirmngr - starting '/usr/bin/dirmngr'
% curl -sSL 'http://keyserver.ubuntu.com/pks/lookup?op=get&search=0x5DE10266B40665E66D7301F660FC2865A39A32B2' | apt-key add -
% apt-get install -y software-properties-common
% # add-apt-repository --enable-source ppa:alfonsosanchezbeato/arm64-vitis # failed, so I manually update the source list
# deb http://ppa.launchpad.net/alfonsosanchezbeato/arm64-vitis/ubuntu focal main
# deb-src http://ppa.launchpad.net/alfonsosanchezbeato/arm64-vitis/ubuntu focal main
% sudo apt build-dep -y vitis-ai
% for  i in libunilog_1.3.1_arm64.deb  libtarget-factory_1.3.1_arm64.deb libxir_1.3.1_arm64.deb libvart_1.3.1_arm64.deb libvitis_ai_library_1.3.1_arm64.deb; do dpkg -i /tmp/$i; done
% apt-get update --fix-missing
% apt-get install -y xrt-zocl-dkms
```

the xrt installation, I get some erros like below.

```
It is likely that 5.4.0-xilinx-v2020.2 belongs to a chroot's host
Building for 5.4.0-65-generic
This package appears to be a binaries-only package
 you will not be able to build against kernel 5.4.0-65-generic
  since the package source was not provided
  Finished DKMS common.postinst
  install: cannot stat '/usr/src/xrt-2.7.0/driver/zocl/10-zocl.rules': No such file or directory
  Loading new XRT Linux kernel modules
  modprobe: FATAL: Module zocl not found in directory /lib/modules/5.4.0-xilinx-v2020.2
  ****************************************************************
  * DKMS failed to install XRT drivers.
  * Please check if kernel development headers are installed for OS variant used.
  *
  * Check build logs in /var/lib/dkms/xrt/2.7.0
  ****************************************************************
  INFO: Creating ICD entry for Xilinx Platform
  Setting up linux-headers-generic (5.4.0.65.68) ...
  Processing triggers for libc-bin (2.31-0ubuntu9) ...
  Processing triggers for man-db (2.9.1-1) ...
```
