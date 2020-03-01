

start docker

```
ssh xcosda93
cd /home/chunywan/build/vitis-ai-docker
./docker_run.sh xdock.xilinx.com/vitis-ai:tools-1.0.3-cpu
cmake --version
```
create working directory

```
mkdir -p /home/chunywan/build/vitis-ai-docker/d/working
cd /home/chunywan/build/vitis-ai-docker/d/working
git clone gits@xcdl190260:aisw/unilog
git clone gits@xcdl190260:aisw/xir
git clone gits@xcdl190260:aisw/vart
```

prerequisites

```
mkdir -p /workspace/opt
cd /workspace/opt
wget https://github.com/Kitware/CMake/releases/download/v3.16.4/cmake-3.16.4.tar.gz
tar -zxvf cmake-3.16.4.tar.gz
cd cmake-3.16.4
mkdir build
cd build
cmake ..
make
chmod o+rwx .
sudo make install

cd /workspace/opt
wget https://github.com/protocolbuffers/protobuf/archive/v3.4.0.tar.gz
tar -zxvf v3.4.0.tar.gz
cd protobuf-3.4.0
mkdir -p build
cd build
cmake -Dprotobuf_BUILD_TESTS=off -Dprotobuf_BUILD_EXAMPLES=off -DBUILD_SHARED_LIBS=on ../cmake
make -j4
chmod o+rwx . && sudo make install

cd /workspace/opt
wget https://github.com/pybind/pybind11/archive/v2.4.3.tar.gz
tar -zxvf v2.4.3.tar.gz
cd pybind11-2.4.3
mkdir build
cd build
cmake -DPYBIND11_TEST=off -DPYBIND11_INSTALL=on ..
make
chmod o+rwx . && sudo make install

sudo apt update
sudo apt install automake

sudo apt-get install -y python3-dev

cd /workspace/opt
wget https://github.com/json-c/json-c/archive/json-c-0.13.1-20180305.tar.gz
tar -xzvf json-c-0.13.1-20180305.tar.gz
cd json-c-json-c-0.13.1-20180305
bash autogen.sh
./configure
make -j4
sudo make install

sudo apt install -y libopencv-dev
```

build everything

```
# in docker
cd /workspace/d/working/unilog
./cmake.sh --type=debug
cd /workspace/d/working/xir
./cmake.sh --build-python --type=debug
cd /workspace/d/working/vart
sudo ./cmake.sh --cmake-options=-DENABLE_DPU_RUNNER=ON --cmake-options=-DENABLE_SIM_RUNNER=OFF --cmake-options=-DENABLE_CPU_RUNNER=OFF  --clean --type=debug --build-python
```

install models

```
#host
scp xcdl190256:/wrk/xcdhdnobkup1/chunywan/build/build.Ubuntu.18.04.x86_64.Debug/model_zoo_builder/xilinx_model_zoo-1.0.0-Linux.tar.gz .
./docker_run.sh wcy_xdock
```

```
# in container
cd /workspace
sudo tar -zxvf xilinx_model_zoo-1.0.0-Linux.tar.gz --strip-components=1  -C /
```

install dpu.xclbin

```
cd /workspace
sudo cp dpu.xclbin hbm_address_assignment.txt /usr/lib/
```

start resnet 50

```
cd  ~/.local/Ubuntu.18.04.x86_64.Debug/share/vart/samples/resnet50
sudo bash build.sh
export LD_LIBRARY_PATH=$HOME/.local/Ubuntu.18.04.x86_64.Debug/lib/:/opt/xilinx/xrt/lib
env XLNX_CHECK_COMMIT_ID_ENABLE=0 ./resnet50 model_dir_for_U50/

```
end
