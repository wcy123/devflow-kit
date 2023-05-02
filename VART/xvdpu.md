## debug xv dpu

NOTE:

    3. `XLNX_ENABLE_FINGERPRINT_CHECK` 目前模型指纹和硬件指纹还对不上

## 安装

这一步骤不用重复做，只要做一次就可以了。 如果安装 debug 版本，把目录名里面的 `Release` 改成 `Debug`


``` console
% cp -av /group/xbjlab/dphi_software/software/workspace/chunywan/petalinux-sdk2/sysroots/aarch64-xilinx-linux/install/Release/lib/* /usr/lib/
% for i in /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Release/Vitis-AI-Library/overview/test_jpeg_classification  \
     /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Release/vart/dpu-runner/test/test_dpu_runner  \
     /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Release/vart/util/vart_version    \
     /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Release/vart/dpu-runner/test/test_dpu_runner_mt \
     /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Release/Vitis-AI-Library/overview/test_performance_classification  \
     /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Debug/test_alloc_bo \
     ; do \
          cp -av $i /usr/bin;chrpath /usr/lib $i;  \
     done;

# 拷贝测试数据
% cp -av /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/vitis-ai-library-samples-res/samples/classification /usr/share
```

检查环境， 当前版本是 `1.2.0-4640fa8f7adcc34d27df07f9620c1b94321378c5`

``` console
% unset LD_LIBRARY_PATH
% vart_version
```

## 功能测试。

模型信息。

```
ade1fb955ede189367c86ec9428e1685  mlp_res50_elp8_c32_0813.xmodel
b0d80b64f9ed4076284c820a7205b085  subgraph_1_input_image_aquant_vart-sim-runner.bin
faabf1a387f2d3371e2c892bc4a0fef5  subgraph_1_output_resnet_model_dense_BiasAdd_aquant_vart-sim-runner.bin
```

### 上板运行
``` console
% function d() { md5sum $1; stat -c %s $1; xxd $1 | head -n 16; }
% env XLNX_ENABLE_DUMP=1 \
    DEBUG_DPU_RUNNER=1 \
    DEBUG_DPU_RUNNER_DRY_RUN=0 \
    XLNX_ENABLE_FINGERPRINT_CHECK=1 \
    DEBUG_TENSOR_BUFFER_ALLOCATOR=1 \
    DEBUG_AP_START_CU_XVDPU=0 \
    DEBUG_XRT_DEVICE_HANDLE=1 \
    DEBUG_XRT_CU=9 \
    /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Debug/vart/dpu-runner/test/test_dpu_runner \
    /group/xbjlab/dphi_software/software/workspace/chunywan/debug_xvdpu/1.5/xvdpu_1.5_resnet_v1_50_prefetch.xmodel \
    subgraph_fake_downsample_0_ReplaceConv2d \
   /group/xbjlab/dphi_software/software/workspace/chunywan/debug_xvdpu/1.5/subgraph_1_input_image_aquant_vart-sim-runner.bin \
   1 1
```

### 比较输入

``` console
% d dump/subgraph_fake_downsample_0_ReplaceConv2d/input/1.image_aquant_upload_0.bin
b0d80b64f9ed4076284c820a7205b085  dump/subgraph_fake_downsample_0_ReplaceConv2d/input/1.image_aquant_upload_0.bin
% d /group/xbjlab/dphi_software/software/workspace/chunywan/debug_xvdpu/1.5/subgraph_1_input_image_aquant_vart-sim-runner.bin
b0d80b64f9ed4076284c820a7205b085  /group/xbjlab/dphi_software/software/workspace/chunywan/debug_xvdpu/1.5/subgraph_1_input_image_aquant_vart-sim-runner.bin
```

### 比较输出

``` console
% d ./dump/subgraph_fake_downsample_0_ReplaceConv2d/output/0.resnet_model_dense_BiasAdd_aquant_download_0.bin
% d ./dump/subgraph_fake_downsample_0_ReplaceConv2d/output/1.resnet_model_dense_BiasAdd_aquant_download_0.bin
% d ./dump/subgraph_fake_downsample_0_ReplaceConv2d/output/2.resnet_model_dense_BiasAdd_aquant_download_0.bin
faabf1a387f2d3371e2c892bc4a0fef5  ./dump/subgraph_fake_downsample_0_ReplaceConv2d/output/2.resnet_model_dense_BiasAdd_aquant_download_0.bin
% d /group/xbjlab/dphi_software/software/workspace/chunywan/debug_xvdpu/1.5/subgraph_1_output_resnet_model_dense_BiasAdd_aquant_vart-sim-runner.bin
faabf1a387f2d3371e2c892bc4a0fef5  /group/xbjlab/dphi_software/software/workspace/chunywan/debug_xvdpu/1.5/subgraph_1_output_resnet_model_dense_BiasAdd_aquant_vart-sim-runner.bin
```

performance test

## 配置和检查环境

``` console
% cd /usr/share/classification;ls
% cp /usr/share/vitis_ai_library/models/resnet50/resnet50.prototxt /group/xbjlab/dphi_software/software/workspace/chunywan/debug_xvdpu/1.5/mlp_res50_elp8_c32_0813.prototxt # on xbjlabdpsvr15
% which test_dpu_runner
% env LD_TRACE_LOADED_OBJECTS=1 `which test_dpu_runner` | grep vart
% vart_version
```

### 正式单张图片测试

``` console
% env DEEPHI_PROFILE=1 \
   DEBUG_BUFFER_OBJECT=1 \
   DEBUG_XRT_CU=0 \
   XLNX_SHOW_DPU_COUNTER=0 \
   DEBUG_DPU_RUNNER=0 \
  test_jpeg_classification  \
  /group/xbjlab/dphi_software/software/workspace/chunywan/debug_xvdpu/1.5/xvdpu_1.5_resnet_v1_50_prefetch.xmodel \
  sample_classification.jpg
```

测试结果

```
I0324 22:42:35.427969   614 xrt_cu.cpp:221] device_core_idx =0 handle =0xaaaacfd72120 time = 2865 time0 = 2882 ts0 = 0 ts1 = 4238602920650
I0324 22:42:35.427999   614 xrt_cu.cpp:106] Total: 2912us       ToDriver: 43us  ToCU: 41us      Complete: 2819us        Done: 8us
core_idx = 0  LSTART 585  LEND 585  CSTART 609  CEND 609  SSTART 1  SEND 1  MSTART 264  MEND 264  CYCLE_L 935054  CYCLE_H 0
```

用 `2819us` 的 DPU 时间换算成 FPS= 1064 。 935054 = 1068 FPS.

### 正式 E2E 多线程测试

``` console
% env \
  test_performance_classification  \
  /group/xbjlab/dphi_software/software/workspace/chunywan/debug_xvdpu/1.5/xvdpu_1.5_resnet_v1_50_prefetch.xmodel \
  -t 2 \
  -s 60 \
  test_performance_classification.list
```

```
FPS=1040.39
E2E_MEAN=5762.49
DPU_MEAN=3847.74
```

`1040/1064=97.7%`


### 参考测试，不包含前后处理的测试。

``` console
% env XLNX_ENABLE_DUMP=0 \
    /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Debug/vart/dpu-runner/test/test_dpu_runner_mt \
    /group/xbjlab/dphi_software/software/workspace/chunywan/debug_xvdpu/1.5/xvdpu_1.5_resnet_v1_50_prefetch.xmodel \
   resnet50_0 2
```

测试结果

```
I0324 22:54:58.194833   686 performance_test.hpp:77] FPS= 1054.5 number_of_frames= 63276 time= 60.0057 seconds.
```

`1054/1064=99.0%`


## caffe resnet50 v1.0 的测试。

``` console
% cp /usr/share/vitis_ai_library/models/resnet50/resnet50.prototxt /group/xbjlab/dphi_software/software/workspace/chunywan/debug_xvdpu/1.0/resnet_v1_50_DPUCVDX8G_ISA0_B8192C32B1_ELP8_sim.prototxt
% env \
   DEBUG_XRT_CU=9 \
   XLNX_SHOW_DPU_COUNTER=1 \
   DEBUG_DPU_RUNNER=1 \
   XLNX_ENABLE_FINGERPRINT_CHECK=0 \
   test_jpeg_classification  \
  /group/xbjlab/dphi_software/software/workspace/chunywan/debug_xvdpu/1.0/resnet_v1_50_DPUCVDX8G_ISA0_B8192C32B1_ELP8_sim.xmodel \
  sample_classification.jpg

I0325 04:31:58.975815   977 xrt_cu.cpp:106] Total: 3081us       ToDriver: 332us ToCU: 21us      Complete: 2634us        Done: 92us
core_idx = 0  LSTART 589  LEND 589  CSTART 576  CEND 576  SSTART 1  SEND 1  MSTART 274  MEND 274  CYCLE_L 873457  CYCLE_H 0

```

按照 counter 计算的 , `873457 cycles = 1143 FPS`

``` console
% env \
   DEBUG_DPU_RUNNER=0 \
   XLNX_ENABLE_FINGERPRINT_CHECK=0 \
   DEBUG_AP_START_CU_XVDPU=0 \
  test_performance_classification  \
  /group/xbjlab/dphi_software/software/workspace/chunywan/debug_xvdpu/1.0/resnet_v1_50_DPUCVDX8G_ISA0_B8192C32B1_ELP8_sim.xmodel \
  -t 2 \
  -s 60 \
  test_performance_classification.list
```

```
FPS=1116.74
E2E_MEAN=5368.07
DPU_MEAN=3427.88
```

`1116.74/1143=97.7%`


``` console
% env XLNX_ENABLE_DUMP=0 \
    DEBUG_DPU_RUNNER_DRY_RUN=0 \
    XLNX_ENABLE_FINGERPRINT_CHECK=0 \
    DEBUG_TENSOR_BUFFER_ALLOCATOR=0 \
    DEBUG_AP_START_CU_XVDPU=0 \
    DEBUG_XRT_DEVICE_HANDLE=0 \
   test_dpu_runner_mt \
   /group/xbjlab/dphi_software/software/workspace/chunywan/debug_xvdpu/1.0/resnet_v1_50_DPUCVDX8G_ISA0_B8192C32B1_ELP8_sim.xmodel \
   resnet50_0 2

I0325 04:37:29.260725   982 performance_test.hpp:77] FPS= 1138.83 number_of_frames= 68337 time= 60.0062 seconds.
```

`1138.83/1143=99.6%`
`

## troubleshooting


NOTE

    目前不支持保存 uboot 参数，需要登陆 `xbjlabdpwstn02` 连接串口，在 uboot 启动的时候，修改启动参数

```
% ssh xbjlabdpwstn02
% /tools/xgs/bin/sudo cu -l /dev/ttyUSB1 -s 115200
uboot> setenv  bootargs "console=ttyAMA0 earlycon=pl011,mmio32,0xFF000000,115200n8 clk_ignore_unused root=/dev/mmcblk0p2 rw rootwait"
uboot> boot
```

更新驱动

```
% rmmod zocl
% insmod /home/root/zocl.ko
```


用下面的方法验证一下，是否可以分配 lpddr 上的内存。


```
% test_alloc_bo 1
```

``` console
%  sshpass -p root ssh root@10.176.178.176;
%  sshpass -p root ssh root@10.176.179.67;
% while sleep 1; do ping -c 1 -w 1 10.176.178.176 && sshpass -p root ssh root@10.176.178.176; done
% sshpass -p root ssh root@10.176.179.54
% mkdir -p /group/xbjlab
% mount -t nfs -o nolock 10.176.178.33:/group_xbjlab/ /group/xbjlab
% export LD_LIBRARY_PATH=/group/xbjlab/dphi_software/software/workspace/chunywan/petalinux-sdk2/sysroots/aarch64-xilinx-linux/install/Debug/lib
% mkdir -p /home/root/wcy/; cd /home/root/wcy;ls
% /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Debug/vart/xrt-device-handle/xrt_read_register \
  /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/vart/xrt-device-handle/test/reg_xvdpu_hack.conf D 0
% /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Release/vart/dpu-controller/show_dpu
% xbutil query
% ls /group/xbjlab/dphi_software/software/workspace/guohaot/to_haotian/
% /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Release/test_alloc_bo 1
% env XLNX_ENABLE_DUMP=1 \
    DEBUG_DPU_RUNNER=1 \
    DEBUG_TENSOR_BUFFER_ALLOCATOR=1 \
    XLNX_SHOW_DPU_COUNTER=1 \
   /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Release/vart/dpu-runner/test/test_dpu_runner \
    /group/xbjlab/dphi_software/software/workspace/chunywan/debug_xvdpu/1.5/xvdpu_1.5_resnet_v1_50_prefetch.xmodel \
   resnet50_0 \
   /group/xbjlab/dphi_software/software/workspace/guohaot/to_haotian/golden/dump_results_1/input_aquant.bin \
   1 1
% cat /proc/interrupts | grep zocl
% xbutil query; /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Debug/vart/xrt-device-handle/xrt_read_register /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/vart/xrt-device-handle/test/reg_xvdpu.conf xv 0
% env XLNX_ENABLE_DUMP=0 XLNX_XRT_CU_DRY_RUN=0 XLNX_ENABLE_FINGERPRINT_CHECK=0  DEBUG_XRT_DEVICE_HANDLE=1 DEBUG_XRT_CU=9 DEBUG_AP_START_CU_CLOUD=1 DEBUG_DPU_CONTROLLER=1 XLNX_SHOW_DPU_COUNTER=1  DEBUG_DPU_RUNNER=1  /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Debug/vart/dpu-runner/test/test_dpu_runner  ../to_haotian/res50_llw_elp8_reorder_tyr.xmodel  resnet50_0 ~/dump/resnet50_0/input/0.resnet50_0_INPUT_0.bin  1 1;
% while sleep 1; do env XLNX_ENABLE_DUMP=0 XLNX_XRT_CU_DRY_RUN=0 XLNX_ENABLE_FINGERPRINT_CHECK=0  DEBUG_XRT_DEVICE_HANDLE=1 DEBUG_XRT_CU=9 DEBUG_AP_START_CU_CLOUD=1 DEBUG_DPU_CONTROLLER=1 XLNX_SHOW_DPU_COUNTER=1  DEBUG_DPU_RUNNER=1  /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Debug/vart/dpu-runner/test/test_dpu_runner  ../to_haotian/res50_llw_elp8_reorder_tyr.xmodel  resnet50_0 ~/dump/resnet50_0/input/0.resnet50_0_INPUT_0.bin  1 1;done
%
% function d() { md5sum $1; stat -c %s $1; xxd $1 | head -n 16; }
% ls /group/xbjlab/dphi_software/software/workspace/guohaot/to_haotian/golden/

% d ./dump/subgraph_resnet_v1_50_block1_unit_1_bottleneck_v1_add/input/0.input_aquant_upload_0.bin
% d ./dump/subgraph_resnet_v1_50_block1_unit_1_bottleneck_v1_add/output/0.resnet_v1_50_predictions_Reshape_aquant_download_0.bin
% d /group/xbjlab/dphi_software/software/workspace/guohaot/to_haotian/golden/dump_results_1/resnet_v1_50_logits_BiasAdd_aquant.bin
% d /group/xbjlab/dphi_software/software/workspace/guohaot/to_haotian/golden/dump_results_1/ | grep 1000
% /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Debug/vart/buffer-object/mem_read 0x60100000 25530472 | md5sum
63cede554986d34636d46b2c27cc4605  -
% /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Debug/xir/tools/xir dump_txt ../to_haotian/res50_llw_elp8_reorder_tyr.xmodel ../to_haotian/res50_llw_elp8_reorder_tyr.txt
```

## work log

### 08-Sep-20

``` console
% ssh xcdl190253
% ls -l /wrk/dpcollab/vitis_xvdpu/xvdpu_vck190_SDfiles/NewXvdpu_Lpddr1600M/sd_card
```


``` console
% mkdir -p $HOME/build/bit/0908; cd $HOME/build/bit/0908
% scp xcdl190253:/wrk/dpcollab/vitis_xvdpu/xvdpu_vck190_SDfiles/NewXvdpu_Lpddr1600M/sd_card/BOOT.BIN BOOT.BIN.0908
% scp xcdl190253:/wrk/dpcollab/vitis_xvdpu/xvdpu_vck190_SDfiles/NewXvdpu_Lpddr1600M/sd_card/DPUCVDX8G_final_20200905.xclbin DPUCVDX8G_final_20200905.xclbin
% md5sum DPUCVDX8G_final_20200905.xclbin BOOT.BIN.0908
% sshpass -p root scp BOOT.BIN.0908 DPUCVDX8G_final_20200905.xclbin root@10.176.178.176:/mnt/sd-mmcblk0p1/
```

``` console
% sshpass -p root ssh root@10.176.178.176
% cd /mnt/sd-mmcblk0p1/
% cp DPUCVDX8G_final_20200905.xclbin /usr/lib/dpu.xclbin
% cp BOOT.BIN.0908 BOOT.BIN
% md5sum BOOT.BIN /usr/lib/dpu.xclbin
```

``` console
%
% env XLNX_ENABLE_DUMP=0 \
     /group/xbjlab/dphi_software/software/workspace/mingyue/build/build.linux.2020.1.aarch64.Release/vart/dpu-runner/test/test_dpu_runner_mt \
     /group/xbjlab/dphi_software/software/workspace/chunywan/debug_xvdpu/1.5/xvdpu_1.5_resnet_v1_50_prefetch.xmodel \
    resnet50_0 2
```


### 09-Sep-20

``` console
% ssh xcdl190253
% find /group/dphi_edge/workspace/davidxu/share/versal_bootbin/xvdpu_v0_1_0_18_expert_dbg1C4_load2/sd_card
```


``` console
% mkdir -p $HOME/build/bit/0909; cd $HOME/build/bit/0909
% scp xcdl190253:/group/dphi_edge/workspace/davidxu/share/versal_bootbin/xvdpu_v0_1_0_18_expert_dbg1C4_load2/sd_card/BOOT.BIN BOOT.BIN.0907
% scp xcdl190253:/group/dphi_edge/workspace/davidxu/share/versal_bootbin/xvdpu_v0_1_0_18_expert_dbg1C4_load2/sd_card/DPUCVDX8G_final_20200907.xclbin .
% md5sum BOOT.BIN.0907 DPUCVDX8G_final_20200907.xclbin
% sshpass -p root scp BOOT.BIN.0907 DPUCVDX8G_final_20200907.xclbin root@10.176.179.54:/mnt/sd-mmcblk0p1/
```

``` console
% sshpass -p root ssh root@10.176.179.54
% cd /mnt/sd-mmcblk0p1/
% cp DPUCVDX8G_final_20200907.xclbin /usr/lib/dpu.xclbin; cp BOOT.BIN.0907 BOOT.BIN
% md5sum BOOT.BIN /usr/lib/dpu.xclbin
% sync;sync;sync;
% reboot
```

``` console
% sshpass -p root ssh root@10.176.179.54
% ls
% ./xrt_read_register reg_xvdpu.conf D 0
% mkdir -p /group/xbjlab
% mount -t nfs -o nolock 10.176.178.33:/group_xbjlab/ /group/xbjlab
% cp -av /group/xbjlab/dphi_software/software/workspace/chunywan/debug_xvdpu/1.5/subgraph_1_input_image_aquant_vart-sim-runner.bin input.data
% env XLNX_ENABLE_DUMP=1 \
     /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Release/vart/dpu-runner/test/test_dpu_runner  \
    classification/xvdpu_1.5_resnet_v1_50_prefetch/xvdpu_1.5_resnet_v1_50_prefetch.xmodel \
    resnet50_0 \
    input.data \
    1 1
% md5sum ./dump/subgraph_fake_downsample_0_ReplaceConv2d/output/{0,1,2}.resnet_model_dense_BiasAdd_aquant_download_0.bin
% env  \
    /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Release/vart/dpu-runner/test/test_dpu_runner_mt classification/xvdpu_1.5_resnet_v1_50_prefetch/xvdpu_1.5_resnet_v1_50_prefetch.xmodel \
    resnet50_0 \
    4
%
```


### load = 1

``` console
% mkdir -p $HOME/build/bit/0909; cd $HOME/build/bit/0909
% scp xcdl190253:/group/dphi_edge/workspace/davidxu/share/versal_bootbin/xvdpu_v0_1_0_18_expert_dbg1C4_load1/BOOT.BIN BOOT.BIN.0908.LOAD.1
% scp xcdl190253:/group/dphi_edge/workspace/davidxu/share/versal_bootbin/xvdpu_v0_1_0_18_expert_dbg1C4_load1/sd_card/DPUCVDX8G_final_20200908.xclbin DPUCVDX8G_final_20200908.xclbin.LOAD.1
% md5sum BOOT.BIN.0908.LOAD.1 DPUCVDX8G_final_20200908.xclbin.LOAD.1
% sshpass -p root scp BOOT.BIN.0908.LOAD.1 DPUCVDX8G_final_20200908.xclbin.LOAD.1 root@10.176.179.54:/mnt/sd-mmcblk0p1/
% sshpass -p root ssh root@10.176.179.54 "cd /mnt/sd-mmcblk0p1/; cp DPUCVDX8G_final_20200908.xclbin.LOAD.1 /usr/lib/dpu.xclbin; cp BOOT.BIN.0908.LOAD.1 BOOT.BIN;md5sum BOOT.BIN /usr/lib/dpu.xclbin"
% sshpass -p root ssh root@10.176.179.54 " sync;sync;sync;reboot"
```


### Load i=2 dbg1CC

``` console
% mkdir -p $HOME/build/bit/0909; cd $HOME/build/bit/0909
% ssh xcdl190253 find /group/dphi_edge/workspace/davidxu/share/versal_bootbin/xvdpu_v0_1_0_18_expert_dbg1CC_load2
% scp xcdl190253:/group/dphi_edge/workspace/davidxu/share/versal_bootbin/xvdpu_v0_1_0_18_expert_dbg1CC_load2/BOOT.BIN BOOT.BIN.xvdpu_v0_1_0_18_expert_dbg1CC_load2
% scp xcdl190253:/group/dphi_edge/workspace/davidxu/share/versal_bootbin/xvdpu_v0_1_0_18_expert_dbg1CC_load2/sd_card/DPUCVDX8G_final_20200909.xclbin DPUCVDX8G_final_20200909.xclbin.xvdpu_v0_1_0_18_expert_dbg1CC_load2
% md5sum BOOT.BIN.xvdpu_v0_1_0_18_expert_dbg1CC_load2 DPUCVDX8G_final_20200909.xclbin.xvdpu_v0_1_0_18_expert_dbg1CC_load2
% sshpass -p root scp BOOT.BIN.xvdpu_v0_1_0_18_expert_dbg1CC_load2 root@10.176.179.54:/mnt/sd-mmcblk0p1/BOOT.BIN
% sshpass -p root scp DPUCVDX8G_final_20200909.xclbin.xvdpu_v0_1_0_18_expert_dbg1CC_load2 root@10.176.179.54:/usr/bin/dpu.xclbin
% sshpass -p root ssh root@10.176.179.54 "cd /mnt/sd-mmcblk0p1/; md5sum BOOT.BIN /usr/lib/dpu.xclbin"
%  sshpass -p root ssh root@10.176.179.54 " sync;sync;sync;reboot"
```
