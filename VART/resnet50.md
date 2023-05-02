# compre results


``` console

```

goden
``` console
% d /scratch/group/modelzoo/internal-cooperation-models/caffe/resnet50.baseline9213_ck/fix/acc/dump_gpu/data.bin

743f1f81f99ea3708560edfac3c2d236  /scratch/group/modelzoo/internal-cooperation-models/caffe/resnet50.baseline9213_ck/fix/acc/dump_gpu/data.bin

% d  /scratch/group/modelzoo/internal-cooperation-models/caffe/resnet50.baseline9213_ck/fix/acc/dump_gpu/fc1000.bin

1419317ad942a1cb76a16b31b76cfb1e  /scratch/group/modelzoo/internal-cooperation-models/caffe/resnet50.baseline9213_ck/fix/acc/dump_gpu/fc1000.bin

```

old model

``` console
% cd ~/d/working/run/resnet50
% env XLNX_ENABLE_DUMP=1 XLNX_SHOW_DPU_COUNTER=1 XLNX_DPU_CORE_ID=0 DEBUG_XRT_DEVICE_HANDLE=1   ~/build/build.CentOS.7.6.1810.x86_64.Debug/vart/dpu-runner/test/test_dpu_runner /scratch/chunywan/models/usr/share/vitis_ai_library/models/resnet50/resnet50.xmodel  k_0 /scratch/group/modelzoo/internal-cooperation-models/caffe/resnet50.baseline9213_ck/fix/acc/dump_gpu/data.bin 1 1
% mv dump old_dump
% d dump/subgraph_res5c_branch2b_bias/input/0.data_fixed.bin
c8d5063cfb6cb97c77279bd53de63a35  dump/subgraph_res5c_branch2b_bias/input/0.data_fixed.bin

% d old_dump/subgraph_res5c_branch2b_bias/input/0.data_fixed.bin
%
% d old_dump/subgraph_res5c_branch2b_bias/output/0.fc1000_fixed.bin



```

new model

``` console
% cd ~/d/working/run/resnet50
% env XLNX_ENABLE_DUMP=1 XLNX_SHOW_DPU_COUNTER=1 XLNX_DPU_CORE_ID=0 DEBUG_XRT_DEVICE_HANDLE=1   ~/build/build.CentOS.7.6.1810.x86_64.Debug/vart/dpu-runner/test/test_dpu_runner  resnet50.xmodel k_0 /scratch/group/modelzoo/internal-cooperation-models/caffe/resnet50.baseline9213_ck/fix/acc/dump_gpu/data.bin 1 1
% d dump/subgraph_res5b_branch2b_weights/input/0.data_fixed.bin
% d dump/subgraph_res5b_branch2b_weights/input/1.data_fixed.bin
% d dump/subgraph_res5b_branch2b_weights/output/0.fc1000_fixed.bin
% d dump/subgraph_res5b_branch2b_weights/output/0.fc1000_fixed.bin
% d dump/subgraph_res5b_branch2b_weights/output/1.fc1000_fixed.bin
1419317ad942a1cb76a16b31b76cfb1e  dump_new/subgraph_res5b_branch2b_weights/output/0.fc1000_fixed.bin
% md5sum /scratch/group/modelzoo/internal-cooperation-models/caffe/resnet50.baseline9213_ck/fix/acc/dump_gpu/data.bin
743f1f81f99ea3708560edfac3c2d236
% xxd dump/subgraph_res5b_branch2b_weights/input/0.data_fixed.bin>0.txt
% xxd dump/subgraph_res5b_branch2b_weights/input/1.data_fixed.bin>1.txt
% paste  0.txt 1.txt | less
```



edge

``` console
% sshpass -p root ssh root@10.176.178.107
% mkdir -p /group/xbjlab
% mount -t nfs -o nolock 10.176.178.33:/group_xbjlab/ /group/xbjlab
% mkdir -p /home/root/wcy/resnet50
% cd /home/root/wcy/resnet50
% scp chunywan@10.176.178.16:/scratch/group/modelzoo/internal-cooperation-models/caffe/resnet50.baseline9213_ck/fix/acc//dump_gpu/data.bin .
% export LD_LIBRARY_PATH=/group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2019.2.aarch64.Release/vart/dpu-runner:/group/xbjlab/dphi_software/software/workspace/chunywan/petalinux-sdk/sysroots/aarch64-xilinx-linux/install/Release/lib
% env XLNX_SHOW_DPU_COUNTER=1  XLNX_ENABLE_DUMP=1 /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Debug/vart/dpu-runner/test/test_dpu_runner /usr/share/vitis_ai_library/models/resnet50/resnet50.xmodel resnet50_0 ../a.xmodel 1 1
% function d() { md5sum $1; stat -c %s $1; xxd $1 | head -n 16; }
% d ./dump/resnet50_0/output/0.fc1000_55.bin
1419317ad942a1cb76a16b31b76cfb1e  ./dump/resnet50_0/output/0.fc1000_55.bin
```


``` console
# debug
env XLNX_ENABLE_DUMP=1 XLNX_SHOW_DPU_COUNTER=1 XLNX_DPU_CORE_ID=0 DEBUG_DPU_RUNNER=1   ~/build/build.CentOS.7.6.1810.x86_64.Debug/vart/dpu-runner/test/test_dpu_runner /scratch/chunywan/models/usr/share/vitis_ai_library/models/resnet50/resnet50.xmodel  k_0 /scratch/group/modelzoo/internal-cooperation-models/caffe/resnet50.baseline9213_ck/fix/acc/dump_gpu/data.bin 1 1
```
