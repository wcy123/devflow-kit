## start to verify samples

extract model

```
ls -l /scratch/chunywan/
mkdir -p /scratch/chunywan/models
tar -xvf /scratch/chunywan/xilinx_model_zoo-0.1.1-Linux.tar.gz -C /scratch/chunywan/models --strip-components=1
ls -l /scratch/chunywan/models
```


```
cd $HOME/d/working/aisw/unilog
git checkout dev
git fetch --all; git pull --rebase
./cmake.sh --clean

cd $HOME/d/working/aisw/xir
git fetch --all; git pull --rebase
./cmake.sh --build-python --clean

cd $HOME/d/working/aisw/vart
git pull --rebase
./cmake.sh --cmake-options=-DENABLE_DPU_RUNNER=ON --cmake-options=-DENABLE_SIM_RUNNER=OFF --cmake-options=-DENABLE_CPU_RUNNER=OFF  --clean --type=debug --build-python

```

build and resnet50 on cloud

```
cd $HOME/d/working/aisw/vart/dpu-runner/samples/resnet50
bash -ex build.sh
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/xilinx/xrt/lib:/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib
./resnet50 model_dir_for_U50/
```

buidl and test adas_detection

```
cd $HOME/d/working/aisw/vart/dpu-runner/samples/adas_detection
bash -ex build.sh
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/xilinx/xrt/lib:/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib
./adas_detection /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/Vitis-AI/mpsoc/vitis_ai_samples_zcu102/adas_detection/video/adas.avi model_dir_for_U50
```
