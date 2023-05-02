# debug `facereid-large_pt`


## get golden with vaie

``` console
% mkdir -p /workspace/aisw/debug_facereid-large_pt
% cd /workspace/aisw/debug_facereid-large_pt
% mkdir -p ./usr/share/vitis_ai_library/models
% scp -r xsjsda153:/proj/xsjhdstaff4/yanjunz/vitis-ai-staging/myws/test/debug_xmodel/models/facereid-large_pt ./usr/share/vitis_ai_library/models
% env MODE=ref GOLDEN_CACHE=/workspace/aisw/vitis-ai-library-samples-res/input_bin/golden MODEL=facereid-large_pt MODEL_ZOO_ROOT=/workspace/aisw/debug_facereid-large_pt  DEBUG_COMPARE=1 python3 /workspace/aisw/Vitis-AI-Library/graph_runner/test/run_vaie.py /workspace/aisw/sw_jenkins_pipeline/config/xmodel_graph_edge.json
```

``` console
% xdputil xmodel -t a.txt ./usr/share/vitis_ai_library/models/facereid-large_pt/facereid-large_pt.xmodel
% xdputil xmodel -s a.svg ./usr/share/vitis_ai_library/models/facereid-large_pt/facereid-large_pt.xmodel
% xdputil xmodel -S s.svg ./usr/share/vitis_ai_library/models/facereid-large_pt/facereid-large_pt.xmodel
% xdputil xmodel -l ./usr/share/vitis_ai_library/models/facereid-large_pt/facereid-large_pt.xmodel
```

## on board test

```
% scp
```

``` console
% ssh b0
% cd /group/xbjlab/dphi_software/software/workspace/qiuyuny/sft_zcu102_bs/workspace/sw_zcu102_internal_test@13/vitis-ai-library/graph_runner/test
% env GOLDEN_CACHE=/group/xbjlab/dphi_software/software/workspace/qiuyuny/sft_zcu102_bs/workspace/sw_zcu102_internal_test@13/vitis-ai-library-samples-res/input_bin/golden MODEL=facereid-large_pt MODEL_ZOO_ROOT=/  DEBUG_COMPARE=1 python3 /home/wcy/graph_runner/test/run_graph.py /group/xbjlab/dphi_software/software/workspace/qiuyuny/sft_zcu102_bs/workspace/sw_zcu102_internal_test@13/config/xmodel_graph_edge.json

I0819 05:27:11.835904  4764 compare.cpp:152] dump tensor Resnet18__Resnet18_BatchNorm1d_bottleneck__411 on error. op: Resnet18__Resnet18_BatchNorm1d_bottleneck__411; type=batchnorm; actual_md5sum: d34f175ff1385c165d9f8384fce7827a expected_md5sum: 242fed80714d60be5731d3ee9cd0f202 filename=/tmp/root/error_result/0/Resnet18__Resnet18_BatchNorm1d_bottleneck__411.bin data=0xaaaac7ab5e70 size=1024
```

we found that `pool-fix` is the first op that is not correct.

## back on server


```
# output of vaie
[UNILOG][INFO] Dump Resnet18__Resnet18_BatchNorm1d_bottleneck__411 (shape={1, 256}, type=FLOAT32) into /tmp/chunywan/vaie.log/facereid-large_pt/ref/batch_0/Resnet18__Resnet18_BatchNorm1d_bottleneck__411.bin
[UNILOG][INFO] Dump Resnet18__Resnet18_input_fix (shape={1, 256}, type=XINT8) into /tmp/chunywan/vaie.log/facereid-large_pt/ref/batch_0/Resnet18__Resnet18_input_fix.bin
```

``` console
% mkdir -p /workspace/aisw/debug_facereid-large_pt
% cd /workspace/aisw/debug_facereid-large_pt
% mkdir -p out; mkdir -p ref
% cp /tmp/chunywan/vaie.log/facereid-large_pt/ref/batch_0/Resnet18__Resnet18_BatchNorm1d_bottleneck__411.bin ref/Resnet18__Resnet18_input_fix_Resnet18__Resnet18_BatchNorm1d_bottleneck__411.bin
% cp -av /tmp/chunywan/vaie.log/facereid-large_pt/ref/batch_0/Resnet18__Resnet18_input_fix.bin ref/Resnet18__Resnet18_input_fix_0.bin
% env XLNX_ENABLE_DUMP=1 USE_CPU_TASK=0 /home/chunywan/build/build.Ubuntu.18.04.x86_64.Debug/Vitis-AI-Library/graph_runner/test_graph_runner ./usr/share/vitis_ai_library/models/facereid-large_pt/facereid-large_pt.xmodel /home/chunywan/build/build.Ubuntu.18.04.x86_64.Debug/Vitis-AI-Library/graph_runner/test_graph_runner  -i 2
% d 0.Resnet18__Resnet18_BatchNorm1d_bottleneck__411.bin
% cp 0.Resnet18__Resnet18_BatchNorm1d_bottleneck__411.bin ref.bin

% XLNX_ENABLE_DUMP=1 USE_CPU_TASK=1 /home/chunywan/build/build.Ubuntu.18.04.x86_64.Debug/Vitis-AI-Library/graph_runner/test_graph_runner ./usr/share/vitis_ai_library/models/facereid-large_pt/facereid-large_pt.xmodel /home/chunywan/build/build.Ubuntu.18.04.x86_64.Debug/Vitis-AI-Library/graph_runner/test_graph_runner  -i 2
% d 0.Resnet18__Resnet18_BatchNorm1d_bottleneck__411.bin ref.bin
% 242fed80714d60be5731d3ee9cd0f202  0.Resnet18__Resnet18_BatchNorm1d_bottleneck__411.bin
% diff -u <(xxd out/efficientnet-edgetpu-L_model_head_global_average_pooling2d_Mean_mul_aquant.bin) <(xxd ./ref/efficientnet-edgetpu-L_model_head_global_average_pooling2d_Mean_mul_aquant.bin)
```

it is strange that on x86, the op is correct.

test is on zcu102


``` console
% ssh b0
% mkdir -p /workspace/aisw/debug_facereid-large_pt
% cd /workspace/aisw/debug_facereid-large_pt
% mkdir -p out; mkdir -p ref
% exit
% rsync -av ref b0:/workspace/aisw/debug_facereid-large_pt/
% rsync -av usr b0:/workspace/aisw/debug_facereid-large_pt/
% ssh b0
% mkdir -p /workspace/aisw/debug_facereid-large_pt
% cd /workspace/aisw/debug_facereid-large_pt
% env XLNX_ENABLE_DUMP=1 USE_CPU_TASK=1 /usr/share/vitis_ai_library/test/graph_runner/test_graph_runner ./usr/share/vitis_ai_library/models/facereid-large_pt/facereid-large_pt.xmodel /home/chunywan/build/build.Ubuntu.18.04.x86_64.Debug/Vitis-AI-Library/graph_runner/test_graph_runner  -i 2
% xxd 0.Resnet18__Resnet18_BatchNorm1d_bottleneck__411.bin
% md5sum 0.Resnet18__Resnet18_BatchNorm1d_bottleneck__411.bin
% cp 0.Resnet18__Resnet18_BatchNorm1d_bottleneck__411.bin ref.bin

% XLNX_ENABLE_DUMP=1 USE_CPU_TASK=1 /home/chunywan/build/build.Ubuntu.18.04.x86_64.Debug/Vitis-AI-Library/graph_runner/test_graph_runner ./usr/share/vitis_ai_library/models/facereid-large_pt/facereid-large_pt.xmodel /home/chunywan/build/build.Ubuntu.18.04.x86_64.Debug/Vitis-AI-Library/graph_runner/test_graph_runner  -i 2
% d 0.Resnet18__Resnet18_BatchNorm1d_bottleneck__411.bin ref.bin
% 242fed80714d60be5731d3ee9cd0f202  0.Resnet18__Resnet18_BatchNorm1d_bottleneck__411.bin
% diff -u <(xxd out/efficientnet-edgetpu-L_model_head_global_average_pooling2d_Mean_mul_aquant.bin) <(xxd ./ref/efficientnet-edgetpu-L_model_head_global_average_pooling2d_Mean_mul_aquant.bin)
```


## debug

``` console
% mkdir -p /workspace/aisw/debug_facereid-large_pt
% cd /workspace/aisw/debug_facereid-large_pt
% mkdir -p config
% mkdir -p log
% cp /workspace/aisw/vart/cpu-runner/config/config.txt config
% emacs -nw config/config.txt # change cpu_run_mode to 1
% cp ref/efficientnet-edgetpu-L_model_head_Relu_aquant.bin ref/efficientnet-edgetpu-L_model_head_Relu_aquant_0.bin
% env XLNX_ENABLE_DUMP=1 USE_CPU_TASK=0 gdb --args /home/chunywan/build/build.Ubuntu.18.04.x86_64.Debug/Vitis-AI-Library/graph_runner/test_graph_runner ./usr/share/vitis_ai_library/models/facereid-large_pt/facereid-large_pt.xmodel /home/chunywan/build/build.Ubuntu.18.04.x86_64.Debug/Vitis-AI-Library/graph_runner/test_graph_runner  -i 2
% ls -l
% d 0.efficientnet-edgetpu-L_model_head_global_average_pooling2d_Mean_mul_aquant.bin
% env XLNX_ENABLE_DUMP=1 USE_CPU_TASK=1 gdb --args /home/chunywan/build/build.Ubuntu.18.04.x86_64.Debug/Vitis-AI-Library/graph_runner/test_graph_runner ./usr/share/vitis_ai_library/models/facereid-large_pt/facereid-large_pt.xmodel /home/chunywan/build/build.Ubuntu.18.04.x86_64.Debug/Vitis-AI-Library/graph_runner/test_graph_runner  -i 2
% d 0.efficientnet-edgetpu-L_model_head_global_average_pooling2d_Mean_mul_aquant.bin
```
