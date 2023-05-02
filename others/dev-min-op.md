

# prepare input

``` console
% mkdir -p  /workspace/aisw/min-op; cd  /workspace/aisw/min-op
% scp xcdl190253:/group/dphi_software/software/workspace/huizhang/model_zoo_builder/build_0x601001036088131_other_rcan_full/ML-2767-RCAN-48x48/ML-2767-RCAN-48x48.xmodel .
% scp xcdl190253:/group/dphi_software/software/workspace/huizhang/model_zoo_builder/build_0x601001036088131_other_rcan_small/ML-2767-RCAN-48x48/ML-2767-RCAN-48x48.xmodel ML-2767-RCAN-48x48_small.xmodel
% scp xcdl190253:/group/dphi_software/software/workspace/huizhang/vitis-ai-library/graph_runner/test/ML-2767-RCAN-48x48.json .
% mkdir -p a6;
% scp xcdl190253:/group/dphi_software/software/workspace/huizhang/vitis-ai-library/graph_runner/test/golden/a6/5b71f8857bdbd0d6a0fed959aa586d a6/
% cat ML-2767-RCAN-48x48.json
% ls -la
% tree .
```



# run vaie

``` console
% cd  /workspace/aisw/min-op
% env GOLDEN_CACHE=. MODE=sim MODEL_ZOO_ROOT=. python3 /workspace/aisw/Vitis-AI-Library/graph_runner/test/run_vaie.py ML-2767-RCAN-48x48.json
% mv /tmp/chunywan/vaie.log/ML-2767-RCAN-48x48-tensorflow/sim/batch_0 .
% tree .
```

# check supported op types

``` console
% mkdir -p  /workspace/aisw/min-op; cd  /workspace/aisw/min-op
% ~/.local/Ubuntu.18.04.x86_64.Debug/share/vitis_ai_library/test/cpu_task/check_supported_op ML-2767-RCAN-48x48.xmodel
```

# analyze the xmodel

``` console
% mkdir -p  /workspace/aisw/min-op; cd  /workspace/aisw/min-op
% xdputil xmodel -t ML-2767-RCAN-48x48.txt ML-2767-RCAN-48x48.xmodel
% xdputil xmodel -l ML-2767-RCAN-48x48.xmodel | tee subgraph.json
% xdputil xmodel -s ML-2767-RCAN-48x48.svg ML-2767-RCAN-48x48.xmodel
% xdputil xmodel -t ML-2767-RCAN-48x48_small.txt ML-2767-RCAN-48x48_small.xmodel
% xdputil xmodel -l ML-2767-RCAN-48x48_small.xmodel | tee subgraph.json
% xdputil xmodel -s ML-2767-RCAN-48x48_small.svg ML-2767-RCAN-48x48_small.xmodel
```

# get ref result


``` console
% mkdir -p  /workspace/aisw/min-op; cd  /workspace/aisw/min-op
% mkdir -p ref
% mkdir -p config
% mkdir -p log
% cp /workspace/aisw/vart/cpu-runner/config/config.txt config
% cp -av batch_0/add_14_aquant.bin ref/
% env XLNX_ENABLE_DUMP=1 USE_CPU_TASK=0  /home/chunywan/build/build.Ubuntu.18.04.x86_64.Debug/Vitis-AI-Library/graph_runner/test_graph_runner ML-2767-RCAN-48x48.xmodel -i 2
% cp 0.Round_round_typecast.bin 0.Round_round_typecast.bin.ref
% md5sum 0.Round_round_typecast.bin.ref batch_0/Round_round_typecast.bin
```

# run test graph runner

``` console
% mkdir -p  /workspace/aisw/min-op; cd  /workspace/aisw/min-op
% env XLNX_ENABLE_DUMP=1 USE_CPU_TASK=1  /home/chunywan/build/build.Ubuntu.18.04.x86_64.Debug/Vitis-AI-Library/graph_runner/test_graph_runner ML-2767-RCAN-48x48.xmodel -i 2
% md5sum 0.Round_round_typecast.bin.ref 0.Round_round_typecast.bin batch_0/Round_round_typecast.bin
```
