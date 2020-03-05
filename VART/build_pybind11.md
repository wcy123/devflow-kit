
# install pybind11


## download `pybind11`

```
gitlab=xcdl192026
git clone ssh://gits@$gitlab/3rd-party/pybind11
```

### install `pybind11` on host

```
# you have to install python3-dev  as below
# sudo apt-get install -y python3-dev
cd $HOME/d/working/aisw/pybind11
mkdir build;cd build;
cmake -DCMAKE_INSTALL_PREFIX=$HOME/.local -DPYBIND11_TEST=off -DPYBIND11_INSTALL=on ..
```


### install `pybind11` on petalinux sdk

```
unset LD_LIBRARY_PATH;source /group/xbjlab/dphi_software/software/workspace/$USER/petalinux-sdk/environment-setup-aarch64-xilinx-linux
cp -av $HOME/d/working/aisw/pybind11/include/pybind11 $OECORE_TARGET_SYSROOT/usr/include
```
