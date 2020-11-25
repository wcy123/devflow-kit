# dev log for `graph_task` and `cpu_task`

## Keras-GoogleNet-ResNet

### develop dw-conv op


``` console
% ssh xcdl190253 md5sum  /group/modelzoo/Vitis-AI-Tutorials/Keras-GoogleNet-ResNet/files/quantized_results/cifar10/miniResNet/dump/dump_results_0/batch_normalization_1_FusedBatchNormV3_1_add_aquant.bin


4139c788d5d5881f258c65676897765e  /group/modelzoo/Vitis-AI-Tutorials/Keras-GoogleNet-ResNet/files/quantized_results/cifar10/miniResNet/dump/dump_results_0/batch_normalization_1_FusedBatchNormV3_1_add_aquant.bin

```

generate reference result by `vaie`

``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/debug_vaie
% /home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/bin/vaie-run -i /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/usr/share/vitis_ai_library/models/Keras-GoogleNet-ResNet-cifar10-miniResNet"/"Keras-GoogleNet-ResNet-cifar10-miniResNet.xmodel  --init 'conv2d_1_input/aquant /scratch/models/cache/golden/a8/572a5837ab4ee567818b2b11621a63' --deploy --release --disable-debug --dump 'batch_normalization_1/FusedBatchNormV3_1/add/aquant b1.bin' --target run
/scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/usr/share/vitis_ai_library/models/Keras-GoogleNet-ResNet-cifar10-miniResNet"/"Keras-GoogleNet-ResNet-cifar10-miniResNet.xmodel
% env XLNX_ENABLE_DUMP=1 /home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/bin/vaie-run -i /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/usr/share/vitis_ai_library/models/Keras-GoogleNet-ResNet-cifar10-miniResNet"/"Keras-GoogleNet-ResNet-cifar10-miniResNet.xmodel  --init 'conv2d_1_input/aquant /scratch/models/cache/golden/a8/572a5837ab4ee567818b2b11621a63' --deploy --release --disable-debug --dump 'batch_normalization_1/FusedBatchNormV3_1/add/aquant b1.bin' --target run

% d b1.bin

4139c788d5d5881f258c65676897765e  b1.bin
3072
0000000: ecdd dfe1 d1d3 dfd3 d8de d7e4 e4e7 faec  ................
0000010: f509 f301 18f6 031c fc09 1fff 0b1f f5fe  ................
0000020: 12f3 fb0e fd08 19fa 051a f600 16f1 fa10  ................
0000030: f600 16f3 0013 ecfa 0cf5 0618 f305 18f0  ................
0000040: 0013 f200 15f5 0118 fc0b 2002 1429 0717  .......... ..)..
0000050: 2b04 1326 0513 2407 1424 040f 2005 0e1d  +..&..$..$.. ...
0000060: d0bd bfc4 adb4 c4b3 c1c9 c3d9 d2d6 f3df  ................
0000070: ed09 e1f3 0fdf f00f e3f2 0edf ec06 dce4  ................
0000080: ffda e2fd dae4 ffda e705 d9e4 02dc e504  ................
0000090: dfec 09d9 e502 d5e4 ffe1 f30e e1f5 0fdd  ................
00000a0: f00b e2f3 12de ed0c dcec 0be2 f312 e6f5  ................
00000b0: 12e8 f613 e9f8 13e7 f20c e3ef 09e8 f20b  ................
00000c0: d2c0 c6c4 b3bf c9c3 d8d3 d4f0 dee5 02e6  ................
00000d0: f510 e7f6 10e2 ed0b dfea 05df ea04 e1ec  ................
00000e0: 04e1 e8ff dce7 ffe2 f50f e2f2 0ce7 f510  ................
00000f0: e7f3 0fe4 f00b dfec 06e2 f009 e6f8 10e7  ................


```


reference input is

``` console
% d  /scratch/models/cache/golden/a8/572a5837ab4ee567818b2b11621a63
```


test op implementation

``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/debug_vaie
% mkdir -p out
% mkdir -p ref
% ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/cpu_task/test_op_imp -g /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/Keras-GoogleNet-ResNet-cifar10-miniResNet/Keras-GoogleNet-ResNet-cifar10-miniResNet.xmodel --op 'batch_normalization_1/FusedBatchNormV3_1/offset/wquant_const_const' -d out -r ref
% d out/batch_normalization_1_FusedBatchNormV3_1_offset_wquant.bin
7094cafa619f5c7e02f38a92b07964b9  out/batch_normalization_1_FusedBatchNormV3_1_offset_wquant.bin
3
0000000: 4f44 3c                                  OD<

% ssh xcdl190253 md5sum  /group/modelzoo/Vitis-AI-Tutorials/Keras-GoogleNet-ResNet/files/quantized_results/cifar10/miniResNet/dump/dump_results_weights/batch_normalization_1_FusedBatchNormV3_1_offset_wquant.bin
7094cafa619f5c7e02f38a92b07964b9

% ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/cpu_task/test_op_imp -g /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/Keras-GoogleNet-ResNet-cifar10-miniResNet/Keras-GoogleNet-ResNet-cifar10-miniResNet.xmodel --op 'batch_normalization_1/FusedBatchNormV3_1/scale/wquant_const_const(transfered_depthwise_conv2d_weights)' -d out -r ref

% d out/batch_normalization_1_FusedBatchNormV3_1_scale_wquant_const_const_inserted_fix_0.bin
3689eb2944acbf765ee18b71122d6dba  out/batch_normalization_1_FusedBatchNormV3_1_scale_wquant_const_const_inserted_fix_0.bin
3
0000000: 5064 5b                                  Pd[

% ssh xcdl190253 md5sum /group/modelzoo/Vitis-AI-Tutorials/Keras-GoogleNet-ResNet/files/quantized_results/cifar10/miniResNet/dump/dump_results_weights/batch_normalization_1_FusedBatchNormV3_1_scale_wquant.bin

chunywan@xbjlabdpsvr16:debug_vaie% xxd -g3 ref/conv2d_1_input_aquant.bin | head
0000000: e0dfde d7d7d6 d6d8d9 d5dbe2 dae5f1 e0  ................
0000010: eefce6 f606e8 f709ed fb0bef fc0be7 f4  ................
0000020: 02e6f2 ffeefa 07ebf8 08e8f5 05e4f1 01  ................
0000030: e8f505 e6f503 e0f1fe e7f906 e6f806 e3  ................
0000040: f503e5 f504e7 f606ed fc0cf2 0212f6 04  ................
0000050: 14f301 10f401 0ff602 0ff3ff 0cf4fe 0a  ................
0000060: cacac8 c0c0c0 c0c4c9 c4ceda cbdaec d6  ................
0000070: e9fcd7 ed00d6 eb00d9 ecffd6 e8fad3 e3  ................
0000080: f5d2e2 f3d2e3 f5d2e5 f9d1e3 f7d3e4 f8  ................

% /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir dump_txt /tmp/a.xmodel a.txt
% vim a.txt
```

now `batch_normalization_1/FusedBatchNormV3_1/offset/wquant_const_const` is ok. copy it to ref

``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/debug_vaie
% cp /scratch/models/cache/golden/a8/572a5837ab4ee567818b2b11621a63 ref/conv2d_1_input_aquant.bin
% cp out/batch_normalization_1_FusedBatchNormV3_1_offset_wquant.bin ref
% cp out/batch_normalization_1_FusedBatchNormV3_1_scale_wquant_const_const_inserted_fix_0.bin ref
% ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/cpu_task/test_op_imp -g /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/Keras-GoogleNet-ResNet-cifar10-miniResNet/Keras-GoogleNet-ResNet-cifar10-miniResNet.xmodel --op 'batch_normalization_1/FusedBatchNormV3_1/mul(TransferMulToDepthwiseConv2d)(ReplaceDepthwiseConv2d)' -d out -r ref
% # verify that output is ok, compare with b1.bin
% d out/batch_normalization_1_FusedBatchNormV3_1_add_aquant.bin
4139c788d5d5881f258c65676897765e  out/batch_normalization_1_FusedBatchNormV3_1_add_aquant.bin
3072
0000000: ecdd dfe1 d1d3 dfd3 d8de d7e4 e4e7 faec  ................
% d b1.bin
```

## test the whole network

``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner MODEL="Keras-GoogleNet-ResNet-cifar10-miniResNet.xmodel"  DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
% # debug it if somethign wrong
% env PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner MODEL="Keras-GoogleNet-ResNet-cifar10-miniResNet.xmodel"  DEBUG_COMPARE=1  python3  run_graph.py vai-1.3.json
```

第二节网络结果不对

``` console
% # Keras-GoogleNet-ResNet-cifar10-miniResNet.xmodel"
% env XLNX_ENABLE_DUMP=1 ~/build/build.CentOS.7.6.1810.x86_64.Debug/vart/dpu-runner/test/test_dpu_runner /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/Keras-GoogleNet-ResNet-cifar10-miniResNet/Keras-GoogleNet-ResNet-cifar10-miniResNet.xmodel "subgraph_add_2/add(ReplaceEltwise)"
```


``` console
% cd /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/Keras-GoogleNet-ResNet-cifar10-miniResNet
% /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir dump_txt Keras-GoogleNet-ResNet-cifar10-miniResNet.xmodel Keras-GoogleNet-ResNet-cifar10-miniResNet.txt
% mkdir -p code
% mkdir -p code/subgraph_add_27
% mkdir -p code/subgraph_add_19
% mkdir -p code/subgraph_add_23
% /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir dump_bin Keras-GoogleNet-ResNet-cifar10-miniResNet.xmodel code

% mkdir -p ref; mkdir -p log; mkdir -p dump_cpu_runner

% cp /scratch/models/cache/golden/41/39c788d5d5881f258c65676897765e ref/batch_normalization_1_FusedBatchNormV3_1_add_aquant.bin
% env XLNX_ENABLE_DUMP=1 USE_CPU_TASK=1   ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/graph_task/test_graph_task Keras-GoogleNet-ResNet-cifar10-miniResNet.xmodel -i 2

# correct

% scp xcdl190253:/group/modelzoo/Vitis-AI-Tutorials/Keras-GoogleNet-ResNet/files/quantized_results/cifar10/miniResNet/dump/dump_results_0/activation_4_Relu_aquant.bin ref/activation_4_Relu_aquant.bin
% env XLNX_ENABLE_DUMP=1 USE_CPU_TASK=1   ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/graph_task/test_graph_task Keras-GoogleNet-ResNet-cifar10-miniResNet.xmodel -i 4
% env XLNX_ENABLE_DEBUG=1 XLNX_ENABLE_DUMP=1 USE_CPU_TASK=1   ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/graph_task/test_graph_task Keras-GoogleNet-ResNet-cifar10-miniResNet.xmodel -i 4


% scp xcdl190253:/group/modelzoo/Vitis-AI-Tutorials/Keras-GoogleNet-ResNet/files/quantized_results/cifar10/miniResNet/dump/dump_results_0/conv2d_1_input_aquant.bin .
% mkdir sim-log
% /home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/bin/vaie-run -i Keras-GoogleNet-ResNet-cifar10-miniResNet.xmodel --init 'conv2d_1_input/aquant conv2d_1_input_aquant.bin;' --dump 'dense_1/BiasAdd/aquant null/Keras-GoogleNet-ResNet-cifar10-miniResNet/dense_1_BiasAdd_aquant_dump_DPUCAHX8H_ISA2_ELP2_debug_sim.bin;' --target sim --log-path ./sim-log --deploy debug

% env MODE=sim XLNX_ENABLE_DEBUG=1 XLNX_ENABLE_DUMP=1 USE_CPU_TASK=1   ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/graph_task/test_graph_task Keras-GoogleNet-ResNet-cifar10-miniResNet.xmodel -i 4
% env MODE=run XLNX_ENABLE_DEBUG=1 XLNX_ENABLE_DUMP=1 USE_CPU_TASK=1   ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/graph_task/test_graph_task Keras-GoogleNet-ResNet-cifar10-miniResNet.xmodel -i 4
```


## run the whole test


``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK

```


## test "Keras-GoogleNet-ResNet-cifar10-miniVggNet"

``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env MODEL="ML-Caffe-Segmentation-Tutorial-enet.xmodel" LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```


## test "ML-Caffe-Segmentation-Tutorial-enet.xmodel"

```
libvart_op_imp_transposed-depthwise-conv2d-fix.so
```


``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/debug_vaie
% # find input

%
% /home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/bin/vaie-run -i /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/ML-Caffe-Segmentation-Tutorial-enet/ML-Caffe-Segmentation-Tutorial-enet.xmodel  --init 'data_fixed /scratch/models/cache/golden/fc/ab4f59c050a0be105da865547fa4af' --deploy --release --disable-debug --dump 'UpsamplingBilinear2d_1_fixed b1.bin' --target run
% # checkout b1.bin is correct or not
% scp xcdl190253:/group/modelzoo/Vitis-AI-Tutorials/ML-Caffe-Segmentation-Tutorial/Segment/VAI/enet/quantize/acc/dump_gpu/UpsamplingBilinear2d_1.bin .
% d b1.bin UpsamplingBilinear2d_1.bin  # 2f57e5c0cfd0b7f552df51f9edf208b7 OK. correct

% # prepare input
% scp xcdl190253:/group/modelzoo/Vitis-AI-Tutorials/ML-Caffe-Segmentation-Tutorial/Segment/VAI/enet/quantize/acc/dump_gpu/ConvNd_74.bin .
% cp ConvNd_74.bin ref/BatchNorm_72_fixed.bin
% # for weight
% ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/cpu_task/test_op_imp -g /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/ML-Caffe-Segmentation-Tutorial-enet/ML-Caffe-Segmentation-Tutorial-enet.xmodel --op 'UpsamplingBilinear2d_1_weights' -r ref -d out
% cp out/UpsamplingBilinear2d_1_weights_fixneuron.bin ref/
% # for bias
% ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/cpu_task/test_op_imp -g /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/ML-Caffe-Segmentation-Tutorial-enet/ML-Caffe-Segmentation-Tutorial-enet.xmodel --op 'UpsamplingBilinear2d_1_fake_bias(StandardizeConvlikeOp)' -r ref -d out
% cp out/UpsamplingBilinear2d_1_fake_bias_fix.bin ref
% # run it
% ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/cpu_task/test_op_imp -g /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/ML-Caffe-Segmentation-Tutorial-enet/ML-Caffe-Segmentation-Tutorial-enet.xmodel --op 'UpsamplingBilinear2d_1(ReplaceTransposedDepthwiseConv2d)' -r ref -d out
% gdb --args  ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/cpu_task/test_op_imp -g /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/ML-Caffe-Segmentation-Tutorial-enet/ML-Caffe-Segmentation-Tutorial-enet.xmodel --op 'UpsamplingBilinear2d_1(ReplaceTransposedDepthwiseConv2d)' -r ref -d out

% # show weight
% ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/cpu_task/show_binary_image  -f ref/UpsamplingBilinear2d_1_weights_fixneuron.bin --num_of_channels=64 -w 4 -h 4 -c 0

% # show output
% d out/UpsamplingBilinear2d_1_fixed.bin UpsamplingBilinear2d_1.bin
%
%
```

## `Keras-GoogleNet-ResNet-cifar10-miniVggNet`


``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env MODEL="Keras-GoogleNet-ResNet-cifar10-miniVggNet.xmodel" LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```

softmax md5sum is not correct, update the md5sum value.

run it again

## `Keras-GoogleNet-ResNet-fmnist-LeNet`


``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env MODEL="Keras-GoogleNet-ResNet-fmnist-LeNet.xmodel" LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```

softmax md5sum is not correct, update the md5sum value.

run it again

## `"Keras-GoogleNet-ResNet-fmnist-miniGoogleNet"`


``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env MODEL="Keras-GoogleNet-ResNet-fmnist-miniGoogleNet.xmodel" LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```


softmax md5sum is not correct, update the md5sum value.

run it again


## "Keras-GoogleNet-ResNet-fmnist-miniResNet"


``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env MODEL="Keras-GoogleNet-ResNet-fmnist-miniResNet.xmodel" LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```

similiar to the other mini resnet, the second subgraph is not correct.


## `"Keras-GoogleNet-ResNet-fmnist-miniVggNet"`


``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env MODEL=Keras-GoogleNet-ResNet-fmnist-miniVggNet.xmodel LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```


softmax md5sum is not correct, update the md5sum value.

run it again

## `ML-Caffe-Segmentation-Tutorial-FPN`



``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env MODEL=ML-Caffe-Segmentation-Tutorial-FPN.xmodel LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```

update golden hash.


## `ML-Caffe-Segmentation-Tutorial-espnet`



``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env MODEL=ML-Caffe-Segmentation-Tutorial-espnet.xmodel LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```

``` console
% cd  /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/ML-Caffe-Segmentation-Tutorial-espnet/
% /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir dump_txt ML-Caffe-Segmentation-Tutorial-espnet.xmodel ML-Caffe-Segmentation-Tutorial-espnet.txt
% /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir subgraph ML-Caffe-Segmentation-Tutorial-espnet.xmodel

% mkdir -p ref; mkdir -p log; mkdir -p dump_cpu_runner
% scp xcdl190253:/group/modelzoo/Vitis-AI-Tutorials/ML-Caffe-Segmentation-Tutorial/Segment/VAI/espnet/quantize/acc/dump_gpu/data.bin ref/data_fixed.bin
% env XLNX_ENABLE_DEBUG_MODE=1 XLNX_ENABLE_DUMP=1 USE_CPU_TASK=0  ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/graph_task/test_graph_task ML-Caffe-Segmentation-Tutorial-espnet.xmodel -i 1
```

1. `./dump/subgraph_ConvNd_1/output/0.BatchNorm_1_fixed_download_0.bin` and `ConvNd_1.bin` ,  `ff99643e67e017c45678eb6ff6a55c58`
2. `./dump/subgraph_AvgPool2d_1/input/0.data_fixed_upload_0.bin` and `data.bin` , `f54959bc00c38ff5444d8267e1de491f`
3. `./dump/subgraph_AvgPool2d_1/output/0.AvgPool2d_1_mul_fix.bin` `AvgPool2d_1.bin` fail

```
chunywan@xcdl190253:dump_gpu% pwd
/group/modelzoo/Vitis-AI-Tutorials/ML-Caffe-Segmentation-Tutorial/Segment/VAI/espnet/quantize/acc/dump_gpu
chunywan@xcdl190253:dump_gpu% d AvgPool2d_1.bin
bfafb9b830058a06ee3dccdcea082609  AvgPool2d_1.bin
98304
00000000: f1f4 f2f2 f5f3 f3f7 f4f6 fbf8 fafe fdfc  ................
00000010: 00ff f9fc f9f2 f3f2 eff0 f0f0 f1f1 f3f7  ................
00000020: f4fd 00ff 0609 0709 0a09 090d 0b08 0a07  ................
00000030: 0e0e 0d12 1512 0b11 0c09 0b08 0a0e 0b0c  ................
00000040: 0e0c 0f0f 0e10 1211 0e13 0f0b 0e0b 0e0f  ................
00000050: 0e0b 0e0d 0c0e 0c0e 110e 0f13 100b 0f0c  ................
00000060: 0c0e 0d0c 110e 0c10 0d0f 100d 1012 100c  ................
00000070: 110c 090c 0909 0c09 0407 0502 0503 fe00  ................
00000080: fffc fefd fbfe fefc ff00 fe01 0100 0505  ................
00000090: 0509 0800 0302 0002 0202 0707 0206 0603  ................
000000a0: 0808 0409 0a03 0808 0105 0400 0302 ff01  ................
000000b0: 0000 0302 0004 03f5 f7f6 f2f2 f2f4 f5f6  ................
000000c0: fafd fdf6 f7f7 f6f7 f8f8 fbfb f5f7 f8f2  ................
000000d0: f3f4 f1f1 f2f0 f1f1 f0ef f0f0 f0f1 f2f3  ................
000000e0: f4f8 fafa fbfe fef5 f6f7 f1f0 f1f2 f1f3  ................
000000f0: f6f6 f6f9 fbfc fe01 02fe 0102 f9fc fdf4  ................
```

```
545381ea8e94819dae880c2686e82cf8  ./dump/subgraph_AvgPool2d_1/output/0.AvgPool2d_1_mul_fix.bin
98304
0000000: f1f3 f2f2 f5f2 f3f7 f4f5 faf7 fafe fcfc  ................
0000010: 00fe f8fb f9f2 f3f1 efef efef f1f0 f2f6  ................
0000020: f4fc 01fe 0609 070a 0b0a 090e 0b09 0b08  ................
0000030: 0e0e 0d12 1512 0b11 0d09 0b08 0b0e 0b0c  ................
0000040: 0f0c 0f10 0e11 1311 0e14 0f0c 0e0c 0e10  ................
0000050: 0e0c 0f0d 0d0f 0d0f 110f 1013 100b 0f0c  ................
0000060: 0d0f 0d0c 110e 0d10 0d10 110e 1013 110c  ................
0000070: 110d 0a0c 0a0a 0d09 0407 0503 0504 fe01  ................
0000080: fffb fdfc fbfd fefc ffff fe01 0201 0505  ................
0000090: 050a 0901 0302 ff02 0303 0707 0207 0603  ................
00000a0: 0909 040a 0a04 0808 0205 0500 0302 ff01  ................
00000b0: 0100 0303 0005 03f5 f6f5 f1f1 f2f4 f5f5  ................
00000c0: fafd fdf6 f6f7 f6f6 f7f7 fafb f4f7 f7f1  ................
00000d0: f3f3 f0f1 f1f0 f0f1 efef f0f0 eff1 f2f3  ................
00000e0: f4f8 fafa fbfd fef4 f5f6 f0ef f1f2 f0f2  ................
00000f0: f6f6 f6f9 fbfc fe01 02fe 0203 f9fb fcf3  ................

```


``` console
% ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/cpu_task/show_binary_image -f ref/data_fixed.bin -w 256 -h 512 --num_of_channels 3 -c 0 >data_fix.txt
% ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/cpu_task/show_binary_image -f ./dump/subgraph_AvgPool2d_1/output/0.AvgPool2d_1_mul_fix.bin -w 128 -h 256 --num_of_channels 3 -c 0 >pool.dpu.txt
```
skipped.

## `ML-Caffe-Segmentation-Tutorial-unet-full`



``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env MODEL=ML-Caffe-Segmentation-Tutorial-unet-full.xmodel LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```

first subgraph is OK. golden is updated.

first cpu graph failed.

```console
chunywan@xbjlabdpsvr16:test% d /tmp/error_result/0/relu_d0c_fix.bin
f081e8b3dd2d27845368b67753a40d99  /tmp/error_result/0/relu_d0c_fix.bin
33554432
0000000: 0000 0705 0001 0002 0000 0307 0006 0c00  ................
0000010: 0c1b 0004 0000 0019 0300 0900 0e00 0400  ................
0000020: 0007 0607 0006 0007 000c 1005 0000 0000  ................
0000030: 0000 0900 010c 0815 0401 0b01 0000 0000  ................
0000040: 0000 0008 1200 0000 0500 0a01 000c 0e0a  ................
0000050: 1115 0000 0000 0018 0500 0600 0001 0900  ................
0000060: 0003 000b 000a 0005 0006 030f 0000 0000  ................
0000070: 0200 1700 0508 0003 0800 1201 0000 0009  ................
0000080: 0000 0006 1100 0002 0400 0c04 0007 1300  ................
0000090: 1209 0000 0000 001d 0400 0500 0000 0800  ................
00000a0: 0007 0006 0010 0003 0006 0308 0000 0000  ................
00000b0: 0000 1300 030c 0009 0800 0b08 0000 0009  ................
00000c0: 0000 0007 1500 0004 0400 0c04 0008 1100  ................
00000d0: 1a09 0000 0000 001d 0a00 0400 0005 0a00  ................
00000e0: 0005 0000 0010 0000 0001 0111 0001 0000  ................
00000f0: 0000 1302 0010 000f 0900 1004 0000 000c  ................

chunywan@xcdl190253:dump_gpu% pwd
/group/modelzoo/Vitis-AI-Tutorials/ML-Caffe-Segmentation-Tutorial/Segment/VAI/unet-full/quantize/acc/dump_gpu
chunywan@xcdl190253:dump_gpu% d relu_d0c.bin
1f81a416ece7ec05d93857b610d4e1d3  relu_d0c.bin
33554432
00000000: 0000 0605 0001 0001 0000 0206 0005 0b00  ................
00000010: 0b1b 0003 0000 0019 0200 0800 0e00 0400  ................
00000020: 0006 0507 0005 0007 000b 0f05 0000 0000  ................
00000030: 0000 0900 000b 0714 0401 0a01 0000 0000  ................
00000040: 0000 0007 1200 0000 0400 0a01 000c 0d09  ................
00000050: 1015 0000 0000 0017 0500 0600 0001 0800  ................
00000060: 0002 000b 0009 0005 0005 030e 0000 0000  ................
00000070: 0100 1600 0407 0003 0700 1101 0000 0008  ................
00000080: 0000 0005 1100 0001 0300 0b03 0006 1200  ................
00000090: 1208 0000 0000 001d 0400 0500 0000 0700  ................
000000a0: 0006 0005 0010 0002 0005 0307 0000 0000  ................
000000b0: 0000 1200 020b 0008 0700 0a08 0000 0008  ................
000000c0: 0000 0006 1400 0003 0300 0b03 0007 1000  ................
000000d0: 1908 0000 0000 001d 0a00 0400 0004 0900  ................
000000e0: 0004 0000 0010 0000 0001 0011 0000 0000  ................
000000f0: 0000 1202 000f 000e 0900 1004 0000 000b  ................

```

use vaie to run

``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/debug_vaie
% # check input
% env DEBUG_DPU_RUNNER=1 XLNX_ENABLE_DEVICES=0,1 /home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/bin/vaie-run -i /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/usr/share/vitis_ai_library/models/ML-Caffe-Segmentation-Tutorial-unet-full/ML-Caffe-Segmentation-Tutorial-unet-full.xmodel  --init 'data_fixed /scratch/models/cache/golden/fc/ab4f59c050a0be105da865547fa4af' --deploy --release --disable-debug --dump 'd0c_fixed input.bin;BatchNorm_d0c/fix/scale weight.bin;BatchNorm_d0c_bias_fixneuron bias.bin;relu_d0c_fix output.bin' --target run
% d input.bin
```

there is a bug in the xmodel

debug with `xlnx_test_dpu_runner`

```console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/debug_vaie
% env XLNX_ENABLE_DEVICES=0 DEBUG_DPU_RUNNER=1 XLNX_ENABLE_DUMP=1  ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/usefultools/xilinx_test_dpu_runner /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/usr/share/vitis_ai_library/models/ML-Caffe-Segmentation-Tutorial-unet-full/ML-Caffe-Segmentation-Tutorial-unet-full.xmodel -i 0  dump/subgraph_conv_d0a_b/input/0.data_fixed.bin
```

update `test_graph_task.cpp` to support debugging and calibration

``` console
% env USE_CPU_TASK=0  ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/graph_task/test_graph_task /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/usr/share/vitis_ai_library/models/ML-Caffe-Segmentation-Tutorial-unet-full/ML-Caffe-Segmentation-Tutorial-unet-full.xmodel -i 2
% chunywan@xbjlabdpsvr16:debug_vaie% d 0.relu_d0c_fix.bin
f081e8b3dd2d27845368b67753a40d99  0.relu_d0c_fix.bin
33554432
0000000: 0000 0705 0001 0002 0000 0307 0006 0c00  ................
0000010: 0c1b 0004 0000 0019 0300 0900 0e00 0400  ................
0000020: 0007 0607 0006 0007 000c 1005 0000 0000  ................
0000030: 0000 0900 010c 0815 0401 0b01 0000 0000  ................
0000040: 0000 0008 1200 0000 0500 0a01 000c 0e0a  ................
0000050: 1115 0000 0000 0018 0500 0600 0001 0900  ................
0000060: 0003 000b 000a 0005 0006 030f 0000 0000  ................
0000070: 0200 1700 0508 0003 0800 1201 0000 0009  ................
0000080: 0000 0006 1100 0002 0400 0c04 0007 1300  ................
0000090: 1209 0000 0000 001d 0400 0500 0000 0800  ................
00000a0: 0007 0006 0010 0003 0006 0308 0000 0000  ................
00000b0: 0000 1300 030c 0009 0800 0b08 0000 0009  ................
00000c0: 0000 0007 1500 0004 0400 0c04 0008 1100  ................
00000d0: 1a09 0000 0000 001d 0a00 0400 0005 0a00  ................
00000e0: 0005 0000 0010 0000 0001 0111 0001 0000  ................
00000f0: 0000 1302 0010 000f 0900 1004 0000 000c  ................
```

it is as same as the `cpu_task` implementation, the golden result has something wrong.


## `"ML-Caffe-Segmentation-Tutorial-unet-lite"`


``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env MODEL=ML-Caffe-Segmentation-Tutorial-unet-lite.xmodel LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```

the first subgraph is not correct

``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/debug_vaie
% cp /scratch/models/cache/golden/f5/4959bc00c38ff5444d8267e1de491f ref/data_fixed.bin
% env  USE_CPU_TASK=1  ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/graph_task/test_graph_task /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/usr/share/vitis_ai_library/models/ML-Caffe-Segmentation-Tutorial-unet-lite/ML-Caffe-Segmentation-Tutorial-unet-lite.xmodel -i 1
```

## `ML-at-Edge-yolov3`

``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env MODEL=ML-at-Edge-yolov3.xmodel LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```

pass

## `MLPerf_resnet50_v1.5_tf`


``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env MODEL=MLPerf_resnet50_v1.5_tf.xmodel LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```

3 outputs have same md5sum.


``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/debug_vaie
% cp /scratch/models/cache/golden/4c/64ee8d0de09dcf71c9d97072428021 ref/input_tensor_aquant.bin
% env  USE_CPU_TASK=1  ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/graph_task/test_graph_task /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/usr/share/vitis_ai_library/models/MLPerf_resnet50_v1.5_tf/MLPerf_resnet50_v1.5_tf.xmodel -i 1
% cp 0.resnet_model_dense_BiasAdd_aquant.bin ref/resnet_model_dense_BiasAdd_aquant.bin
% env  USE_CPU_TASK=1  ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/graph_task/test_graph_task /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/usr/share/vitis_ai_library/models/MLPerf_resnet50_v1.5_tf/MLPerf_resnet50_v1.5_tf.xmodel -i 2
```

after troubleshooting, I learned that it was because `fix` op is not properly implemented.


## `MNIST-Classification-TensorFlow`

``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env MODEL=MNIST-Classification-TensorFlow.xmodel LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```

pass

## `MT-resnet18_mixed_pt`

``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env MODEL=MT-resnet18_mixed_pt.xmodel LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK

```

error

```
MTNet__MTNet_708_fix(ReplaceResize) on error. actual_md5sum: de883235c87930ed1f99f2a254ef6973 expected_md5sum: f78912c33edb2ce2e3e552ebdcfff081 f
ilename=/tmp/chunywan/error_result/0/MTNet__MTNet_708_fix.bin data=0xa233ea0 size=163840
```

``` console
% /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir subgraph /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/MT-resnet18_mixed_pt/MT-resnet18_mixed_pt.xmodel
```


``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% rm -fr dump
% env  MODEL=MT-resnet18_mixed_pt.xmodel LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=1 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
% d dump/subgraph_MTNet__MTNet_Conv2d_input_2/output/0.MTNet__MTNet_Sequential_toplayer3__Conv2d_toplayer3_conv__input_56_fix.bin
% mkdir ref
% cp dump/subgraph_MTNet__MTNet_Conv2d_input_2/output/0.MTNet__MTNet_Sequential_toplayer3__Conv2d_toplayer3_conv__input_56_fix.bin ref/MTNet__MTNet_Sequential_toplayer3__Conv2d_toplayer3_conv__input_56_fix.bin
% mkdir log
% env USE_CPU_TASK=0   ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/graph_task/test_graph_task /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/MT-resnet18_mixed_pt/MT-resnet18_mixed_pt.xmodel -i 2
% d 0.MTNet__MTNet_708_fix.bin
% env USE_CPU_TASK=1   ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/graph_task/test_graph_task /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/MT-resnet18_mixed_pt/MT-resnet18_mixed_pt.xmodel -i 2
% d 0.MTNet__MTNet_708_fix.bin
% /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir dump_txt /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/MT-resnet18_mixed_pt/MT-resnet18_mixed_pt.xmodel a.txt
```

fix a bug in `upsample-fix.cpp`

``` console
% find dump/subgraph_MTNet__MTNet_Sequential_toplayer2__Conv2d_toplayer2_conv__input_59
% d dump/subgraph_MTNet__MTNet_Sequential_toplayer2__Conv2d_toplayer2_conv__input_59/input/0.MTNet__MTNet_Sequential_BasicBlock_1__ReLU_relu__input_42_fix.bin
% # 51252194dc99bc78e5b99b793a382415 OK
% d dump/subgraph_MTNet__MTNet_Sequential_toplayer2__Conv2d_toplayer2_conv__input_59/input/0.MTNet__MTNet_708_fix.bin
% # f78912c33edb2ce2e3e552ebdcfff081 OK
% cp dump/subgraph_MTNet__MTNet_Sequential_toplayer2__Conv2d_toplayer2_conv__input_59/input/0.MTNet__MTNet_Sequential_BasicBlock_1__ReLU_relu__input_42_fix.bin ref/MTNet__MTNet_Sequential_BasicBlock_1__ReLU_relu__input_42_fix.bin
% cp dump/subgraph_MTNet__MTNet_Sequential_toplayer2__Conv2d_toplayer2_conv__input_59/input/0.MTNet__MTNet_708_fix.bin ref/MTNet__MTNet_708_fix.bin
% env XLNX_ENABLE_DUMP=1 USE_CPU_TASK=0   ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/graph_task/test_graph_task /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/MT-resnet18_mixed_pt/MT-resnet18_mixed_pt.xmodel -i 3
% d ./dump/subgraph_MTNet__MTNet_Sequential_toplayer2__Conv2d_toplayer2_conv__input_59/output/0.MTNet__MTNet_Sequential_toplayer2__Conv2d_toplayer2_conv__input_59_fix.bin
% # a728e81d72ef627fdbfe628c70d84bfb, FAIL, not "823adff472a346e900aeb28cebef617b"
```

## `RefineDet-Medical_EDD_tf`

``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env MODEL=RefineDet-Medical_EDD_tf.xmodel LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK

```

## `Resnet50_v1.5_pruned_74`

``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env MODEL=Resnet50_v1.5_pruned_74.xmodel LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```

## `SemanticFPN_cityscapes_pt`

``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env MODEL=SemanticFPN_cityscapes_pt.xmodel LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```

## `VAI-Caffe-ML-CATSvsDOGS`

``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env MODEL=VAI-Caffe-ML-CATSvsDOGS.xmodel LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```

## `VAI-Caffe-ML-CATSvsDOGS-pruned`

``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env MODEL=VAI-Caffe-ML-CATSvsDOGS-pruned.xmodel LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```

## `VAI-Caffe-SSD-Tutorial-Mobilenetv2-SSD`

``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env MODEL=VAI-Caffe-SSD-Tutorial-Mobilenetv2-SSD.xmodel LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```

```
F1119 09:31:39.637473  3351 op_imp.cpp:91] Check failed: handle != NULL cannot open library! lib=libvart_op_imp_priorbox.so;error=libva
```

``` console
% /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir dump_txt /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/VAI-Caffe-SSD-Tutorial-Mobilenetv2-SSD/VAI-Caffe-SSD-Tutorial-Mobilenetv2-SSD.xmodel /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/VAI-Caffe-SSD-Tutorial-Mobilenetv2-SSD/VAI-Caffe-SSD-Tutorial-Mobilenetv2-SSD.txt
```

``` console
% mkdir -p /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/cp
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/cp
% git clone gits@xcdl190260:cp/caffe
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/cp/caffe
% git status
% SRC_DIR=$PWD
% cp Makefile.config.example Makefile.config
% make -j30 -k
```

<!-- % bash $SRC_DIR/tools/gen_git_version.sh $SRC_DIR/src/caffe/pruning/version.cpp # Need a version -->
<!-- % cat $SRC_DIR/src/caffe/pruning/version.cpp -->
<!-- % PREFIX=$HOME/.local/CentOS.7.6.1810.x86_64.Debug -->
<!-- % BUILD_DIR=$HOME/build/build.CentOS.7.6.1810.x86_64.Debug/caffe -->
<!-- % BUILD_PREFIX=$PREFIX -->
<!-- % sudo yum install -y hdf5-devel yaml-cpp-devel openblas-devel leveldb-devel lmdb-devel -->
<!-- % mkdir -p $BUILD_DIR -->
<!-- % cd $BUILD_DIR; pwd -->
<!-- % source /opt/rh/devtoolset-9/enable -->
<!-- % cmake -DUSE_CUDNN=0 -DUSE_NCCL=0 -DOPENCV_VERSION=3 -DCMAKE_CXX_STANDARD=11 -DCMAKE_LIBRARY_PATH=${BUILD_PREFIX}/lib  -DCMAKE_INCLUDE_PATH=${BUILD_PREFIX}/include -DCMAKE_PREFIX_PATH=$BUILD_PREFIX -DCPU_ONLY=1 -DBLAS="open" -DCMAKE_INSTALL_PREFIX="${PREFIX}" -DCMAKE_INSTALL_LIBDIR=lib -Dpython_version=$PY_VER -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON -DCRYPTO_KEY=deephi-tech -DDPU_ACCURACY=1 $SRC_DIR -->

see `caffe.makefile.config`


``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/debug_vaie
% cd /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/VAI-Caffe-SSD-Tutorial-Mobilenetv2-SSD/
% rsync -avz xcdl190253:/group/modelzoo/Vitis-AI-Tutorials/VAI-Caffe-SSD-Tutorial/SSD/VAI/Mobilenetv2-SSD .
% cd /var/lib/docker/scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/usr/share/vitis_ai_library/models/VAI-Caffe-SSD-Tutorial-Mobilenetv2-SSD/Mobilenetv2-SSD/quantize/acc
% env DECENT_DEBUG=5 /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/cp/caffe/build/tools/vai_q test -model dump.prototxt -weights ../quantize_train_test.caffemodel -test_iter=1
```


``` gdb-session
"min_size: 15\nmin_size: 30\nmax_size: 33\nmax_size: 66\naspect_ratio: 2\nflip: true\nclip: false\nvariance: 0.1\nvariance: 0.1\nvariance: 0.2\nvariance: 0.2\nstep: 8\noffset: 0.5\n"
p layer_param_.name()

"conv4_3_norm_mbox_priorbox"

(gdb) p layer_width
$7 = 60
(gdb) p layer_height
$8 = 45
(gdb) p layer_width
$7 = 60
(gdb) p layer_height
$8 = 45
(gdb) p step_w
$12 = 8
(gdb) p step_h
$13 = 8
141       int dim = layer_height * layer_width * num_priors_ * 4;
(gdb) p dim
$14 = 86400
(gdb) p num_priors_
$15 = 8
(gdb) p offset_
$16 = 0.5
```

 debug the `op_imp`

``` console
% cd /var/lib/docker/scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/usr/share/vitis_ai_library/models/VAI-Caffe-SSD-Tutorial-Mobilenetv2-SSD/Mobilenetv2-SSD/quantize/acc
% mkdir debug_graph_task
% cd debug_graph_task
% mkdir ref
% ls -l ../dump_gpu/ | grep 'conv4_7.*expan'
% /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir subgraph /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/VAI-Caffe-SSD-Tutorial-Mobilenetv2-SSD/VAI-Caffe-SSD-Tutorial-Mobilenetv2-SSD.xmodel | grep conv4_3
% cp ../dump_gpu/conv4_7_expand.bin ref/conv4_7_expand_bn_fixed.bin
% cp ../dump_gpu/data.bin ref/data_fixed.bin
% env XLNX_ENABLE_DUMP=1 USE_CPU_TASK=1   ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/graph_task/test_graph_task /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/VAI-Caffe-SSD-Tutorial-Mobilenetv2-SSD/VAI-Caffe-SSD-Tutorial-Mobilenetv2-SSD.xmodel -i 22
```

## `VAI-KERAS-FCN8-SEMSEG-fcn8`

``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env MODEL=VAI-KERAS-FCN8-SEMSEG-fcn8.xmodel LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```


``` console
% cd /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/VAI-KERAS-FCN8-SEMSEG-fcn8/
% /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir dump_txt  VAI-KERAS-FCN8-SEMSEG-fcn8.xmodel VAI-KERAS-FCN8-SEMSEG-fcn8.txt
```

calibrate with VAIE

``` console
% /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir subgraph /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/VAI-KERAS-FCN8-SEMSEG-fcn8/VAI-KERAS-FCN8-SEMSEG-fcn8.xmodel
```

``` console
% cd /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/VAI-KERAS-FCN8-SEMSEG-fcn8/
% mkdir ref
% cp /scratch/models/cache/golden/bb/0132cd6a8f08429db9411256c7a74d ref/conv2d_transpose_3_conv2d_transpose_aquant.bin
% env XLNX_ENABLE_DUMP=1 USE_CPU_TASK=1   ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/graph_task/test_graph_task /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/VAI-KERAS-FCN8-SEMSEG-fcn8/VAI-KERAS-FCN8-SEMSEG-fcn8.xmodel -i 2
% mv 0.activation_1_truediv.bin 0.activation_1_truediv.bin.cputask
% env XLNX_ENABLE_DUMP=1 USE_CPU_TASK=0   ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/graph_task/test_graph_task /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/VAI-KERAS-FCN8-SEMSEG-fcn8/VAI-KERAS-FCN8-SEMSEG-fcn8.xmodel -i 2
% mv 0.activation_1_truediv.bin 0.activation_1_truediv.bin.vaie
% d 0.activation_1_truediv.bin.vaie 0.activation_1_truediv.bin.cputask
% d 0.activation_1_truediv.bin 0.activation_1_truediv.bin.vaie
```

## `VAI-KERAS-FCN8-SEMSEG-fcn8ups`


``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env MODEL=VAI-KERAS-FCN8-SEMSEG-fcn8ups.xmodel LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```

``` console

% cd /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/VAI-KERAS-FCN8-SEMSEG-fcn8ups
%  /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir dump_txt VAI-KERAS-FCN8-SEMSEG-fcn8ups.xmodel VAI-KERAS-FCN8-SEMSEG-fcn8ups.txt

% /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir subgraph  /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/VAI-KERAS-FCN8-SEMSEG-fcn8ups/VAI-KERAS-FCN8-SEMSEG-fcn8ups.xmodel

% # open  /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/VAI-KERAS-FCN8-SEMSEG-fcn8ups/VAI-KERAS-FCN8-SEMSEG-fcn8ups.txt

% mkdir -p ref; mkdir -p log; mkdir -p dump_cpu_runner

% cp /scratch/models/cache/golden/47/a28e223f0d07911b218b4cf63f5e05 ref/pool411_b_Relu_aquant.bin
% ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/cpu_task/show_binary_image -f ref/pool411_b_Relu_aquant.bin -w 14 -h 14 --num_of_channels 12 -c 1

% env XLNX_ENABLE_DUMP=1 USE_CPU_TASK=0   ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/graph_task/test_graph_task /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/VAI-KERAS-FCN8-SEMSEG-fcn8ups/VAI-KERAS-FCN8-SEMSEG-fcn8ups.xmodel -i 2

% ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/cpu_task/show_binary_image -f log/up_sampling2d_2_ResizeBilinear_aquant.bin -w 28 -h 28 --num_of_channels 12 -c 1

% env XLNX_ENABLE_DUMP=1 USE_CPU_TASK=1   ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/graph_task/test_graph_task /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/VAI-KERAS-FCN8-SEMSEG-fcn8ups/VAI-KERAS-FCN8-SEMSEG-fcn8ups.xmodel -i 2

% ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/cpu_task/show_binary_image -f dump/subgraph_up_sampling2d_2_2f_ResizeBilinear_28_ReplaceResize_29_/up_sampling2d_2_2f_ResizeBilinear_2f_aquant_28_ReplaceResize_29__0.bin -w 28 -h 28 --num_of_channels 12 -c 1

% d dump/subgraph_up_sampling2d_2_2f_ResizeBilinear_28_ReplaceResize_29_/up_sampling2d_2_2f_ResizeBilinear_2f_aquant_28_ReplaceResize_29__0.bin log/up_sampling2d_2_ResizeBilinear_aquant.bin
```

## `VAI-KERAS-FCN8-SEMSEG-unet1`


``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env MODEL=VAI-KERAS-FCN8-SEMSEG-unet1.xmodel LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```


``` console

% cd /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/VAI-KERAS-FCN8-SEMSEG-unet1
%  /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir dump_txt VAI-KERAS-FCN8-SEMSEG-unet1.xmodel VAI-KERAS-FCN8-SEMSEG-unet1.txt

% /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir subgraph  /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/VAI-KERAS-FCN8-SEMSEG-unet1/VAI-KERAS-FCN8-SEMSEG-unet1.xmodel

% # open  /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/VAI-KERAS-FCN8-SEMSEG-unet1/VAI-KERAS-FCN8-SEMSEG-unet1.txt

% mkdir -p ref; mkdir -p log; mkdir -p dump_cpu_runner

% cp /scratch/models/cache/golden/23/65423b17a6a2a2e1d30d3eed2573ee ref/activation_10_Relu_aquant.bin
% ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/cpu_task/show_binary_image -f ref/pool411_b_Relu_aquant.bin -w 14 -h 14 --num_of_channels 12 -c 1

% env XLNX_ENABLE_DUMP=1 USE_CPU_TASK=0   ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/graph_task/test_graph_task /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/VAI-KERAS-FCN8-SEMSEG-unet1/VAI-KERAS-FCN8-SEMSEG-unet1.xmodel -i 2

% mv 0.up_sampling2d_1_ResizeBilinear_aquant.bin 0.up_sampling2d_1_ResizeBilinear_aquant.bin.vaie
% ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/cpu_task/show_binary_image -f log/up_sampling2d_2_ResizeBilinear_aquant.bin -w 28 -h 28 --num_of_channels 12 -c 1

% env XLNX_ENABLE_DUMP=1 USE_CPU_TASK=1   ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/graph_task/test_graph_task /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/VAI-KERAS-FCN8-SEMSEG-unet1/VAI-KERAS-FCN8-SEMSEG-unet1.xmodel -i 2

% ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/cpu_task/show_binary_image -f dump/subgraph_up_sampling2d_2_2f_ResizeBilinear_28_ReplaceResize_29_/up_sampling2d_2_2f_ResizeBilinear_2f_aquant_28_ReplaceResize_29__0.bin -w 28 -h 28 --num_of_channels 12 -c 1

% d 0.up_sampling2d_1_ResizeBilinear_aquant.bin 0.up_sampling2d_1_ResizeBilinear_aquant.bin.vaie
```

## `VAI-KERAS-FCN8-SEMSEG-unet2`


``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env MODEL=VAI-KERAS-FCN8-SEMSEG-unet2.xmodel LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```


``` console

% cd /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/VAI-KERAS-FCN8-SEMSEG-unet2
%  /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir dump_txt VAI-KERAS-FCN8-SEMSEG-unet2.xmodel VAI-KERAS-FCN8-SEMSEG-unet2.txt

% /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir subgraph  /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/VAI-KERAS-FCN8-SEMSEG-unet2/VAI-KERAS-FCN8-SEMSEG-unet2.xmodel

% # open  /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/VAI-KERAS-FCN8-SEMSEG-unet2/VAI-KERAS-FCN8-SEMSEG-unet2.txt

% mkdir -p ref; mkdir -p log; mkdir -p dump_cpu_runner

% cp /scratch/models/cache/golden/ed/61787b7bae7b1b72b88d61014a5d3f ref/activation_10_Relu_aquant.bin
% ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/cpu_task/show_binary_image -f ref/pool411_b_Relu_aquant.bin -w 14 -h 14 --num_of_channels 12 -c 1

% env XLNX_ENABLE_DUMP=1 USE_CPU_TASK=0   ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/graph_task/test_graph_task /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/VAI-KERAS-FCN8-SEMSEG-unet2/VAI-KERAS-FCN8-SEMSEG-unet2.xmodel -i 2

% mv 0.up_sampling2d_1_ResizeBilinear_aquant.bin 0.up_sampling2d_1_ResizeBilinear_aquant.bin.vaie
% ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/cpu_task/show_binary_image -f log/up_sampling2d_2_ResizeBilinear_aquant.bin -w 28 -h 28 --num_of_channels 12 -c 1

% env XLNX_ENABLE_DUMP=1 USE_CPU_TASK=1   ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/graph_task/test_graph_task /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/VAI-KERAS-FCN8-SEMSEG-unet2/VAI-KERAS-FCN8-SEMSEG-unet2.xmodel -i 2

% ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/cpu_task/show_binary_image -f dump/subgraph_up_sampling2d_2_2f_ResizeBilinear_28_ReplaceResize_29_/up_sampling2d_2_2f_ResizeBilinear_2f_aquant_28_ReplaceResize_29__0.bin -w 28 -h 28 --num_of_channels 12 -c 1

% d 0.up_sampling2d_1_ResizeBilinear_aquant.bin 0.up_sampling2d_1_ResizeBilinear_aquant.bin.vaie
```

## `VAI-KERAS-FCN8-SEMSEG-unet2`


``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env MODEL=VAI-KERAS-FCN8-SEMSEG-unet2.xmodel LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```

## `densebox_320_320`


``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env MODEL=densebox_320_320.xmodel LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```


``` console
ssh xcdl190253 md5sum /group/modelzoo/internal-cooperation-models/caffe/densebox_320_320/fix/acc/decrypted/../dump_gpu/pixel-tile.bin
ssh xcdl190253 md5sum /group/modelzoo/internal-cooperation-models/caffe/densebox_320_320/fix/acc/decrypted/../dump_gpu/bb-tile.bin
```


## `densebox_640_360`


``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env MODEL=densebox_640_360.xmodel LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```


``` console
ssh xcdl190253 md5sum /group/modelzoo/internal-cooperation-models/caffe/densebox_640_360/fix/acc/decrypted/../dump_gpu/pixel-tile.bin
ssh xcdl190253 md5sum /group/modelzoo/internal-cooperation-models/caffe/densebox_640_360/fix/acc/decrypted/../dump_gpu/bb-tile.bin
```




``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env MODEL=resnet50_tf2.xmodel LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```

``` console
% cd /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/resnet50_tf2/

% mkdir -p ref; mkdir -p log; mkdir -p dump_cpu_runner

% cp /scratch/models/cache/golden/1a/d6c0d31760238b2ddad9898478d9d3 ref
% cp /scratch/models/cache/golden/1a/d6c0d31760238b2ddad9898478d9d3 ref/quant_predictions_softmax_fix.bin
% env XLNX_ENABLE_DUMP=1 USE_CPU_TASK=1   ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/graph_task/test_graph_task /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/resnet50_tf2/resnet50_tf2.xmodel -i 2

```


## `face-quality`


``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env MODEL=face-quality.xmodel LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```


## `face-quality_pt`


``` console
% cd /group/face-quality_pt.xmodelxbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env MODEL=face-quality_pt.xmodel LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```

## `face_landmark`


``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env MODEL=face_landmark.xmodel LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```


## `facerec-resnet20_mixed_pt`


``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env MODEL=facerec-resnet20_mixed_pt.xmodel LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```


## `facerec_resnet20`


``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env MODEL=facerec_resnet20.xmodel LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```


## `facerec_resnet64`


``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env MODEL=facerec_resnet64.xmodel LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```

``` console
% ssh xcdl190253 md5sum /group/modelzoo/internal-cooperation-models/caffe/facerec_resnet64/quantized/acc/dump_gpu/Addmm_1.bin
```

## `facereid-large_pt`


``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env MODEL=facereid-large_pt.xmodel LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```

`libvart_op_imp_batchnorm.so` is not implemenated.

``` console
% cd /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/facereid-large_pt/
% ~/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir dump_txt facereid-large_pt.xmodel facereid-large_pt.txt
% mkdir -p ref; mkdir -p log; mkdir -p dump_cpu_runner
% cp /scratch/models/cache/golden/86/b5ffdce06e14fcc3cba432f23378a8 ref/Resnet18__Resnet18_input_fix.bin
% ~/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir subgraph facereid-large_pt.xmodel
% env USE_CPU_TASK=0  ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/graph_task/test_graph_task facereid-large_pt.xmodel -i 2
% cp 0.Resnet18__Resnet18_BatchNorm1d_bottleneck__411.bin 0.Resnet18__Resnet18_BatchNorm1d_bottleneck__411.bin.vaie
% env USE_CPU_TASK=1  ~/build/build.CentOS.7.6.1810.x86_64.Debug/Vitis-AI-Library/graph_task/test_graph_task facereid-large_pt.xmodel -i 2
% d 0.Resnet18__Resnet18_BatchNorm1d_bottleneck__411.bin 0.Resnet18__Resnet18_BatchNorm1d_bottleneck__411.bin.vaie

```

## `facereid-small_pt`


``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env MODEL=facereid-small_pt.xmodel LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```

## `fpn`


``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env MODEL=fpn.xmodel LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```

## `"hourglass-pe_mpii"`


``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env MODEL="hourglass-pe_mpii".xmodel LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```


## `inception_resnet_v2_tf`


``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env MODEL=inception_resnet_v2_tf.xmodel LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```

``` console
% ~/build/build.CentOS.7.4.1708.x86_64.Debug/xir/tools/xir dump_txt /group/xbjlab/dphi_software/software/workspace/chunywan/debug_xvdpu/1.5/xvdpu_1.5_
```

## `inception_v1`


``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env MODEL=inception_v1.xmodel LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```

## `inception_v1_tf`


``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env MODEL=inception_v1_tf.xmodel LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```

## `inception_v2`


``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% env MODEL=inception_v2.xmodel LD_LIBRARY_PATH=/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0 PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner   DEBUG_COMPARE=1 python3  run_graph.py vai-1.3.json && echo OK
```


``` console
% cd /var/lib/docker/scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/usr/share/vitis_ai_library/models/inception_v2;
% /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir dump_txt inception_v2.xmodel inception_v2.txt
% /home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/tools/xir subgraph inception_v2.xmodel
```



## show

``` console
% /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI-Library/graph_task/test
% python3 show_json.py vai-1.3.json
```
