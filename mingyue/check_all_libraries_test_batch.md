### compile unilog&xir&vart&vitis-ai-library
```
ssh mingyue@xsjsda153
cd $HOME/d/working/mingyue/unilog
g p
./cmake.sh --type=release

cd $HOME/d/working/mingyue/xir
g p
./cmake.sh --type=release

cd $HOME/d/working/mingyue/vart
g p
./cmake.sh --cmake-options=-DENABLE_DPU_RUNNER=ON --cmake-options=-DENABLE_SIM_RUNNER=OFF --cmake-options=-DENABLE_CPU_RUNNER=OFF --type=release

cd $HOME/d/working/mingyue/Vitis-AI-Library
g s
g stash
g p
./cmake.sh --type=release --cmake-options='-DENABLE_OVERVIEW=ON'
```
### prepare models & samples (from 152 /usr/share)
```
/tools/xgs/bin/sudo ln -s /proj/rdi/staff/mingyue/share/vitis_ai_library /usr/share/vitis_ai_library
ls /proj/rdi/staff/mingyue/share/vitis_ai_library
ls /usr/share/vitis_ai_library/models
```
```
export LD_LIBRARY_PATH=/opt/xilinx/xrt/lib:/usr/local/lib:/usr/local/lib64:/home/mingyue/.local/RedHatEnterpriseWorkstation.7.4.x86_64.Release/lib
```
### Test
#### classification
```
cd /proj/xsjhdstaff6/mingyue/share/vitis_ai_library/samples/classification
ls
ls images

<!-- resnet_v1_50_tf-->
env DEBUG_XRT_DEVICE_HANDLE=1 XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=1 DEBUG_DPU_CORE_ID=0 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/classification/test_classification_batch resnet_v1_50_tf images/001.JPEG images/002.JPEG images/003.JPEG
env XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=1 DEBUG_DPU_CORE_ID=1 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/classification/test_classification_batch resnet_v1_50_tf images/001.JPEG images/002.JPEG images/003.JPEG

/home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/overview/test_performance_classification resnet_v1_50_tf test_performance_classification.list -t 4 -s 10

<!-- inception_v1_tf -->
env XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=1 DEBUG_DPU_CORE_ID=0 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/classification/test_classification_batch inception_v1_tf images/001.JPEG images/002.JPEG images/003.JPEG
env XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=1 DEBUG_DPU_CORE_ID=1 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/classification/test_classification_batch inception_v1_tf images/001.JPEG images/002.JPEG images/003.JPEG
/home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/overview/test_performance_classification inception_v1_tf test_performance_classification.list -t 4 -s 10

/home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/classification

<!-- inception_v1_tf-->
env XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=1 DEBUG_DPU_CORE_ID=0 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/classification/test_classification_batch inception_v1 images/001.JPEG images/002.JPEG images/003.JPEG
env XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=1 DEBUG_DPU_CORE_ID=1 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/classification/test_classification_batch inception_v1 images/001.JPEG images/002.JPEG images/003.JPEG

```
#### Test facedetect
```
cd /proj/xsjhdstaff6/mingyue/share/vitis_ai_library/samples/facedetect
ls
ls images

<!-- densebox_320_320-->
env XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=1 DEBUG_DPU_CORE_ID=0 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/facedetect/test_facedetect_batch densebox_320_320 images/001.jpg images/002.jpg images/003.jpg

env XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=1 DEBUG_DPU_CORE_ID=1 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/facedetect/test_facedetect_batch densebox_320_320 images/001.jpg images/002.jpg images/003.jpg

/home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/overview/test_performance_facedetect densebox_320_320 test_performance_facedetect.list -t 4 -s 10


<!-- densebox_640_360-->
env XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=1 DEBUG_DPU_CORE_ID=0 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/facedetect/test_facedetect_batch densebox_640_360 images/001.jpg images/002.jpg images/003.jpg

env XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=1 DEBUG_DPU_CORE_ID=1 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/facedetect/test_facedetect_batch densebox_640_360 images/001.jpg images/002.jpg images/003.jpg

/home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/overview/test_performance_facedetect densebox_640_360 test_performance_facedetect.list -t 4 -s 10
```

#### Test facelandmark
```
cd /proj/xsjhdstaff6/mingyue/share/vitis_ai_library/samples/facedetect
ls
ls images

env XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=1 DEBUG_DPU_CORE_ID=0 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/facelandmark/test_face_landmark_batch face_landmark images/001.jpg images/002.jpg images/003.jpg
env XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=1 DEBUG_DPU_CORE_ID=1 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/facelandmark/test_face_landmark_batch face_landmark images/001.jpg images/002.jpg images/003.jpg

```

#### Test lanedetect

```
cd /proj/xsjhdstaff6/mingyue/share/vitis_ai_library/samples/lanedetect
cat readme
ls
ls images
env XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=1 DEBUG_DPU_CORE_ID=0 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/lanedetect/test_lanedetect_batch vpgnet_pruned_0_99 images/001.png images/002.png images/003.png
env XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=1 DEBUG_DPU_CORE_ID=1 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/lanedetect/test_lanedetect_batch vpgnet_pruned_0_99 images/001.png images/002.png images/003.png

```
#### Test multitask

```
cd /proj/xsjhdstaff6/mingyue/share/vitis_ai_library/samples/multitask
ls
cd images
#scp mingyue@xcdl190256:/group/dphi_software/software/test_accuracy_library/multitask/images/* .

ls images
cat readme
env XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=1 DEBUG_DPU_CORE_ID=0 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/multitask/test_multitask_batch multi_task images/001.jpg images/7d128593-0ccfea4c.png images/7d209219-ccdc1a09.png images/7d2f7975-e0c1c5a7.png
env XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=1 DEBUG_DPU_CORE_ID=1 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/multitask/test_multitask_batch multi_task images/001.jpg images/7d128593-0ccfea4c.png images/7d209219-ccdc1a09.png images/7d2f7975-e0c1c5a7.png

```
#### Test openpose

```
cd /proj/xsjhdstaff6/mingyue/share/vitis_ai_library/samples/openpose
ls
rm sample_openpose_result.jpg
ls images
cat readme
env XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=1 DEBUG_DPU_CORE_ID=0 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/openpose/test_open_pose_batch openpose_pruned_0_3 images/001.jpg images/002.jpg images/003.jpg
env XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=1 DEBUG_DPU_CORE_ID=1 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/openpose/test_open_pose_batch openpose_pruned_0_3 images/001.jpg images/002.jpg images/003.jpg

```
#### posedetect

```
cd /proj/xsjhdstaff6/mingyue/share/vitis_ai_library/samples/posedetect
ls
ls images
cat readme
env XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=1 DEBUG_DPU_CORE_ID=0 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/posedetect/test_pose_detect_batch sp_net images/001.jpg images/002.jpg images/003.jpg
env XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=1 DEBUG_DPU_CORE_ID=1 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/posedetect/test_pose_detect_batch sp_net images/001.jpg images/002.jpg images/003.jpg
```
#### refinedet

```
cd /proj/xsjhdstaff6/mingyue/share/vitis_ai_library/samples/refinedet
ls
ls images
cat readme
env XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=1 DEBUG_DPU_CORE_ID=0 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/refinedet/test_refinedet_batch refinedet_pruned_0_8 images/001.jpg images/002.jpg images/003.jpg
env XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=1 DEBUG_DPU_CORE_ID=1 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/refinedet/test_refinedet_batch refinedet_pruned_0_8 images/001.jpg images/002.jpg images/003.jpg


env XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=1 DEBUG_DPU_CORE_ID=0 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/refinedet/test_refinedet_batch refinedet_pruned_0_92 images/001.jpg images/002.jpg images/003.jpg
env XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=1 DEBUG_DPU_CORE_ID=1 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/refinedet/test_refinedet_batch refinedet_pruned_0_92 images/001.jpg images/002.jpg images/003.jpg

```

#### reid

```
cd /proj/xsjhdstaff6/mingyue/share/vitis_ai_library/samples/reid
ls
ls images
cat readme
env XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=0 DEBUG_DPU_CORE_ID=0 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/reid/test_reid_batch reid images/001.jpg images/002.jpg images/003.jpg
env XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=1 DEBUG_DPU_CORE_ID=1 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/reid/test_reid_batch reid images/001.jpg images/002.jpg images/003.jpg
```

#### segmentation

```
cd /proj/xsjhdstaff6/mingyue/share/vitis_ai_library/samples/segmentation
ls
ls images
cat readme
env XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=0 DEBUG_DPU_CORE_ID=0 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/segmentation/test_segmentation_batch fpn images/001.png images/002.png images/003.png
env XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=0 DEBUG_DPU_CORE_ID=1 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/segmentation/test_segmentation_batch fpn images/001.png images/002.png images/003.png

```


#### ssd

```
cd /proj/xsjhdstaff6/mingyue/share/vitis_ai_library/samples/ssd
ls
ls images
cat readme
ssd_traffic_pruned_0_9
env XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=0 DEBUG_DPU_CORE_ID=0 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/ssd/test_ssd_batch ssd_traffic_pruned_0_9 images/001.jpg images/002.jpg images/003.jpg
env XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=0 DEBUG_DPU_CORE_ID=1 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/ssd/test_ssd_batch ssd_traffic_pruned_0_9 images/001.jpg images/002.jpg images/003.jpg

```
#### tfssd
```
cd /proj/xsjhdstaff6/mingyue/share/vitis_ai_library/samples/tfssd
ls
ls images
cat readmpe
tfssd_traffic_pruned_0_9

env XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=0 DEBUG_DPU_CORE_ID=0 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/tfssd/test_tfssd_batch ssd_resnet_50_fpn_coco_tf images/001.JPEG images/002.JPEG images/003.JPEG
env XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=0 DEBUG_DPU_CORE_ID=1 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/tfssd/test_tfssd_batch ssd_resnet_50_fpn_coco_tf images/001.JPEG images/002.JPEG images/003.JPEG
env XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=0 DEBUG_DPU_CORE_ID=1 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/tfssd/test_tfssd_batch ssd_resnet_50_fpn_coco_tf images/001.JPEG images/002.JPEG images/003.JPEG

```

#### yolov2
```
cd /proj/xsjhdstaff6/mingyue/share/vitis_ai_library/samples/yolov2
ls
ls images
cat readme
yolov2_voc_pruned_0_77

env XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=0 DEBUG_DPU_CORE_ID=0 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/yolov2/test_yolov2_batch yolov2_voc_pruned_0_77 images/001.png images/002.png images/003.png
env XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=0 DEBUG_DPU_CORE_ID=1 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/yolov2/test_yolov2_batch yolov2_voc_pruned_0_77 images/001.png images/002.png images/003.png


```

#### yolov3
```
cd /proj/xsjhdstaff6/mingyue/share/vitis_ai_library/samples/yolov3
ls
ls images
cat readme
yolov3_voc_pruned_0_77

env XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=0 DEBUG_DPU_CORE_ID=0 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/yolov3/test_yolov3_batch yolov3_voc_tf images/001.png images/002.png images/003.png
env XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=0 DEBUG_DPU_CORE_ID=1 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/yolov3/test_yolov3_batch yolov3_voc_tf images/001.png images/002.png images/003.png images/008.png
env XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=0 DEBUG_DPU_CORE_ID=1 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/yolov3/test_yolov3_batch yolov3_voc_pruned_0_77 images/005.png images/002.png images/008.png


```



end
