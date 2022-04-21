
## copy fixed model from xcd
```
## pytorch resnet50_pt
% scp /group/modelzoo/internal-cooperation-models/torchvision/resnet50/qat/ResNet_0_int.xmodel /workspace/tmp/
% scp /group/modelzoo/internal-cooperation-models/tensorflow_1.15_quantize/classification/resnet_v1_50/quantize_results/quantize_eval_model.pb /workspace/tmp/

% scp /workspace/tmp/ResNet_0_int.xmodel root@10.176.179.199:/home/root/models/
% scp /workspace/tmp/quantize_eval_model.pb root@10.176.179.199:/home/root/models/

```

## rsync debug compiler lib
```
% rsync -av /opt/petalinux/2022.1/sysroots/cortexa72-cortexa53-xilinx-linux/install/Debug xbjjmphost01:~/tmp/

% rsync -av /opt/petalinux/2022.1/sysroots/cortexa72-cortexa53-xilinx-linux/install/Debug/lib/libvitis_ai_library-graph_runner.so* 10.176.179.199:/home/root/Debug/lib/

% scp ~/build/build.linux.2022.1.aarch64.Debug/Vitis-AI-Library/graph_runner/test_graph_runner_2 root@10.176.179.199:~/

% ssh xbjjmphost01
% cd ~/tmp
% rsync -av Debug root@10.176.179.199:~/

```


## execute
```
% ssh root@10.176.179.199
% export PYTHONPATH=/home/root/Debug/lib/python3.9/site-packages/
% export LD_LIBRARY_PATH=/home/root/Debug/lib

% xdputil query
## xnnc
% python3 /home/root/Debug/lib/python3.9/site-packages/xnnc/__main__.py  --type tensorflow --layout NHWC --model ~/models/quantize_eval_model.pb --out resnet_v1_50_tf_xnnc.xmodel

## compiler
% ~/Debug/bin/xcompiler -i ~/resnet_v1_50_tf_xnnc.xmodel -o resnet_v1_50_tf.xmodel -t "DPUCZDX8G_ISA1_B4096"
% ~/Debug/bin/xcompiler -i ~/resnet_v1_50_tf_xnnc.xmodel -o resnet_v1_50_tf.xmodel -f "0x101000016010407"

## test
% ~/test_graph_runner_2 ~/resnet_v1_50_tf.xmodel
% ~/test_graph_runner_2 ~/resnet_v1_50_tf_xnnc.xmodel
% ~/test_graph_runner_2 ~/models/quantize_eval_model.pb

## test error case
% ~/test_graph_runner_2 ~/models/ResNet_0_int.xmodel.a
% ~/test_graph_runner_2 ~/a.svg.dot


```
