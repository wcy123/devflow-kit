
```
ssh root@10.176.179.60
mount -t nfs -o nolock 10.176.178.33:/group_xbjlab/ /group/xbjlab
export LD_LIBRARY_PATH=/group/xbjlab/dphi_software/software/workspace/mingyue/d/working/aisw/petalinux_sdk/sysroots/aarch64-xilinx-linux/install/Debug/lib/

env DEBUG_DPU_RUNNER=1 DEBUG_XRT_DEVICE_HANDLE=1 DEBUG_DPU_CONTROLLER=1 DEBUG_BUFFER_OBJECT=1 XLNX_GOLDEN_DIR=resnet_v1_50_tf_0/dump_results_1 XLNX_ENABLE_DUMP=1 /group/xbjlab/dphi_software/software/workspace/mingyue/build/build.linux.2020.1.aarch64.Debug/vart/dpu-runner/test/test_dpu_runner  /usr/share/vitis_ai_library/models/resnet_v1_50_tf/resnet_v1_50_tf.elf resnet_v1_50_tf_0 resnet_v1_50_tf/dump_results_1/input_aquant.bin 1 1


gdb /group/xbjlab/dphi_software/software/workspace/mingyue/build/build.linux.2020.1.aarch64.Debug/vart/dpu-runner/test/test_dpu_runner
set env DEBUG_DPU_RUNNER=1
set env DEBUG_XRT_DEVICE_HANDLE=1
set env DEBUG_DPU_CONTROLLER=1
set env DEBUG_BUFFER_OBJECT=1
set env XLNX_GOLDEN_DIR=resnet_v1_50_tf_0/dump_results_1
run /usr/share/vitis_ai_library/models/resnet_v1_50_tf/resnet_v1_50_tf.elf resnet_v1_50_tf_0 resnet_v1_50_tf/dump_results_1/input_aquant.bin 1 1




```


```
ssh root@10.176.179.65
mount -t nfs -o nolock 10.176.178.33:/group_xbjlab/ /group/xbjlab
export LD_LIBRARY_PATH=/group/xbjlab/dphi_software/software/workspace/mingyue/d/working/aisw/petalinux_sdk/sysroots/aarch64-xilinx-linux/install/Debug/lib/
cd test_zero_copy

env DEBUG_DPU_RUNNER=1 XLNX_SHOW_DPU_COUNTER=1 XLNX_ENABLE_DUMP=0 DEBUG_SFM_RUNNER=1 /group/xbjlab/dphi_software/software/workspace/mingyue/build/build.linux.2020.1.aarch64.Debug/Vitis-AI-Library/overview/test_jpeg_classification resnet50 ~/Vitis-AI/vitis_ai_library/samples/classification/sample_classification.jpg
mv dump dump_jpeg

env DEBUG_DPU_RUNNER=1 XLNX_SHOW_DPU_COUNTER=1 XLNX_ENABLE_DUMP=0 DEBUG_SFM_RUNNER=1 DEBUG_TENSOR_BUFFER_ALLOCATOR=1 /group/xbjlab/dphi_software/software/workspace/mingyue/build/build.linux.2020.1.aarch64.Debug/vart/dpu-runner/test/resnet50_zero_copy /usr/share/vitis_ai_library/models/resnet50/resnet50.xmodel ~/Vitis-AI/vitis_ai_library/samples/classification/sample_classification.jpg

```
end
