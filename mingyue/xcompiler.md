##
```
cd /home/mingyue/d/working/aisw/model_zoo_builder
cat rev.list
bash  -ex build_xcompiler.sh --build-xcompiler
```
## resnet_v1_50_v1.5_pruned
```
~/.local/bin/xnnc-run --type tensorflow --layout NHWC --model /home/mingyue/d/working/dpdlf/xvdpu/pb/Resnet50_v1.5_pruned_74/quantize_eval_model.pb --out /home/mingyue/d/working/dpdlf/xvdpu/pb/Resnet50_v1.5_pruned_74/Resnet50_v1.5_pruned_74_parsed.xmodel
~/.local/CentOS.7.6.1810.x86_64.Release/bin/xcompiler -i /home/mingyue/d/working/dpdlf/xvdpu/pb/Resnet50_v1.5_pruned_74/Resnet50_v1.5_pruned_74_parsed.xmodel -o /home/mingyue/d/working/dpdlf/xvdpu/pb/Resnet50_v1.5_pruned_74/Resnet50_v1.5_pruned_74.xmodel -a "DPUCVDX8G_ISA0_B8192C32B3_ELP8"
scp /home/mingyue/d/working/dpdlf/xvdpu/pb/Resnet50_v1.5_pruned_74/Resnet50_v1.5_pruned_74.xmodel root@10.176.179.54:~/
```
## yolov3_voc caffe
```
~/.local/bin/xnnc-run --type caffe --layout NHWC --model /home/mingyue/d/working/dpdlf/xvdpu/pb/yolov3_voc/deploy.caffemodel --proto /home/mingyue/d/working/dpdlf/xvdpu/pb/yolov3_voc/deploy.prototxt  --out /home/mingyue/d/working/dpdlf/xvdpu/pb/yolov3_voc/yolov3_voc_parsed.xmodel
~/.local/CentOS.7.6.1810.x86_64.Release/bin/xcompiler -i /home/mingyue/d/working/dpdlf/xvdpu/pb/yolov3_voc/yolov3_voc_parsed.xmodel -o /home/mingyue/d/working/dpdlf/xvdpu/pb/yolov3_voc/yolov3_voc.xmodel -a "DPUCVDX8G_ISA0_B8192C32B3_ELP8"
scp /home/mingyue/d/working/dpdlf/xvdpu/pb/yolov3_voc/yolov3_voc.xmodel root@10.176.179.54:~/
```
## yolov3_voc tf
```
~/.local/bin/xnnc-run --type tensorflow --layout NHWC --model /home/mingyue/d/working/dpdlf/xvdpu/pb/yolov3_voc_tf/quantize_eval_model.pb --out /home/mingyue/d/working/dpdlf/xvdpu/pb/yolov3_voc_tf/yolov3_voc_tf_parsed.xmodel --inputs-shape "1,416,416,3"

~/.local/CentOS.7.6.1810.x86_64.Release/bin/xcompiler -i /home/mingyue/d/working/dpdlf/xvdpu/pb/yolov3_voc_tf/yolov3_voc_tf_parsed.xmodel -o /home/mingyue/d/working/dpdlf/xvdpu/pb/yolov3_voc_tf/yolov3_voc_tf.xmodel -a "DPUCVDX8G_ISA0_B8192C32B3_ELP8"

scp /home/mingyue/d/working/dpdlf/xvdpu/pb/Resnet50_v1.5_pruned_74/Resnet50_v1.5_pruned_74.xmodel root@10.176.179.54:~/

```
