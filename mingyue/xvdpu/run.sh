#!/bin/bash
check_fingerprint=$1

vart_version
env XLNX_ENABLE_FINGERPRINT_CHECK=$check_fingerprint ./xrt_read_register reg_xvdpu.conf DPU 0

#compare data
rm -rf dump*
env XLNX_ENABLE_FINGERPRINT_CHECK=$check_fingerprint XLNX_ENABLE_DUMP=1  ./test_dpu_runner classification/xvdpu_1.5_resnet_v1_50_prefetch/xvdpu_1.5_resnet_v1_50_prefetch.xmodel xvdpu_1.5_resnet_v1_50_prefetch_0 classification/xvdpu_1.5_resnet_v1_50_prefetch/subgraph_1_input_image_aquant_vart-sim-runner.bin 1 1 2>dump_resnet50.log 1>&2
md5sum -c xvdpu_1.5_resnet_v1_50_prefetch.md5
mv dump dump_resnet50

env XLNX_ENABLE_FINGERPRINT_CHECK=$check_fingerprint XLNX_ENABLE_DUMP=1  ./test_dpu_runner classification/Resnet50_v1.5_pruned_74/Resnet50_v1.5_pruned_74.xmodel Resnet50_v1.5_pruned_74_0 classification/Resnet50_v1.5_pruned_74/input_tensor_aquant.bin 1 1 2>dump_resnet50_pruned.log 1>&2
md5sum -c Resnet50_v1.5_pruned_74.md5
mv dump dump_resnet50_pruned_74

env XLNX_ENABLE_FINGERPRINT_CHECK=$check_fingerprint XLNX_ENABLE_DUMP=1 ./test_dpu_runner yolov3/yolov3_voc/yolov3_voc.xmodel yolov3_voc_0 yolov3/yolov3_voc/dump_gpu/data_fixed.bin 1 1 2>dump_yolov3_voc.log
md5sum -c yolov3_voc.md5
mv dump dump_yolov3_voc

env XLNX_ENABLE_FINGERPRINT_CHECK=$check_fingerprint XLNX_ENABLE_DUMP=1 ./test_dpu_runner yolov3/yolov3_voc_tf/yolov3_voc_tf.xmodel yolov3_voc_0 yolov3/yolov3_voc_tf/dump_results_0/input_1_aquant.bin 1 1 2>dump_yolov3_voc_tf.log 1>&2
md5sum -c yolov3_voc_tf.md5
mv dump dump_yolov3_voc_tf

#test_dpu_runner_mt
## mlperf_resnet_v1_50
env XLNX_ENABLE_FINGERPRINT_CHECK=$check_fingerprint ./test_dpu_runner_mt classification/xvdpu_1.5_resnet_v1_50_prefetch/xvdpu_1.5_resnet_v1_50_prefetch.xmodel xvdpu_1.5_resnet_v1_50_prefetch_0 1
env XLNX_ENABLE_FINGERPRINT_CHECK=$check_fingerprint ./test_dpu_runner_mt classification/xvdpu_1.5_resnet_v1_50_prefetch/xvdpu_1.5_resnet_v1_50_prefetch.xmodel xvdpu_1.5_resnet_v1_50_prefetch_0 4
## mlperf_resnet_v1_50_pruned_74
env XLNX_ENABLE_FINGERPRINT_CHECK=$check_fingerprint ./test_dpu_runner_mt classification/Resnet50_v1.5_pruned_74/Resnet50_v1.5_pruned_74.xmodel Resnet50_v1.5_pruned_74_0 1
env XLNX_ENABLE_FINGERPRINT_CHECK=$check_fingerprint ./test_dpu_runner_mt classification/Resnet50_v1.5_pruned_74/Resnet50_v1.5_pruned_74.xmodel Resnet50_v1.5_pruned_74_0 4
## yolov3_voc
env XLNX_ENABLE_FINGERPRINT_CHECK=$check_fingerprint ./test_dpu_runner_mt yolov3/yolov3_voc/yolov3_voc.xmodel yolov3_voc_0 1
env XLNX_ENABLE_FINGERPRINT_CHECK=$check_fingerprint ./test_dpu_runner_mt yolov3/yolov3_voc/yolov3_voc.xmodel yolov3_voc_0 4

## yolov3_voc_tf
env XLNX_ENABLE_FINGERPRINT_CHECK=$check_fingerprint ./test_dpu_runner_mt yolov3/yolov3_voc_tf/yolov3_voc_tf.xmodel yolov3_voc_tf_0 1
env XLNX_ENABLE_FINGERPRINT_CHECK=$check_fingerprint ./test_dpu_runner_mt yolov3/yolov3_voc_tf/yolov3_voc_tf.xmodel yolov3_voc_tf_0 4

env XLNX_ENABLE_FINGERPRINT_CHECK=$check_fingerprint ./xrt_read_register reg_xvdpu.conf DPU 0


#test jpeg & performance
cd ~/classification
env XLNX_ENABLE_FINGERPRINT_CHECK=$check_fingerprint XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=1 /usr/share/vitis_ai_library/samples/classification/test_jpeg_classification xvdpu_1.5_resnet_v1_50_prefetch sample_classification.jpg
#env XLNX_ENABLE_FINGERPRINT_CHECK=$check_fingerprint /usr/share/vitis_ai_library/samples/classification/test_performance_classification xvdpu_1.5_resnet_v1_50_prefetch test_performance_classification.list -t 1 -s 60
env XLNX_ENABLE_FINGERPRINT_CHECK=$check_fingerprint /usr/share/vitis_ai_library/samples/classification/test_performance_classification xvdpu_1.5_resnet_v1_50_prefetch test_performance_classification.list -t 4 -s 60
env XLNX_ENABLE_FINGERPRINT_CHECK=$check_fingerprint XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=1 /usr/share/vitis_ai_library/samples/classification/test_jpeg_classification Resnet50_v1.5_pruned_74 sample_classification.jpg
#env XLNX_ENABLE_FINGERPRINT_CHECK=$check_fingerprint /usr/share/vitis_ai_library/samples/classification/test_performance_classification Resnet50_v1.5_pruned_74 test_performance_classification.list -t 1 -s 60
env XLNX_ENABLE_FINGERPRINT_CHECK=$check_fingerprint /usr/share/vitis_ai_library/samples/classification/test_performance_classification Resnet50_v1.5_pruned_74 test_performance_classification.list -t 4 -s 60

cd ~/yolov3
env XLNX_ENABLE_FINGERPRINT_CHECK=$check_fingerprint XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=1 /usr/share/vitis_ai_library/samples/yolov3/test_jpeg_yolov3 yolov3_voc sample_yolov3.jpg
#env XLNX_ENABLE_FINGERPRINT_CHECK=$check_fingerprint /usr/share/vitis_ai_library/samples/yolov3/test_performance_yolov3 yolov3_voc test_performance_yolov3.list -t 1 -s 60
env XLNX_ENABLE_FINGERPRINT_CHECK=$check_fingerprint /usr/share/vitis_ai_library/samples/yolov3/test_performance_yolov3 yolov3_voc test_performance_yolov3.list -t 4 -s 60
env XLNX_ENABLE_FINGERPRINT_CHECK=$check_fingerprint XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=1 /usr/share/vitis_ai_library/samples/yolov3/test_jpeg_yolov3 yolov3_voc_tf sample_yolov3.jpg
#env XLNX_ENABLE_FINGERPRINT_CHECK=$check_fingerprint /usr/share/vitis_ai_library/samples/yolov3/test_performance_yolov3 yolov3_voc_tf test_performance_yolov3.list -t 1 -s 60
env XLNX_ENABLE_FINGERPRINT_CHECK=$check_fingerprint /usr/share/vitis_ai_library/samples/yolov3/test_performance_yolov3 yolov3_voc_tf test_performance_yolov3.list -t 4 -s 60
