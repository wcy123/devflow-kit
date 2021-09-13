## pointpillar
### 1, compiler xmodel
xir use MR206


### 2, add customer op

### 3, test graph runner
```
% scp /workspace/tmp/pointpillar/pointpillar_VoxelNet_int_compiled_DPUCZDX8G_ISA0_B4096_MAX_BG2.xmodel root@b1:~/
% cd /workspace/aisw/Vitis-AI-Library
% unset LD_LIBRARY_PATH && source /opt/petalinux/2021.1/environment-setup-cortexa72-cortexa53-xilinx-linux
% make all
% rsync -avz /opt/petalinux/2021.1/sysroots/cortexa72-cortexa53-xilinx-linux/install/Debug b1:/home/root/mingyue/

% cd /workspace/aisw/Vitis-AI-Library/cpu_task/examples/op_PPScatter
% make all
% scp ~/build/customer_op/libvart_op_imp_PPScatter.so  root@b1:/tmp/lib/
% rsync -avz /workspace/aisw/Vitis-AI-Library/usefultools/python b1:/home/root/mingyue
```

```
% ssh b1
% cd /home/root/mingyue/python
% env LD_LIBRARY_PATH=/home/root/mingyue/Debug/lib PYTHONPATH=/home/root/mingyue/Debug/lib/python3.8/site-packages/ python3 xdputil.py xmodel -l ~/pointpillar_VoxelNet_int_compiled_DPUCZDX8G_ISA0_B4096_MAX_BG2.xmodel

% env LD_LIBRARY_PATH=/home/root/mingyue/Debug/lib:/tmp/libs /home/root/mingyue/Debug/share/vitis_ai_library/test/graph_runner/test_graph_runner -i -1 ~/pointpillar_VoxelNet_int_compiled_DPUCZDX8G_ISA0_B4096_MAX_BG2.xmodel ~/pointpillar_VoxelNet_int_compiled_DPUCZDX8G_ISA0_B4096_MAX_BG2.xmodel

% env LD_LIBRARY_PATH=/home/root/mingyue/Debug/lib PYTHONPATH=/home/root/mingyue/Debug/lib/python3.8/site-packages/ python3 xdputil.py run -i 3 ~/pointpillar_VoxelNet_int_compiled_DPUCZDX8G_ISA0_B4096_MAX_BG2.xmodel ~/pointpillar_VoxelNet_int_compiled_DPUCZDX8G_ISA0_B4096_MAX_BG2.xmodel ~/pointpillar_VoxelNet_int_compiled_DPUCZDX8G_ISA0_B4096_MAX_BG2.xmodel
%

```


### 4, delopy
