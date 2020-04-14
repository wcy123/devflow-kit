# setup environment


follow [XBulter](https://confluence.xilinx.com/display/~vincentm/XButler)

## XRT

it is already installed.

## anaconda

nNOTE: refer to [anaconda](../VART/anaconda_env.md)

due to lib confilctions, we cannto use it, refer to [](butler.bak.md) for your reference.

## prerequites

```
sudo yum -y install jsoncpp-devel
```


## XIP/XButler

### prepare

```
which g++
g++ --version # make sure it is gcc6 or above
source /opt/rh/devtoolset-6/enable
g++ --version # make sure it is gcc6 or above
make clean
make
```

### make

```
% cd $HOME/d/working/
% git clone gits@xcdl190260:wangchunye/XIP.git
% cd $HOME/d/working/XIP/Butler/src
% source /opt/rh/devtoolset-6/enable
% make clean
% make DEBUG=1 -j10
```
rt
### prepare dsa files
```
mkdir -p /opt/xilinx/dsa/
sudo cp -av /usr/lib/dpu.xclbin /opt/xilinx/dsa/verify.xclbin
ssh xbjlabdpsvr15 ls -l /opt/xilinx/dsa/
ls -la /opt/xilinx/dsa/
sudo chmod o+rw /opt/xilinx/dsa/
scp xbjlabdpsvr15:/opt/xilinx/dsa/dpu.xclbin.vitis.1.1 /opt/xilinx/dsa/
cp /opt/xilinx/dsa/dpu.xclbin.vitis.1.1 /opt/xilinx/dsa/verify.xclbin
md5sum /opt/xilinx/dsa/dpu.xclbin.vitis.1.1 /opt/xilinx/dsa/verify.xclbin
# it should be b7229999dca837511de0ac716d904870
/opt/xilinx/xrt/bin/xbutil query | less
```

it seems that we must ensure `XILINX_XRT=/opt/xilinx/xrt/`, at least, we must run `source /opt/xilinx/xrt/setup.sh`

### start server
```
% export XILINX_XRT=/opt/xilinx/xrt/
% export LD_LIBRARY_PATH=/group/xbjlab/dphi_software/software/workspace/chunywan/d/working/XIP/Butler/src/lib/:/usr/local/lib:/usr/local/lib64:/opt/xilinx/xrt/lib
% cd $HOME/d/working/XIP/Butler/src
% export BUTLER_VERBOSE=1
% export GLOG_logtostderr=1
% bin/xbutler 2>&1 | tee a.log && less a.log
```

### start client

``` console
% export XILINX_XRT=/opt/xilinx/xrt/
% export LD_LIBRARY_PATH=/group/xbjlab/dphi_software/software/workspace/chunywan/d/working/XIP/Butler/src/lib/:/usr/local/lib:/usr/local/lib64:/opt/xilinx/xrt/lib
% cd $HOME/d/working/XIP/Butler/src
% export BUTLER_VERBOSE=1
% export GLOG_logtostderr=1
bin/test_xbutler
```

``` console
% source /opt/rh/devtoolset-6/enable
% ls -l ~/build/build.CentOS.7.6.1810.x86_64.Debug/vart/xrt-device-handle/test_xrt_device_handle
% env DEBUG_XRT_DEVICE_HANDLE=1 ~/build/build.CentOS.7.6.1810.x86_64.Debug/vart/xrt-device-handle/test_xrt_device_handle dpu 1 2>&1 | tee a.log
% killall -2 xbutler
% less a.log
% ls /usr/share/ | grep vi
% cd  ~/build
% curl -Lo xilinx_model_zoo-1.1.0-Linux.deb https://www.xilinx.com/bin/public/openDownload?filename=xilinx_model_zoo-1.1.0-Linux.deb
% sudo yum install dpkg  #
% dpkg -x xilinx_model_zoo-1.1.0-Linux.deb models
% ls    /var/lib/docker/scratch/chunywan/build/models/usr/share/vitis_ai_library/models/resnet50
% sudo mkdir -p /scratch/group/modelzoo
% sudo chown chunywan: -R /scratch/group
% sudo chmod o+rwx /scratch/group
% rsync -avz xbjlabdpsvr15:/scratch/group/modelzoo /scratch/group
% for i in 0 1 2 3 ; do env XLNX_SHOW_DPU_COUNTER=1 DEBUG_DPU_CORE_ID=$i DEBUG_XRT_DEVICE_HANDLE=1 ~/build/build.CentOS.7.6.1810.x86_64.Debug/vart/dpu-runner/test/test_dpu_runner \
    /var/lib/docker/scratch/chunywan/build/models/usr/share/vitis_ai_library/models/resnet50/resnet50.xmodel \
    k_0 \
    /scratch/group/modelzoo/internal-cooperation-models/caffe/resnet50.baseline9213_ck/fix/acc/dump_gpu/data.bin 1 1 2>&1 | tee a$i.log ; done
% cd $HOME/build/build.CentOS.7.6.1810.x86_64.Debug/vart/xrt-device-handle; ls
% cp  $HOME/d/working/aisw/vart/xrt-device-handle/test/reg_cloud.conf .
% for  i in 0 1 2 3; do ./xrt_read_register $HOME/d/working/aisw/vart/xrt-device-handle/test/reg_cloud.conf dpu $i 2>&1 |  grep EXEC_CYCLE ;done
% grep CYCLE a*.log
```

``` plain
chunywan@xbjlabdpsvr16:xrt-device-handle% grep CYCLE a*.log
a0.log:I0414 15:04:01.068480 77841 dpu_control_xrt_cloud.cpp:139] core_idx = 0  LSTART 34901  LEND 34901  CSTART 7022  CEND 7022  SSTART 5108  SEND 5108  PSTART 4735  PEND 4735  CYCLE 3674481
a1.log:I0414 15:04:03.891945 77856 dpu_control_xrt_cloud.cpp:139] core_idx = 1  LSTART 34901  LEND 34901  CSTART 7022  CEND 7022  SSTART 5108  SEND 5108  PSTART 4735  PEND 4735  CYCLE 3674508
a2.log:I0414 15:04:06.435626 77871 dpu_control_xrt_cloud.cpp:139] core_idx = 2  LSTART 34901  LEND 34901  CSTART 7022  CEND 7022  SSTART 5108  SEND 5108  PSTART 4735  PEND 4735  CYCLE 3675819
a3.log:I0414 15:04:08.809621 77886 dpu_control_xrt_cloud.cpp:139] core_idx = 3  LSTART 34901  LEND 34901  CSTART 7022  CEND 7022  SSTART 5108  SEND 5108  PSTART 4735  PEND 4735  CYCLE 3669278
chunywan@xbjlabdpsvr16:xrt-device-handle% for  i in 0 1 2 3; do ./xrt_read_register $HOME/d/working/aisw/vart/xrt-device-handle/test/reg_cloud.conf dpu $i 2>&1 |  grep EXEC_CYCLE ;done
I0414 15:04:18.464761 77926 read_counter.cpp:51] 0x14000a8      0x381171                    3674481     EXEC_CYCLE_H
I0414 15:04:18.464769 77926 read_counter.cpp:51] 0x14000a8      0x381171                    3674481     EXEC_CYCLE_H
I0414 15:04:20.283426 77941 read_counter.cpp:51] 0x14000a8      0x38118c                    3674508     EXEC_CYCLE_H
I0414 15:04:20.283434 77941 read_counter.cpp:51] 0x14000a8      0x38118c                    3674508     EXEC_CYCLE_H
I0414 15:04:22.121119 77956 read_counter.cpp:51] 0x14100a8      0x3816ab                    3675819     EXEC_CYCLE_H
I0414 15:04:22.121127 77956 read_counter.cpp:51] 0x14100a8      0x3816ab                    3675819     EXEC_CYCLE_H
I0414 15:04:24.141234 77970 read_counter.cpp:51] 0x14100a8      0x37fd1e                    3669278     EXEC_CYCLE_H
I0414 15:04:24.141243 77970 read_counter.cpp:51] 0x14100a8      0x37fd1e                    3669278     EXEC_CYCLE_H
```
end mark
