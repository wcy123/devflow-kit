# work log for mlperf


```
ssh xsjjump03
ssh demo@xsjfislx40

target_factory :  4b6615e59a3630b14eab8d3734e54c1280879552
unilog  : 27fb298ddbb876684652ac29bdf7bd5e30f2d391
xir : 21fae71a944698220a4e3d21f509a3ea38b642e1
vart : gits@xcdl190260:wangchunye/vart.git: feat-async-runner :  fc7ea237e02262f1d618ec09e1b7f0cd8535010c

mlperf-vitis-benchmark-app : gits@xcdl190260:vitis/mlperf-vitis-benchmark-app.git ： dpuv4e : f952f4ff88f9bfd43174f12d2e781e8138a3086b
update : gits@xcdl190260:wangchunye/mlperf-vitis-benchmark-app.git : br-dpuv4e-vart


git clone https://github.com/mlperf/inference.git mlperf_inference



cd /home/demo/mingyue/mlperf-vitis-benchmark-app
make
export LD_LIBRARY_PATH=/home/demo/.local/CentOS.7.6.1810.x86_64.Release/lib:/usr/local/lib:/usr/local/lib64:/opt/xilinx/xrt/lib:/home/demo/aaronn/mlperf-inference/loadgen/build
env XLNX_MAX_WAITING_TIME_IN_MS=1 XLNX_ENABLE_FINGERPRINT_CHECK=0 DEBUG_ASYNC_RUNNER=0 XLNX_ASYNC_RUNNER_PERF=1 ./app.exe -d /home/demo/xysheng/class/resnet50_new_v4e_acc/resnet50_new_v4e_acc.xmodel -i /home/demo/CK-TOOLS/dataset-imagenet-ilsvrc2012-val-min --mode PerformanceOnly --scenario Server --num_samples 80 -a 200 -r 3250;cat mlperf_log_summary.txt | grep 'Complete\|Scheduled'


env XLNX_ENABLE_FINGERPRINT_CHECK=0 DEBUG_ASYNC_RUNNER=1 ./app.exe -d /home/demo/xysheng/class/resnet50_new_v4e_acc/resnet50_new_v4e_acc.xmodel -i /home/demo/mingyue/mlperf-vitis-benchmark-app/test_jpeg --mode AccuracyOnly --scenario Server --num_samples 2 -a 200 -r 3250


env XLNX_ENABLE_FINGERPRINT_CHECK=0 DEBUG_ASYNC_RUNNER=1 ./app.exe -d /home/demo/xysheng/class/resnet50_new_v4e_acc/resnet50_new_v4e_acc.xmodel -i  /home/demo/CK-TOOLS/dataset-imagenet-ilsvrc2012-val-min --mode AccuracyOnly --scenario Server --num_samples 80 -a 200 -r 3250



./run.sh --exe app --mode AccuracyOnly --scenario  SingleStream





env  ASYNC=1 DEBUG_ASYNC_RUNNER=0 XLNX_MAX_WAITING_TIME_IN_MS=20 XLNX_ASYNC_RUNNER_PERF=0 NUM_OF_RUNNERS=2 DEBUG_XRT_DEVICE_HANDLE=0 DEBUG_DPU_RUNNER=0 XLNX_ENABLE_FINGERPRINT_CHECK=0 XLNX_SHOW_DPU_COUNTER=0 ~/build/build.CentOS.7.6.1810.x86_64.Release/my_vart/dpu-runner/test/test_dpu_runner_mt /home/demo/xysheng/class/resnet50_new_v4e_acc/resnet50_new_v4e_acc.xmodel subgraph_fake_downsample_0_ReplaceConv2d 32


----------------------
cd /home/mingyue/d/working/mlperf
env ASYNC=1 NUM_OF_RUNNERS=1 XLNX_ENABLE_FINGERPRINT_CHECK=0 DEBUG_DPU_RUNNER=1 DEBUG_XRT_DEVICE_HANDLE=1 ~/build/build.CentOS.7.6.1810.x86_64.Release/Vitis-AI-Library/classification/test_classification resnet50_acc dataset-imagenet-ilsvrc2012-val-min/ILSVRC2012_val_00000001.JPEG


export LD_LIBRARY_PATH=/home/mingyue/.local/CentOS.7.6.1810.x86_64.Release/lib:/usr/local/lib:/usr/local/lib64:/opt/xilinx/xrt/lib:/home/mingyue/d/working/mlperf/mlperf_inference/loadgen/build
cd /home/mingyue/d/working/mlperf/mlperf-vitis-benchmark-app
env XLNX_ENABLE_FINGERPRINT_CHECK=0 DEBUG_ASYNC_RUNNER=1 ./app.exe -d ../resnet50_acc/resnet50_acc.xmodel -i ../dataset-imagenet-ilsvrc2012-val-min --mode AccuracyOnly --scenario Server --num_samples 1 -a 200 -r 3200



```
