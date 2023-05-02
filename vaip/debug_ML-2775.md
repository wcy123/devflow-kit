

# prepare input

``` console
% mkdir -p  /workspace/aisw/debug_ML_2775; cd  /workspace/aisw/debug_ML_2775
% scp xcdl190253:/group/dphi_software/software/workspace/huizhang/model_zoo_builder/build_0x601001036088131_other_full/ML-2775-subaru_model_SASS4-20-model_a/ML-2775-subaru_model_SASS4-20-model_a.xmodel .
# 裁剪过的xmodel:
% scp xcdl190253:/group/dphi_software/software/workspace/huizhang/model_zoo_builder/build_0x601001036088131_other_small/ML-2775-subaru_model_SASS4-20-model_a/ML-2775-subaru_model_SASS4-20-model_a.xmodel ML-2775-subaru_model_SASS4-20-model_a-small.xmodel

# 输入：
% mkdir bc
% scp xcdl190253:/group/dphi_software/software/workspace/huizhang/vitis-ai-library/graph_runner/test/golden/bc/49479f3ea7096688c8a3450c095abe bc/
% scp xcdl190253:/group/dphi_software/software/workspace/huizhang/vitis-ai-library/graph_runner/test/ML-2775-subaru_model_SASS4-20-model_a.json .
% tree .
```


# run vaie

``` console
% cd  /workspace/aisw/debug_ML_2775
% env GOLDEN_CACHE=. MODE=sim MODEL_ZOO_ROOT=. python3 /workspace/aisw/Vitis-AI-Library/graph_runner/test/run_vaie.py ML-2775-subaru_model_SASS4-20-model_a.json
% mv /tmp/chunywan/vaie.log/ML-2775-subaru_model_SASS4-20-model_a-tensorflow .
% scp root@10.176.179.73:/tmp/qiuyuny/error_result/2/semantic_segmentation_semantic_segmentationsoftmax_truediv.bin  .
```

# run test graph runner

``` console
% mkdir -p ref
% cp -av ML-2775-subaru_model_SASS4-20-model_a-tensorflow/sim/batch_0/semantic_segmentation_semantic_segmentationlogits_semantic_BiasAdd_aquant.bin ref
% cp -av ML-2775-subaru_model_SASS4-20-model_a-tensorflow/sim/batch_0/semantic_segmentation_semantic_segmentationlogits_semantic_BiasAdd_aquant_reshaped_inserted_fix_1.bin ref
% mkdir -p config
% mkdir -p log
% cp /workspace/aisw/vart/cpu-runner/config/config.txt config
% env XLNX_ENABLE_DUMP=1 USE_CPU_TASK=0  /home/chunywan/build/build.Ubuntu.18.04.x86_64.Debug/Vitis-AI-Library/graph_runner/test_graph_runner ML-2775-subaru_model_SASS4-20-model_a.xmodel -i 2
% env XLNX_ENABLE_DUMP=1 USE_CPU_TASK=1  /home/chunywan/build/build.Ubuntu.18.04.x86_64.Debug/Vitis-AI-Library/graph_runner/test_graph_runner ML-2775-subaru_model_SASS4-20-model_a.xmodel -i 2
```


tips update cpu runner to enable config.

```diff
modified   cpu-runner/src/cpu_runner.cpp
@@ -324,7 +324,13 @@ xir::Op* CPURunner::get_xir_op(const string& op_name) const {
 }  // namespace cpu
 }  // namespace vart

+#include "vitis/ai/env_config.hpp"
+DEF_ENV_PARAM(XLNX_ENABLE_DUMP, "0")
 extern "C" vart::Runner* create_runner(const xir::Subgraph* subgraph) {
+  if (ENV_PARAM(XLNX_ENABLE_DUMP)) {
+    vart::cpu::CPUCfg::Instance().LoadConfig();
+    vart::cpu::CPUCfg::Instance().PrintConfig();
+  }
   auto ret = std::make_unique<vart::cpu::CPURunner>(subgraph);
   return ret.release();
 }
```


# compare the op by op

``` console
% find log | grep inserted
% find dump | grep inserted
% md5sum log/semantic_segmentation_semantic_segmentationsoftmax_Max_inserted_fix_2.bin dump/subgraph_semantic_segmentation_semantic_segmentationlogits_semantic_BiasAdd_aquant_semantic_segmentation_semantic_segmentationsoftmax_sub/semantic_segmentation_semantic_segmentationsoftmax_Max_inserted_fix_2_0.bin

% find log | grep Max_fix
% find dump | grep Max_fix
% md5sum log/semantic_segmentation_semantic_segmentationsoftmax_Max_fix.bin dump/subgraph_semantic_segmentation_semantic_segmentationlogits_semantic_BiasAdd_aquant_semantic_segmentation_semantic_segmentationsoftmax_sub/semantic_segmentation_semantic_segmentationsoftmax_Max_fix_0.bin

% find log | grep 'Max_fix.*softmax_sub.bin'
% find dump | grep 'Max_fix.*softmax_sub_0.bin'
% md5sum log/semantic_segmentation_semantic_segmentationsoftmax_Max_fix_semantic_segmentation_semantic_segmentationsoftmax_sub.bin dump/subgraph_semantic_segmentation_semantic_segmentationlogits_semantic_BiasAdd_aquant_semantic_segmentation_semantic_segmentationsoftmax_sub/semantic_segmentation_semantic_segmentationsoftmax_Max_fix_semantic_segmentation_semantic_segmentationsoftmax_sub_0.bin

% find log | grep 'BiasAdd'
% find dump | grep 'BiasAdd_aq'
% md5sum log/semantic_segmentation_semantic_segmentationlogits_semantic_BiasAdd_aquant_semantic_segmentation_semantic_segmentationsoftmax_sub.bin dump/subgraph_semantic_segmentation_semantic_segmentationlogits_semantic_BiasAdd_aquant_semantic_segmentation_semantic_segmentationsoftmax_sub/semantic_segmentation_semantic_segmentationlogits_semantic_BiasAdd_aquant_semantic_segmentation_semantic_segmentationsoftmax_sub_0.bin

% find log | grep sub.bin
% find dump | grep sub_0.bin
% md5sum log/semantic_segmentation_semantic_segmentationsoftmax_sub.bin dump/subgraph_semantic_segmentation_semantic_segmentationlogits_semantic_BiasAdd_aquant_semantic_segmentation_semantic_segmentationsoftmax_sub/semantic_segmentation_semantic_segmentationsoftmax_sub_0.bin

% find log | grep Exp
% find dump | grep Exp
% md5sum dump/subgraph_semantic_segmentation_semantic_segmentationlogits_semantic_BiasAdd_aquant_semantic_segmentation_semantic_segmentationsoftmax_sub/semantic_segmentation_semantic_segmentationsoftmax_Exp_0.bin log/semantic_segmentation_semantic_segmentationsoftmax_Exp.bin
% d dump/subgraph_semantic_segmentation_semantic_segmentationlogits_semantic_BiasAdd_aquant_semantic_segmentation_semantic_segmentationsoftmax_sub/semantic_segmentation_semantic_segmentationsoftmax_Exp_0.bin log/semantic_segmentation_semantic_segmentationsoftmax_Exp.bin


% find log | grep Sum
% find dump | grep Sum
% md5sum log/semantic_segmentation_semantic_segmentationsoftmax_Sum.bin dump/subgraph_semantic_segmentation_semantic_segmentationlogits_semantic_BiasAdd_aquant_semantic_segmentation_semantic_segmentationsoftmax_sub/semantic_segmentation_semantic_segmentationsoftmax_Sum_0.bin

% find log | grep truediv
% find dump | grep truediv
% md5sum log/semantic_segmentation_semantic_segmentationsoftmax_truediv.bin dump/subgraph_semantic_segmentation_semantic_segmentationlogits_semantic_BiasAdd_aquant_semantic_segmentation_semantic_segmentationsoftmax_sub/semantic_segmentation_semantic_segmentationsoftmax_truediv_0.bin
```

# why Exp is not exactly same.

```
% cp log/semantic_segmentation_semantic_segmentationsoftmax_sub.bin  ref/semantic_segmentation_semantic_segmentationsoftmax_sub.bin
% ~/.local/Ubuntu.18.04.x86_64.Debug/share/vitis_ai_library/test/cpu_task/test_op_imp -g ML-2775-subaru_model_SASS4-20-model_a.xmodel --op 'semantic_segmentation/semantic_segmentationsoftmax/Exp' -d out -r ref
% # input and output are same. !!!!
% md5sum dump/subgraph_semantic_segmentation_semantic_segmentationlogits_semantic_BiasAdd_aquant_semantic_segmentation_semantic_segmentationsoftmax_sub/semantic_segmentation_semantic_segmentationsoftmax_sub_0.bin dump/subgraph_semantic_segmentation_semantic_segmentationlogits_semantic_BiasAdd_aquant_semantic_segmentation_semantic_segmentationsoftmax_sub/semantic_segmentation_semantic_segmentationsoftmax_Exp_0.bin
```


# verify that the bug is fixed.

``` console
% env USE_CPU_TASK=0  /home/chunywan/build/build.Ubuntu.18.04.x86_64.Debug/Vitis-AI-Library/graph_runner/test_graph_runner ML-2775-subaru_model_SASS4-20-model_a.xmodel -i 2
% cp 0.semantic_segmentation_semantic_segmentationsoftmax_truediv.bin right.bin
% env USE_CPU_TASK=1  /home/chunywan/build/build.Ubuntu.18.04.x86_64.Debug/Vitis-AI-Library/graph_runner/test_graph_runner ML-2775-subaru_model_SASS4-20-model_a.xmodel -i 2
% md5sum 0.semantic_segmentation_semantic_segmentationsoftmax_truediv.bin right.bin
```
