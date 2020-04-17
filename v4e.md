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
# ./test_resnet50.sh
% XCLBIN_PATH=${1-'./xclbin/binary_container_1.xclbin'}
% HBM_ADDRESS_PATH=${2-'./xclbin/hbm_batch_1.txt'}

set -x
% env DEBUG_DPU_CONTROLLER=1 XLNX_SHOW_DPU_COUNTER=1 XLNX_ENABLE_CLEAR=0 XLNX_ENABLE_DUMP_PARAMTER=1 XLNX_ENABLE_UPLOAD=0 XLNX_GOLDEN_DIR=./resnet50_golden XLNX_ENABLE_DEBUG_MODE=0  DEBUG_XRT_CU=2 DEBUG_XRT_DEVICE_HANDLE=1 XLNX_MAT_CONFIG=$HBM_ADDRESS_PATH  XLNX_VART_FIRMARE=$XCLBIN_PATH  XLNX_ENABLE_DUMP=1 XLNX_SHORT_CIRCUIT_DPU_CODE=0 DEEPHI_PROFILING=1 DEBUG_DPU_RUNNER=1 XLNX_CHECK_COMMIT_ID_ENABLE=0 ./test_dpu_runner ./model/debug.xmodel subgraph_resnet_v1_50/block1/unit_2/bottleneck_v1/conv3/Conv2D\(fix\) ./resnet50_golden/input_aquant.bin 1 1

```


check code md5sum


``` console
% ./mem_read 0xc280000000 467724 >a.code
% md5sum a.code
# da78401b3efa136f048a644bd33d5933  a.code
% mkdir -p model_dump;cd model_dump;
% env ENABLE_DUMP=1 ~/working/build/build.CentOS.7.4.1708.x86_64.Debug/xir/test/xir_cat.bin -tmodel.txt  /home/xysheng/test_dpuv4/model/debug.xmodel
% less model.txt
# bytes_value {
#          value: bytes = 467724 md5sum = da78401b3efa136f48a644bd33d5933
#           head:

% ./mem_read 0xc200000000 28032 >reg0.bin
% ./mem_read 0xc200007000 12785664 >reg2.bin
% ./mem_read 0xc240000000 12785664 >reg3.bin
% md5sum reg0.bin reg2.bin reg3.bin
% grep md5sum model.txt | grep '28032\|12785664'
% function d() { md5sum $1; stat -c %s $1; xxd $1 | head -n 16; }
##
##            value: bytes = 28032 md5sum = 5c44cadf66bdf4a75b9fdbc62a84a05b
##            value: bytes = 12785664 md5sum = 4b2c7061da5b91ab8a2adf98d9bc41a
##            value: bytes = 12785664 md5sum = edbacc31aaec19a85742085ee5872a2
% ./mem_read 0xc000001000 150528 > input.dat
% d input.dat #
% # 5b94b56093f6dd346aec7474e198d646  input.dat
% # 0000000: 0200 6003 0200 c001 007f 6008 1701 0200  ..`.......`.....
% d resnet50_golden/input_aquant.bin
% cat resnet50_golden/input_aquant.bin | ./mem_write 0xc000001000 150528
% env XLNX_VART_FIRMARE=$HOME/toYongsheng/dpu.xclbin ./xrt_read_register reg_cloud.conf dpu 0
%
% env XLNX_VART_FIRMARE=$HOME/toYongsheng/dpu.xclbin ./write_counter dpu 0
% env XLNX_VART_FIRMARE=$HOME/toYongsheng/dpu.xclbin ./xrt_read_register reg_cloud.conf dpu 0
% grep 0.resnet_v1_50_logits_BiasAdd_aquant.bin a.log
% ./mem_read 0xc0008c0300 1000 > output.bin
% d output.bin
% d resnet50_golden/resnet_v1_50_logits_BiasAdd_aquant.bin
```

``` console
% # upload code
% cat model_dump/2e14f176720aca3bcbc718de361ec81.bin | ./mem_write 0xc280000000  6388
% ./mem_read   0xc280000000  6388 | md5sum
% cat resnet50_golden/input_aquant.bin | ./mem_write 0xc000001000 150528
% ./mem_read 0xc000001000 150528 | md5sum
% env XLNX_VART_FIRMARE=$HOME/toYongsheng/dpu.xclbin ./write_counter dpu 0
% env XLNX_VART_FIRMARE=$HOME/toYongsheng/dpu.xclbin ./xrt_read_register reg_cloud.conf dpu 0
% ./mem_read 0xc000025c00 200704 > c1.bin
% d c1.bin # 01c9b6144f1ac0c354e8a3eab486046a
% d resnet50_golden/resnet_v1_50_pool1_MaxPool_aquant.bin # c5238b814db75bf1f1f2aa79a16287d2
% d dump/subgraph_resnet_v1_50_block1_unit_2_bottleneck_v1_conv3_Conv2D/internal/0.resnet_v1_50_pool1_MaxPool_aquant.bin
% ./mem_read 0xc000001000 150528 > i1.bin
% d i1.bin # 5b94b56093f6dd346aec7474e198d646
% dd if=/dev/zero of=$HOME/working/zeros bs=1024 count=$((32*4*1024))
% cat $HOME/working/zeros | ./mem_write 0xc000000000 134217728
```
