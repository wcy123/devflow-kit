# setup DPU on microblaze

## install sdk

``` console
% cd ~/build
% scp xcdl190253:/tmp/for_chunye_mb/sdk.sh mb_sdk.sh
% ./mb_sdk.sh -d /group/xbjlab/dphi_software/software/workspace/$USER/mb_sdk/ -y
```

there is a bug related with MicroBlaze SDK, here the workaround

```
% mkdir -p /group/xbjlab/dphi_software/software/workspace/chunywan/mb_sdk/sysroots/x86_64-petalinux-linux/usr/microblazeel-xilinx-linux

% ln -s /group/xbjlab/dphi_software/software/workspace/chunywan/mb_sdk/sysroots/microblazeel-v11.0-bs-cmp-re-mh-div-xilinx-linux/usr/include/c++/8.2.0/microblazeel-xilinx-linux  /group/xbjlab/dphi_software/software/workspace/chunywan/mb_sdk/sysroots/x86_64-petalinux-linux/usr/microblazeel-xilinx-linux/include
```

## build them

``` console
% unset LD_LIBRARY_PATH;source /group/xbjlab/dphi_software/software/workspace/chunywan/mb_sdk/environment-setup-microblazeel-v11.0-bs-cmp-re-mh-div-xilinx-linux
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/;
% cd unilog;
% ./cmake.sh
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/;
% cd target_factory;
% ./cmake.sh
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/;
% cd xir;
% ./cmake.sh
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/;
% cd vart;
% ./cmake.sh --cmake-options=-DENABLE_DPU_RUNNER=ON --cmake-options=-DENABLE_SIM_RUNNER=OFF --cmake-options=-DENABLE_CPU_RUNNER=OFF
```
