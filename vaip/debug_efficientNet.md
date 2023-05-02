# debug `efficientNet-edgetpu-L_tf`


## get golden with vaie

``` console
% mkdir -p /workspace/aisw/debug_efficientNet-edgetpu-L_tf
% cd /workspace/aisw/debug_efficientNet-edgetpu-L_tf
% mkdir -p ./usr/share/vitis_ai_library/models
% scp -r xsjsda153:/proj/xsjhdstaff4/yanjunz/vitis-ai-staging/myws/test/debug_xmodel/models/efficientNet-edgetpu-L_tf ./usr/share/vitis_ai_library/models
% env MODE=ref GOLDEN_CACHE=/workspace/aisw/vitis-ai-library-samples-res/input_bin/golden MODEL=efficientNet-edgetpu-L_tf MODEL_ZOO_ROOT=/workspace/aisw/debug_efficientNet-edgetpu-L_tf  DEBUG_COMPARE=1 python3 /workspace/aisw/Vitis-AI-Library/graph_runner/test/run_vaie.py /workspace/aisw/sw_jenkins_pipeline/config/xmodel_graph_edge.json
```

``` console
% xdputil xmodel -t a.txt ./usr/share/vitis_ai_library/models/efficientNet-edgetpu-L_tf/efficientNet-edgetpu-L_tf.xmodel
% xdputil xmodel -s a.svg ./usr/share/vitis_ai_library/models/efficientNet-edgetpu-L_tf/efficientNet-edgetpu-L_tf.xmodel
% xdputil xmodel -S s.svg ./usr/share/vitis_ai_library/models/efficientNet-edgetpu-L_tf/efficientNet-edgetpu-L_tf.xmodel
```

## on board test

```
% scp
```

``` console
% ssh b0
% cd /group/xbjlab/dphi_software/software/workspace/qiuyuny/sft_zcu102_bs/workspace/sw_zcu102_internal_test@13/vitis-ai-library/graph_runner/test
% env GOLDEN_CACHE=/group/xbjlab/dphi_software/software/workspace/qiuyuny/sft_zcu102_bs/workspace/sw_zcu102_internal_test@13/vitis-ai-library-samples-res/input_bin/golden MODEL=efficientNet-edgetpu-L_tf MODEL_ZOO_ROOT=/  DEBUG_COMPARE=1 python3 run_graph.py /group/xbjlab/dphi_software/software/workspace/qiuyuny/sft_zcu102_bs/workspace/sw_zcu102_internal_test@13/config/xmodel_graph_edge.json
% env LD_LIBRARY_PATH=/home/root/wcy/ GOLDEN_CACHE=/group/xbjlab/dphi_software/software/workspace/qiuyuny/sft_zcu102_bs/workspace/sw_zcu102_internal_test@13/vitis-ai-library-samples-res/input_bin/golden MODEL=efficientNet-edgetpu-L_tf MODEL_ZOO_ROOT=/  DEBUG_COMPARE=1 python3 run_graph.py /group/xbjlab/dphi_software/software/workspace/qiuyuny/sft_zcu102_bs/workspace/sw_zcu102_internal_test@13/config/xmodel_graph_edge.json
```

we found that `pool-fix` is the first op that is not correct.

## back on server


```
# output of vaie
[UNILOG][INFO] Dump efficientnet-edgetpu-L/model/head/Relu/aquant (shape={1, 10, 10, 1536}, type=XINT8) into /tmp/chunywan/vaie.log/efficientNet-edgetpu-L_tf/ref/batch_0/efficientnet-edgetpu-L_model_head_Relu_aquant.bin
[UNILOG][INFO] Dump efficientnet-edgetpu-L/model/head/dense/BiasAdd/aquant (shape={1, 1001}, type=XINT8) into /tmp/chunywan/vaie.log/efficientNet-edgetpu-L_tf/ref/batch_0/efficientnet-edgetpu-L_model_head_dense_BiasAdd_aquant.bin
[UNILOG][INFO] Dump efficientnet-edgetpu-L/model/head/global_average_pooling2d/Mean/mul/aquant (shape={1, 1, 1, 1536}, type=XINT8) into /tmp/chunywan/vaie.log/efficientNet-edgetpu-L_tf/ref/batch_0/efficientnet-edgetpu-L_model_head_global_average_pooling2d_Mean_mul_aquant.bin
[UNILOG][INFO] Dump logits_fix_ (shape={1, 1001}, type=FLOAT32) into /tmp/chunywan/vaie.log/efficientNet-edgetpu-L_tf/ref/batch_0/logits_fix_.bin

```

``` console
% mkdir -p /workspace/aisw/debug_efficientNet-edgetpu-L_tf
% cd /workspace/aisw/debug_efficientNet-edgetpu-L_tf
% mkdir -p out; mkdir -p ref
% cp -av /tmp/chunywan/vaie.log/efficientNet-edgetpu-L_tf/ref/batch_0/efficientnet-edgetpu-L_model_head_Relu_aquant.bin ./ref/
% cp -av /tmp/chunywan/vaie.log/efficientNet-edgetpu-L_tf/ref/batch_0/efficientnet-edgetpu-L_model_head_global_average_pooling2d_Mean_mul_aquant.bin ./ref
% ~/.local/Ubuntu.18.04.x86_64.Debug/share/vitis_ai_library/test/cpu_task/test_op_imp -g ./usr/share/vitis_ai_library/models/efficientNet-edgetpu-L_tf/efficientNet-edgetpu-L_tf.xmodel --op 'efficientnet-edgetpu-L/model/head/global_average_pooling2d/Mean' -d out -r ref
% d  out/efficientnet-edgetpu-L_model_head_global_average_pooling2d_Mean_mul_aquant.bin ./ref/efficientnet-edgetpu-L_model_head_global_average_pooling2d_Mean_mul_aquant.bin
% diff -u <(xxd out/efficientnet-edgetpu-L_model_head_global_average_pooling2d_Mean_mul_aquant.bin) <(xxd ./ref/efficientnet-edgetpu-L_model_head_global_average_pooling2d_Mean_mul_aquant.bin)
```


## debug

``` console
% mkdir -p /workspace/aisw/debug_efficientNet-edgetpu-L_tf
% cd /workspace/aisw/debug_efficientNet-edgetpu-L_tf
% mkdir -p config
% mkdir -p log
% cp /workspace/aisw/vart/cpu-runner/config/config.txt config
% emacs -nw config/config.txt # change cpu_run_mode to 1
% cp ref/efficientnet-edgetpu-L_model_head_Relu_aquant.bin ref/efficientnet-edgetpu-L_model_head_Relu_aquant_0.bin
% env XLNX_ENABLE_DUMP=1 USE_CPU_TASK=0 gdb --args /home/chunywan/build/build.Ubuntu.18.04.x86_64.Debug/Vitis-AI-Library/graph_runner/test_graph_runner ./usr/share/vitis_ai_library/models/efficientNet-edgetpu-L_tf/efficientNet-edgetpu-L_tf.xmodel /home/chunywan/build/build.Ubuntu.18.04.x86_64.Debug/Vitis-AI-Library/graph_runner/test_graph_runner  -i 2
% ls -l
% d 0.efficientnet-edgetpu-L_model_head_global_average_pooling2d_Mean_mul_aquant.bin
% env XLNX_ENABLE_DUMP=1 USE_CPU_TASK=1 gdb --args /home/chunywan/build/build.Ubuntu.18.04.x86_64.Debug/Vitis-AI-Library/graph_runner/test_graph_runner ./usr/share/vitis_ai_library/models/efficientNet-edgetpu-L_tf/efficientNet-edgetpu-L_tf.xmodel /home/chunywan/build/build.Ubuntu.18.04.x86_64.Debug/Vitis-AI-Library/graph_runner/test_graph_runner  -i 2
% d 0.efficientnet-edgetpu-L_model_head_global_average_pooling2d_Mean_mul_aquant.bin
```
