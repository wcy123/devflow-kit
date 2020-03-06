# build `unilog` `xir` `vart` and `vitis-ai-library`


## download source code

```
gitlab=xcdl192026
#gitlab=localhost:10260
mkdir -p $HOME/d/working/aisw/
cd  $HOME/d/working/aisw/
git clone ssh://gits@$gitlab/aisw/unilog
git clone ssh://gits@$gitlab/aisw/xir
git clone ssh://gits@$gitlab/aisw/vart
git clone ssh://gits@$gitlab/aisw/Vitis-AI-Library
```

## prerequsites

1. [install glog 0.4.0](build_glog_v0.4.0.md)
2. [install pybind11](build_pybind11.md)

## environment setting

the build commands are same for both host native build and petalinux
cross compile build, but we need to setup the different building
environment before starting the build.

### for host native build, U50

set the common environment for host

```
build_type=Debug  ;\
os=`lsb_release -a | grep "Distributor ID" | sed 's/^.*:\s*//'`  ;\
os_version=`lsb_release -a | grep "Release" | sed 's/^.*:\s*//'` ;\
arch=`uname -p`  ;\
target_info=${os}.${os_version}.${arch}  ;\
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/xilinx/xrt/lib:/home/$USER/.local/${target_info}.${build_type}/lib ;
```

install the petalinux SDK.

```
/group/xbjlab/dphi_software/petalinux_sdk/sdk-zcu104-1128.sh -y -d /group/xbjlab/dphi_software/software/workspace/$USER/petalinux-sdk/environment-setup-aarch64-xilinx-linux
```

set the common environment for edge

```
unset LD_LIBRARY_PATH;source /group/xbjlab/dphi_software/software/workspace/$USER/petalinux-sdk/environment-setup-aarch64-xilinx-linux
```

### build `unilog`

```
cd $HOME/d/working/aisw/unilog;
./cmake.sh --pack=deb --clean
```

### build `xir`

```
cd $HOME/d/working/aisw/xir
./cmake.sh --clean --pack=deb --build-python  # no need to --build-python if you don't build xcompiler
```

### build `vart`

```
cd $HOME/d/working/aisw/vart
./cmake.sh --pack=deb --cmake-options=-DENABLE_DPU_RUNNER=ON --cmake-options=-DENABLE_SIM_RUNNER=OFF --cmake-options=-DENABLE_CPU_RUNNER=OFF  --clean --build-python
```


### build `Vitis-AI-Library`

```
cd $HOME/d/working/aisw/Vitis-AI-Library
./cmake.sh --pack=deb --clean
```
