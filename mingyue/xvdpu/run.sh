#!/bin/bash
vart_version

#compare data

#test_dpu_runner_mt
./xrt_read_register reg_xvdpu.conf DPU 0
## mlperf_resnet_v1_50

./test_dpu_runner_mt classification/xvdpu_1.5_resnet_v1_50_prefetch/xvdpu_1.5_resnet_v1_50_prefetch.xmodel xvdpu_1.5_resnet_v1_50_prefetch_0 1
./test_dpu_runner_mt classification/xvdpu_1.5_resnet_v1_50_prefetch/xvdpu_1.5_resnet_v1_50_prefetch.xmodel xvdpu_1.5_resnet_v1_50_prefetch_0 4
## mlperf_resnet_v1_50_pruned_74
./test_dpu_runner_mt classification/Resnet50_v1.5_pruned_74/Resnet50_v1.5_pruned_74.xmodel Resnet50_v1.5_pruned_74_0 4

./xrt_read_register reg_xvdpu.conf DPU 0

#test jpeg
cd ~/classification
/usr/share/vitis_ai_library/samples/classification/test_jpeg_classification xvdpu_1.5_resnet_v1_50_prefetch sample_classification.jpg
/usr/share/vitis_ai_library/samples/classification/test_performance_classification xvdpu_1.5_resnet_v1_50_prefetch test_performance_classification.list -t 4 -s 60
/usr/share/vitis_ai_library/samples/classification/test_performance_classification Resnet50_v1.5_pruned_74 test_performance_classification.list -t 4 -s 60
