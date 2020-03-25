
## ssh xbjlabdpsvr15
```
ssh -p 10115 mingyue@xbj-pvapjmp11
```
## start mongodb
```
mongo -version
systemctl start mongod
systemctl status mongod
```

## build vitis-ai-library
```
#rsync -e 'ssh -p 10115'  $HOME/build/glog-v0.4.0.tar.gz xbj-pvapjmp11:/home/mingyue/build
cd ~/build
tar -zxvf glog-v0.4.0.tar.gz
cd ~/build/glog-0.4.0/
mkdir -p build_for_host
cd build_for_host
cmake -DWITH_GFLAGS=off  -DCPACK_GENERATOR=TGZ -DBUILD_SHARED_LIBS=on -DCMAKE_INSTALL_PREFIX=$HOME/.local ..
make -j10 && make install


cd ~/d/working/aisw
cd unilog
./cmake.sh
cd ../xir
./cmake.sh
cd ../vart
git checkout br-dim-calc
git branch
 ./cmake.sh --cmake-options=-DENABLE_DPU_RUNNER=ON --cmake-options=-DENABLE_SIM_RUNNER=OFF --cmake-options=-DENABLE_CPU_RUNNER=OFF --clean
cd ../Vitis-AI-Library
./cmake.sh --cmake-options='-DENABLE_OVERVIEW=ON'
git checkout br-refactor-cmake
g branch
g p
./cmake.sh --cmake-options='-DENABLE_OVERVIEW=ON'

```

## build vmss server
```
mkdir -p $HOME/d/working/vmss/
cd $HOME/d/working/vmss/
#153
#git clone https://gitenterprise.xilinx.com/ips-video-ml/VMSS.git
#cd VMSS
#git submodule update --init
#rsync -e 'ssh -p 10115'  $HOME/d/working/mingyue/vmss/VMSS.tar.gz xbj-pvapjmp11:/home/mingyue/d/working/vmss/
#tar -zxvf VMSS.tar.gz
cp -r /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/vmss/VMSS $HOME/d/working/vmss
cd VMSS
export VMSS_HOME=$HOME/d/working/vmss/VMSS
make DEBUG=1

```

## build DPU plugsins
```
cd $HOME/d/working/vmss
ls
#153
#rsync -e 'ssh -p 10115'  $HOME/d/working/mingyue/vmss/VMSS_DPU_Plugins.tar.gz xbj-pvapjmp11:/home/mingyue/d/working/vmss/
#tar -zxvf VMSS_DPU_Plugins.tar.gz
cd VMSS_DPU_Plugins
./cmake.sh
```

## install the plugins
```
build_type=Debug
os=`lsb_release -a | grep "Distributor ID" | sed 's/^.*:\s*//'`
os_version=`lsb_release -a | grep "Release" | sed 's/^.*:\s*//'`
arch=`uname -p`
target_info=${os}.${os_version}.${arch}
VMSS_HOME=/group/xbjlab/dphi_software/software/workspace/mingyue/d/working/vmss/VMSS
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
VMSS_HOME=/group/xbjlab/dphi_software/software/workspace/mingyue/d/working/vmss/VMSS

cd $VMSS_HOME/server
export LD_LIBRARY_PATH=/usr/local/lib:/usr/local/lib64:/opt/xilinx/xrt/lib:/home/$USER/.local/${target_info}.${build_type}/lib:$VMSS_HOME/server/libs:$VMSS_HOME/server/libs/extern:$VMSS_HOME/server/libs/extern/ml-suite-py3
gdb vmss_server
```
in the gdb session
```
   start ~/d/working/vmss/VMSS_DPU_Plugins/conf
   set env DEBUG_DPU_PLUGIN=5
```
## VMSS clinet
### sample resnet50
#### 1. send request to vmss server for create connection
```
cd $VMSS_HOME/client/gstreamer
ls data/commands
cat data/commands/vmss_open_jpeg_resnet_request.txt
./vmss_client 127.0.0.1 8001 data/commands/vmss_open_jpeg_resnet_request.txt
```
client log :
```
> ---------------------------------
>   Sending the following msg
> ---------------------------------
> {
>  "type": "open",
>  "encoding": "jpeg",
>  "width": 224,
>  "height": 224,
>  "network": "resnet50",
>  "protocol": "rtp",
>  "clientIP": "127.0.1.1"
> }
> ---------------------------------
>   Response msg from server
> ---------------------------------
> Session UUID = 5e788e8be666c146054df0f3
> RTP port = 5030
> RTCP port = 5031

> RTP Session bash prompt:
```
### 2. send image
```
cat ./scripts/gst_send_rtp.sh
# in the forked subshell
./scripts/gst_send_rtp.sh -rd 10 -w 224 -h 224 -f  data/classification/beagle.jpg
```
`-rd 10` : 1times /10s
client log:
```
> -----------------
> Settings
>   Dest   : 127.0.0.1
>   Port   : 5030
>   Enc    : jpeg
>   Rate   : 1/1
>   Width  : 224
>   Height : 224
> -----------------
> Setting pipeline to PAUSED ...
> Pipeline is PREROLLING ...
> Pipeline is PREROLLED ...
> Setting pipeline to PLAYING ...
> New clock: GstSystemClock
> ^Chandling interrupt.
> Interrupt: Stopping pipeline ...
> Execution ended after 0:00:22.897393993
> Setting pipeline to PAUSED ...
> Setting pipeline to READY ...
> Setting pipeline to NULL ...
> Freeing pipeline ...
```
server log:
```
> I0323 19:01:19.346180 62339 dpu_task_imp.cpp:374] n 1
> I0323 19:01:19.385772 62339 dpuMLInferencePlg.cpp:371] ctx network-ctxt@0x6a25c0[name=resnet50] performance counter: num_of_dpu_inputs =  136 num_of_user_inputs = 50
> *******************************************************************************************************
> {
>     "timestamp": 1584961277,
>     "ts_us_offset": 344604,
>    "frame": 50,
>    "network": "resnet50",
>    "item count": 1,
>    "items": {
>         "item 1": {
>             "classification": "CANDLE",
>             "confidence": 0.76439999999999997,
>             "width": 0,
>             "height": 0,
>             "x": 0,
>             "y": 0,
>             "box_id": 0,
>             "iou_score": 0.0
>         }
>     }
> }
> *******************************************************************************************************
```

### 3. quit
```
# after tesing
exit
# exit will close the session.
```
server log:
```
> New connection , socket fd is 27 , ip is : 0.0.0.0 , port : 8001
> -----------------------
> Request Message
> -----------------------
> {
>  "type": "close",
>  "session_id": "5e788e8be666c146054df0f3"
> }

> End-of-stream
> [Thread 0x7fffa5ffb700 (LWP 63113) exited]
> -----------------------
> Response Message
> -----------------------
> {
>  "status": "ok",
>  "rtp_port": 5030,
>  "rtcp_port": 5031,
>  "session_id": "5e788e8be666c146054df0f3"
> }
> Adding to list of sockets as 0
> VMSS Server started and listening on port 8001
> VMSS Server started and listening on port 8001
> [Thread 0x7fff8afe3700 (LWP 63144) exited]
```
end
