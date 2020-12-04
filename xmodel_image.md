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
