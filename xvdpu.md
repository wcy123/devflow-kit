## debug xv dpu

NOTE:

    1. `XLNX_DIRTY_HACK_XVDPU_GEN_BASE` 调整寄存器基地址的其实偏移量。
    2. `DEBUG_AP_START_CU_XVDPU` 目前 `EXEC_WRITE` 方式还起不来
    3. `XLNX_ENABLE_FINGERPRINT_CHECK` 目前模型指纹和硬件指纹还对不上


``` console
% sshpass -p root ssh root@10.176.178.176
% sshpass -p root ssh root@10.176.179.54
% mkdir -p /group/xbjlab
% mount -t nfs -o nolock 10.176.178.33:/group_xbjlab/ /group/xbjlab
% export LD_LIBRARY_PATH=/group/xbjlab/dphi_software/software/workspace/chunywan/petalinux-sdk2/sysroots/aarch64-xilinx-linux/install/Debug/lib
% mkdir -p /home/root/wcy/; cd /home/root/wcy;ls
% /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Debug/vart/xrt-device-handle/xrt_read_register \
  /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/vart/xrt-device-handle/test/reg_xvdpu_hack.conf D 0
% /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Debug/vart/dpu-controller/show_dpu
% xbutil query
% ls /group/xbjlab/dphi_software/software/workspace/guohaot/to_haotian/
% /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Debug/test_alloc_bo 1
% env XLNX_ENABLE_DUMP=0 \
    XLNX_DIRTY_HACK_XVDPU_GEN_BASE=0x60 \
    XLNX_XRT_CU_DRY_RUN=0 \
    DEBUG_DPU_RUNNER=1 \
    DEBUG_DPU_RUNNER_DRY_RUN=0 \
    XLNX_ENABLE_FINGERPRINT_CHECK=0 \
    DEBUG_TENSOR_BUFFER_ALLOCATOR=1 \
    DEBUG_AP_START_CU_XVDPU=1 \
    DEBUG_XRT_DEVICE_HANDLE=1 \
    DEBUG_XRT_CU=9 \
   /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Debug/vart/dpu-runner/test/test_dpu_runner \
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
% d /group/xbjlab/dphi_software/software/workspaced/guohaot/to_haotian/golden/dump_results_1/input_aquant.bin
% d /group/xbjlab/dphi_software/software/workspace/guohaot/to_haotian/golden/dump_results_1/resnet_v1_50_predictions_Reshape_aquant.bin
% d ./dump/subgraph_resnet_v1_50_block1_unit_1_bottleneck_v1_add/input/0.input_aquant_upload_0.bin
% d ./dump/subgraph_resnet_v1_50_block1_unit_1_bottleneck_v1_add/output/0.resnet_v1_50_predictions_Reshape_aquant_download_0.bin
% d /group/xbjlab/dphi_software/software/workspace/guohaot/to_haotian/golden/dump_results_0/resnet_v1_50_logits_BiasAdd_aquant.bin
% d /group/xbjlab/dphi_software/software/workspace/guohaot/to_haotian/golden/dump_results_0/ | grep 1000
% /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Debug/vart/buffer-object/mem_read 0x60100000 25530472 | md5sum
63cede554986d34636d46b2c27cc4605  -
% /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Debug/xir/tools/xir dump_txt ../to_haotian/res50_llw_elp8_reorder_tyr.xmodel ../to_haotian/res50_llw_elp8_reorder_tyr.txt
```

performance test
24
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
   XLNX_DIRTY_HACK_XVDPU_GEN_BASE=0x60 \
   DEBUG_AP_START_CU_XVDPU=1 \
  /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Release/Vitis-AI-Library/overview/test_jpeg_classification  \
  /group/xbjlab/dphi_software/software/workspace/chunywan/xvdpu/res50_llw_elp8_reorder_tyr.xmodel \
  sample_classification.jpg

% env \
   DEBUG_DPU_RUNNER=0 \
   XLNX_ENABLE_FINGERPRINT_CHECK=0 \
   XLNX_DIRTY_HACK_XVDPU_GEN_BASE=0x60 \
   DEBUG_AP_START_CU_XVDPU=1 \
  /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Release/Vitis-AI-Library/overview/test_performance_classification  \
  /group/xbjlab/dphi_software/software/workspace/chunywan/xvdpu/res50_llw_elp8_reorder_tyr.xmodel \
  -t 4 \
  -s 60 \
  test_performance_classification.list
```



```
root@xilinx-vck190-2020_1:~/wcy# d ./dump/subgraph_resnet_v1_50_block1_unit_1_bottleneck_v1_add/output/0.resnet_v1_50_predictions_Reshape_aquant_download_0.bin
a6439aa6b0e454c986d6811008d3aae6  ./dump/subgraph_resnet_v1_50_block1_unit_1_bottleneck_v1_add/output/0.resnet_v1_50_predictions_Reshape_aquant_download_0.bin
1000
00000000: 0e0c 0308 0e1b 1304 02fd fa01 f8fb 07ff  ................
00000010: f2fe 04fe 01f6 fcf9 0104 03ff 020c 0405  ................
00000020: 000d 0e15 180e f9fc fbfc fdf9 070b 07fc  ................
00000030: 0104 0000 0303 fd11 fcf6 01fd 04ff fd02  ................
00000040: 0a19 fcf8 f30b fb06 f707 0204 0207 0403  ................
00000050: fdfb 00ff 16ff 0a06 07fe 00f7 f5f6 fbfc  ................
00000060: fc11 f5fa 04ff 050f fc00 040d 143b 0c11  .............;..
00000070: 1413 1117 0f0d 0812 030a 0415 0b12 13fa  ................
00000080: 04fa fafa f3f7 fcf9 fdfe fef9 fbf9 f2f6  ................
00000090: f604 f700 0014 0b02 f504 0000 fb01 03fb  ................
000000a0: f4fd fb03 06ff 00f8 01f5 f904 fbfb fefb  ................
000000b0: f7fc fff9 fb04 fe09 05ff f6ff fcfe 0210  ................
000000c0: 01ff 0206 fd02 fe05 f9fe 0500 fe00 0e05  ................
000000d0: 020c f8fc f901 fffb 05fd fc04 fc06 03fa  ................
000000e0: 0604 04fd 000a fd07 ff00 00fc fc0c 0105  ................
000000f0: 02fe 0203 f700 fb04 f9fc f904 fb00 02fb  ................
root@xilinx-vck190-2020_1:~/wcy# d  ~/dump/resnet50_0/output/0.fc1000_55.bin
ae675c267f3e3e077d4d39a7f135e8d6  /home/root/dump/resnet50_0/output/0.fc1000_55.bin
1000
00000000: 0f0f fe0b 0c27 200c 0aff 010c fcff 0005  .....' .........
00000010: 01fd 0902 0df6 fefe fd02 0705 000f 060b  ................
00000020: 040e 050d 120b f9ff fff9 f9fc 0405 06fe  ................
00000030: 0303 fbfd 03ff fc18 f6f7 0502 0800 f604  ................
00000040: 0d23 01fa f60f 0406 fc09 040a 070b 0b02  .#..............
00000050: 0104 0502 0903 0e02 02fd 03fa f7f5 fcfb  ................
00000060: fd0d fbff 0504 060c fffc 0314 2048 1910  ............ H..
00000070: 1618 1520 1b0e 0e1d 0b0f 061a 0d15 17fa  ... ............
00000080: fefa fcf9 f0fd 01f9 fb01 01fc 02ff f800  ................
00000090: f803 fafe f616 0a01 f504 fdf5 f6fd 02f8  ................
000000a0: f3f9 fc02 03fb fef7 fdf1 f700 f8fb f8f8  ................
000000b0: f5f9 fdfe fc01 fd06 02fd f4f8 00fe fe0a  ................
000000c0: faff f900 f801 fb01 f900 fafa fcf9 0b01  ................
000000d0: 0007 f9fe f6fc 00fb 01f9 fb01 f907 f9f8  ................
000000e0: 0400 fcfd f806 fb03 fefd faf3 fc0d fd00  ................
```
