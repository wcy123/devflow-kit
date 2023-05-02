# build the model

``` console
% cd /workspace/aisw/debug_models/
% scp -r  xcdl190253:/proj/rdi/staff/kylexiao/workspace/DECENT_Q_TF_dev_v0.3/examples/mnist/mnist_tf_direct_quantize  .
% find . -iname '*.pb'
% conda activate vitis-ai-tensorflow
% vai_c_tensorflow -a /opt/vitis_ai/compiler/arch/DPUCAHX8H/U50/arch.json -o mnist_tf_direct -f mnist_tf_direct_quantize/quantize_results/quantize_eval_model.pb -n  mnist_tf_direct
% vai_c_tensorflow -h
% find mnist_tf_direct
```


# run ref result

``` console
% cd /workspace/aisw/Vitis-AI-Library/graph_task/test
% python3 xmodel_to_json.py /workspace/aisw/debug_models/mnist_tf_direct/mnist_tf_direct.xmodel
% find /workspace/aisw/debug_models/ | grep bin
% /workspace/aisw/debug_models/mnist_tf_direct/mnist_tf_direct.xmodel
% cp vai-1.3-generated.json mnist_tf_direct.json
%  # edit vai-1.3-generated.json and update input tensors and md5
% export PATH=/usr/local/cargo/bin:/opt/vitis_ai/utility:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$HOME/.local/bin:$HOME/.local/Ubuntu.18.04.x86_64.Debug/bin
% which vaie-run
% sudo mkdir -p /scratch/models/cache/golden/13
% sudo chmod -R o+rwx /scratch/models/cache/golden
% cp -av /workspace/aisw/debug_models/mnist_tf_direct_quantize/quantize_results/dump_results_0/reshape_Reshape_aquant.bin  /scratch/models/cache/golden/13/18bf5899ea83cceed6358374eb8c8a
% env MODEL_ZOO_ROOT=/workspace/aisw/debug_models/mnist_tf_direct LD_LIBRARY_PATH=$HOME/.local/Ubuntu.18.04.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0    DEBUG_COMPARE=1 python3  run_vaie.py mnist_tf_direct.json
% env MODEL_ZOO_ROOT=/workspace/aisw/debug_models/mnist_tf_direct LD_LIBRARY_PATH=$HOME/.local/Ubuntu.18.04.x86_64.Debug/lib:$HOME/.local/lib:/usr/local/lib:/usr/local/lib64 XLNX_ENABLE_DUMP=0    DEBUG_COMPARE=1 python3  run_graph.py mnist_tf_direct.json
```
