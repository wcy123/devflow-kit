# work log for mlperf


```
ssh xsjjump03
ssh demo@xsjfislx40

target_factory :  4b6615e59a3630b14eab8d3734e54c1280879552
unilog  : 27fb298ddbb876684652ac29bdf7bd5e30f2d391
vart : gits@xcdl190260:wangchunye/vart.git: feat-async-runner :  fc7ea237e02262f1d618ec09e1b7f0cd8535010c

mlperf-vitis-benchmark-app : gits@xcdl190260:vitis/mlperf-vitis-benchmark-app.git ： dpuv4e : f952f4ff88f9bfd43174f12d2e781e8138a3086b

cd /home/demo/mingyue/mlperf-vitis-benchmark-app
make
export LD_LIBRARY_PATH=/home/demo/.local/CentOS.7.6.1810.x86_64.Release/lib:/usr/local/lib:/usr/local/lib64:/opt/xilinx/xrt/lib:/home/demo/aaronn/mlperf-inference/loadgen/build
env XLNX_MAX_WAITING_TIME_IN_MS=1 XLNX_ENABLE_FINGERPRINT_CHECK=0 DEBUG_ASYNC_RUNNER=0 XLNX_ASYNC_RUNNER_PERF=1 ./app.exe -d /home/demo/xysheng/class/resnet50_new_v4e_acc/resnet50_new_v4e_acc.xmodel -i /home/demo/CK-TOOLS/dataset-imagenet-ilsvrc2012-val-min --mode PerformanceOnly --scenario Server --num_samples 80 -a 200 -r 3250;cat mlperf_log_summary.txt | grep 'Complete\|Scheduled'


env XLNX_ENABLE_FINGERPRINT_CHECK=0 DEBUG_ASYNC_RUNNER=1 ./app.exe -d /home/demo/xysheng/class/resnet50_new_v4e_acc/resnet50_new_v4e_acc.xmodel -i /home/demo/mingyue/mlperf-vitis-benchmark-app/test_jpeg --mode AccuracyOnly --scenario Server --num_samples 2 -a 200 -r 3250


env XLNX_ENABLE_FINGERPRINT_CHECK=0 DEBUG_ASYNC_RUNNER=1 ./app.exe -d /home/demo/xysheng/class/resnet50_new_v4e_acc/resnet50_new_v4e_acc.xmodel -i  /home/demo/CK-TOOLS/dataset-imagenet-ilsvrc2012-val-min --mode AccuracyOnly --scenario Server --num_samples 80 -a 200 -r 3250



./run.sh --exe app --mode AccuracyOnly --scenario  SingleStream





```
