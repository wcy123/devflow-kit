# 101.76.179.68   v1.2 image

## densebox_320_320
```
% cd  /home/root/Vitis-AI/vitis_ai_library/samples/facedetect
% env XLNX_SHOW_DPU_COUNTER=1 XLNX_DPU_CORE_ID=1 ./test_jpeg_facedetect densebox_320_320 sample_facedetect.jpg
% xrt_read_register  ~/reg_edge.conf DPU 0
% env XLNX_SHOW_DPU_COUNTER=1 XLNX_DPU_CORE_ID=0 ./test_jpeg_facedetect densebox_320_320 sample_facedetect.jpg
% xrt_read_register  ~/reg_edge.conf DPU 1
% env XLNX_SHOW_DPU_COUNTER=1 XLNX_DPU_CORE_ID=2 ./test_jpeg_facedetect densebox_320_320 sample_facedetect.jpg
% xrt_read_register  ~/reg_edge.conf DPU 2

% env XLNX_DPU_CORE_ID=1 ./test_performance_facedetect densebox_320_320 test_performance_facedetect.list -s 60 -t 1
% env XLNX_DPU_CORE_ID=1 ./test_performance_facedetect densebox_320_320 test_performance_facedetect.list -s 60 -t 2
% env XLNX_DPU_CORE_ID=0 ./test_performance_facedetect densebox_320_320 test_performance_facedetect.list -s 60 -t 1
% env XLNX_DPU_CORE_ID=0 ./test_performance_facedetect densebox_320_320 test_performance_facedetect.list -s 60 -t 2
% env XLNX_DPU_CORE_ID=2 ./test_performance_facedetect densebox_320_320 test_performance_facedetect.list -s 60 -t 1
% env XLNX_DPU_CORE_ID=2 ./test_performance_facedetect densebox_320_320 test_performance_facedetect.list -s 60 -t 2
% env ./test_performance_facedetect densebox_320_320 test_performance_facedetect.list -s 60 -t 6
```
## densebox_640_360
```
% cd  /home/root/Vitis-AI/vitis_ai_library/samples/facedetect
% env XLNX_SHOW_DPU_COUNTER=1 XLNX_DPU_CORE_ID=1 ./test_jpeg_facedetect densebox_640_360 sample_facedetect.jpg
% xrt_read_register  ~/reg_edge.conf DPU 0
% env XLNX_SHOW_DPU_COUNTER=1 XLNX_DPU_CORE_ID=0 ./test_jpeg_facedetect densebox_640_360 sample_facedetect.jpg
% xrt_read_register  ~/reg_edge.conf DPU 1
% env XLNX_SHOW_DPU_COUNTER=1 XLNX_DPU_CORE_ID=2 ./test_jpeg_facedetect densebox_640_360 sample_facedetect.jpg
% xrt_read_register  ~/reg_edge.conf DPU 2

% env XLNX_DPU_CORE_ID=1 ./test_performance_facedetect densebox_640_360 test_performance_facedetect.list -s 60 -t 1
% env XLNX_DPU_CORE_ID=1 ./test_performance_facedetect densebox_640_360 test_performance_facedetect.list -s 60 -t 2
% env XLNX_DPU_CORE_ID=0 ./test_performance_facedetect densebox_640_360 test_performance_facedetect.list -s 60 -t 1
% env XLNX_DPU_CORE_ID=0 ./test_performance_facedetect densebox_640_360 test_performance_facedetect.list -s 60 -t 2
% env XLNX_DPU_CORE_ID=2 ./test_performance_facedetect densebox_640_360 test_performance_facedetect.list -s 60 -t 1
% env XLNX_DPU_CORE_ID=2 ./test_performance_facedetect densebox_640_360 test_performance_facedetect.list -s 60 -t 2
% env ./test_performance_facedetect densebox_640_360 test_performance_facedetect.list -s 60 -t 6
```
## fpn
```
% cd /home/root/Vitis-AI/vitis_ai_library/samples/segmentation
% env XLNX_SHOW_DPU_COUNTER=1 XLNX_DPU_CORE_ID=1 ./test_jpeg_segmentation fpn sample_segmentation.jpg
% env XLNX_SHOW_DPU_COUNTER=1 XLNX_DPU_CORE_ID=0 ./test_jpeg_segmentation fpn sample_segmentation.jpg
% env XLNX_SHOW_DPU_COUNTER=1 XLNX_DPU_CORE_ID=2 ./test_jpeg_segmentation fpn sample_segmentation.jpg
% xrt_read_register  ~/reg_edge.conf DPU 1
% xrt_read_register  ~/reg_edge.conf DPU 0
% xrt_read_register  ~/reg_edge.conf DPU 2

% env XLNX_DPU_CORE_ID=1 ./test_performance_segmentation fpn test_performance_segmentation.list -s 60 -t 1
% env XLNX_DPU_CORE_ID=0 ./test_performance_segmentation fpn test_performance_segmentation.list -s 60 -t 1
% env XLNX_DPU_CORE_ID=2 ./test_performance_segmentation fpn test_performance_segmentation.list -s 60 -t 1

% env XLNX_DPU_CORE_ID=1 ./test_performance_segmentation fpn test_performance_segmentation.list -s 60 -t 2
% env XLNX_DPU_CORE_ID=0 ./test_performance_segmentation fpn test_performance_segmentation.list -s 60 -t 2
% env XLNX_DPU_CORE_ID=2 ./test_performance_segmentation fpn test_performance_segmentation.list -s 60 -t 2

% ./test_performance_segmentation fpn test_performance_segmentation.list -s 60 -t 6
```
## inception_v2
```
% cd /home/root/Vitis-AI/vitis_ai_library/samples/classification
% env XLNX_SHOW_DPU_COUNTER=1 XLNX_DPU_CORE_ID=1 ./test_jpeg_classification inception_v2 sample_classification.jpg
% env XLNX_SHOW_DPU_COUNTER=1 XLNX_DPU_CORE_ID=0 ./test_jpeg_classification inception_v2 sample_classification.jpg
% env XLNX_SHOW_DPU_COUNTER=1 XLNX_DPU_CORE_ID=2 ./test_jpeg_classification inception_v2 sample_classification.jpg
% xrt_read_register  ~/reg_edge.conf DPU 0
% xrt_read_register  ~/reg_edge.conf DPU 1
% xrt_read_register  ~/reg_edge.conf DPU 2

% env XLNX_DPU_CORE_ID=1 ./test_performance_classification inception_v2 test_performance_classification.list -s 60 -t 1
% env XLNX_DPU_CORE_ID=0 ./test_performance_classification inception_v2 test_performance_classification.list -s 60 -t 1
% env XLNX_DPU_CORE_ID=2 ./test_performance_classification inception_v2 test_performance_classification.list -s 60 -t 1

% env XLNX_DPU_CORE_ID=1 ./test_performance_classification inception_v2 test_performance_classification.list -s 60 -t 2
% env XLNX_DPU_CORE_ID=0 ./test_performance_classification inception_v2 test_performance_classification.list -s 60 -t 2
% env XLNX_DPU_CORE_ID=2 ./test_performance_classification inception_v2 test_performance_classification.list -s 60 -t 2

% ./test_performance_classification inception_v2 test_performance_classification.list -s 60 -t 6
```
## inception_v1_tf
```
% cd /home/root/Vitis-AI/vitis_ai_library/samples/classification
% env XLNX_SHOW_DPU_COUNTER=1 XLNX_DPU_CORE_ID=1 ./test_jpeg_classification inception_v1_tf sample_classification.jpg
% env XLNX_SHOW_DPU_COUNTER=1 XLNX_DPU_CORE_ID=0 ./test_jpeg_classification inception_v1_tf sample_classification.jpg
% env XLNX_SHOW_DPU_COUNTER=1 XLNX_DPU_CORE_ID=2 ./test_jpeg_classification inception_v1_tf sample_classification.jpg
% xrt_read_register  ~/reg_edge.conf DPU 0
% xrt_read_register  ~/reg_edge.conf DPU 1
% xrt_read_register  ~/reg_edge.conf DPU 2

% env XLNX_DPU_CORE_ID=1 ./test_performance_classification inception_v1_tf test_performance_classification.list -s 60 -t 1
% env XLNX_DPU_CORE_ID=0 ./test_performance_classification inception_v1_tf test_performance_classification.list -s 60 -t 1
% env XLNX_DPU_CORE_ID=2 ./test_performance_classification inception_v1_tf test_performance_classification.list -s 60 -t 1

% env XLNX_DPU_CORE_ID=1 ./test_performance_classification inception_v1_tf test_performance_classification.list -s 60 -t 2
% env XLNX_DPU_CORE_ID=0 ./test_performance_classification inception_v1_tf test_performance_classification.list -s 60 -t 2
% env XLNX_DPU_CORE_ID=2 ./test_performance_classification inception_v1_tf test_performance_classification.list -s 60 -t 2

% ./test_performance_classification inception_v1_tf test_performance_classification.list -s 60 -t 6
```

## vpgnet_pruned_0_99
```
% cd /home/root/Vitis-AI/vitis_ai_library/samples/lanedetect
% env XLNX_SHOW_DPU_COUNTER=1 XLNX_DPU_CORE_ID=1 ./test_jpeg_lanedetect vpgnet_pruned_0_99 sample_lanedetect.jpg
% env XLNX_SHOW_DPU_COUNTER=1 XLNX_DPU_CORE_ID=0 ./test_jpeg_lanedetect vpgnet_pruned_0_99 sample_lanedetect.jpg
% env XLNX_SHOW_DPU_COUNTER=1 XLNX_DPU_CORE_ID=2 ./test_jpeg_lanedetect vpgnet_pruned_0_99 sample_lanedetect.jpg
% xrt_read_register  ~/reg_edge.conf DPU 0
% xrt_read_register  ~/reg_edge.conf DPU 1
% xrt_read_register  ~/reg_edge.conf DPU 2

% env XLNX_DPU_CORE_ID=1 ./test_performance_lanedetect vpgnet_pruned_0_99 test_performance_lanedetect.list -s 60 -t 1
% env XLNX_DPU_CORE_ID=0 ./test_performance_lanedetect vpgnet_pruned_0_99 test_performance_lanedetect.list -s 60 -t 1
% env XLNX_DPU_CORE_ID=2 ./test_performance_lanedetect vpgnet_pruned_0_99 test_performance_lanedetect.list -s 60 -t 1

% env XLNX_DPU_CORE_ID=1 ./test_performance_lanedetect vpgnet_pruned_0_99 test_performance_lanedetect.list -s 60 -t 2
% env XLNX_DPU_CORE_ID=0 ./test_performance_lanedetect vpgnet_pruned_0_99 test_performance_lanedetect.list -s 60 -t 2
% env XLNX_DPU_CORE_ID=2 ./test_performance_lanedetect vpgnet_pruned_0_99 test_performance_lanedetect.list -s 60 -t 2

% ./test_performance_lanedetect vpgnet_pruned_0_99 test_performance_lanedetect.list -s 60 -t 6
```

## yolov3_voc
```
% cd /home/root/Vitis-AI/vitis_ai_library/samples/yolov3
% env XLNX_SHOW_DPU_COUNTER=1 XLNX_DPU_CORE_ID=1 ./test_jpeg_yolov3 yolov3_voc sample_yolov3.jpg
% env XLNX_SHOW_DPU_COUNTER=1 XLNX_DPU_CORE_ID=0 ./test_jpeg_yolov3 yolov3_voc sample_yolov3.jpg
% env XLNX_SHOW_DPU_COUNTER=1 XLNX_DPU_CORE_ID=2 ./test_jpeg_yolov3 yolov3_voc sample_yolov3.jpg
% xrt_read_register  ~/reg_edge.conf DPU 1
% xrt_read_register  ~/reg_edge.conf DPU 0
% xrt_read_register  ~/reg_edge.conf DPU 2

% env XLNX_DPU_CORE_ID=1 ./test_performance_yolov3 yolov3_voc test_performance_yolov3.list -s 60 -t 1
% env XLNX_DPU_CORE_ID=0 ./test_performance_yolov3 yolov3_voc test_performance_yolov3.list -s 60 -t 1
% env XLNX_DPU_CORE_ID=2 ./test_performance_yolov3 yolov3_voc test_performance_yolov3.list -s 60 -t 1

% env XLNX_DPU_CORE_ID=1 ./test_performance_yolov3 yolov3_voc test_performance_yolov3.list -s 60 -t 2
% env XLNX_DPU_CORE_ID=0 ./test_performance_yolov3 yolov3_voc test_performance_yolov3.list -s 60 -t 2
% env XLNX_DPU_CORE_ID=2 ./test_performance_yolov3 yolov3_voc test_performance_yolov3.list -s 60 -t 2

% ./test_performance_yolov3 yolov3_voc test_performance_yolov3.list -s 60 -t 6
```


V1.3
```
%mkdir -p /group/xbzjlab && mount -t nfs -o nolock 10.176.178.33:/group_xbjlab/ /group/xbjlab
%export LD_LIBRARY_PATH=/group/xbjlab/dphi_software/software/workspace/mingyue/d/working/aisw/petalinux_sdk/sysroots/aarch64-xilinx-linux/install/Release/lib
% export XLNX_ENABLE_FINGERPRINT_CHECK=0
```

# densebox_320_320
```
% cd  /home/root/Vitis-AI/vitis_ai_library/samples/facedetect
% env XLNX_SHOW_DPU_COUNTER=1 XLNX_DPU_DEVICE_CORES=0 ./test_jpeg_facedetect densebox_320_320 sample_facedetect.jpg
% env XLNX_SHOW_DPU_COUNTER=1 XLNX_DPU_DEVICE_CORES=1 ./test_jpeg_facedetect densebox_320_320 sample_facedetect.jpg
% env XLNX_SHOW_DPU_COUNTER=1 XLNX_DPU_DEVICE_CORES=2 ./test_jpeg_facedetect densebox_320_320 sample_facedetect.jpg


% env XLNX_DPU_DEVICE_CORES=0 ./test_performance_facedetect densebox_320_320 test_performance_facedetect.list -s 60 -t 1
% env XLNX_DPU_DEVICE_CORES=1 ./test_performance_facedetect densebox_320_320 test_performance_facedetect.list -s 60 -t 1
% env XLNX_DPU_DEVICE_CORES=2 ./test_performance_facedetect densebox_320_320 test_performance_facedetect.list -s 60 -t 1

% env XLNX_DPU_DEVICE_CORES=0 ./test_performance_facedetect densebox_320_320 test_performance_facedetect.list -s 60 -t 2
% env XLNX_DPU_DEVICE_CORES=1 ./test_performance_facedetect densebox_320_320 test_performance_facedetect.list -s 60 -t 2
% env XLNX_DPU_DEVICE_CORES=2 ./test_performance_facedetect densebox_320_320 test_performance_facedetect.list -s 60 -t 2
% env XLNX_DPU_DEVICE_CORES=0,1,2 ./test_performance_facedetect densebox_320_320 test_performance_facedetect.list -s 60 -t 6
```
# inception_v1_tf
```
% cd  /home/root/Vitis-AI/vitis_ai_library/samples/classification
% env XLNX_SHOW_DPU_COUNTER=1 XLNX_DPU_DEVICE_CORES=0 /group/xbjlab/dphi_software/software/workspace/mingyue/build/build.linux.2020.2.aarch64.Release/Vitis-AI-Library/overview/test_jpeg_classification inception_v1_tf sample_classification.jpg
% env XLNX_SHOW_DPU_COUNTER=1 XLNX_DPU_DEVICE_CORES=1 /group/xbjlab/dphi_software/software/workspace/mingyue/build/build.linux.2020.2.aarch64.Release/Vitis-AI-Library/overview/test_jpeg_classification inception_v1_tf sample_classification.jpg
% env XLNX_SHOW_DPU_COUNTER=1 XLNX_DPU_DEVICE_CORES=2 /group/xbjlab/dphi_software/software/workspace/mingyue/build/build.linux.2020.2.aarch64.Release/Vitis-AI-Library/overview/test_jpeg_classification inception_v1_tf sample_classification.jpg



% env XLNX_DPU_DEVICE_CORES=0 /group/xbjlab/dphi_software/software/workspace/mingyue/build/build.linux.2020.2.aarch64.Release/Vitis-AI-Library/overview/test_performance_classification inception_v1_tf test_performance_classification.list -s 60 -t 1
% env XLNX_DPU_DEVICE_CORES=1 /group/xbjlab/dphi_software/software/workspace/mingyue/build/build.linux.2020.2.aarch64.Release/Vitis-AI-Library/overview/test_performance_classification inception_v1_tf test_performance_classification.list -s 60 -t 1
% env XLNX_DPU_DEVICE_CORES=2 /group/xbjlab/dphi_software/software/workspace/mingyue/build/build.linux.2020.2.aarch64.Release/Vitis-AI-Library/overview/test_performance_classification inception_v1_tf test_performance_classification.list -s 60 -t 1

% env XLNX_DPU_DEVICE_CORES=0 /group/xbjlab/dphi_software/software/workspace/mingyue/build/build.linux.2020.2.aarch64.Release/Vitis-AI-Library/overview/test_performance_classification inception_v1_tf test_performance_classification.list -s 60 -t 2
% env XLNX_DPU_DEVICE_CORES=1 /group/xbjlab/dphi_software/software/workspace/mingyue/build/build.linux.2020.2.aarch64.Release/Vitis-AI-Library/overview/test_performance_classification inception_v1_tf test_performance_classification.list -s 60 -t 2
% env XLNX_DPU_DEVICE_CORES=2 /group/xbjlab/dphi_software/software/workspace/mingyue/build/build.linux.2020.2.aarch64.Release/Vitis-AI-Library/overview/test_performance_classification inception_v1_tf test_performance_classification.list -s 60 -t 2
% env XLNX_DPU_DEVICE_CORES=0,1,2 /group/xbjlab/dphi_software/software/workspace/mingyue/build/build.linux.2020.2.aarch64.Release/Vitis-AI-Library/overview/test_performance_classification inception_v1_tf test_performance_classification.list -s 60 -t 6
```

# vpgnet_pruned_0_99
```
% cd  /home/root/Vitis-AI/vitis_ai_library/samples/lanedetect
% env XLNX_SHOW_DPU_COUNTER=1 XLNX_DPU_DEVICE_CORES=0 /group/xbjlab/dphi_software/software/workspace/mingyue/build/build.linux.2020.2.aarch64.Release/Vitis-AI-Library/overview/test_jpeg_lanedetect vpgnet_pruned_0_99 sample_lanedetect.jpg
% env XLNX_SHOW_DPU_COUNTER=1 XLNX_DPU_DEVICE_CORES=1 /group/xbjlab/dphi_software/software/workspace/mingyue/build/build.linux.2020.2.aarch64.Release/Vitis-AI-Library/overview/test_jpeg_lanedetect vpgnet_pruned_0_99 sample_lanedetect.jpg
% env XLNX_SHOW_DPU_COUNTER=1 XLNX_DPU_DEVICE_CORES=2 /group/xbjlab/dphi_software/software/workspace/mingyue/build/build.linux.2020.2.aarch64.Release/Vitis-AI-Library/overview/test_jpeg_lanedetect vpgnet_pruned_0_99 sample_lanedetect.jpg



% env XLNX_DPU_DEVICE_CORES=0 /group/xbjlab/dphi_software/software/workspace/mingyue/build/build.linux.2020.2.aarch64.Release/Vitis-AI-Library/overview/test_performance_lanedetect vpgnet_pruned_0_99 test_performance_lanedetect.list -s 60 -t 1
% env XLNX_DPU_DEVICE_CORES=1 /group/xbjlab/dphi_software/software/workspace/mingyue/build/build.linux.2020.2.aarch64.Release/Vitis-AI-Library/overview/test_performance_lanedetect vpgnet_pruned_0_99 test_performance_lanedetect.list -s 60 -t 1
% env XLNX_DPU_DEVICE_CORES=2 /group/xbjlab/dphi_software/software/workspace/mingyue/build/build.linux.2020.2.aarch64.Release/Vitis-AI-Library/overview/test_performance_lanedetect vpgnet_pruned_0_99 test_performance_lanedetect.list -s 60 -t 1

% env XLNX_DPU_DEVICE_CORES=0 /group/xbjlab/dphi_software/software/workspace/mingyue/build/build.linux.2020.2.aarch64.Release/Vitis-AI-Library/overview/test_performance_lanedetect vpgnet_pruned_0_99 test_performance_lanedetect.list -s 60 -t 2
% env XLNX_DPU_DEVICE_CORES=1 /group/xbjlab/dphi_software/software/workspace/mingyue/build/build.linux.2020.2.aarch64.Release/Vitis-AI-Library/overview/test_performance_lanedetect vpgnet_pruned_0_99 test_performance_lanedetect.list -s 60 -t 2
% env XLNX_DPU_DEVICE_CORES=2 /group/xbjlab/dphi_software/software/workspace/mingyue/build/build.linux.2020.2.aarch64.Release/Vitis-AI-Library/overview/test_performance_lanedetect vpgnet_pruned_0_99 test_performance_lanedetect.list -s 60 -t 2
% env XLNX_DPU_DEVICE_CORES=0,1,2 /group/xbjlab/dphi_software/software/workspace/mingyue/build/build.linux.2020.2.aarch64.Release/Vitis-AI-Library/overview/test_performance_lanedetect vpgnet_pruned_0_99 test_performance_lanedetect.list -s 60 -t 6
```
