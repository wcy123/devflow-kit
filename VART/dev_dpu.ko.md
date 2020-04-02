# DPU



```
ssh root@10.176.179.64
```

## install `dpu.ko`

```
insmod /lib/modules/4.19.0-xilinx-v2019.2/extra/dpu.ko
lsmod
dmesg | tail
```

check device tree
```
cat /proc/device-tree/dpu@8f000000/core-num | xxd
```

create nfs mount
```
mkdir -p /group/xbjlab
mount -t nfs -o nolock 10.176.178.33:/group_xbjlab/ /group/xbjlab
ls /group/xbjlab
```

build `usefultools`


```
cd ~/d/working/dpdlf/
git clone ssh://gits@localhost:10260/dpdlf/usefultools
git clone ssh://gits@localhost:10260/dpdlf/cmake_config
git clone ssh://gits@localhost:10260/dpdlf/dpcommon
git clone ssh://gits@localhost:10260/dpdlf/dp_elf_util

cp -av ~/d/working/aisw/unilog/cmake.sh  ~/d/working/dpdlf/dpcommon
cd ~/d/working/dpdlf/dpcommon; ./cmake.sh --cmake-options=-DCMAKE_MODULE_PATH=$HOME/d/working/dpdlf/cmake_config --cmake-options=-DBUILD_SHARED_LIBS=on

cp -av ~/d/working/aisw/unilog/cmake.sh  ~/d/working/dpdlf/dp_elf_util
cd ~/d/working/dpdlf/dp_elf_util;./cmake.sh --cmake-options=-DCMAKE_MODULE_PATH=$HOME/d/working/dpdlf/cmake_config --cmake-options=-DBUILD_SHARED_LIBS=on

cp -av ~/d/working/aisw/unilog/cmake.sh  ~/d/working/dpdlf/usefultools
cd ~/d/working/dpdlf/usefultools;./cmake.sh --cmake-options=-DCMAKE_MODULE_PATH=$HOME/d/working/dpdlf/cmake_config --cmake-options=-DBUILD_SHARED_LIBS=on

ls -l /group/xbjlab/dphi_software/software/workspace/chunywan/petalinux-sdk/sysroots/aarch64-xilinx-linux/install/Debug/bin | grep ver
ls -l /group/xbjlab/dphi_software/software/workspace/chunywan/petalinux-sdk/sysroots/aarch64-xilinx-linux/install/Debug/bin/xlnx
```

go to the session of ssh to board.

```
echo $PATH
PATH=/group/xbjlab/dphi_software/software/workspace/chunywan/petalinux-sdk/sysroots/aarch64-xilinx-linux/install/Debug/bin:/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin:/sbin

PATH=/group/xbjlab/dphi_software/software/workspace/chunywan/petalinux-sdk/sysroots/aarch64-xilinx-linux/install/Debug/bin:/usr/local/bin:/group/xbjlab/dphi_software/software/workspace/chunywan/petalinux-sdk/sysroots/aarch64-xilinx-linux/install/Debug/bin:/usr/local/bin/xlnx:/usr/bin:/bin:/usr/local/sbin:/usr/sbin:/sbin
```

check verreg

```
xilinx_verreg
```

install models
```
scp -P10256 localhost:/group/dphi_software/vitis_ai_library/r1.1/vitis_ai_model_ZCU102_2019.2-r1.1.0.deb /scratch/chunywan/
scp /scratch/chunywan/vitis_ai_model_ZCU102_2019.2-r1.1.0.deb root@10.176.179.64:/home/root/wcy
```

it is already mirrored at `/group/xbjlab/dphi_software/software/vitis_ai_library/r1.1/`

on board

```
mkdir -p /home/root/wcy
cd /home/root/wcy
touch /var/lib/dpkg/status # junpeng will fix this bug
dpkg -i vitis_ai_model_ZCU102_2019.2-r1.1.0.deb
```

copy golden to boad
```
scp -r /var/lib/docker/scratch/group/modelzoo/internal-cooperation-models/caffe/resnet50.baseline9213_ck/fix/acc/dump_gpu root@10.176.179.64:/home/root/wcy
```


on board


```
echo -ne '\x00\x00\x20\x72' > t.code
export LD_LIBRARY_PATH=/group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2019.2.aarch64.Debug/vart/dpu-runner:/group/xbjlab/dphi_software/software/workspace/chunywan/petalinux-sdk/sysroots/aarch64-xilinx-linux/install/Debug/lib

/group/xbjlab/dphi_software/software/workspace/chunywan/petalinux-sdk/sysroots/aarch64-xilinx-linux/install/Debug/bin/dpu_model_inspect \
    /usr/share/vitis_ai_library/models/resnet50/resnet50.elf


env DEBUG_XRT_DEVICE_HANDLE=1 DEBUG_DPU_CONTROLLER=1 XLNX_SHORT_CIRCUIT_DPU_CODE=1 \
/group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2019.2.aarch64.Debug/vart/dpu-runner/test/test_dpu_runner \
/usr/share/vitis_ai_library/models/resnet50/resnet50.elf resnet50_0 dump_gpu/data.bin 1 1

/group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2019.2.aarch64.Debug/Vitis-AI-Library/classification/test_classification resnet50 /group/xbjlab/dphi_software/software/workspace/chunywan/images/001.JPEG
# enable dpu debug level

```

download kernel source code

```
mkdir -p /var/lib/docker/scratch/chunywan/linux-kernel
cd /var/lib/docker/scratch/chunywan/linux-kernel
scp -P10256 localhost:/proj/xcdhdstaff1/junpengl/chunye/kernel-source_3dpu.tgz  .
scp -P10256 localhost:/proj/xcdhdstaff1/junpengl/chunye/zcu102_3dpu.config/  .
tar -xf kernel-source_3dpu.tgz
cd /var/lib/docker/scratch/chunywan/linux-kernel/kernel-source
unset LD_LIBRARY_PATH;source /group/xbjlab/dphi_software/software/workspace/$USER/petalinux-sdk/environment-setup-aarch64-xilinx-linux
export ARCH=arm64
export CROSS_COMPILE=aarch64-xilinx-linux-
cp /var/lib/docker/scratch/chunywan/linux-kernel/zcu102_3dpu.config .config
# make xilinx_zynqmp_defconfig
make -j10
#check version , must be '4.19.0-xilinx-v2019.2'
cat include/config/kernel.release

mkdir -p /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/dnndk
cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/dnndk
git clone ssh://gits@localhost:10260/SDK/vitis-ai-dnndk.git
cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/dnndk/vitis-ai-dnndk/driver
cat Makefile
cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/dnndk/vitis-ai-dnndk/driver/;unset LD_LIBRARY_PATH;source /group/xbjlab/dphi_software/software/workspace/$USER/petalinux-sdk/environment-setup-aarch64-xilinx-linux;make KERNELDIR=/var/lib/docker/scratch/chunywan/linux-kernel/kernel-source ARCH=arm64 CROSS_COMPILE=aarch64-xilinx-linux-
```


on board
```
rmmod dpu
rmmod dpu;insmod /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/dnndk/vitis-ai-dnndk/driver/dpu.ko;dmesg -c

```

give up this version of `dpu.ko`, offset calculation is messy.


```
scp -r -P10256 localhost:/proj/xcdhdstaff1/junpengl/dpu_bsp $HOME/d/working
cd $HOME/d/working/chunywan/dpu_bsp/dpu/files;ls
cat Makefile
cd $HOME/d/working/dpu_bsp/dpu/files;unset LD_LIBRARY_PATH;source /group/xbjlab/dphi_software/software/workspace/$USER/petalinux-sdk/environment-setup-aarch64-xilinx-linux;make KERNEL_SRC=/var/lib/docker/scratch/chunywan/linux-kernel/kernel-source ARCH=arm64 CROSS_COMPILE=aarch64-xilinx-linux-
```


on board

```
dmesg -C; rmmod dpu;insmod  /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/dpu_bsp/dpu/files/dpu.ko;dmesg
ls -l /sys/module/dpu
ls -l /sys/module/dpu/parameters
cat /sys/module/dpu/parameters/coremask | xxd

ls
```
