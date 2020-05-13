##  start docker
```
ssh xsjsda153
cd /wrk/xsjhdnobkup6/mingyue/
mkdir docker_test_0513
cd docker_test_0513
git clone gits@xcdl190260:vitis/vitis-ai-docker.git

cd $HOME
ln -s /wrk/xsjhdnobkup6/mingyue/docker_test_0513/vitis-ai-docker docker_test_0513
cd docker_test_0513

cd $HOME/docker_test_0513
./docker_run.sh xdock.xilinx.com/vitis-ai-cpu:1.1.55

export INTERNAL_BUILD=1
export LD_LIBRARY_PATH=/opt/xilinx/xrt/lib:/usr/lib:/usr/lib/x86_64-linux-gnu:/opt/vitis_ai/conda/envs/vitis-ai-tensorflow/lib/
```
## compile vart
```

git clone https://gitenterprise.xilinx.com/aisw/vart.git

cd /workspace/vart
./cmake.sh --cmake-options=-DENABLE_DPU_RUNNER=ON --cmake-options=-DENABLE_SIM_RUNNER=OFF --cmake-options=-DENABLE_CPU_RUNNER=OFF --type=release --pack=deb --cmake-options=-DCMAKE_PROJECT_VERSION_MAJOR=1 --cmake-options=-DCMAKE_PROJECT_VERSION_MINOR=1 --cmake-options=-DCMAKE_PROJECT_VERSION_PATCH=0

cp /home/mingyue/build/build.Ubuntu.18.04.x86_64.Release/vart/libvart-1.1.0-Linux.deb /workspace/

```

## use deb
#### replace files in the system with files in the deb package.
```
sudo dpkg -i libvart-1.1.0-Linux.deb
```
