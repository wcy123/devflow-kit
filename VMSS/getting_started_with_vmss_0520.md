## start mongodb
```
mongo -version

systemctl start mongod
systemctl status mongod
```
## build vitis-ai-library
```
#clear .local && build
rm -rf /group/xbjlab/dphi_software/software/workspace/mingyue/build
mkdir /group/xbjlab/dphi_software/software/workspace/mingyue/build
ls -l
rm -rf /group/xbjlab/dphi_software/software/workspace/mingyue/.local
mkdir /group/xbjlab/dphi_software/software/workspace/mingyue/.local
ls -la

#153
rsync -e 'ssh -p 10115'  $HOME/build/glog-v0.4.0.tar.gz xbj-pvapjmp11:/home/mingyue/build

cd ~/build
tar -zxvf glog-v0.4.0.tar.gz
cd ~/build/glog-0.4.0/
mkdir -p build_for_host
cd build_for_host
cmake -DWITH_GFLAGS=off  -DCPACK_GENERATOR=TGZ -DBUILD_SHARED_LIBS=on -DCMAKE_INSTALL_PREFIX=$HOME/.local ..
make -j10 && make install

cd ~/d/working
mkdir vmss_vitis_libs
cd vmss_vitis_libs
git clone https://gitenterprise.xilinx.com/aisw/unilog.git
git clone https://gitenterprise.xilinx.com/aisw/xir.git
git clone https://gitenterprise.xilinx.com/aisw/vart.git
git clone https://gitenterprise.xilinx.com/aisw/Vitis-AI-Library.git

cd ~/d/working/vmss_vitis_libs
cd unilog
./cmake.sh
cd ../xir
./cmake.sh
cd ../vart
 ./cmake.sh --cmake-options=-DENABLE_DPU_RUNNER=ON --cmake-options=-DENABLE_SIM_RUNNER=OFF --cmake-options=-DENABLE_CPU_RUNNER=OFF
cd ../Vitis-AI-Library
git checkout dev
git clone 053b48fbfdbe5c3bc9fc3aa422ac403c90607ad0
./cmake.sh s--cmake-options='-DENABLE_OVERVIEW=ON'
```

## build vmss server
```
mkdir -p $HOME/d/working/VMSS/
git clone git@gitenterprise.xilinx.com:chunywan/VMSS_Plugins.git
cp ~/d/working/vmss/VMSS /home/mingyue/d/working/VMSS/VMSS_Plugins/ml/
mv /home/mingyue/d/working/VMSS/VMSS_Plugins/ml/DPU /home/mingyue/d/working/VMSS/VMSS_Plugins/ml/VMSS_DPU_Plugins/

cd /home/mingyue/d/working/VMSS/VMSS_Plugins/ml/VMSS
export VMSS_HOME=/home/mingyue/d/working/VMSS/VMSS_Plugins/ml/VMSS
export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig:/usr/local/lib64/pkgconfig
make DEBUG=1

```

## build DPU plugins
```
cd /home/mingyue/d/working/VMSS/VMSS_Plugins/ml/VMSS_DPU_Plugins
./cmake.sh --clean --cmake-options=-DCMAKE_EXPORT_COMPILE_COMMANDS=ON

```
## install the plugins
```
build_type=Debug
os=`lsb_release -a | grep "Distributor ID" | sed 's/^.*:\s*//'`
os_version=`lsb_release -a | grep "Release" | sed 's/^.*:\s*//'`
arch=`uname -p`
target_info=${os}.${os_version}.${arch}
VMSS_HOME=/group/xbjlab/dphi_software/software/workspace/mingyue/d/working/VMSS/VMSS_Plugins/ml/VMSS
ln -sf $HOME/.local/${target_info}.${build_type}/lib/libdpuMLPreProcPlg.so $VMSS_HOME/server/plugins
ln -sf $HOME/.local/${target_info}.${build_type}/lib/libdpuMLInferencePlg.so $VMSS_HOME/server/plugins
ln -sf $HOME/.local/${target_info}.${build_type}/lib/libdpuMLPostProcPlg.so $VMSS_HOME/server/plugins
ls -l $VMSS_HOME/server/plugins

```
## start vmss server : Debug
open a new window
```
ssh -p 10115 mingyue@xbj-pvapjmp11
build_type=Debug
os=`lsb_release -a | grep "Distributor ID" | sed 's/^.*:\s*//'`
os_version=`lsb_release -a | grep "Release" | sed 's/^.*:\s*//'`
arch=`uname -p`
target_info=${os}.${os_version}.${arch}
VMSS_HOME=/group/xbjlab/dphi_software/software/workspace/mingyue/d/working/VMSS/VMSS_Plugins/ml/VMSS

cd $VMSS_HOME/server
export LD_LIBRARY_PATH=/usr/local/lib:/usr/local/lib64:/opt/xilinx/xrt/lib:/home/$USER/.local/${target_info}.${build_type}/lib:$VMSS_HOME/server/libs:$VMSS_HOME/server/libs/extern:$VMSS_HOME/server/libs/extern/ml-suite-py3
gdb vmss_server
```
in the gdb session
```
   set env DEBUG_DPU_PLUGIN=5
   set env DEBUG_XRT_DEVICE_HANDLE=1
   set env XLNX_ENABLE_DEVICES=0
   start ~/d/working/VMSS/VMSS_Plugins/ml/VMSS_DPU_Plugins/conf
   b src/vmss_gst_common.c:183
   c
```
## VMSS clinet
### sample resnet50
#### 1. send request to vmss server for create connection
```
cd $VMSS_HOME/client/gstreamer
ls data/commands
cat data/commands/vmss_open_jpeg_resnet_request.txt
./vmss_client 127.0.0.1 8001 data/commands/vmss_open_jpeg_resnet_request.txt
./vmss_client 127.0.0.1 8001 data/commands/vmss_open_jpeg_tinyyolov3_request.txt
```
### 2. send image
```
cat ./scripts/gst_send_rtp.sh
# in the forked subshell
./scripts/gst_send_rtp.sh -rd 10 -w 224 -h 224 -f  data/classification/beagle.jpg
./scripts/gst_send_rtp.sh -rd 10 -w 416 -h 416 -f  data/classification/yolov3_01.jpeg
```
