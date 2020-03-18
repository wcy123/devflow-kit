```
cd ~/d/working/mingyue/vart_samples_release
scp mingyue@xcdl190256:/group/dphi_software/vitis_ai_library/r1.1/*.deb ./
ls
dpkg -X vitis_ai_model_ZCU102_2019.2-r1.1.0.deb 102_models
dpkg -X vitis_ai_model_ZCU104_2019.2-r1.1.0.deb 104_models
dpkg -X xilinx_model_zoo-1.1.0-Linux.deb u50_models

ls
cd vart_samples_and_models
rm -rf videos
rm -rf samples/images
find . -iname *.xmodel

cp ../u50_models/usr/share/vitis_ai_library/models/yolov3_adas_pruned_0_9/yolov3_adas_pruned_0_9.xmodel ./samples/adas_detection/model_dir_for_U50/yolov3_adas_pruned_0_9.xmodel
vi ../u50_models/usr/share/vitis_ai_library/models/yolov3_adas_pruned_0_9/meta.json
# kernle : subgraph_layer117-conv_weights(fix)
cat ./samples/adas_detection/model_dir_for_U50/meta.json

cp ../102_models/usr/share/vitis_ai_library/models/yolov3_adas_pruned_0_9/yolov3_adas_pruned_0_9.elf  ./samples/adas_detection/model_dir_for_zcu102/yolov3_adas_pruned_0_9.elf
cp ../104_models/usr/share/vitis_ai_library/models/yolov3_adas_pruned_0_9/yolov3_adas_pruned_0_9.elf  ./samples/adas_detection/model_dir_for_zcu104/yolov3_adas_pruned_0_9.elf




cp ../u50_models/usr/share/vitis_ai_library/models/inception_v1_tf/inception_v1_tf.xmodel ./samples/inception_v1_mt_py/model_dir_for_U50/inception_v1_tf.xmodel
md5sum ../u50_models/usr/share/vitis_ai_library/models/inception_v1_tf/inception_v1_tf.xmodel ./samples/inception_v1_mt_py/model_dir_for_U50/inception_v1_tf.xmodel
vi ../u50_models/usr/share/vitis_ai_library/models/inception_v1_tf/meta.json
# ** "kernel": [ "subgraph_InceptionV1/InceptionV1/Mixed_4b/Branch_3/Conv2d_0b_1x1/Conv2D(fix)" ]
cat ./samples/inception_v1_mt_py/model_dir_for_U50/meta.json
vi ./samples/inception_v1_mt_py/model_dir_for_U50/meta.json
cp ../102_models/usr/share/vitis_ai_library/models/inception_v1_tf/inception_v1_tf.elf ./samples/inception_v1_mt_py/model_dir_for_zcu102/inception_v1_tf.elf
cp ../104_models/usr/share/vitis_ai_library/models/inception_v1_tf/inception_v1_tf.elf ./samples/inception_v1_mt_py/model_dir_for_zcu104/inception_v1_tf.elf



cp ../u50_models/usr/share/vitis_ai_library/models/sp_net/sp_net.xmodel ./samples/pose_detection/model_dir_for_U50/pose_0/sp_net.xmodel
cp ../u50_models/usr/share/vitis_ai_library/models/sp_net/sp_net.xmodel ./samples/pose_detection/model_dir_for_U50/pose_2/sp_net.xmodel
cp ../u50_models/usr/share/vitis_ai_library/models/ssd_pedestrain_pruned_0_97/ssd_pedestrain_pruned_0_97.xmodel ./samples/pose_detection/model_dir_for_U50/ssd/ssd_pedestrain_pruned_0_97.xmodel
vi ../u50_models/usr/share/vitis_ai_library/models/sp_net/meta.json
#  "kernel": [ "subgraph_inception_4d/pool(fix)","subgraph_fc_coordinate_weights(fix)","subgraph_fc_visible_weights(fix)" ],
cat ./samples/pose_detection/model_dir_for_U50/pose_0/meta.json
cat ./samples/pose_detection/model_dir_for_U50/pose_2/meta.json
cat ../u50_models/usr/share/vitis_ai_library/models/ssd_pedestrain_pruned_0_97/meta.json
#  **"kernel": [ "subgraph_mbox_conf(OptimizeDDRFlattenConcatStructure)(ModifyAsix)_generation_0_child_concat(StandardizeConcat)(fix)" ]
cat ./samples/pose_detection/model_dir_for_U50/ssd/meta.json
vi ./samples/pose_detection/model_dir_for_U50/ssd/meta.json
/home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/vart/dpu-runner/test/show_kernel ../u50_models/usr/share/vitis_ai_library/models/ssd_pedestrain_pruned_0_97/ssd_pedestrain_pruned_0_97.xmodel

ls ./samples/pose_detection/model_dir_for_zcu102/pose_0
cp ../102_models/usr/share/vitis_ai_library/models/sp_net/sp_net.elf  ./samples/pose_detection/model_dir_for_zcu102/pose_0/sp_net.elf
cp ../102_models/usr/share/vitis_ai_library/models/sp_net/sp_net.elf  ./samples/pose_detection/model_dir_for_zcu102/pose_2/sp_net.elf
cp ../104_models/usr/share/vitis_ai_library/models/sp_net/sp_net.elf  ./samples/pose_detection/model_dir_for_zcu104/pose_0/sp_net.elf
cp ../104_models/usr/share/vitis_ai_library/models/sp_net/sp_net.elf  ./samples/pose_detection/model_dir_for_zcu104/pose_2/sp_net.elf
cp ../102_models/usr/share/vitis_ai_library/models/ssd_pedestrain_pruned_0_97/ssd_pedestrain_pruned_0_97.elf  ./samples/pose_detection/model_dir_for_zcu102/ssd/ssd_pedestrain_pruned_0_97.elf
cp ../104_models/usr/share/vitis_ai_library/models/ssd_pedestrain_pruned_0_97/ssd_pedestrain_pruned_0_97.elf  ./samples/pose_detection/model_dir_for_zcu104/ssd/ssd_pedestrain_pruned_0_97.elf



md5sum ../u50_models/usr/share/vitis_ai_library/models/resnet50/resnet50.xmodel ./samples/resnet50/model_dir_for_U50/resnet50.xmodel
cp ../u50_models/usr/share/vitis_ai_library/models/resnet50/resnet50.xmodel ./samples/resnet50/model_dir_for_U50/resnet50.xmodel
vi ../u50_models/usr/share/vitis_ai_library/models/resnet50/meta.json
#  "kernel": [ "subgraph_res5b_branch2a_weights(fix)" ]
cat ./samples/resnet50/model_dir_for_U50/meta.json
cp ../102_models/usr/share/vitis_ai_library/models/resnet50/resnet50.elf ./samples/resnet50/model_dir_for_zcu102/resnet50.elf
cp ../104_models/usr/share/vitis_ai_library/models/resnet50/resnet50.elf ./samples/resnet50/model_dir_for_zcu104/resnet50.elf


find . -iname *.xmodel
cp ../u50_models/usr/share/vitis_ai_library/models/fpn/fpn.xmodel ./samples/segmentation/model_dir_for_U50/fpn.xmodel
vi  ../u50_models/usr/share/vitis_ai_library/models/fpn/meta.json
#  "kernel": [ "subgraph_inception_4e/pool(fix)" ]
cat ./samples/segmentation/model_dir_for_U50/meta.json
vi ./samples/segmentation/model_dir_for_U50/meta.json
cp ../102_models/usr/share/vitis_ai_library/models/fpn/fpn.elf ./samples/segmentation/model_dir_for_zcu102/fpn.elf
cp ../104_models/usr/share/vitis_ai_library/models/fpn/fpn.elf ./samples/segmentation/model_dir_for_zcu104/fpn.elf


cp ../u50_models/usr/share/vitis_ai_library/models/ssd_traffic_pruned_0_9/ssd_traffic_pruned_0_9.xmodel ./samples/video_analysis/model_dir_for_U50/ssd_traffic_pruned_0_9.xmodel
cat ../u50_models/usr/share/vitis_ai_library/models/ssd_traffic_pruned_0_9/meta.json
# ** "kernel": [ "subgraph_mbox_conf(OptimizeDDRFlattenConcatStructure)(ModifyAsix)_generation_0_child_concat(StandardizeConcat)(fix)" ]
cat ./samples/video_analysis/model_dir_for_U50/meta.json
vi ./samples/video_analysis/model_dir_for_U50/meta.json
cp ../102_models/usr/share/vitis_ai_library/models/ssd_traffic_pruned_0_9/ssd_traffic_pruned_0_9.elf ./samples/video_analysis/model_dir_for_zcu102/ssd_traffic_pruned_0_9.elf
cp ../104_models/usr/share/vitis_ai_library/models/ssd_traffic_pruned_0_9/ssd_traffic_pruned_0_9.elf ./samples/video_analysis/model_dir_for_zcu104/ssd_traffic_pruned_0_9.elf




cd samples
ls
cd adas_detection
ls
cd model_dir_for_U50
ls



```
