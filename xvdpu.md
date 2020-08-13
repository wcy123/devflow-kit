## debug xv dpu

NOTE:

    1. `XLNX_DIRTY_HACK_XVDPU_GEN_BASE` 调整寄存器基地址的其实偏移量。
    2. `DEBUG_AP_START_CU_XVDPU` 目前 `EXEC_WRITE` 方式还起不来
    3. `XLNX_ENABLE_FINGERPRINT_CHECK` 目前模型指纹和硬件指纹还对不上


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
% /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Debug/test_alloc_bo 1
```




```

``` console
% while sleep 1; do ping -c 1 -w 1 10.176.178.176 && sshpass -p root ssh root@10.176.178.176; done
% sshpass -p root ssh root@10.176.179.54
% mkdir -p /group/xbjlab
% mount -t nfs -o nolock 10.176.178.33:/group_xbjlab/ /group/xbjlab
% export LD_LIBRARY_PATH=/group/xbjlab/dphi_software/software/workspace/chunywan/petalinux-sdk2/sysroots/aarch64-xilinx-linux/install/Release/lib
% mkdir -p /home/root/wcy/; cd /home/root/wcy;ls
% /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Debug/vart/xrt-device-handle/xrt_read_register \
  /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/vart/xrt-device-handle/test/reg_xvdpu_hack.conf D 0
% /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Debug/vart/dpu-controller/show_dpu
% xbutil query
% ls /group/xbjlab/dphi_software/software/workspace/guohaot/to_haotian/
% /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Debug/test_alloc_bo 1
% env XLNX_ENABLE_DUMP=0 \
    XLNX_DIRTY_HACK_XVDPU_GEN_BASE=0x200 \
    XLNX_XRT_CU_DRY_RUN=0 \
    DEBUG_DPU_RUNNER=1 \
    DEBUG_DPU_RUNNER_DRY_RUN=0 \
    XLNX_ENABLE_FINGERPRINT_CHECK=0 \
    DEBUG_TENSOR_BUFFER_ALLOCATOR=1 \
    DEBUG_AP_START_CU_XVDPU=0 \
    DEBUG_XRT_DEVICE_HANDLE=1 \
    DEBUG_XRT_CU=9 \
    XLNX_SHOW_DPU_COUNTER=1 \
   /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Release/vart/dpu-runner/test/test_dpu_runner \
   /group/xbjlab/dphi_software/software/workspace/guohaot/to_haotian/res50_llw_elp8_reorder_tyr.xmodel \
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

performance test

``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/vitis-ai-library-samples-res/samples/classification;ls
% export LD_LIBRARY_PATH=/group/xbjlab/dphi_software/software/workspace/chunywan/petalinux-sdk2/sysroots/aarch64-xilinx-linux/install/Release/lib
% env LD_TRACE_LOADED_OBJECTS=1 /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Release/vart/dpu-runner/test/test_dpu_runner | grep vart
% # do it on xbjlabdpsvr15
% cp -av /group/xbjlab/dphi_software/software/workspace/guohaot/to_haotian/res50_llw_elp8_reorder_tyr.xmodel /group/xbjlab/dphi_software/software/workspace/chunywan/xvdpu
% cp -av /usr/share/vitis_ai_library/models/resnet50/resnet50.prototxt /group/xbjlab/dphi_software/software/workspace/chunywan/xvdpu/res50_llw_elp8_reorder_tyr.prototxt
% env \
   DEBUG_DPU_RUNNER=0 \
   XLNX_ENABLE_FINGERPRINT_CHECK=0 \
  /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Release/Vitis-AI-Library/overview/test_jpeg_classification  \
  /group/xbjlab/dphi_software/software/workspace/chunywan/xvdpu/res50_llw_elp8_reorder_tyr.xmodel \
  sample_classification.jpg

% ls
% env \
   DEBUG_DPU_RUNNER=0 \
   XLNX_ENABLE_FINGERPRINT_CHECK=0 \
   XLNX_DIRTY_HACK_XVDPU_GEN_BASE=0x200 \
   DEBUG_AP_START_CU_XVDPU=0 \
  /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Release/Vitis-AI-Library/overview/test_performance_classification  \
  /group/xbjlab/dphi_software/software/workspace/chunywan/xvdpu/res50_llw_elp8_reorder_tyr.xmodel \
  -t 2 \
  -s 60 \
  test_performance_classification.list

% env XLNX_ENABLE_DUMP=0 \
    XLNX_DIRTY_HACK_XVDPU_GEN_BASE=0x200 \
    DEBUG_DPU_RUNNER_DRY_RUN=0 \
    XLNX_ENABLE_FINGERPRINT_CHECK=0 \
    DEBUG_TENSOR_BUFFER_ALLOCATOR=0 \
    DEBUG_AP_START_CU_XVDPU=0 \
    DEBUG_XRT_DEVICE_HANDLE=0 \
   /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Debug/vart/dpu-runner/test/test_dpu_runner_mt \
   /group/xbjlab/dphi_software/software/workspace/guohaot/to_haotian/res50_llw_elp8_reorder_tyr.xmodel \
   resnet50_0 2
% env XLNX_ENABLE_DUMP=0 \
    XLNX_DIRTY_HACK_XVDPU_GEN_BASE=0x200 \
    DEBUG_DPU_RUNNER_DRY_RUN=0 \
    XLNX_ENABLE_FINGERPRINT_CHECK=0 \
    DEBUG_TENSOR_BUFFER_ALLOCATOR=0 \
    DEBUG_AP_START_CU_XVDPU=0 \
    DEBUG_XRT_DEVICE_HANDLE=0 \
   /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Debug/vart/dpu-runner/test/test_dpu_runner_mt \
   /group/xbjlab/dphi_software/software/workspace/chunywan/debug_xvdpu/1.0/resnet_v1_50_DPUCVDX8G_ISA0_B8192C32B1_ELP8_sim.xmodel \
   resnet50_0 2
```




## 对数

``` console
% scp xcdl190253:/group/dphi_edge/workspace/dylanwu/chunye/res50_v100_llw_elp8_naie/*.bin /group/xbjlab/dphi_software/software/workspace/chunywan/debug_xvdpu/to_Chunye/
% ls  /group/xbjlab/dphi_software/software/workspace/chunywan/debug_xvdpu/to_Chunye/
% function d() { md5sum $1; stat -c %s $1; xxd $1 | head -n 16; }
# 上板运行
% env XLNX_ENABLE_DUMP=1 \
    XLNX_DIRTY_HACK_XVDPU_GEN_BASE=0x200 \
    XLNX_XRT_CU_DRY_RUN=0 \
    DEBUG_DPU_RUNNER=1 \
    DEBUG_DPU_RUNNER_DRY_RUN=0 \
    XLNX_ENABLE_FINGERPRINT_CHECK=0 \
    DEBUG_TENSOR_BUFFER_ALLOCATOR=1 \
    DEBUG_AP_START_CU_XVDPU=0 \
    DEBUG_XRT_DEVICE_HANDLE=1 \
    DEBUG_XRT_CU=9 \
   /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Debug/vart/dpu-runner/test/test_dpu_runner \
   /group/xbjlab/dphi_software/software/workspace/chunywan/debug_xvdpu/1.0/resnet_v1_50_DPUCVDX8G_ISA0_B8192C32B1_ELP8_sim.xmodel \
   resnet50_0 \
   /group/xbjlab/dphi_software/software/workspace/guohaot/to_haotian/golden/dump_results_1/input_aquant.bin \
   1 1
# 比较输入
% d dump/subgraph_resnet_v1_50_block1_unit_1_bottleneck_v1_add/input/0.input_aquant_upload_0.bin
b0d80b64f9ed4076284c820a7205b085  dump/subgraph_resnet_v1_50_block1_unit_1_bottleneck_v1_add/input/0.input_aquant_upload_0.bin
% d subgraph_1_input_input_aquant_vart-sim-runner.bin
b0d80b64f9ed4076284c820a7205b085  /group/xbjlab/dphi_software/software/workspace/chunywan/debug_xvdpu/1.0/subgraph_1_input_input_aquant_vart-sim-runner.bin
% d /group/xbjlab/dphi_software/software/workspace/guohaot/to_haotian/golden/dump_results_1/input_aquant.bin
b0d80b64f9ed4076284c820a7205b085
% d /group/xbjlab/dphi_software/software/workspace/chunywan/debug_xvdpu/to_Chunye/subgraph_1_input_input_aquant_vart-sim-runner.bin
b0d80b64f9ed4076284c820a7205b085  /group/xbjlab/dphi_software/software/workspace/chunywan/debug_xvdpu/to_Chunye/subgraph_1_input_input_aquant_vart-sim-runner.bin

# 比较输出
% d /group/xbjlab/dphi_software/software/workspace/guohaot/to_haotian/golden/dump_results_1/resnet_v1_50_predictions_Reshape_aquant.bin
9cbf3391839a820be18c6f33364dfea4  /group/xbjlab/dphi_software/software/workspace/guohaot/to_haotian/golden/dump_results_1/resnet_v1_50_predictions_Reshape_aquant.bin
% d /group/xbjlab/dphi_software/software/workspace/chunywan/debug_xvdpu/1.0/subgraph_1_output_resnet_v1_50_predictions_Reshape_aquant_vart-sim-runner.bin

% d dump/subgraph_resnet_v1_50_block1_unit_1_bottleneck_v1_add/output/0.resnet_v1_50_predictions_Reshape_aquant_download_0.bin
9cbf3391839a820be18c6f33364dfea4  dump/subgraph_resnet_v1_50_block1_unit_1_bottleneck_v1_add/output/0.resnet_v1_50_predictions_Reshape_aquant_download_0.bin
% /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Debug/vart/buffer-object/mem_read 0x501f0100000 1000 > o.bin
% d o.bin
```
