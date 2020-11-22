# build python from source code

## build `libffi` from source code

if you don't have root

``` console
% cd $HOME/build
% curl -Lo libffi-3.3.tar.gz ftp://sourceware.org/pub/libffi/libffi-3.3.tar.gz
% tar -xvf libffi-3.3.tar.gz
% cd libffi-3.3/
% ./configure --prefix=$HOME/.local
% make -j10 && make install
```

## download source code and extract

```console
% vim ~/tmp/a.txt
% mkdir -p ~/build; cd ~/build; ls
% curl -Lo python-v3.9.0a5.tar.gz https://github.com/python/cpython/archive/v3.9.0a5.tar.gz
% tar -zxvf python-v3.9.0a5.tar.gz
% # NO NO, cmake does not support python 3.9, use python 3.8 insteadd
% curl -Lo Python-3.8.3.tgz  https://www.python.org/ftp/python/3.8.3/Python-3.8.3.tgz
% tar xvf Python-3.8.3.tgz
```

## configure, build and install


```console
%
% alias sudo=/tools/xgs/bin/sudo # need in xilinx env
% sudo yum install -y libffi-devel libsqlite3x-devel openssl-devel zlib-devel # for Centos , libgdbm-devel not found
% # sudo apt-get install -y libffi-dev libgdbm-dev libsqlite3-dev libssl-dev zlib1g-dev # for ubuntu
% # NO NO, cmake does not support python 3.9, use python 3.8 insteadd
% cd ~/build/Python-3.8.3
% aclocal
% autoreconf
% env PKG_CONFIG_PATH=$HOME/.local/lib/pkgconfig ./configure --prefix=$HOME/.local  CXX=`which g++` --disable-static --enable-shared --enable-optimizations
% grep LIBFFI_INCLUDEDIR Makefile
% make -j30 && make install
% ./python -c 'import _ctypes'
% # it does not work, we still need to install libffi-dev
```

```
generate-posix-vars failed
https://bugs.python.org/issue34112
Updating gcc to 8.1.0 fixed the problem. or #no  --enable-optimizations
```

## update pip to use sock

Notes: we should install `libffi-dev` before configuring python, otherwise,
we get error as below when building pysock

```
ModuleNotFoundError: No module named '_ctypes'
```

```console
% cd $HOME/build
% curl -Lo PySocks.1.7.0.tar.gz https://github.com/Anorov/PySocks/archive/1.7.0.tar.gz
% rm -fr PySocks-1.7.0/
% tar xvf PySocks.1.7.0.tar.gz
% cd PySocks-1.7.0/
% $HOME/.local/bin/python3 setup.py install
```

## install upgrade pip

```console
% pip3 install --upgrade --user pip
```

## install a pip package

```console
% pip3 install cmake-format
```

## on xcdsda29

cmake version is 3.16, too low, cannot find python3.9, but 3.8 is needed.
``` console
% scp chunywan@localhost:build/Python-3.8.3.tgz ~/build/
% tar xvf Python-3.8.3.tgz
% source /opt/rh/devtoolset-9/enable # gcc4 has bug, cannot build python
% cd ~/build/Python-3.8.3/
% aclocal
% autoreconf
% ./configure --prefix=$HOME/.local --enable-optimizations && make -j30 && make install
```

## create a virtual env

``` console
% pip3 install virtualenvl;
% python3 -m venv ~/.virtualenvs/base
% rm -fr tutorial-env
```
