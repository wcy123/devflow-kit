## pointpillar
### 1, compiler xmodel
xir use MR206


### 2, add customer op

### 3, test graph runner
```
% scp /workspace/tmp/pointpillar/pointpillar_VoxelNet_int_compiled_DPUCZDX8G_ISA0_B4096_MAX_BG2.xmodel root@b0:~/
% cd /workspace/aisw/Vitis-AI-Library
% unset LD_LIBRARY_PATH && source /opt/petalinux/2021.1/environment-setup-cortexa72-cortexa53-xilinx-linux
% make all
% rsync -avz /opt/petalinux/2021.1/sysroots/cortexa72-cortexa53-xilinx-linux/install/Release b0:/home/root/mingyue/

% cd /workspace/aisw/Vitis-AI-Library/cpu_task/examples/op_PPScatter
% make all
% scp ~/build/customer_op/libvart_op_imp_PPScatterV2.so  root@b0:/tmp/lib/
% rsync -avz /workspace/aisw/Vitis-AI-Library/usefultools/python b0:/home/root/mingyue
% scp /workspace/tmp/pointpillar/*.bin root@b0:/home/root/mingyue/pointpillars/ref/
```

```
% ssh b1
% cd /home/root/mingyue/python
% env LD_LIBRARY_PATH=/home/root/mingyue/Debug/lib PYTHONPATH=/home/root/mingyue/Debug/lib/python3.8/site-packages/ python3 xdputil.py xmodel -l ~/pointpillar_VoxelNet_int_compiled_DPUCZDX8G_ISA0_B4096_MAX_BG2.xmodel

% cd /home/root/mingyue/pointpillar
% mkdir ref
% env LD_LIBRARY_PATH=/home/root/mingyue/Debug/lib:/tmp/lib XLNX_ENABLE_DUMP=1 /home/root/mingyue/Debug/share/vitis_ai_library/test/graph_runner/test_graph_runner -i -1 ~/pointpillar_VoxelNet_int_compiled_DPUCZDX8G_ISA0_B4096_MAX_BG2.xmodel

```

### 4, test_op_imp to compare op
```
% env LD_LIBRARY_PATH=/home/root/mingyue/Debug/lib:/tmp/lib  /home/root/mingyue/Debug/share/vitis_ai_library/test/cpu_task/test_op_imp -g ~/pointpillar_VoxelNet_int_compiled_DPUCZDX8G_ISA0_B4096_MAX_BG2.xmodel --op  "VoxelNet__VoxelNet_input_4" -d out -r ref 2>a.log 1>&2
```
### 4, add graph runner sample : pointpillars_graph_runner

```
% scp /workspace/aisw/Vitis-AI-Library/graph_runner/samples/pointpillars_graph_runner/pointpillars_graph_runner b1:/home/root/mingyue/
% env LD_LIBRARY_PATH=/home/root/mingyue/Debug/lib:/tmp/lib /home/root/mingyue/pointpillars_graph_runner ~/pointpillar_VoxelNet_int_compiled_DPUCZDX8G_ISA0_B4096_MAX_BG2.xmodel ~/pointpillar_VoxelNet_int_compiled_DPUCZDX8G_ISA0_B4096_MAX_BG2.xmodel

```


### deephi_profiling
```

% cd /home/root/mingyue/pointpillars
% mkdir ref
% env DEBUG_CPU_TASK=1 DEEPHI_PROFILING=1 LD_LIBRARY_PATH=/home/root/mingyue/Release/lib:/tmp/lib XLNX_ENABLE_DUMP=0 /home/root/mingyue/Release/share/vitis_ai_library/test/graph_runner/test_graph_runner -i -1 ~/pointpillar_VoxelNet_int_compiled_DPUCZDX8G_ISA0_B4096_MAX_BG2.xmodel

```
