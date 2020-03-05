# build glog v0.4.0

## why

v0.3.0 does not support `find_package(glog)`.

## download

```
cd ~/build
curl -Lo glog-v0.4.0.tar.gz https://github.com/google/glog/archive/v0.4.0.tar.gz
tar -zxvf glog-v0.4.0.tar.gz
cd glog-0.4.0
```

## build for  petalinux

```
mkdir build_for_petalinux
cd build_for_petalinux
unset LD_LIBRARY_PATH; source ~/build/zcu104_sdk/environment-setup-aarch64-xilinx-linux # your petalinux might install another dir
cmake -DCPACK_GENERATOR=TGZ -DBUILD_SHARED_LIBS=on -DCMAKE_INSTALL_PREFIX=$OECORE_TARGET_SYSROOT/usr ..
make && make install
make package
```

to deploy on the target board

```
cd ~/bulid/glog-0.4.0/build_for_petalinux
cat glog-0.4.0-Linux.tar.gz | ssh root@10.176.179.66 tar -zxvf - -C /
```


## build for host

```
cd ~/build/glog-0.4.0/
mkdir -p build_for_host
cd build_for_host
# cmake -DWITH_GFLAGS=off  -DCPACK_GENERATOR=TGZ -DBUILD_SHARED_LIBS=on -DCMAKE_INSTALL_PREFIX=$HOME/.local .. # install in your home directory
cmake -DWITH_GFLAGS=off  -DCPACK_GENERATOR=TGZ -DBUILD_SHARED_LIBS=on -DCMAKE_INSTALL_PREFIX=$HOME/.local ..
make -j10 && make install
make package
```
