## cu_base_addr

```
ssh -p 10116 mingyue@xbj-pvapjmp11

export LD_LIBRARY_PATH=/opt/xilinx/xrt/lib:/usr/local/lib:/usr/local/lib64:/home/mingyue/.local/CentOS.7.6.1810.x86_64.Debug/lib

cd $HOME/d/working/cloud_test/resnet_v1_50_tf

env DEBUG_XRT_DEVICE_HANDLE=1 XLNX_GOLDEN_DIR=dump_results_1 XLNX_EBABLE_CLEAR=0 DEBUG_DPU_RUNNER=1 DEBUG_DPU_CONTROLLER=1 XLNX_ENABLE_DEBUG_MODE=0 XLNX_ENABLE_UPLOAD=0 XLNX_ENABLE_DUMP_PARAMTER=0 XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_ENABLE_DUMP=0 XLNX_SHOW_DPU_COUNTER=1 /home/mingyue/build/build.CentOS.7.6.1810.x86_64.Debug/vart/dpu-runner/test/test_dpu_runner resnet_v1_50_tf/resnet_v1_50_tf.xmodel resnet50_v1_50_0 dump_results_1/input_aquant.bin 4 1 2>a.log 1>&2

lspci -vvvxxx >1.log



```
