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
% cd ~/unilog
% ./cmake.sh
% emacs -nw cmake.sh
% git remote add wcy gits@xcdl190260:wangchunye/unilog
% git checkout -b br-ubuntu-20.04 origin/dev
% git push -u wcy br-ubuntu-20.04
% emacs cmake.sh
% # xir
% cd ~/xir
% sudo chmod o+w /usr/lib/python3/dist-packages/
% ./cmake.sh --build-python
% # target_factory
% cd ~/target_factory
% ./cmake.sh
% # vart
% ./cmake.sh --pack=deb --cmake-options=-DENABLE_DPU_RUNNER=ON --cmake-options=-DENABLE_SIM_RUNNER=OFF --cmake-options=-DENABLE_CPU_RUNNER=OFF  --clean --build-python
% cd $HOME
% git clone --depth 1 gits@xcdl190260:aisw/Vitis-AI-Library
% cd Vitis-AI-Library
% ./cmake.sh --cmake-options='-DENABLE_OVERVIEW=ON -DBUILD_PYTHON=ON'
```
