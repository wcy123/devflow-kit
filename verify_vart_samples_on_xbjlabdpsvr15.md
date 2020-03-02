# start to verify samples

## extract model

```
ls -l /scratch/chunywan/
mkdir -p /scratch/chunywan/models
tar -xvf /scratch/chunywan/xilinx_model_zoo-0.1.1-Linux.tar.gz -C /scratch/chunywan/models --strip-components=1
ls -l /scratch/chunywan/models
```

## build unilog/xir/vart

### on on host

```
cd $HOME/d/working/aisw/unilog
git checkout dev
git fetch --all; git pull --rebase
./cmake.sh --clean

cd $HOME/d/working/aisw/xir
git fetch --all; git pull --rebase
./cmake.sh  --clean # --build-python --

cd $HOME/d/working/aisw/vart
git pull --rebase
./cmake.sh --cmake-options=-DENABLE_DPU_RUNNER=ON --cmake-options=-DENABLE_SIM_RUNNER=OFF --cmake-options=-DENABLE_CPU_RUNNER=OFF  --clean --type=debug --build-python

```

### for zcu102

install petalinux sdk

```
/group/xbjlab/dphi_software/petalinux_sdk/sdk-zcu104-1128.sh -y -d /group/xbjlab/dphi_software/software/workspace/chunywan/petalinux-sdk
unset LD_LIBRARY_PATH;source ~/build/sdk/environment-setup-aarch64-xilinx-linux
```

and repeate the above steps


## build examples

set the common environment for host

```
os=`lsb_release -a | grep "Distributor ID" | sed 's/^.*:\s*//'`
os_version=`lsb_release -a | grep "Release" | sed 's/^.*:\s*//'`
arch=`uname -p`
target_info=${os}.${os_version}.${arch}
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/xilinx/xrt/lib:/home/chunywan/.local/${target_info}.Debug/lib
```

set the common environment for edge

```
unset LD_LIBRARY_PATH;source ~/build/sdk/environment-setup-aarch64-xilinx-linux
```
##

build and run `resnet50`

```
cd $HOME/d/working/aisw/vart/dpu-runner/samples/resnet50
bash -ex build.sh
./resnet50 model_dir_for_U50/
```

build and run `adas_detection`

```
cd $HOME/d/working/aisw/vart/dpu-runner/samples/adas_detection
ln -s /usr/share/vitis_ai_library/models/yolov3_adas_pruned_0_9/yolov3_adas_pruned_0_9.elf model_dir_for_zcu102/
ln -s /scratch/chunywan/models/usr/share/vitis_ai_library/models/yolov3_adas_pruned_0_9/yolov3_adas_pruned_0_9.xmodel model_dir_for_U50/
bash -ex build.sh
./adas_detection /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI/mpsoc/vitis_ai_samples_zcu102/adas_detection/video/adas.avi model_dir_for_U50
```

build and run `video_analysis`

```

cd $HOME/d/working/aisw/vart/dpu-runner/samples/video_analysis
ln -s /scratch/chunywan/models/usr/share/vitis_ai_library/models/ssd_traffic_pruned_0_9/ssd_traffic_pruned_0_9.xmodel model_dir_for_U50/
$HOME/build/build.${target_info}.Debug/vart/dpu-runner/test/show_kernel model_dir_for_U50/ssd_traffic_pruned_0_9.xmodel
bash -ex build.sh
./video_analysis /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI/mpsoc/vitis_ai_samples_zcu102/video_analysis/video/structure.mp4 model_dir_for_U50
```


build and run `segementation`

```
cd $HOME/d/working/aisw/vart/dpu-runner/samples/segmentation
ln -s /scratch/chunywan/models/usr/share/vitis_ai_library/models/fpn/fpn.xmodel model_dir_for_U50/
$HOME/build/build.${target_info}.Debug/vart/dpu-runner/test/show_kernel model_dir_for_U50/fpn.xmodel
bash -ex build.sh
./segmentation  /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI/mpsoc/vitis_ai_samples_zcu102/./segmentation/video/traffic.mp4 model_dir_for_U50/
```
