# debug `efficientnet-b0-tf2`


## get golden with vaie

``` console
% mkdir -p /workspace/aisw/debug_efficientnet-b0_tf2
% cd /workspace/aisw/debug_efficientnet-b0_tf2
% mkdir -p ./usr/share/vitis_ai_library/models
% scp -r xsjsda153:/proj/xsjhdstaff4/yanjunz/vitis-ai-staging/myws/test/debug_xmodel/models/efficientnet-b0_tf2 ./usr/share/vitis_ai_library/models
% env MODE=ref GOLDEN_CACHE=/workspace/aisw/vitis-ai-library-samples-res/input_bin/golden MODEL=efficientnet-b0_tf2 MODEL_ZOO_ROOT=/workspace/aisw/debug_efficientnet-b0_tf2  DEBUG_COMPARE=1 python3 /workspace/aisw/Vitis-AI-Library/graph_runner/test/run_vaie.py /workspace/aisw/sw_jenkins_pipeline/config/xmodel_graph_edge.json
```

``` console
% xdputil xmodel -t a.txt ./usr/share/vitis_ai_library/models/efficientnet-b0_tf2/efficientnet-b0_tf2.xmodel
% xdputil xmodel -s a.svg ./usr/share/vitis_ai_library/models/efficientnet-b0_tf2/efficientnet-b0_tf2.xmodel
% xdputil xmodel -S s.svg ./usr/share/vitis_ai_library/models/efficientnet-b0_tf2/efficientnet-b0_tf2.xmodel
% xdputil xmodel -l ./usr/share/vitis_ai_library/models/efficientnet-b0_tf2/efficientnet-b0_tf2.xmodel
```

## on board test

```
% scp
```

``` console
% ssh b0
% cd /group/xbjlab/dphi_software/software/workspace/qiuyuny/sft_zcu102_bs/workspace/sw_zcu102_internal_test@13/vitis-ai-library/graph_runner/test
% env LD_LIBRARY_PATH=/home/root/mingyue/Debug/lib GOLDEN_CACHE=/group/xbjlab/dphi_software/software/workspace/qiuyuny/sft_zcu102_bs/workspace/sw_zcu102_internal_test@13/vitis-ai-library-samples-res/input_bin/golden MODEL=efficientnet-b0_tf2 MODEL_ZOO_ROOT=/  DEBUG_COMPARE=1 python3 /home/wcy/graph_runner/test/run_graph.py /group/xbjlab/dphi_software/software/workspace/qiuyuny/sft_zcu102_bs/workspace/sw_zcu102_internal_test@13/config/xmodel_graph_edge.json

```



## back on server


```
# output of vaie
[UNILOG][INFO] Dump Resnet18__Resnet18_BatchNorm1d_bottleneck__411 (shape={1, 256}, type=FLOAT32) into /tmp/chunywan/vaie.log/efficientnet-b0_tf2/ref/batch_0/Resnet18__Resnet18_BatchNorm1d_bottleneck__411.bin
[UNILOG][INFO] Dump Resnet18__Resnet18_input_fix (shape={1, 256}, type=XINT8) into /tmp/chunywan/vaie.log/efficientnet-b0_tf2/ref/batch_0/Resnet18__Resnet18_input_fix.bin
```
min
``` console
% mkdir -p /workspace/aisw/debug_efficientnet-b0_tf2
% cd /workspace/aisw/debug_efficientnet-b0_tf2
% mkdir -p out; mkdir -p ref

## input
% cp /tmp/mingyue/vaie.log/efficientnet-b0_tf2/ref/batch_0/quant_stem_conv_fix.bin ref/quant_stem_conv_fix_0.bin


## output
% cp /tmp/mingyue/vaie.log/efficientnet-b0_tf2/ref/batch_0/quant_stem_activation_mul_fix.bin ref/quant_stem_activation_mul_fix.bin


% cd /workspace/aisw/debug_efficientnet-b0_tf2
% env XLNX_ENABLE_DUMP=1 USE_CPU_TASK=0 /home/mingyue/build/build.Ubuntu.18.04.x86_64.Debug/Vitis-AI-Library/graph_runner/test_graph_runner ./usr/share/vitis_ai_library/models/efficientnet-b0_tf2/efficientnet-b0_tf2.xmodel /home/mingyue/build/build.Ubuntu.18.04.x86_64.Debug/Vitis-AI-Library/graph_runner/test_graph_runner  -i 2
% d 0.quant_stem_activation_mul_fix.bin
% d ref/quant_stem_activation_mul_fix.bin
% cp ref/quant_stem_activation_mul_fix.bin ref.bin
% cp 0.Resnet18__Resnet18_BatchNorm1d_bottleneck__411.bin ref.bin

%env XLNX_ENABLE_DUMP=1 USE_CPU_TASK=1 /home/mingyue/build/build.Ubuntu.18.04.x86_64.Debug/Vitis-AI-Library/graph_runner/test_graph_runner ./usr/share/vitis_ai_library/models/efficientnet-b0_tf2/efficientnet-b0_tf2.xmodel /home/mingyue/build/build.Ubuntu.18.04.x86_64.Debug/Vitis-AI-Library/graph_runner/test_graph_runner  -i 2


```

it is strange that on x86, the op is correct.

test is on zcu102


``` console
% ssh b3
% mkdir -p out; mkdir -p ref
% exit
% rsync -av /opt/petalinux/2021.1/sysroots/cortexa72-cortexa53-xilinx-linux/install/Debug b3:/home/root/mingyue/Debug
% cd /home/mingyue/test
% env LD_LIBRARY_PATH=/home/root/mingyue/Debug/lib GOLDEN_CACHE=/group/xbjlab/dphi_software/software/workspace/qiuyuny/sft_zcu102_bs/workspace/sw_zcu102_internal_test@13/vitis-ai-library-samples-res/input_bin/golden MODEL=efficientnet-b0_tf2 MODEL_ZOO_ROOT=/  DEBUG_COMPARE=1 python3 run_graph.py xmodel_graph_edge.json
```
