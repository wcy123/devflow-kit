```

% cd /group/xbjlab/dphi_software/software/workspace/mingyue/d/working/aisw/Vitis-AI-Library
% git branch
%  unset LD_LIBRARY_PATH;source /group/xbjlab/dphi_software/software/workspace/mingyue/d/working/aisw/petalinux/environment-setup-cortexa72-cortexa53-xilinx-linux
% make all
```


```
% cat /etc/hosts
% sshpass -p root ssh root@b0


```
### FADNet_2_pt
```
% cd /group/xbjlab/dphi_software/software/workspace/qiuyuny/sft_zcu102_bs/workspace/sw_zcu102_internal_test@13/vitis-ai-library/graph_runner/test
% env GOLDEN_CACHE=/group/xbjlab/dphi_software/software/workspace/qiuyuny/sft_zcu102_bs/workspace/sw_zcu102_internal_test@13/vitis-ai-library-samples-res/input_bin/golden MODEL=FADNet_2_pt MODEL_ZOO_ROOT=/  DEBUG_COMPARE=1 python3 run_graph.py /group/xbjlab/dphi_software/software/workspace/qiuyuny/sft_zcu102_bs/workspace/sw_zcu102_internal_test@13/config/xmodel_graph_edge.json


% env LD_LIBRARY_PATH=/group/xbjlab/dphi_software/software/workspace/mingyue/d/working/aisw/petalinux/sysroots/cortexa72-cortexa53-xilinx-linux/install/Debug/lib GOLDEN_CACHE=/group/xbjlab/dphi_software/software/workspace/qiuyuny/sft_zcu102_bs/workspace/sw_zcu102_internal_test@13/vitis-ai-library-samples-res/input_bin/golden MODEL=FADNet_2_pt MODEL_ZOO_ROOT=/  DEBUG_COMPARE=1 python3 run_graph.py /group/xbjlab/dphi_software/software/workspace/qiuyuny/sft_zcu102_bs/workspace/sw_zcu102_internal_test@13/config/xmodel_graph_edge.json

% cd /home/root/mingyue/test
## cp Vitis_AI_Library/graph_runner/test/* to test dir
## FADNet_2_pt json is not correct
% xdputil xmodel -l /usr/share/vitis_ai_library/models/FADNet_2_pt/FADNet_2_pt.xmodel

% env LD_LIBRARY_PATH=/group/xbjlab/dphi_software/software/workspace/mingyue/d/working/aisw/petalinux/sysroots/cortexa72-cortexa53-xilinx-linux/install/Debug/lib /usr/share/vitis_ai_library/test/cpu_task/check_supported_op /usr/share/vitis_ai_library/models/FADNet_2_pt/FADNet_2_pt.xmodel
## add data op & leaky_relu op

% env LD_LIBRARY_PATH=/group/xbjlab/dphi_software/software/workspace/mingyue/d/working/aisw/petalinux/sysroots/cortexa72-cortexa53-xilinx-linux/install/Debug/lib /usr/share/vitis_ai_library/test/graph_runner/test_graph_runner /usr/share/vitis_ai_library/models/FADNet_2_pt/FADNet_2_pt.xmodel -i 7

% env LD_LIBRARY_PATH=/group/xbjlab/dphi_software/software/workspace/mingyue/d/working/aisw/petalinux/sysroots/cortexa72-cortexa53-xilinx-linux/install/Debug/lib python3 xmodel_to_json.py

env LD_LIBRARY_PATH=/group/xbjlab/dphi_software/software/workspace/mingyue/d/working/aisw/petalinux/sysroots/cortexa72-cortexa53-xilinx-linux/install/Debug/lib GOLDEN_CACHE=/home/root/mingyue/golden MODEL=FADNet_2_pt MODEL_ZOO_ROOT=/  DEBUG_COMPARE=1 python3 run_graph.py vai-1.3-generated.json

```

# medical_seg_cell
```

# vitis AI Library add hard-sigmoid-fix op

% env GOLDEN_CACHE=/group/xbjlab/dphi_software/software/workspace/qiuyuny/sft_zcu102_bs/workspace/sw_zcu102_internal_test@13/vitis-ai-library-samples-res/input_bin/golden MODEL=medical_seg_cell_tf2 MODEL_ZOO_ROOT=/  DEBUG_COMPARE=1 python3 run_graph.py /group/xbjlab/dphi_software/software/workspace/qiuyuny/sft_zcu102_bs/workspace/sw_zcu102_internal_test@13/config/xmodel_graph_edge.json
% env LD_LIBRARY_PATH=/group/xbjlab/dphi_software/software/workspace/mingyue/d/working/aisw/petalinux/sysroots/cortexa72-cortexa53-xilinx-linux/install/Debug/lib GOLDEN_CACHE=/group/xbjlab/dphi_software/software/workspace/qiuyuny/sft_zcu102_bs/workspace/sw_zcu102_internal_test@13/vitis-ai-library-samples-res/input_bin/golden MODEL=medical_seg_cell_tf2 MODEL_ZOO_ROOT=/  DEBUG_COMPARE=1 python3 run_graph.py /group/xbjlab/dphi_software/software/workspace/qiuyuny/sft_zcu102_bs/workspace/sw_zcu102_internal_test@13/config/xmodel_graph_edge.json
```

# efficientnet-b0_tf2
```
## add hard-sigmoid-fix & depthwise-fix  op

% cd /home/root/mingyue/test
% env LD_LIBRARY_PATH=/group/xbjlab/dphi_software/software/workspace/mingyue/d/working/aisw/petalinux/sysroots/cortexa72-cortexa53-xilinx-linux/install/Debug/lib GOLDEN_CACHE=/group/xbjlab/dphi_software/software/workspace/qiuyuny/sft_zcu102_bs/workspace/sw_zcu102_internal_test@13/vitis-ai-library-samples-res/input_bin/golden MODEL=efficientnet-b0_tf2 MODEL_ZOO_ROOT=/  DEBUG_COMPARE=1 python3 run_graph.py /group/xbjlab/dphi_software/software/workspace/qiuyuny/sft_zcu102_bs/workspace/sw_zcu102_internal_test@13/config/xmodel_graph_edge.json
```
