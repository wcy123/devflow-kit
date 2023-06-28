# 781 https://gitenterprise.xilinx.com/VitisAI/vaip/issues/781

```
ssh -p 10022 localhost
cd /home/chunywan/build/vaip_regression/type2
scp -r xcdw200210:C://Users/genmingz/cache/01_diffOpOutput/dump .

cmp ./dump/cpurunner_pb_bin/onnx__DequantizeLinear_178.bin ./dump/cpu_runner/onnx.Conv_181_upload_0.bin && echo ok

./dump/cpu_runner/onnx.Add_200_vaip_136.bin
```

```
ipython

import numpy as np
import matplotlib.pyplot as plt


xmodel_Add_200 = np.fromfile("./dump/cpu_runner/onnx.Add_200_vaip_136.bin", dtype=np.int8).reshape([1, 112, 112, 64])

xmodel_Add_200_f = np.transpose(xmodel_Add_200.astype(np.float32) * 0.125, [0, 3, 1, 2])

ep_197 = np.fromfile("./dump/ort_pb_bin/onnx__Add_200.bin", dtype=np.float32).reshape([1, 64, 112, 112])

ep_blob = np.fromfile("./dump/ort_pb_bin/blob.bin", dtype=np.float32).reshape([1, 112, 112, 64])

xmodel_Add_200_f[0,0:4,0,0]
ep_blob[0,0:4,0,0]
ep_197[0,0:4,0,0]
```


# 622 https://gitenterprise.xilinx.com/VitisAI/vaip/issues/622

```
ssh -p 10022 localhost
export W=/workspace
cd $W/vaip
```

```
git status
git branch -a
cat .git/branches.txt | grep ci

git stash
git checkout -b ci-test-for-one 1ecff3694812ccffe6f2d72f5a5e224bb0b11117
git checkout  ci-test-for-one
git rvs
git push -u fork ci-test-for-one
python $W/vai-rt/main.py --dev-mode --project vaip

env VITISAI_EP_JSON_CONFIG=$W/vaip/vaip/etc/vaip_config.json python $W/vaip/ci/main.py run --env $W/vaip/ci/envs/1_SKIP_FATAL_1_OPT_0.env mlperf-retinanet
env VITISAI_EP_JSON_CONFIG=$W/vaip/vaip/etc/vaip_config.json python $W/vaip/ci/main.py run --env $W/vaip/ci/envs/1_SKIP_FATAL_1_OPT_0.env apple_recognition
env VITISAI_EP_JSON_CONFIG=$W/vaip/vaip/etc/vaip_config.json python $W/vaip/ci/main.py run --env $W/vaip/ci/envs/1_SKIP_FATAL_1_OPT_0.env ByobNet_int

# debug


env VITISAI_EP_JSON_CONFIG=$W/vaip/vaip/etc/vaip_config.json `cat $W/vaip/debug_env.txt`  `cat $W/vaip/ci/envs/1_SKIP_FATAL_1_OPT_0.env` gdb --args /home/chunywan/.local/Ubuntu.20.04.x86_64.Debug/bin/test_onnx_runner /home/chunywan/build/vaip_regression/mlperf-retinanet/TraceWrapper_int.onnx

env VITISAI_EP_JSON_CONFIG=$W/vaip/vaip/etc/vaip_config.json  `cat $W/vaip/debug_env.txt` `cat $W/vaip/ci/envs/1_SKIP_FATAL_1_OPT_0.env` gdb --args /home/chunywan/.local/Ubuntu.20.04.x86_64.Debug/bin/test_onnx_runner /home/chunywan/build/vaip_regression/apple_recognition/text_quantized_recogizer_py37_round_mode2_with_pretrain_v2_shapeinfo_cnn_only_0217.onnx
env VITISAI_EP_JSON_CONFIG=$W/vaip/vaip/etc/vaip_config.json  `cat $W/vaip/debug_env.txt` `cat $W/vaip/ci/envs/1_SKIP_FATAL_1_OPT_0.env` gdb --args /home/chunywan/.local/Ubuntu.20.04.x86_64.Debug/bin/test_onnx_runner /home/chunywan/build/vaip_regression/ByobNet_int/ByobNet_int.onnx

r
p ni_axes.node->index_
p *ni_axes.node

xcompiler -i "/tmp/chunywan/vaip/.cache/8d262138921794ae0f17f52506db6f9e/xir.xmodel" -o "/tmp/chunywan/vaip/.cache/8d262138921794ae0f17f52506db6f9e/compiled.xmodel" -t DPUCZDX8G_ISA1_B4096

md5sum /home/chunywan/build/vaip_regression/apple_recognition/text_quantized_recogizer_py37_round_mode2_with_pretrain_v2_shapeinfo_cnn_only_0217.onnx
ls "/tmp/chunywan/vaip/.cache/9a8fa89ca343bf453d7e0f3aee25f181/"


cat "/tmp/chunywan/vaip/.cache/9a8fa89ca343bf453d7e0f3aee25f181/vaip.0005.create_const_op.action_100.txt" | grep 283
/opt/netron/squashfs-root/AppRun netron --no-sandbox "/tmp/chunywan/vaip/.cache/9a8fa89ca343bf453d7e0f3aee25f181/vaip.0005.create_const_op.action_0.onnx"

ls -l "/tmp/chunywan/vaip/.cache/9a8fa89ca343bf453d7e0f3aee25f181/" | grep const
view -nw "/tmp/chunywan/vaip/.cache/9a8fa89ca343bf453d7e0f3aee25f181/const_info_after_const_folding.txt"



```
