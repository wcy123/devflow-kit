
# build


```
echo 'update fingerprint to 576462972818292735 in aie_partition_1x4.json'
sed -i 's/\"inference_fingerprint\": \".*\",/\"inference_fingerprint\": \"576462972818292735\",/g' /workspace/DPU_PHX_KERNEL/aie_partition_1x4.json
mkdir -p /workspace/DPU_PHX_KERNEL/work
cp /workspace/DPU_PHX_KERNEL/scripts/1x4/compile.csh.simnow /workspace/DPU_PHX_KERNEL/work/compile.csh
cp /workspace/DPU_PHX_KERNEL/scripts/set_env.csh.212 /workspace/DPU_PHX_KERNEL/work
cp /workspace/DPU_PHX_KERNEL/graph/graph_all.h /workspace/DPU_PHX_KERNEL/work/graph.h
cp /workspace/DPU_PHX_KERNEL/graph/1x4/graph_all.cpp /workspace/DPU_PHX_KERNEL/work/graph.cpp
cp /workspace/DPU_PHX_KERNEL/constraints/1x4/constraints.json /workspace/DPU_PHX_KERNEL/work/constraints.json
cp /workspace/DPU_PHX_KERNEL/aie_partition_1x4.json aie_partition.json
sed -i 's/\#define ENABLE_FUSION [0-1]/\#define ENABLE_FUSION 0/' /workspace/DPU_PHX_KERNEL/common/Debug.h
sed -i 's/\#define CONV_CASE [0-1]/\#define CONV_CASE 1/' /workspace/DPU_PHX_KERNEL/common/Debug.h
sed -i 's/\#define DWC_CASE [0-1]/\#define DWC_CASE 1/' /workspace/DPU_PHX_KERNEL/common/Debug.h
sed -i 's/\#define POOL_CASE [0-1]/\#define POOL_CASE 1/' /workspace/DPU_PHX_KERNEL/common/Debug.h
sed -i 's/\#define ELEW_ADD_CASE [0-1]/\#define ELEW_ADD_CASE 1/' /workspace/DPU_PHX_KERNEL/common/Debug.h
sed -i 's/\#define ELEW_MUL_CASE [0-1]/\#define ELEW_MUL_CASE 0/' /workspace/DPU_PHX_KERNEL/common/Debug.h
sed -i 's/\#define RESHAPE_CASE [0-1]/\#define RESHAPE_CASE 1/' /workspace/DPU_PHX_KERNEL/common/Debug.h
sed -i 's/\#define HSIGMOID_CASE [0-1]/\#define HSIGMOID_CASE 1/' /workspace/DPU_PHX_KERNEL/common/Debug.h
sed -i 's/\#define TRANSPOSE_CASE [0-1]/\#define TRANSPOSE_CASE 1/' /workspace/DPU_PHX_KERNEL/common/Debug.h
sed -i 's/\#define CONV_HSIG_HSWISH [0-1]/\#define CONV_HSIG_HSWISH 1/' /workspace/DPU_PHX_KERNEL/common/Debug.h
sed -i 's/\#define LEAKY_PRELU_CASE [0-1]/\#define LEAKY_PRELU_CASE 0/' /workspace/DPU_PHX_KERNEL/common/Debug.h
sed -i 's/\#define DWC_HSIG_HSWISH [0-1]/\#define DWC_HSIG_HSWISH 1/' /workspace/DPU_PHX_KERNEL/common/Debug.h
sed -i 's/wrapper_\w*.cc/wrapper_arch.cc/' /workspace/DPU_PHX_KERNEL/work/graph.h
sed -i 's/#define SHIM_DMA [0-1]/#define SHIM_DMA 0/' /workspace/DPU_PHX_KERNEL/common/Debug.h
cd /workspace/DPU_PHX_KERNEL/work && ./compile.csh 0
make: *** No rule to make target '/workspace/DPU_PHX_KERNEL/work/libadf.a', needed by 'full_pdi'.  Stop.
```

```
cd /workspace/DPU_PHX_KERNEL
make xclbin
```


```
/proj/xbuilds/HEAD_plus_daily_latest/installs/lin64/Vitis/HEAD/aietools/bin/unwrapped/lnx64.o/aiecompiler: error while loading shared libraries: libtinfo.so.5: cannot open shared object file: No such file or directory

sudo -E apt-get install libncurses5
```

```
/usr/include/linux/errno.h:1:10: fatal error: asm/errno.h: No such file or directory
 #include <asm/errno.h>

# sudo -E apt-get install -y linux-headers-$(uname -r)
# https://jira.xilinx.com/browse/SR-935308
sudo -E apt-get install -y gcc-multilib

edit makefile
   -include=/usr/include/x86_64-linux-gnu
```

```
ERROR: [aiecompiler 77-4469] driver aiecompiler: Unknown command line argument '--dataflow'.  Try: '/proj/xbuilds/HEAD_plus_daily_latest/installs/lin64/Vitis/HEAD/aietools/bin/aiecompiler --help'
aiecompiler: Did you mean '--target'?
aiecompiler: Unknown command line argument '--aiearch=aie-ml'.  Try: '/proj/xbuilds/HEAD_plus_daily_latest/installs/lin64/Vitis/HEAD/aietools/bin/aiecompiler --help'
aiecompiler: Did you mean '--part=aie-ml'?
aiecompiler: Unknown command line argument '--phydevice=xc10AIE24x5-die-1LP-e-S-es1'.  Try: '/proj/xbuilds/HEAD_plus_daily_latest/installs/lin64/Vitis/HEAD/aietools/bin/aiecompiler --help'
aiecompiler: Did you mean '--list-devices=xc10AIE24x5-die-1LP-e-S-es1'?
```


```
/proj/xbuilds/IPU-TA/9999.0_integration_verified/XRT-IPU/x86_64/centos-default/opt/xilinx/xrt/bin/unwrapped/xclbinutil: error while loading shared libraries: libcrypto.so.10: cannot open shared object file: No such file or directory

sudo -E apt-get install -y libssl1.1

edit setup_env.sh change centos to ubuntu
```

```
/proj/xbuilds/IPU-TA/9999.0_integration_verified/XRT-IPU/x86_64/ubuntu-default/opt/xilinx/xrt/bin/unwrapped/xclbinutil: error while loading shared libraries: libboost_system.so.1.65.1: cannot open shared object file: No such file or directory
```

```
make xclbin v_op=opt_config1.h
```


```
git clone git@gitenterprise.xilinx.com:IPU/run_snl.git
cd run_snl
ls -l
./clone.sh
```
