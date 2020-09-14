```
source  /opt/rh/devtoolset-9/enable
mkdir -p $HOME/d/working/VMSS_1.2
cd $HOME/d/working/VMSS_1.2

ssh xbjlabdpsvr15


git clone git@gitenterprise.xilinx.com:ips-video-ml/VMSS.git
git clone git@gitenterprise.xilinx.com:chunywan/VMSS_Plugins.git

cd VMSS
git checkout develop

#git submodule update --init
cd extern
git clone git@gitenterprise.xilinx.com:ips-video-ml/VMSS_Lib.git
cd VMSS_Lib
git checkout f398cfe236c79bb03f05e81534ff3b4067042d81
git checkout develop
# git checkout f398cfe236c79bb03f05e81534ff3b4067042d81

cd ../
git clone git@gitenterprise.xilinx.com:ips-video-ml/VMSS_Plugins.git
cd VMSS_Plugins
git checkout 3250e64148501140af91dffa80ce147958b8bb38



```
## build vitis-ai-library
```
cd $HOME/d/working/aisw
cd unilog
git checkout br-u30
./cmake.sh

cd ../target_factory
git checkout br-u30
./cmake.sh

cd ../xir
git checkout br-u30
./cmake.sh

cd ../vart
git checkout br-u30
./cmake.sh --cmake-options=-DENABLE_DPU_RUNNER=ON --cmake-options=-DENABLE_SIM_RUNNER=OFF --cmake-options=-DENABLE_CPU_RUNNER=OFF

cd ../Vitis-AI-Library/
git checkout br-u30
./cmake.sh --cmake-options='-DENABLE_OVERVIEW=ON'
```
### check xmodel
```
cd  /home/mingyue/d/working/VMSS_1.2



```

## build VMSS server
```
cd $HOME/d/working/VMSS_1.2/VMSS
export VMSS_HOME=$HOME/d/working/VMSS_1.2/VMSS
#export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig:/usr/local/lib64/pkgconfig

#update server/env.sh  server/Makefile
make DEBUG=1
```

## build DPU plugins
```
cp -r
cp -r $HOME/d/working/VMSS_1.2/VMSS_Plugins/ml/DPU $HOME/d/working/VMSS_1.2/VMSS_DPU_Plugins
cd $HOME/d/working/VMSS_1.2/VMSS_DPU_Plugins/
./cmake.sh --clean --cmake-options=-DCMAKE_EXPORT_COMPILE_COMMANDS=ON

#cp -r $HOME/d/working/VMSS_1.2/VMSS $HOME/d/working/VMSS_1.2/VMSS_Plugins/ml/
#cd $HOME/d/working/VMSS_1.2/VMSS_Plugins/ml/VMSS
#export VMSS_HOME=/home/mingyue/d/working/VMSS_1.2/VMSS_Plugins/ml/VMSS
#make DEBUG=1

#cd ../DPU
#./cmake.sh --clean --cmake-options=-DCMAKE_EXPORT_COMPILE_COMMANDS=ON
```

## patch
```
cp /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/vmss/VMSS/extern/VMSS_Lib/include/vmss_plugin.h ~/d/working/VMSS_1.2/VMSS/extern/VMSS_Lib/include/
cp /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/vmss/VMSS/extern/VMSS_Lib/src/vmss_jobmgr.c ~/d/working/VMSS_1.2/VMSS/extern/VMSS_Lib/src/

```

## install the plugins
```
build_type=Debug
os=`lsb_release -a | grep "Distributor ID" | sed 's/^.*:\s*//'`
os_version=`lsb_release -a | grep "Release" | sed 's/^.*:\s*//'`
arch=`uname -p`
target_info=${os}.${os_version}.${arch}
ln -sf $HOME/.local/${target_info}.${build_type}/lib/libdpuMLPreProcPlg.so $VMSS_HOME/server/plugins
ln -sf $HOME/.local/${target_info}.${build_type}/lib/libdpuMLInferencePlg.so $VMSS_HOME/server/plugins
ln -sf $HOME/.local/${target_info}.${build_type}/lib/libdpuMLPostProcPlg.so $VMSS_HOME/server/plugins
ls -l $VMSS_HOME/server/plugins
```


## start vmss server : Debug
```
cd $VMSS_HOME/server
export LD_LIBRARY_PATH=/usr/local/lib:/usr/local/lib64:/opt/xilinx/xrt/lib:/home/$USER/.local/${target_info}.${build_type}/lib:$VMSS_HOME/server/libs:$VMSS_HOME/server/libs/extern:$VMSS_HOME/server/libs/extern/ml-suite-py3

cp -r /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/vmss/VMSS/extern/VMSS_Plugins_develop/ml/DPU /home/mingyue/d/working/VMSS_1.2/VMSS/extern/VMSS_Plugins/ml/
env DEBUG_DPU_PLUGIN=5 ./vmss_server ~/d/working/VMSS_1.2/VMSS_DPU_Plugins/conf 2>a.log 1>&2

gdb vmss_server
set env DEBUG_DPU_PLUGIN=5
set env DEBUG_XRT_DEVICE_HANDLE=1
set env XLNX_ENABLE_DEVICES=0
run ~/d/working/VMSS_1.2/VMSS_DPU_Plugins/conf
```

## VMSS Client
```
cd $VMSS_HOME/client/gstreamer
cat data/commands/vmss_open_jpeg_resnet_request.txt
cat data/commands/vmss_open_jpeg_retail_request.txt

./vmss_client 127.0.0.1 8001 data/commands/vmss_open_jpeg_resnet_request.txt
./vmss_client 127.0.0.1 8001 data/commands/vmss_open_jpeg_car_detection_request.txt
cat ./scripts/gst_send_rtp.sh
./scripts/gst_send_rtp.sh -rd 10 -w 224 -h 224 -f  data/classification/beagle.jpg
./scripts/gst_send_rtp.sh -rd 10 -w 416 -h 416 -f  data/classification/beagle.jpg
./scripts/gst_send_rtp.sh -rd 10 -w 480 -h 360 -f  data/ssd/sample_ssd.jpg

```
