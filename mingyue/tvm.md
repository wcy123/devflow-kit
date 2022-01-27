##  generate simple conv2d xmodel
```
% cd /workspace/aisw/Vitis-AI-Library
% make all
% cd /workspace/aisw/xcompiler
% ./cmake.sh
```

```
# fix xcompiler
# CMakeLists delete find_package(glog1)
#./cmake.sh ->  make -j $(nproc)
# DebugManger.cpp
-  pb_debug.release_checkpoint();
+  auto pt = pb_debug.release_checkpoint();
+  CHECK(pt != nullptr || true);

# copy /group/dphi_arch/wanghong/gen_xmodel/gen_conv2d.py
# write [/workspace/gen_simple_conv2d.py] by xcompiler to gen xmodel
```
```
% env PYTHON_PATH=~/build/build.Ubuntu.20.04.x86_64.Debug/xir/src/python python3 gen_simple_conv2d.py
% /home/mingyue/.local/Ubuntu.20.04.x86_64.Debug/bin/xcompiler -i /workspace/conv2d_1.xmodel -o conv2d_compiler_1.xmodel -t  DPUCZDX8G_ISA0_B4096_MAX_BG2 --debug_mode function --debug_dump_path /workspace/conv2d_1 -d
## gen xmodel (without ac_code & mc_code) write [/worksapce/gen_simple_conv2d_xmodel.py]

% cd /workspace
% env PYTHON_PATH=~/build/build.Ubuntu.20.04.x86_64.Debug/xir/src/python python3 gen_simple_conv2d_xmodel.py

% gdb -ex r --args python
%
% env PYTHON_PATH=~/build/build.Ubuntu.20.04.x86_64.Debug/xir/src/python python3 gen_simple_conv2d_xmodel.py

% /home/mingyue/.local/Ubuntu.20.04.x86_64.Debug/bin/xcompiler -i /workspace/test.xmodel -o /workspace/test_compiler.xmodel -t  DPUCZDX8G_ISA0_B4096_MAX_BG2 --debug_mode function --debug_dump_path /workspace/test -d

% ~/.local/Ubuntu.20.04.x86_64.Debug/bin/xdputil xmodel -t test.txt /workspace/test.xmodel

```











```

% rsync -avz /opt/petalinux/2021.1/sysroots/cortexa72-cortexa53-xilinx-linux/install/Release 10.176.179.65:/home/root/mingyue/

% scp root@10.176.179.65:/home/root/mingyue/conv2d.xmodel /workspace/
```
```
% scp  mingyue@xcdl190074:/group/dphi_arch/wanghong/gen_xmodel/gen_conv2d.py ./
% scp gen_conv2d.py root@10.176.179.65:~/mingyue/
% ssh root@10.176.179.65


% cd ~/mingyue
% env PYTHON_PATH=/home/root/mingyue/Release/lib/python3.8/site-packages LD_LIBRARY_PATH=/home/root/mingyue/Release/lib:/home/root/mingyue/Release/lib/python3.8/site-packages python3 gen_conv2d.py

```
