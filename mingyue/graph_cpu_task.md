## test all xmodel
# yolov4_leaky_spp_m
```
cd /group/xbjlab/dphi_software/software/workspace/mingyue/d/working/aisw/Vitis-AI-Library/graph_task/test
env XLNX_ENABLE_DEVICES=1 MODEL="yolov4_leaky_spp_m.xmodel" LD_LIBRARY_PATH=$HOME/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK

```
# yolov3_voc_tf
```
cd /group/xbjlab/dphi_software/software/workspace/mingyue/d/working/aisw/Vitis-AI-Library/graph_task/test
env XLNX_ENABLE_DEVICES=1 MODEL="yolov3_voc_tf.xmodel" LD_LIBRARY_PATH=$HOME/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```

# yolov3_voc
```
cd /group/xbjlab/dphi_software/software/workspace/mingyue/d/working/aisw/Vitis-AI-Library/graph_task/test
env XLNX_ENABLE_DEVICES=1 MODEL="yolov3_voc.xmodel" LD_LIBRARY_PATH=$HOME/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```
# yolov3_bdd
```
cd /group/xbjlab/dphi_software/software/workspace/mingyue/d/working/aisw/Vitis-AI-Library/graph_task/test
env XLNX_ENABLE_DEVICES=1 MODEL="yolov3_bdd.xmodel" LD_LIBRARY_PATH=$HOME/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```
# yolov3_adas_pruned_0_9
```
cd /group/xbjlab/dphi_software/software/workspace/mingyue/d/working/aisw/Vitis-AI-Library/graph_task/test
env XLNX_ENABLE_DEVICES=1 MODEL="yolov3_adas_pruned_0_9.xmodel" LD_LIBRARY_PATH=$HOME/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```
# yolov2_voc & yolov2_voc_pruned_0_77 & 71 & 66
```
cd /group/xbjlab/dphi_software/software/workspace/mingyue/d/working/aisw/Vitis-AI-Library/graph_task/test
env XLNX_ENABLE_DEVICES=1 MODEL="yolov2_voc.xmodel" LD_LIBRARY_PATH=$HOME/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
env XLNX_ENABLE_DEVICES=1 MODEL="yolov2_voc_pruned_0_77.xmodel" LD_LIBRARY_PATH=$HOME/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
env XLNX_ENABLE_DEVICES=1 MODEL="yolov2_voc_pruned_0_71.xmodel" LD_LIBRARY_PATH=$HOME/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
env XLNX_ENABLE_DEVICES=1 MODEL="yolov2_voc_pruned_0_66.xmodel" LD_LIBRARY_PATH=$HOME/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```

# xvdpu_1.5_resnet_v1_50_prefetch
```
cd /group/xbjlab/dphi_software/software/workspace/mingyue/d/working/aisw/Vitis-AI-Library/graph_task/test
env XLNX_ENABLE_DEVICES=1 MODEL="xvdpu_1.5_resnet_v1_50_prefetch.xmodel" LD_LIBRARY_PATH=$HOME/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```

# "vpgnet_pruned_0_99"
```
cd /group/xbjlab/dphi_software/software/workspace/mingyue/d/working/aisw/Vitis-AI-Library/graph_task/test
env XLNX_ENABLE_DEVICES=1 MODEL="vpgnet_pruned_0_99.xmodel" LD_LIBRARY_PATH=$HOME/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK

##show a.svg

```
# vgg_19_tf & vgg_16_tf
```
cd /group/xbjlab/dphi_software/software/workspace/mingyue/d/working/aisw/Vitis-AI-Library/graph_task/test
env XLNX_ENABLE_DEVICES=1 MODEL="vgg_19_tf.xmodel" LD_LIBRARY_PATH=$HOME/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK

env XLNX_ENABLE_DEVICES=1 MODEL="vgg_16_tf.xmodel" LD_LIBRARY_PATH=$HOME/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```

# unet_chaos-CT_pt
```
cd /group/xbjlab/dphi_software/software/workspace/mingyue/d/working/aisw/Vitis-AI-Library/graph_task/test
env XLNX_ENABLE_DEVICES=1 MODEL="unet_chaos-CT_pt.xmodel" LD_LIBRARY_PATH=$HOME/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```
# tiny_yolov3_vmss
```
cd /group/xbjlab/dphi_software/software/workspace/mingyue/d/working/aisw/Vitis-AI-Library/graph_task/test
env XLNX_ENABLE_DEVICES=1 MODEL="tiny_yolov3_vmss.xmodel" LD_LIBRARY_PATH=$HOME/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK

#show svg
```
# ssd_traffic_pruned_0_9
```
cd /group/xbjlab/dphi_software/software/workspace/mingyue/d/working/aisw/Vitis-AI-Library/graph_task/test
env XLNX_ENABLE_DEVICES=1 MODEL="ssd_traffic_pruned_0_9.xmodel" LD_LIBRARY_PATH=$HOME/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```

# semantic_seg_citys_tf2
```
cd /group/xbjlab/dphi_software/software/workspace/mingyue/d/working/aisw/Vitis-AI-Library/graph_task/test

env XLNX_ENABLE_DEVICES=1 MODEL="semantic_seg_citys_tf2.xmodel" LD_LIBRARY_PATH=$HOME/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```
# "salsanext_pt"
```
cd /group/xbjlab/dphi_software/software/workspace/mingyue/d/working/aisw/Vitis-AI-Library/graph_task/test
env XLNX_ENABLE_DEVICES=1 MODEL="salsanext_pt.xmodel" LD_LIBRARY_PATH=$HOME/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```
# retinaface
```
cd /group/xbjlab/dphi_software/software/workspace/mingyue/d/working/aisw/Vitis-AI-Library/graph_task/test
env XLNX_ENABLE_DEVICES=1 MODEL="retinaface.xmodel" LD_LIBRARY_PATH=$HOME/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK


# failed segementation fault!  depthwise-conv2d-fix.cpp:160
```
# resnet_v1_50_tf & resnet_v1_152_tf & resnet_v1_101_tf
```
cd /group/xbjlab/dphi_software/software/workspace/mingyue/d/working/aisw/Vitis-AI-Library/graph_task/test
env XLNX_ENABLE_DEVICES=1 MODEL="resnet_v1_50_tf.xmodel" LD_LIBRARY_PATH=$HOME/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
env XLNX_ENABLE_DEVICES=1 MODEL="resnet_v1_152_tf.xmodel" LD_LIBRARY_PATH=$HOME/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
env XLNX_ENABLE_DEVICES=1 MODEL="resnet_v1_101_tf.xmodel" LD_LIBRARY_PATH=$HOME/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```
# resnet50_tf2
```
cd /group/xbjlab/dphi_software/software/workspace/mingyue/d/working/aisw/Vitis-AI-Library/graph_task/test
env XLNX_ENABLE_DEVICES=1 MODEL="resnet50_tf2.xmodel" LD_LIBRARY_PATH=$HOME/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK

# Failed ： DPU compare data failed.

```
# resnet50_pt & resnet50 & resnet18
```
cd /group/xbjlab/dphi_software/software/workspace/mingyue/d/working/aisw/Vitis-AI-Library/graph_task/test

env XLNX_ENABLE_DEVICES=1 MODEL="resnet50_pt.xmodel" LD_LIBRARY_PATH=$HOME/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK

env XLNX_ENABLE_DEVICES=1 MODEL="resnet50.xmodel" LD_LIBRARY_PATH=$HOME/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
env XLNX_ENABLE_DEVICES=1 MODEL="resnet18.xmodel" LD_LIBRARY_PATH=$HOME/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK

# show svg
```

# reid
```
env XLNX_ENABLE_DEVICES=1 MODEL="reid.xmodel" LD_LIBRARY_PATH=$HOME/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK

```

# refinedet_VOC_tf
```
env XLNX_ENABLE_DEVICES=1 MODEL="refinedet_VOC_tf.xmodel" LD_LIBRARY_PATH=$HOME/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```



# model :  /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/
