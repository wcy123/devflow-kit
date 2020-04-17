# enable  v4e


``` console
% ssh xsjfislx12
% cd ~/d/working/aisw/vart; ls -l
% source /opt/rh/devtoolset-6/enable
% /opt/xilinx/xrt/bin/xbutil query | less
```


``` plain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
System Configuration
OS name:        Linux
Release:        3.10.0-693.el7.x86_64
Version:        #1 SMP Tue Aug 22 21:09:27 UTC 2017
Machine:        x86_64
Model:          Super Server
CPU cores:      16
Memory:         15492 MB
Glibc:          2.17
Distribution:   CentOS Linux 7 (Core)
Now:            Thu Apr 16 22:36:51 2020

XRT Information
Version:        2.6.6
Git Hash:       aed407855b46b574e08009b14f1b0b0cda6c313c
Git Branch:     master
Build Date:     2020-02-20 00:55:18
XOCL:           2.6.6,aed407855b46b574e08009b14f1b0b0cda6c313c
XCLMGMT:        2.6.6,aed407855b46b574e08009b14f1b0b0cda6c313c

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Shell                           FPGA                            IDCode
xilinx_v350-es1_xdma_201921_1   xcv350-vsvd1760-2MP-e-S-es1     0x0
Vendor          Device          SubDevice       SubVendor       SerNum
0x10ee          0x5029          0x000e          0x10ee
DDR size        DDR count       Clock0          Clock1          Clock2
8 GB            1               0               0               0
PCIe            DMA chan(bidir) MIG Calibrated  P2P Enabled     OEM ID
GEN 3x16        4               false           N/A
DNA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```


``` console
% cd ~/test_dpuv4;ls -l
% cat ./test_resnet50.sh
% ./test_resnet50.sh ~/toYongsheng/dpu.xclbin
```


``` sh

XCLBIN_PATH=${1-'./xclbin/binary_container_1.xclbin'}
HBM_ADDRESS_PATH=${2-'./xclbin/hbm_batch_1.txt'}

set -x
env DEBUG_DPU_CONTROLLER=1 XLNX_SHOW_DPU_COUNTER=1 XLNX_ENABLE_CLEAR=0 XLNX_ENABLE_DUMP_PARAMTER=1 XLNX_ENABLE_UPLOAD=0 XLNX_GOLDEN_DIR=./resnet50_golden XLNX_ENABLE_DEBUG_MODE=0  DEBUG_XRT_CU=2 DEBUG_XRT_DEVICE_HANDLE=1 XLNX_MAT_CONFIG=$HBM_ADDRESS_PATH  XLNX_VART_FIRMARE=$XCLBIN_PATH  XLNX_ENABLE_DUMP=1 XLNX_SHORT_CIRCUIT_DPU_CODE=0 DEEPHI_PROFILING=1 DEBUG_DPU_RUNNER=1 XLNX_CHECK_COMMIT_ID_ENABLE=0 ./test_dpu_runner ./model/debug.xmodel subgraph_resnet_v1_50/block1/unit_2/bottleneck_v1/conv3/Conv2D\(fix\) ./resnet50_golden/input_aquant.bin 1 1

```
