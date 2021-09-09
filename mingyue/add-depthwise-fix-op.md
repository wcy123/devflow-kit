```
# ls
#  cat /etc/hosts
% sshpass -p root ssh root@b3
% cd /group/xbjlab/dphi_software/software/workspace/qiuyuny/sft_zcu102_bs/workspace/sw_zcu102_internal_test@13/vitis-ai-library/graph_runner/test

% env LD_LIBRARY_PATH=/home/root/mingyue/Debug/lib GOLDEN_CACHE=/group/xbjlab/dphi_software/software/workspace/qiuyuny/sft_zcu102_bs/workspace/sw_zcu102_internal_test@13/vitis-ai-library-samples-res/input_bin/golden MODEL=efficientnet-b0_tf2 MODEL_ZOO_ROOT=/  DEBUG_COMPARE=1 python3 run_graph.py xmodel_graph_edge.json


```

```
% rsync -av /opt/petalinux/2021.1/sysroots/cortexa72-cortexa53-xilinx-linux/install/Debug b3:/home/root/mingyue/
```
