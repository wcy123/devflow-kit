# debug `inception_resnet_v2`



```
/group/modelzoo/internal-cooperation-models/tensorflow_quantize/classification/inception_resnet_v2/dump_results/dump_results_0/ 我用的是这个golden
/proj/xcdhdstaff2/jianweng/workspace/debug/inception_resnet_debug_20200303/compiled_model.xmodel
```

```
os=`lsb_release -a | grep "Distributor ID" | sed 's/^.*:\s*//'`
os_version=`lsb_release -a | grep "Release" | sed 's/^.*:\s*//'`
arch=`uname -p`
target_info=${os}.${os_version}.${arch}
export LD_LIBRARY_PATH=.:/usr/local/lib/:/usr/local/lib64:/opt/xilinx/xrt/lib:/home/$USER/.local/${target_info}.Debug/lib

mkdir -p /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/run/inception_resnet50_v2
cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/run/inception_resnet50_v2

$HOME/build/build.${target_info}.Debug/vart/dpu-runner/test/show_kernel ./compiled_model.xmodel
env XLNX_ENABLE_DUMP=1 $HOME/build/build.${target_info}.Debug/vart/dpu-runner/test/test_dpu_runner ./compiled_model.xmodel k_0 dump_results_0/input_aquant.bin 1 1
function d() { md5sum $1; stat -c %s $1; xxd $1 | head -n 16; }
d ./dump/subgraph_InceptionResnetV2_InceptionResnetV2_Repeat_1_block17_14_Branch_0_Conv2d_1x1_Conv2D/output/0.InceptionResnetV2_Logits_Logits_BiasAdd_aquant.bin
d dump/subgraph_InceptionResnetV2_Logits_AvgPool_1a_8x8_AvgPool/output/0.InceptionResnetV2_Logits_AvgPool_1a_8x8_AvgPool_aquant.bin
d dump/subgraph_InceptionResnetV2_InceptionResnetV2_Repeat_1_block17_14_Branch_0_Conv2d_1x1_Conv2D/internal/0.InceptionResnetV2_Logits_AvgPool_1a_8x8_AvgPool_aquant.bin
d dump_results_0/InceptionResnetV2_Logits_AvgPool_1a_8x8_AvgPool_aquant.bin

#逐层对数
env XLNX_ENABLE_UPLOAD=1 XLNX_GOLDEN_DIR=dump_results_0 XLNX_ENABLE_DEBUG_MODE=1 XLNX_ENABLE_DUMP=1 $HOME/build/build.${target_info}.Debug/vart/dpu-runner/test/test_dpu_runner ./compiled_model.xmodel k_0 dump_results_0/input_aquant.bin 1 1 2>&1 | tee a2.log
grep 'compare data' a2.log >c2.log


```
