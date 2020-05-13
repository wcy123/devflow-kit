

```
cd /wrk/xsjhdnobkup6/mingyue/
mkdir docker_test_0512
cd docker_test_0512
git clone gits@xcdl190260:vitis/vitis-ai-docker.git
pwd
cd ~
ln -s /wrk/xsjhdnobkup6/mingyue/docker_test_0512/vitis-ai-docker docker_test_0512
cd docker_test_0512
git clone https://gitenterprise.xilinx.com/aisw/unilog.git
git clone https://gitenterprise.xilinx.com/aisw/xir.git
git clone https://gitenterprise.xilinx.com/aisw/vart.git
git clone https://gitenterprise.xilinx.com/aisw/Vitis-AI-Library.git



cd $HOME/docker_test_0512
./docker_run.sh xdock.xilinx.com/vitis-ai-cpu:1.1.55
export INTERNAL_BUILD=1
export LD_LIBRARY_PATH=/opt/xilinx/xrt/lib:/usr/lib:/usr/lib/x86_64-linux-gnu:/opt/vitis_ai/conda/envs/vitis-ai-tensorflow/lib/
cd /usr/lib
ls
sudo rm /usr/lib/libxir*
sudo rm /usr/lib/libunilog*
sudo rm /usr/lib/libvart*
sudo mv /usr/share/cmake /usr/share/cmake.bak

cd /workspace/unilog
./cmake.sh --type=release

cd /workspace/xir
./cmake.sh --type=release





cd /workspace/vart
./cmake.sh --cmake-options=-DENABLE_DPU_RUNNER=ON --cmake-options=-DENABLE_SIM_RUNNER=OFF --cmake-options=-DENABLE_CPU_RUNNER=OFF --type=release --pack=deb --cmake-options=-DCMAKE_PROJECT_VERSION_MAJOR=1 --cmake-options=-DCMAKE_PROJECT_VERSION_MINOR=1 --cmake-options=-DCMAKE_PROJECT_VERSION_PATCH=0
cp /home/mingyue/build/build.Ubuntu.18.04.x86_64.Release/vart/libvart-1.1.0-Linux.deb /workspace/


cd /workspace
sudo dpkg -i libvart-1.1.0-Linux.deb

```
