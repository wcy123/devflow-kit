# start to verify samples

## extract model

```
ls -l /scratch/$USER/
mkdir -p /scratch/$USER/models
tar -xvf /scratch/$USER/xilinx_model_zoo-0.1.1-Linux.tar.gz -C /scratch/$USER/models --strip-components=1
ls -l /scratch/$USER/models
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
/group/xbjlab/dphi_software/petalinux_sdk/sdk-zcu104-1128.sh -y -d /group/xbjlab/dphi_software/software/workspace/$USER/petalinux-sdk/environment-setup-aarch64-xilinx-linux
unset LD_LIBRARY_PATH;source /group/xbjlab/dphi_software/software/workspace/$USER/petalinux-sdk/environment-setup-aarch64-xilinx-linux
cp -av $HOME/d/working/aisw/pybind11/include/pybind11 $OECORE_TARGET_SYSROOT/usr/include
```

and repeate the above steps


## build examples

set the common environment for host

```
os=`lsb_release -a | grep "Distributor ID" | sed 's/^.*:\s*//'`
os_version=`lsb_release -a | grep "Release" | sed 's/^.*:\s*//'`
arch=`uname -p`
target_info=${os}.${os_version}.${arch}
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/xilinx/xrt/lib:/home/$USER/.local/${target_info}.Debug/lib
```

set the common environment for edge

```

unset LD_LIBRARY_PATH;source /var/lib/docker/scratch/$USER/build/sdk/environment-setup-aarch64-xilinx-linux
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
ln -s /scratch/$USER/models/usr/share/vitis_ai_library/models/yolov3_adas_pruned_0_9/yolov3_adas_pruned_0_9.xmodel model_dir_for_U50/
bash -ex build.sh
./adas_detection /group/xbjlab/dphi_software/software/workspace/$USER/d/working/aisw/Vitis-AI/mpsoc/vitis_ai_samples_zcu102/adas_detection/video/adas.avi model_dir_for_U50
```

build and run `video_analysis`

```

cd $HOME/d/working/aisw/vart/dpu-runner/samples/video_analysis
ln -s /scratch/$USER/models/usr/share/vitis_ai_library/models/ssd_traffic_pruned_0_9/ssd_traffic_pruned_0_9.xmodel model_dir_for_U50/
$HOME/build/build.${target_info}.Debug/vart/dpu-runner/test/show_kernel model_dir_for_U50/ssd_traffic_pruned_0_9.xmodel
bash -ex build.sh
./video_analysis /group/xbjlab/dphi_software/software/workspace/$USER/d/working/aisw/Vitis-AI/mpsoc/vitis_ai_samples_zcu102/video_analysis/video/structure.mp4 model_dir_for_U50
```


build and run `segementation`

```
cd $HOME/d/working/aisw/vart/dpu-runner/samples/segmentation
ln -s /scratch/$USER/models/usr/share/vitis_ai_library/models/fpn/fpn.xmodel model_dir_for_U50/
$HOME/build/build.${target_info}.Debug/vart/dpu-runner/test/show_kernel model_dir_for_U50/fpn.xmodel
bash -ex build.sh
./segmentation  /group/xbjlab/dphi_software/software/workspace/$USER/d/working/aisw/Vitis-AI/mpsoc/vitis_ai_samples_zcu102/./segmentation/video/traffic.mp4 model_dir_for_U50/
```


build and run `pose detection`

```
cd $HOME/d/working/aisw/vart/dpu-runner/samples/pose_detection
mkdir -p model_dir_for_U50
cp -av model_dir_for_zcu102 model_dir_for_U50
ln -s /scratch/$USER/models/usr/share/vitis_ai_library/models/sp_net/sp_net.xmodel model_dir_for_U50/pose_0
ln -s /scratch/$USER/models/usr/share/vitis_ai_library/models/sp_net/sp_net.xmodel model_dir_for_U50/pose_2
ln -s /scratch/$USER/models/usr/share/vitis_ai_library/models/ssd_pedestrain_pruned_0_97/ssd_pedestrain_pruned_0_97.xmodel model_dir_for_U50/ssd
$HOME/build/build.${target_info}.Debug/vart/dpu-runner/test/show_kernel model_dir_for_U50/pose_0/sp_net.xmodel
$HOME/build/build.${target_info}.Debug/vart/dpu-runner/test/show_kernel model_dir_for_U50/ssd/ssd_pedestrain_pruned_0_97.xmodel
bash -ex build.sh
./pose_detection /group/xbjlab/dphi_software/software/workspace/$USER/d/working/aisw/Vitis-AI/mpsoc/vitis_ai_samples_zcu102/pose_detection/video/pose.mp4 model_dir_for_U50/
```


run resnet50 py

for edge

```
echo export LD_LIBRARY_PATH=.:$OECORE_TARGET_SYSROOT/install/Debug/lib
echo export PYTHONPATH=$OECORE_TARGET_SYSROOT/install/Debug/lib/python3.5/site-packages

ssh root@10.176.179.66
export LD_LIBRARY_PATH=.:/group/xbjlab/dphi_software/software/workspace/chunywan/petalinux-sdk/sysroots/aarch64-xilinx-linux/install/Debug/lib
export PYTHONPATH=/group/xbjlab/dphi_software/software/workspace/chunywan/petalinux-sdk/sysroots/aarch64-xilinx-linux/install/Debug/lib/python3.5/site-packages
cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/vart/dpu-runner/samples/resnet50_mt_py
python3 resnet50.py 1 ../resnet50/model_dir_for_zcu102/

```
