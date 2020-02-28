## start development dev


### download source code

```
gitlab=xcdl192026
#gitlab=localhost:10260
mkdir -p $HOME/d/working/aisw/
cd  $HOME/d/working/aisw/
git clone ssh://gits@$gitlab/aisw/unilog
git clone ssh://gits@$gitlab/aisw/xir
git clone ssh://gits@$gitlab/aisw/vart
git clone ssh://gits@$gitlab/3rd-party/pybind11
```

### install pybind11

```
# you have to install python3-dev  as below
# sudo apt-get install -y python3-dev
cd $HOME/d/working/aisw/pybind11
mkdir build;cd build;
cmake -DCMAKE_INSTALL_PREFIX=$HOME/.local -DPYBIND11_TEST=off -DPYBIND11_INSTALL=on ..
```
### build unilog

```
cd $HOME/d/working/aisw/unilog
./cmake.sh --pack=deb
dpkg -c $HOME/build/build.CentOS.7.6.1810.x86_64.Debug/unilog/libunilog-0.0.1-Linux.deb
```

### build xir

```
cd $HOME/d/working/aisw/xir
./cmake.sh --pack=deb --build-python  # no need to --build-python if you don't build xcompiler
dpkg -c $HOME/build/build.CentOS.7.6.1810.x86_64.Debug/xir/libxir-0.0.1-Linux.deb
```

### build vart

```
cd $HOME/d/working/aisw/vart
./cmake.sh --pack=deb --build-python

```

ls
