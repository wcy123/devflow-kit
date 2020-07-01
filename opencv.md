# build opencv


## download opencv

``` console
% mkdir -p ~/build;cd ~/build/
% curl -Lo opencv-4.3.0.tar.gz https://github.com/opencv/opencv/archive/4.3.0.tar.gz
% curl -Lo opencv-3.4.3.tar.gz https://github.com/opencv/opencv/archive/3.4.3.tar.gz
% tar -zxf opencv-3.4.3.tar.gz
```


## prerequites

https://www.tecmint.com/enable-nux-dexktop-repository-on-rhel-centos/

for centos

``` console
% sudo rpm --import http://li.nux.ro/download/nux/RPM-GPG-KEY-nux.ro
% sudo yum -y install epel-release && sudo rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm
% sudo yum install -y ffmpeg-devel
```

for ubuntu


## configure build and install for your local dev environment

``` console
% cd ~/build/opencv-3.4.3
% mkdir build && cd build
% cat ../CMakeLists.txt | grep OPTION
% cmake -DCMAKE_INSTALL_PREFIX=$HOME/.local -DENABLE_PIC=on -DBUILD_SHARED_LIBS=on -DBUILD_TESTS=off -DBUILD_EXAMPLES=off -DBUILD_PERF_TESTS=off   ../
% make -j30 && make  install
```

## configure build and install for docker environment

``` console
% cd ~/build/opencv-3.4.3
% mkdir build && cd build
% cat ../CMakeLists.txt | grep OPTION
% cmake -DCMAKE_INSTALL_PREFIX=$HOME/.local -DENABLE_PIC=on -DBUILD_SHARED_LIBS=on -DBUILD_TESTS=off -DBUILD_EXAMPLES=off -DBUILD_PERF_TESTS=off   ../
% make -j30 && make  install
```
