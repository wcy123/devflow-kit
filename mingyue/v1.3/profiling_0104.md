# 101.76.179.67  new board &  v1.2 image
```
% ssh root@10.176.179.67

```

## inception_v2  (caffe , model_zoo Inception_v2)
### v1.2 test
```
% cd /home/root/samples/classification
% bash -ex build.sh
% cd  /home/root
% env XLNX_SHOW_DPU_COUNTER=1 XLNX_DPU_CORE_ID=1 /home/root/samples/classification/test_jpeg_classification inception_v2 /home/root/vitis-ai-library-samples-res/samples/classification/sample_classification.jpg
% env XLNX_SHOW_DPU_COUNTER=1 XLNX_DPU_CORE_ID=0 /home/root/samples/classification/test_jpeg_classification inception_v2 /home/root/vitis-ai-library-samples-res/samples/classification/sample_classification.jpg
% env XLNX_SHOW_DPU_COUNTER=1 XLNX_DPU_CORE_ID=2 /home/root/samples/classification/test_jpeg_classification inception_v2 /home/root/vitis-ai-library-samples-res/samples/classification/sample_classification.jpg
% xrt_read_register  /home/root/reg_edge.conf DPU 0
% xrt_read_register  /home/root/reg_edge.conf DPU 1
% xrt_read_register  /home/root/reg_edge.conf DPU 2

```

## fpn
```
% cd /home/root/samples/segmentation/
% bash -ex build.sh
% cd  /home/root
% env XLNX_SHOW_DPU_COUNTER=1 XLNX_DPU_CORE_ID=1 /home/root/samples/segmentation/test_jpeg_segmentation fpn /home/root/vitis-ai-library-samples-res/samples/segmentation/sample_segmentation.jpg
% env XLNX_SHOW_DPU_COUNTER=1 XLNX_DPU_CORE_ID=0 /home/root/samples/segmentation/test_jpeg_segmentation fpn /home/root/vitis-ai-library-samples-res/samples/segmentation/sample_segmentation.jpg
% env XLNX_SHOW_DPU_COUNTER=1 XLNX_DPU_CORE_ID=2 /home/root/samples/segmentation/test_jpeg_segmentation fpn /home/root/vitis-ai-library-samples-res/samples/segmentation/sample_segmentation.jpg
% xrt_read_register  /home/root/reg_edge.conf DPU 0
% xrt_read_register  /home/root/reg_edge.conf DPU 1
% xrt_read_register  /home/root/reg_edge.conf DPU 2
```

### backup inception_v2 to inception_v2_1.2  and fpn to fpn_1.2
```
% mv /usr/share/vitis_ai_library/models/inception_v2 /usr/share/vitis_ai_library/models/inception_v2_1.2
% mv /usr/share/vitis_ai_library/models/fpn /usr/share/vitis_ai_library/models/fpn_v2_1.2

```
### copy v1.3 xmodel
```
% cp -r /group/xbjlab/dphi_software/software/workspace/huizhang/vitis_ai_library/r1.3/xilinx_model_zoo_zcu102_zcu104_all-1.3.0-Linux/usr/share/vitis_ai_library/models/fpn /usr/share/vitis_ai_library/models/
% cp -r /group/xbjlab/dphi_software/software/workspace/huizhang/vitis_ai_library/r1.3/xilinx_model_zoo_zcu102_zcu104_all-1.3.0-Linux/usr/share/vitis_ai_library/models/inception_v2 /usr/share/vitis_ai_library/models/
% export LD_LIBRARY_PATH=/group/xbjlab/dphi_software/software/workspace/mingyue/d/working/aisw/petalinux_sdk/sysroots/aarch64-xilinx-linux/install/Release/lib
```
### inception_v2 1.3
```
% env XLNX_DPU_DEVICE_CORES=0 XLNX_ENABLE_FINGERPRINT_CHECK=0 /group/xbjlab/dphi_software/software/workspace/mingyue/build/build.linux.2020.2.aarch64.Release/Vitis-AI-Library/overview/test_jpeg_classification inception_v2 /home/root/vitis-ai-library-samples-res/samples/classification/sample_classification.jpg
% env XLNX_DPU_DEVICE_CORES=1 XLNX_ENABLE_FINGERPRINT_CHECK=0 /group/xbjlab/dphi_software/software/workspace/mingyue/build/build.linux.2020.2.aarch64.Release/Vitis-AI-Library/overview/test_jpeg_classification inception_v2 /home/root/vitis-ai-library-samples-res/samples/classification/sample_classification.jpg
% env XLNX_DPU_DEVICE_CORES=2 XLNX_ENABLE_FINGERPRINT_CHECK=0 /group/xbjlab/dphi_software/software/workspace/mingyue/build/build.linux.2020.2.aarch64.Release/Vitis-AI-Library/overview/test_jpeg_classification inception_v2 /home/root/vitis-ai-library-samples-res/samples/classification/sample_classification.jpg

% /group/xbjlab/dphi_software/software/workspace/mingyue/build/build.linux.2020.2.aarch64.Release/vart/xrt-device-handle/xrt_read_register /home/root/reg_edge.conf DPU 0
% /group/xbjlab/dphi_software/software/workspace/mingyue/build/build.linux.2020.2.aarch64.Release/vart/xrt-device-handle/xrt_read_register /home/root/reg_edge.conf DPU 1
% /group/xbjlab/dphi_software/software/workspace/mingyue/build/build.linux.2020.2.aarch64.Release/vart/xrt-device-handle/xrt_read_register /home/root/reg_edge.conf DPU 2

```
## fpn 1.3

```
% env XLNX_DPU_DEVICE_CORES=0 XLNX_ENABLE_FINGERPRINT_CHECK=0 /group/xbjlab/dphi_software/software/workspace/mingyue/build/build.linux.2020.2.aarch64.Release/Vitis-AI-Library/overview/test_jpeg_segmentation fpn /home/root/vitis-ai-library-samples-res/samples/segmentation/sample_segmentation.jpg
% env XLNX_DPU_DEVICE_CORES=1 XLNX_ENABLE_FINGERPRINT_CHECK=0 /group/xbjlab/dphi_software/software/workspace/mingyue/build/build.linux.2020.2.aarch64.Release/Vitis-AI-Library/overview/test_jpeg_segmentation fpn /home/root/vitis-ai-library-samples-res/samples/segmentation/sample_segmentation.jpg
% env XLNX_DPU_DEVICE_CORES=2 XLNX_ENABLE_FINGERPRINT_CHECK=0 /group/xbjlab/dphi_software/software/workspace/mingyue/build/build.linux.2020.2.aarch64.Release/Vitis-AI-Library/overview/test_jpeg_segmentation fpn /home/root/vitis-ai-library-samples-res/samples/segmentation/sample_segmentation.jpg

```


## copy inception_v2 to inception_v2_1.2  and fpn to fpn_1.3
```
% cp -r /usr/share/vitis_ai_library/models/inception_v2 /usr/share/vitis_ai_library/models/inception_v2_1.3
% cp -r /usr/share/vitis_ai_library/models/fpn /usr/share/vitis_ai_library/models/fpn_1.3
% cp /home/root/MR352/Inception_v2_352.xmodel /usr/share/vitis_ai_library/models/inception_v2/inception_v2.xmodel
% cp /home/root/MR352/fpn_352.xmodel /usr/share/vitis_ai_library/models/fpn/fpn.xmodel
```


###
```
% cp -r /usr/share/vitis_ai_library/models/inception_v2 /usr/share/vitis_ai_library/models/inception_v2_352
% cp -r /usr/share/vitis_ai_library/models/fpn /usr/share/vitis_ai_library/models/fpn_352
% cp /home/root/MR364/Inception_v2_364.xmodel /usr/share/vitis_ai_library/models/inception_v2/inception_v2.xmodel
% cp /home/root/MR364/fpn_364.xmodel /usr/share/vitis_ai_library/models/fpn/fpn.xmodel
```
