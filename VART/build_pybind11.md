
# install pybind11


## download `pybind11`

```
gitlab=xcdl190260
git clone ssh://gits@$gitlab/3rd-party/pybind11
```

### install `pybind11` on host

```
# you have to install python3-dev  as below
# sudo apt-get install -y python3-dev
cd $HOME/d/working/aisw
git clone ssh://gits@$gitlab/3rd-party/pybind11
cd $HOME/d/working/aisw/pybind11
mkdir build;cd build;
cmake -DCMAKE_INSTALL_PREFIX=$HOME/.local -DPYBIND11_TEST=off -DPYBIND11_INSTALL=on ..
cmake  -DPYBIND11_TEST=off -DPYBIND11_INSTALL=on ..
make
chmod o+rwx .
/tools/xgs/bin/sudo make install
/tools/xgs/bin/sudo yum install python34-dev
```


### install `pybind11` on petalinux sdk

```
unset LD_LIBRARY_PATH;source /group/xbjlab/dphi_software/software/workspace/$USER/petalinux-sdk/environment-setup-aarch64-xilinx-linux
cp -av $HOME/d/working/aisw/pybind11/include/pybind11 $OECORE_TARGET_SYSROOT/usr/include
```


### FAQ


1. `Python.h` is not found. please install `python3-dev`.


```
/home/xbuild/.local/Ubuntu.18.04.x86_64.Release/include/pybind11/detail/common.h:112:10: fatal error: Python.h: No such file or directory
 #include <Python.h>
          ^~~~~~~~~~
compilation terminated.
runner/CMakeFiles/vitis-ai-runner-py.dir/build.make:62: recipe for target 'runner/CMakeFiles/vitis-ai-runner-py.dir/python/runner_py_module.cpp.o' failed

```
