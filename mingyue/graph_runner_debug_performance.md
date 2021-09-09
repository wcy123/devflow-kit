# debug performance for graph_runner
# b1 : 10.176.179.52
```
# cd  aisw/Vitis_AI_Library  && bash -ex build_all.sh --type=release
% rsync -avz /opt/petalinux/2021.1/sysroots/cortexa72-cortexa53-xilinx-linux/install/Release b0:/home/root/mingyue/
% rsync -avz /workspace/aisw/Vitis-AI-Library/usefultools/python b0:/home/root/mingyue
% cd /workspace/tmp
% scp root@b0:/usr/share/vitis_ai_library/models/mlperf_ssd_resnet34_tf/mlperf_ssd_resnet34_tf.xmodel ./
% xdputil xmodel -s a.svg /usr/share/vitis_ai_library/models/mlperf_ssd_resnet34_tf/mlperf_ssd_resnet34_tf.xmodel
% xdputil xmodel -t a.txt /usr/share/vitis_ai_library/models/mlperf_ssd_resnet34_tf/mlperf_ssd_resnet34_tf.xmodel
```
## login b0
```
% sshpass -p root ssh-copy-id root@b0
% ssh root@b0
```
## debug mlperf_ssd_resnet34_tf
```
### 1.4.1     5.17fps
% xdputil benchmark -i -1 /usr/share/vitis_ai_library/models/mlperf_ssd_resnet34_tf/mlperf_ssd_resnet34_tf.xmodel 6

### dev  1.7 fps  && close DPU  2.0fps
%cd  /home/root/mingyue/python
% env XLNX_XRT_CU_DRY_RUN=0 PYTHONPATH=/home/root/mingyue/Release/lib/python3.8/site-packages/ LD_LIBRARY_PATH=/home/root/mingyue/Release/lib  xdputil benchmark -i -1 /usr/share/vitis_ai_library/models/mlperf_ssd_resnet34_tf/mlperf_ssd_resnet34_tf.xmodel 6
% env XLNX_XRT_CU_DRY_RUN=1 PYTHONPATH=/home/root/mingyue/Release/lib/python3.8/site-packages/ LD_LIBRARY_PATH=/home/root/mingyue/Release/lib  xdputil benchmark -i -1 /usr/share/vitis_ai_library/models/mlperf_ssd_resnet34_tf/mlperf_ssd_resnet34_tf.xmodel 6

### CPU subgraph not optimized
```

## debug squeezenet
```
### 1.4.1     1158.26fps
% xdputil benchmark -i -1 /usr/share/vitis_ai_library/models/squeezenet/squeezenet.xmodel 6


### dev  552fps  && close DPU 760fps
%cd  /home/root/mingyue/python
% env XLNX_XRT_CU_DRY_RUN=0 PYTHONPATH=/home/root/mingyue/Release/lib/python3.8/site-packages/ LD_LIBRARY_PATH=/home/root/mingyue/Release/lib python3 xdputil.py benchmark -i -1 /usr/share/vitis_ai_library/models/squeezenet/squeezenet.xmodel 6
% env XLNX_XRT_CU_DRY_RUN=1 PYTHONPATH=/home/root/mingyue/Release/lib/python3.8/site-packages/ LD_LIBRARY_PATH=/home/root/mingyue/Release/lib  python3 xdputil.py benchmark -i -1 /usr/share/vitis_ai_library/models/squeezenet/squeezenet.xmodel 6

% env XLNX_XRT_CU_DRY_RUN=0 DEEPHI_PROFILING=1  DEBUG_CPU_TASK=0 PYTHONPATH=/home/root/mingyue/Release/lib/python3.8/site-packages/ LD_LIBRARY_PATH=/home/root/mingyue/Release/lib  python3 xdputil.py benchmark -i -1 /usr/share/vitis_ai_library/models/squeezenet/squeezenet.xmodel 1


% cd  /home/root/mingyue/squeeznet
%env XLNX_XRT_CU_DRY_RUN=0 DEEPHI_PROFILING=1 DEBUG_CPU_TASK=1 LD_LIBRARY_PATH=/home/root/mingyue/Release/lib /home/root/mingyue/Release/share/vitis_ai_library/test/graph_runner/test_graph_runner /usr/share/vitis_ai_library/models/squeezenet/squeezenet.xmodel -i -1 /usr/share/vitis_ai_library/models/squeezenet/squeezenet.xmodel

```

## ENet_cityscapes_pt
```
% cd /workspace/tmp
% scp root@b0:/usr/share/vitis_ai_library/models/ENet_cityscapes_pt/ENet_cityscapes_pt.xmodel ./
% xdputil xmodel -s ENet_cityscapes_pt.svg /usr/share/vitis_ai_library/models/ENet_cityscapes_pt/ENet_cityscapes_pt.xmodel
% xdputil xmodel -t ENet_cityscapes_pt.txt /usr/share/vitis_ai_library/models/ENet_cityscapes_pt/ENet_cityscapes_pt.xmodel
```
```

### 1.4.1
% cd /home/root
% xdputil benchmark -i -1 /usr/share/vitis_ai_library/models/ENet_cityscapes_pt/ENet_cityscapes_pt.xmodel 6


### dev  552fps  && close DPU 760fps
%cd  /home/root/mingyue/python
% env XLNX_XRT_CU_DRY_RUN=0 PYTHONPATH=/home/root/mingyue/Release/lib/python3.8/site-packages/ LD_LIBRARY_PATH=/home/root/mingyue/Release/lib  python3 xdputil.py benchmark -i -1 /usr/share/vitis_ai_library/models/ENet_cityscapes_pt/ENet_cityscapes_pt.xmodel 6
% env XLNX_XRT_CU_DRY_RUN=1 PYTHONPATH=/home/root/mingyue/Release/lib/python3.8/site-packages/ LD_LIBRARY_PATH=/home/root/mingyue/Release/lib  python3 xdputil.py benchmark -i -1 /usr/share/vitis_ai_library/models/ENet_cityscapes_pt/ENet_cityscapes_pt.xmodel 6


% cd  /home/root/mingyue/squeeznet
% cp /usr/share/vitis_ai_library/models/ENet_cityscapes_pt/ENet_cityscapes_pt.xmodel ref/ENet__input_0_fix_0.bin
%env XLNX_XRT_CU_DRY_RUN=0 DEEPHI_PROFILING=1 DEBUG_CPU_TASK=0 1LD_LIBRARY_PATH=/home/root/mingyue/Release/lib /home/root/mingyue/Release/share/vitis_ai_library/test/graph_runner/test_graph_runner /usr/share/vitis_ai_library/models/ENet_cityscapes_pt/ENet_cityscapes_pt.xmodel -i -1 /usr/share/vitis_ai_library/models/ENet_cityscapes_pt/ENet_cityscapes_pt.xmodel
```

## fpn
```
% cd /workspace/tmp
% scp root@b0:/usr/share/vitis_ai_library/models/fpn/fpn.xmodel ./
% xdputil xmodel -s fpn.svg /usr/share/vitis_ai_library/models/fpn/fpn.xmodel
% xdputil xmodel -t fpn.txt /usr/share/vitis_ai_library/models/fpn/fpn.xmodel
```
```

### 1.4.1
% cd /home/root
% xdputil benchmark -i -1 /usr/share/vitis_ai_library/models/fpn/fpn.xmodel 6


### dev  552fps  && close DPU 760fps
%cd  /home/root/mingyue/python
% env XLNX_XRT_CU_DRY_RUN=0 PYTHONPATH=/home/root/mingyue/Release/lib/python3.8/site-packages/ LD_LIBRARY_PATH=/home/root/mingyue/Release/lib  python3 xdputil.py benchmark -i -1 /usr/share/vitis_ai_library/models/fpn/fpn.xmodel 6
% env XLNX_XRT_CU_DRY_RUN=1 PYTHONPATH=/home/root/mingyue/Release/lib/python3.8/site-packages/ LD_LIBRARY_PATH=/home/root/mingyue/Release/lib  python3 xdputil.py benchmark -i -1 /usr/share/vitis_ai_library/models/fpn/fpn.xmodel 6


% cd  /home/root/mingyue/squeeznet
% cp /usr/share/vitis_ai_library/models/fpn/fpn.xmodel ref/ENet__input_0_fix_0.bin
%env XLNX_XRT_CU_DRY_RUN=0 DEEPHI_PROFILING=1 DEBUG_CPU_TASK=0 1LD_LIBRARY_PATH=/home/root/mingyue/Release/lib /home/root/mingyue/Release/share/vitis_ai_library/test/graph_runner/test_graph_runner /usr/share/vitis_ai_library/models/fpn/fpn.xmodel -i -1 /usr/share/vitis_ai_library/models/fpn/fpn.xmodel
```
