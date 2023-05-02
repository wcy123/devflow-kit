# develop xmode image



## classification

``` console

% env DEBUG_XMODEL_IMAGE=1 DEBUG_XMODEL_JIT=1 /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/classification/test_classification resnet_v1_50_tf /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/vitis-ai-library-samples-res/samples/classification/sample_classification.jpg
% env DEBUG_XMODEL_IMAGE=1 DEBUG_XMODEL_JIT=1 /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/xmodel_image/test_xmodel /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/xmodel_image/models/resnet_v1_50_tf/resnet_v1_50_tf.xmodel /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/vitis-ai-library-samples-res/samples/classification/sample_classification.jpg
```


## densebox

``` console
% ln -s /usr/share/vitis_ai_library/models/densebox_320_320/densebox_320_320.xmodel /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/xmodel_image/models/densebox_320_320/densebox_320_320.xmodel
% env XLNX_ENABLE_DUMP=0 DEBUG_XMODEL_IMAGE=1 DEBUG_XMODEL_JIT=1 /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/overview/test_jpeg_facedetect densebox_320_320 /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/vitis-ai-library-samples-res/samples/facedetect/sample_facedetect.jpg
% mv dump dump.test

% env XLNX_ENABLE_DUMP=0 DEBUG_XMODEL_IMAGE=1 DEBUG_XMODEL_JIT=1 /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/xmodel_image/test_xmodel /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/xmodel_image/models/densebox_320_320/densebox_320_320.xmodel /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/vitis-ai-library-samples-res/samples/facedetect/sample_facedetect.jpg
% d dump/subgraph_L0/input/0.data_fixed.bin  dump.test/subgraph_L0/input/0.data_fixed.bin
% cat /usr/share/vitis_ai_library/models/densebox_320_320/densebox_320_320.prototxt
% find  /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library | grep test_jpeg_face



``` console
% cd /var/lib/docker/scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/usr/share/vitis_ai_library/models/densebox_320_320
% /home/$USER/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir dump_txt densebox_320_320.xmodel densebox_320_320.txt
% /home/$USER/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir subgraph densebox_320_320.xmodel >subgraph.txt
% /home/$USER/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir svg densebox_320_320.xmodel densebox_320_320.svg
% realpath densebox_320_320.svg
% ssh xcdl190253 #
% cd /group/modelzoo/internal-cooperation-models/caffe/densebox_320_320/fix/acc/decrypted/
% scp xcdl190253:/group/modelzoo/internal-cooperation-models/caffe/densebox_320_320/fix/fix_train_test.caffemodel .
%
% scp xcdl190253:/group/modelzoo/internal-cooperation-models/caffe/densebox_320_320/fix/fix_test.prototxt .
% env DECENT_DEBUG=5 LD_LIBRARY_PATH=/home/$USER/.local/lib64:/usr/local/lib:/usr/local/lib64:/opt/xilinx/xrt/lib /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/cp/caffe/build/tools/vai_q test -model fix_test.prototxt  -weights fix_train_test.caffemodel   -test_iter 1
```



## plate number


``` console

% env DEBUG_XMODEL_IMAGE=1 DEBUG_XMODEL_JIT=1 /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/overview/test_jpeg_platenum plate_num /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/vitis-ai-library-samples-res/samples/platenum/samples_platenum.jpg

% env DEBUG_XMODEL_IMAGE=1 DEBUG_XMODEL_JIT=1 /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/xmodel_image/test_xmodel  /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/xmodel_image/models/plate_num/plate_num.xmodel  /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/vitis-ai-library-samples-res/samples/platenum/samples_platenum.jpg
```



## facefeature


``` console
% mkdir -p /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/xmodel_image/models/facerec_resnet20
% ln -s /usr/share/vitis_ai_library/models/facerec_resnet20/facerec_resnet20.xmodel /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/xmodel_image/models/facerec_resnet20

% find /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/xmodel_image/models/facerec_resnet20

% cd /usr/share/vitis_ai_library/models/facerec_resnet20/
% model=$(basename $(pwd))
% /home/$USER/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir dump_txt $model.xmodel $model.txt
% /home/$USER/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir subgraph $model.xmodel >subgraph.txt
% /home/$USER/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir svg $model.xmodel $model.svg
% realpath $model.svg


% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/debug_vaie
% rm -fr dump
% identify /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/vitis-ai-library-samples-res/samples/facefeature/sample_facefeature.jpg

% env DEBUG_IMAGE_UTIL=1 XLNX_ENABLE_DUMP=1 DEBUG_XMODEL_JIT=1 /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/overview/test_jpeg_facefeature facerec_resnet20 /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/vitis-ai-library-samples-res/samples/facefeature/sample_facefeature.jpg
% mv dump dump.lib

% env DEBUG_IMAGE_UTIL=1 XLNX_ENABLE_DUMP=1 DEBUG_XMODEL_JIT=1 /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/xmodel_image/test_xmodel  /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/xmodel_image/models/facerec_resnet20/facerec_resnet20.xmodel  /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/vitis-ai-library-samples-res/samples/facefeature/sample_facefeature.jpg
% find dump | grep input
% d dump/subgraph_Add_1/input/0.data_fixed.bin dump.lib/subgraph_Add_1/input/0.data_fixed.bin
```

## `face_landmark`

``` console


% env DEBUG_IMAGE_UTIL=1 XLNX_ENABLE_DUMP=1 DEBUG_XMODEL_JIT=1 /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/overview/test_jpeg_facelandmark  face_landmark /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/vitis-ai-library-samples-res/samples/facelandmark/sample_facelandmark.jpg

% find /usr/share/vitis_ai_library/models/ | grep land

% cd /usr/share/vitis_ai_library/models/face_landmark
% model=$(basename $(pwd))
% /home/$USER/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir dump_txt $model.xmodel $model.txt
% /home/$USER/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir subgraph $model.xmodel >subgraph.txt
% /home/$USER/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir svg $model.xmodel $model.svg
% realpath $model.svg


% mkdir -p /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/xmodel_image/models/face_landmark
% ln -s /usr/share/vitis_ai_library/models/face_landmark/face_landmark.xmodel /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/xmodel_image/models/face_landmark
% cat /usr/share/vitis_ai_library/models/face_landmark/face_landmark.prototxt



% env DEBUG_IMAGE_UTIL=1 XLNX_ENABLE_DUMP=1 DEBUG_XMODEL_JIT=1 /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/xmodel_image/test_xmodel  /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/xmodel_image/models/face_landmark/face_landmark.xmodel  /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/vitis-ai-library-samples-res/samples/facelandmark/sample_facelandmark.jpg
```


## `facequality5pt`



``` console

% env DEBUG_IMAGE_UTIL=1 XLNX_ENABLE_DUMP=1 DEBUG_XMODEL_JIT=1 /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/overview/test_jpeg_facequality5pt  face-quality /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/vitis-ai-library-samples-res/samples/facequality5pt/sample_facequality5pt.jpg
% find /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/vitis-ai-library-samples-res/ | grep sample_facequality5pt.jpg

% cd /usr/share/vitis_ai_library/models/face-quality/
% model=$(basename $(pwd))
% /home/$USER/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir dump_txt $model.xmodel $model.txt
% /home/$USER/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir subgraph $model.xmodel >subgraph.txt
% /home/$USER/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir svg $model.xmodel $model.svg
% realpath $model.svg


% mkdir -p /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/xmodel_image/models/face-quality
% ln -s /usr/share/vitis_ai_library/models/face-quality/face-quality.xmodel /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/xmodel_image/models/face-quality
% cat /usr/share/vitis_ai_library/models/face-quality/face-quality.prototxt



% env DEBUG_IMAGE_UTIL=1 XLNX_ENABLE_DUMP=1 DEBUG_XMODEL_JIT=1 /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/xmodel_image/test_xmodel  /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/xmodel_image/models/face-quality/face-quality.xmodel /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/vitis-ai-library-samples-res/samples/facequality5pt/sample_facequality5pt.jpg
```

## `hourglass`


``` console

% env DEBUG_IMAGE_UTIL=1 XLNX_ENABLE_DUMP=1 DEBUG_XMODEL_JIT=1 /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/overview/test_jpeg_hourglass  hourglass-pe_mpii /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/vitis-ai-library-samples-res/samples/hourglass/sample_hourglass.png

% cd /usr/share/vitis_ai_library/models/face-quality/
% model=$(basename $(pwd))
% /home/$USER/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir dump_txt $model.xmodel $model.txt
% /home/$USER/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir subgraph $model.xmodel >subgraph.txt
% /home/$USER/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir svg $model.xmodel $model.svg
% realpath $model.svg


% mkdir -p /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/xmodel_image/models/face-quality
% ln -s /usr/share/vitis_ai_library/models/face-quality/face-quality.xmodel /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/xmodel_image/models/face-quality
% cat /usr/share/vitis_ai_library/models/face-quality/face-quality.prototxt



% env DEBUG_IMAGE_UTIL=1 XLNX_ENABLE_DUMP=1 DEBUG_XMODEL_JIT=1 /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/xmodel_image/test_xmodel  /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/xmodel_image/models/face-quality/face-quality.xmodel /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/vitis-ai-library-samples-res/samples/facequality5pt/sample_facequality5pt.jpg
```


## `lanedetect`

``` console

% env DEBUG_IMAGE_UTIL=1 XLNX_ENABLE_DUMP=0 DEBUG_XMODEL_JIT=1  /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/overview/test_jpeg_lanedetect vpgnet_pruned_0_99 /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/vitis-ai-library-samples-res/samples/lanedetect/sample_lanedetect.jpg
% find dump | grep type
% cd /usr/share/vitis_ai_library/models/vpgnet_pruned_0_99
% model=$(basename $(pwd))
% /home/$USER/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir dump_txt $model.xmodel $model.txt
% /home/$USER/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir subgraph $model.xmodel >subgraph.txt
% /home/$USER/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir svg $model.xmodel $model.svg
% realpath $model.svg
% cat subgraph.txt

% mkdir -p ref
% cp dump/subgraph_L6a/output/0.type_tile_fixed.bin ref/type-tile_fixed.bin
% /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/graph_task/test_graph_task /usr/share/vitis_ai_library/models/vpgnet_pruned_0_99/vpgnet_pruned_0_99.xmodel -i 2

% mkdir -p /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/xmodel_image/models/vpgnet_pruned_0_99
% ln -s /usr/share/vitis_ai_library/models/vpgnet_pruned_0_99/vpgnet_pruned_0_99.xmodel /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/xmodel_image/models/vpgnet_pruned_0_99
% cat /usr/share/vitis_ai_library/models/vpgnet_pruned_0_99/vpgnet_pruned_0_99.prototxt


% cp 0.type-tile_fixed_.bin ref/type-tile_fixed_.bin

% env DEBUG_IMAGE_UTIL=1 XLNX_ENABLE_DUMP=1 DEBUG_XMODEL_JIT=1 /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/xmodel_image/test_postprocessor /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/xmodel_image/models/vpgnet_pruned_0_99/vpgnet_pruned_0_99.xmodel

% ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/cpu_task/show_binary_image -w 80 -h 60 --num_of_channels 1 -e 1 -f DEBUG.BIN >a.txt

% env DEBUG_IMAGE_UTIL=1 XLNX_ENABLE_DUMP=0 DEBUG_XMODEL_JIT=1 /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/xmodel_image/test_xmodel  /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/xmodel_image/models/vpgnet_pruned_0_99/vpgnet_pruned_0_99.xmodel  /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/vitis-ai-library-samples-res/samples/lanedetect/sample_lanedetect.jpg

```


## `open pose`

``` console
% cd /usr/share/vitis_ai_library/models/openpose_pruned_0_3
% model=$(basename $(pwd))
% /home/$USER/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir dump_txt $model.xmodel $model.txt
% /home/$USER/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir subgraph $model.xmodel >subgraph.txt
% /home/$USER/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir svg $model.xmodel $model.svg
% realpath $model.svg
% cat subgraph.txt

% env DEBUG_IMAGE_UTIL=1 XLNX_ENABLE_DUMP=1 DEBUG_XMODEL_JIT=1 /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/overview/test_jpeg_openpose openpose_pruned_0_3 /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/vitis-ai-library-samples-res/samples/openpose/sample_openpose.jpg

% mkdir -p ref

% cp dump/subgraph_Mconv1_stage2_L1/output/0.Mconv7_stage6_L2_fixed.bin ref/Mconv7_stage6_L2_fixed.bin
% /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/graph_task/test_graph_task /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/xmodel_image/models/openpose_pruned_0_3/openpose_pruned_0_3.xmodel -i 2
% cp 0.Mconv7_stage6_L2_fixed_.bin ref/

% cp dump/subgraph_Mconv1_stage2_L1/output/0.Mconv7_stage6_L1_fixed.bin ref/Mconv7_stage6_L1_fixed.bin
% /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/graph_task/test_graph_task /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/xmodel_image/models/openpose_pruned_0_3/openpose_pruned_0_3.xmodel -i 3
% cp 0.Mconv7_stage6_L1_fixed_.bin ref/

% cp  ref/0.Mconv7_stage6_L1_fixed_.bin ref/Mconv7_stage6_L1_fixed_.bin
% cp  ref/0.Mconv7_stage6_L2_fixed_.bin ref/Mconv7_stage6_L2_fixed_.bin
% env DEBUG_IMAGE_UTIL=1 XLNX_ENABLE_DUMP=1 DEBUG_XMODEL_JIT=1 /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/xmodel_image/test_postprocessor /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/xmodel_image/models/openpose_pruned_0_3/openpose_pruned_0_3.xmodel


% mkdir -p /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/xmodel_image/models/openpose_pruned_0_3
% ln -s  /usr/share/vitis_ai_library/models/openpose_pruned_0_3/openpose_pruned_0_3.xmodel /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/xmodel_image/models/openpose_pruned_0_3
% cat /usr/share/vitis_ai_library/models/openpose_pruned_0_3/openpose_pruned_0_3.prototxt

% env DEBUG_IMAGE_UTIL=1 XLNX_ENABLE_DUMP=0 DEBUG_XMODEL_JIT=1 /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/xmodel_image/test_xmodel  /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/xmodel_image/models/openpose_pruned_0_3/openpose_pruned_0_3.xmodel /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/vitis-ai-library-samples-res/samples/openpose/sample_openpose.jpg

```


## `tfssd`

``` console
% cd /usr/share/vitis_ai_library/models/ssd_resnet_50_fpn_coco_tf
% model=$(basename $(pwd))
% /home/$USER/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir dump_txt $model.xmodel $model.txt
% /home/$USER/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir subgraph $model.xmodel >subgraph.txt
% /home/$USER/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir svg $model.xmodel $model.svg
% realpath $model.svg
% cat subgraph.txt
% xmodel=$(realpath $model.xmodel)
% jpeg=/group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/vitis-ai-library-samples-res/samples/tfssd/sample_tfssd.jpg


% env DEBUG_IMAGE_UTIL=1 XLNX_ENABLE_DUMP=1 DEBUG_XMODEL_JIT=1 /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/overview/test_jpeg_tfssd $model $jpeg
% mkdir -p ref
% cp dump/subgraph_FeatureExtractor_resnet_v1_50_fpn_bottom_up_block5_Conv2D/input/0.image_tensor_aquant.bin ref/image_tensor_aquant.bin


% env  XLNX_ENABLE_DUMP=1 /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/graph_task/test_graph_task $xmodel -i -1
% find . | grep aquant_box_encodings
% cp 0.class_predictions_with_background_fix.bin ref/class_predictions_with_background_fix.bin

% cp ./dump/subgraph_FeatureExtractor_resnet_v1_50_fpn_bottom_up_block5_Conv2D/output/0.concat_aquant.bin ref/concat_aquant.bin
% /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/graph_task/test_graph_task $xmodel -i 3
% cp ./dump/subgraph_box_encodings_fix/concat_2f_aquant_box_encodings_0.bin ref/concat_aquant_box_encodings.bin
% cp dump/subgraph_class_predictions_with_background_fix/concat_1_2f_aquant_class_predictions_with_background_0.bin ref/concat_1_aquant_class_predictions_with_background.bin

% mkdir -p /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/xmodel_image/models/$model
% ln -s /usr/share/vitis_ai_library/models/$model/$model.xmodel /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/xmodel_image/models/$model
%
% touch /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/xmodel_image/models/$model.py

% env DEBUG_IMAGE_UTIL=1 XLNX_ENABLE_DUMP=1 DEBUG_XMODEL_JIT=1 /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/xmodel_image/test_postprocessor /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/xmodel_image/models/$model/$model.xmodel
```
