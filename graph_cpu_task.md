# develop dw-conv op


``` console
% ssh xcdl190253 md5sum  /group/modelzoo/Vitis-AI-Tutorials/Keras-GoogleNet-ResNet/files/quantized_results/cifar10/miniResNet/dump/dump_results_0/batch_normalization_1_FusedBatchNormV3_1_add_aquant.bin


4139c788d5d5881f258c65676897765e  /group/modelzoo/Vitis-AI-Tutorials/Keras-GoogleNet-ResNet/files/quantized_results/cifar10/miniResNet/dump/dump_results_0/batch_normalization_1_FusedBatchNormV3_1_add_aquant.bin

```

generate reference result by `vaie`

``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/debug_vaie
% /home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/bin/vaie-run -i /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/usr/share/vitis_ai_library/models/Keras-GoogleNet-ResNet-cifar10-miniResNet"/"Keras-GoogleNet-ResNet-cifar10-miniResNet.xmodel  --init 'conv2d_1_input/aquant /scratch/models/cache/golden/a8/572a5837ab4ee567818b2b11621a63' --deploy --release --disable-debug --dump 'batch_normalization_1/FusedBatchNormV3_1/add/aquant b1.bin' --target run

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
% env PYTHONPATH=/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/xir/src/python:/home/chunywan/build/build.CentOS.7.6.1810.x86_64.Debug/vart/runner MODEL="Keras-GoogleNet-ResNet-cifar10-miniResNet.xmodel"  DEBUG_COMPARE=1 gdb --args python3  run_graph.py vai-1.3.json
```

第二节网络结果不对

``` console
% # Keras-GoogleNet-ResNet-cifar10-miniResNet.xmodel"
% env XLNX_ENABLE_DUMP=1 ~/build/build.CentOS.7.6.1810.x86_64.Debug/vart/dpu-runner/test/test_dpu_runner /scratch/models/xilinx_model_zoo_u50_1.3.0_amd64/./usr/share/vitis_ai_library/models/Keras-GoogleNet-ResNet-cifar10-miniResNet/Keras-GoogleNet-ResNet-cifar10-miniResNet.xmodel "subgraph_add_2/add(ReplaceEltwise)"
```


## run the who test


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
