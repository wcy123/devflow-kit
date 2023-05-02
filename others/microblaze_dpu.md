# setup DPU on microblaze

## install sdk

``` console
% cd ~/build
% scp xcdl190253:/tmp/for_chunye_mb/sdk.sh mb_sdk.sh
% ./mb_sdk.sh -d /group/xbjlab/dphi_software/software/workspace/$USER/mb_sdk/ -y
```

there is a bug related with MicroBlaze SDK, here the workaround

```
% mkdir -p $OECORE_NATIVE_SYSROOT/usr/microblazeel-xilinx-linux
% ln -s $OECORE_TARGET_SYSROOT/usr/include/c++/8.2.0/microblazeel-xilinx-linux $OECORE_NATIVE_SYSROOT/usr/microblazeel-xilinx-linux/include
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

## on board testing

copy data to xbjlabdpwstn03

``` console
% rsync -avz /group/xbjlab/dphi_software/software/workspace/chunywan/mb_sdk/sysroots/microblazeel-v11.0-bs-cmp-re-mh-div-xilinx-linux/install/Debug xbjlabdpwstn03:/scratch/chunywan/
% rsync -avz /group/xbjlab/dphi_software/software/workspace/chunywan/mb_sdk/sysroots/microblazeel-v11.0-bs-cmp-re-mh-div-xilinx-linux/usr/lib/libcrypto.so* xbjlabdpwstn03:/scratch/chunywan/Debug/lib
% rsync -avz /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2019.2.microblazeel.Debug/vart/dpu-runner/test/test_dpu_runner xbjlabdpwstn03:/scratch/chunywan/Debug/bin
```

``` console
% ssh xbjlabdpwstn03
xbjlabdpwstn03% mkdir $HOME/nfs_root
xbjlabdpwstn03% /tools/xgs/bin/sudo mount -t nfs 192.168.1.1:/ $HOME/nfs_root
xbjlabdpwstn03% ssh root@192.168.1.1
root@xilinx-ku060-mb-dpu-v2019:# ls -l /scratch/chunywan
root@xilinx-ku060-mb-dpu-v2019:# export LD_LIBRARY_PATH=/scratch/chunywan/Debug/lib
root@xilinx-ku060-mb-dpu-v2019:# /scratch/chunywan/Debug/bin/xir subgraph /scratch/chunywan/resnet50.elf
root@xilinx-ku060-mb-dpu-v2019:# env DEBUG_DPU_RUNNER=1   /scratch/chunywan/Debug/bin/test_dpu_runner /scratch/chunywan/resnet50.elf resnet50_0 /scratch/chunywan/resnet50.elf 1 1
```


``` console
% sshpass -p root ssh root@10.176.178.27
% mkdir -p /group/xbjlab
% mount -t nfs -o nolock 10.176.178.33:/group_xbjlab/ /group/xbjlab
% export LD_LIBRARY_PATH=/group/xbjlab/dphi_software/software/workspace/hawkwang/build/mb_sdk/sysroots/microblazeel-v11.0-bs-cmp-re-mh-div-xilinx-linux/install/Debug/lib
% export LD_LIBRARY_PATH=/group/xbjlab/dphi_software/software/workspace/chunywan/mb_sdk/sysroots/microblazeel-v11.0-bs-cmp-re-mh-div-xilinx-linux/install/Release/lib
% sshpass -p root scp /var/lib/docker/scratch/chunywan/build/build.linux.2019.2.microblazeel.Release/Vitis-AI-Library/overview/test_jpeg_classification root@10.176.178.27:
% ls /group/xbjlab/dphi_software/software/workspace/chunywan/mb_sdk/sysroots/microblazeel-v11.0-bs-cmp-re-mh-div-xilinx-linux/install/Release/lib
% env DEEPHI_PROFILING=1 ~/test_jpeg_classification resnet18 sample_classification.jpg
% /group/xbjlab/dphi_software/software/workspace/hawkwang/build/build.linux.2019.2.microblazeel.Debug/vart/buffer-object/test_buffer_object 26214400
% scp root@10.176.179.61:/usr/share/vitis_ai_library/models/resnet50/resnet50.elf .
% env DEBUG_DPU_RUNNER=1 /group/xbjlab/dphi_software/software/workspace/hawkwang/build/build.linux.2019.2.microblazeel.Debug/vart/dpu-runner/test/test_dpu_runner resnet50.elf resnet50_0 resnet50.elf 1 1
```
