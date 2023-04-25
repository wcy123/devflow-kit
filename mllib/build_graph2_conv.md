
# setup Vitis development environment.

```
% ssh -J  localhost:10022 xcdl190344.xilinx.com
% ls -l /proj/xbuilds/SWIP_plus/9999.0_0401_2052plus/installs/lin64/Vitis/2023.2/
% source /opt/xilinx/xrt/setup.sh
% source /proj/xbuilds/SWIP_plus/9999.0_0401_2052plus/installs/lin64/Vitis/2023.2/settings64.sh
% cd /group/dphi_software/software/workspace/chunywan/d/working/xdock-vitis-ai-sw/workspace/graph2_conv
```


# debug x86sim

```
% git submodule update --init --recursive
% pwd
% cd genstream
% ./makeGen.sh
% ./trans.sh
% cd ..

% find . -iname run_graph.sh
% ./run_graph.sh
```



```
% cd /group/dphi_software/software/workspace/chunywan/d/working/xdock-vitis-ai-sw/workspace/graph2_conv/workspace
% aiecompiler --target=x86sim -v --log-level=5 -include=./direct_conv_int8x8_C16  ../graph/graph_conv_casc_mt.cpp --aiearch=aie-ml --use-phy-shim=true --disable-dma-autostart --stacksize=1280 --workdir=./Work --phydevice=xcvc2802-vsvh1760-2MP-i-S-es1 --pl-freq=100 --Xmapper=outgoingpliolimitpertile:6 --Xmapper=incomingpliolimitpertile:8
```
