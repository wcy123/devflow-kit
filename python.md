# build python from source code


## download source code and extract

```console
% mkdir -p ~/build; cd ~/build; ls
% curl -Lo python-v3.9.0a5.tar.gz https://github.com/python/cpython/archive/v3.9.0a5.tar.gz
% tar -zxvf python-v3.9.0a5.tar.gz
```

## configure, build and install

```console
% source /opt/rh/devtoolset-9/enable # gcc4 has bug, cannot build python
% cd ~/build/cpython-3.9.0a5
% aclocal
% autoreconf
% ./configure --prefix=$HOME/.local --enable-optimizations && make -j30 && make install
%
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
% cd Python-3.8.3/
% aclocal
% autoreconf
% ./configure --prefix=$HOME/.local --enable-optimizations && make -j30 && make install
```
