# Getting  started with VMSS.

`NOTE`: working in progress, it only works on xbjlabdpsvr15
environment. You might need minor tweaks for your environment.

# external prerequistes

## install and start `mongodb`

TODO: install `mongodb`

### start mongodb

```
systemctl start mongod
systemctl status mongod
```

```
mongo -version
MongoDB shell version v4.2.3
git version: 6874650b362138df74be53d366bbefc321ea32d4
OpenSSL version: OpenSSL 1.0.1e-fips 11 Feb 2013
allocator: tcmalloc
modules: none
build environment:
    distmod: rhel70
    distarch: x86_64
    target_arch: x86_64
```
## internal prerequites

## build `Vitis-AI-Library`

please refert to [build Vitis AI Library](../VART/build_unilog_xir_vart_ailib.md)

## build vmss server

```
mkdir -p $HOME/d/workingvmss/
cd $HOME/d/working/vmss/
git clone https://gitenterprise.xilinx.com/ips-video-ml/VMSS.git
cd VMSS
export VMSS_HOME=$PWD
git submodule update --init
make DEBUG=1
```


## build DPU plugsins

```
mkdir -p $HOME/d/workingvmss/
cd $HOME/d/working/vmss/
git clone gits@xcdl190260:wangchunye/VMSS_DPU_Plugins.git
cd VMSS_DPU_Plugins
./cmake.sh
```

## install the plugins


```
build_type=Debug  ;\
os=`lsb_release -a | grep "Distributor ID" | sed 's/^.*:\s*//'`  ;\
os_version=`lsb_release -a | grep "Release" | sed 's/^.*:\s*//'` ;\
arch=`uname -p`  ;\
target_info=${os}.${os_version}.${arch}  ;\
# VMSS_HOME=/group/xbjlab/dphi_software/software/workspace/chunywan/d/working/vmss/my_vmss
ln -sf $HOME/.local/${target_info}.${build_type}/lib/libdpuMLPreProcPlg.so $VMSS_HOME/server/plugins
ln -sf $HOME/.local/${target_info}.${build_type}/lib/libdpuMLInferencePlg.so $VMSS_HOME/server/plugins
ln -sf $HOME/.local/${target_info}.${build_type}/lib/libdpuMLPostProcPlg.so $VMSS_HOME/server/plugins
ls -l $VMSS_HOME/server/plugins
```


## debug vmss server

```
cd $VMSS_HOME/server
export LD_LIBRARY_PATH=/usr/local/lib:/usr/local/lib64:/opt/xilinx/xrt/lib:/home/$USER/.local/${target_info}.${build_type}/lib:$VMSS_HOME/server/libs:$VMSS_HOME/server/libs/extern:$VMSS_HOME/server/libs/extern/ml-suite-py3
gdb vmss_server
```

in the gdb session

```
start conf
continue
```
