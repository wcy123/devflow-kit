```
ssh mingyue@xcosda93
cd /proj/xcohdstaff5/mingyue/nobkup/
rm -rf /proj/xcohdstaff5/mingyue/nobkup/vitis-ai-docker
git clone gits@xcdl190260:vitis/vitis-ai-docker.git
cd $HOME
ln -s /proj/xcohdstaff5/mingyue/nobkup/vitis-ai-docker vitis-ai-docker
cd vitis-ai-docker
ls
```
```
mkdir -p d/working
cd d/working
ls
git clone gits@xcdl190260:aisw/unilog
git clone gits@xcdl190260:aisw/xir
git clone gits@xcdl190260:aisw/vart

cd $HOME/vitis-ai-docker
scp -r mingyue@xcosda13:/proj/rdi/staff/mingyue/d/working/mingyue/cloud_test/7E100M ./
scp xcdl190256:/wrk/xcdhdnobkup1/chunywan/build/build.Ubuntu.18.04.x86_64.Debug/model_zoo_builder/xilinx_model_zoo-1.0.0-Linux.tar.gz .
```
<!--cp /home/chunywan/build/vitis-ai-docker/docker_run.sh -->
```
docker images

./docker_run.sh xdock.xilinx.com/vitis-ai-cpu:1.1.45

export INTERNAL_BUILD=1

sudo
/opt/xilinx/xrt/bin/xbutil query
ls
sudo cp 7E100M/* /usr/lib
md5sum /usr/lib/dpu.xclbin /usr/lib/hbm_address_assignment.txt
/opt/xilinx/xrt/bin/xbutil program -d 0 -p  /usr/lib/dpu.xclbin
```
```
mkdir /workspace/opt
cd  /workspace/opt
cmake --version
- need cmake 3.16.4
ls
wget https://github.com/Kitware/CMake/releases/download/v3.16.4/cmake-3.16.4.tar.gz
tar -zxvf cmake-3.16.4.tar.gz
cdvitis-ai-docker cmake-3.16.4
mkdir build
cd build
cmake ..
make
chmod o+rwx .
sudo make install

<!-- whereis cmake -->
<!--/usr/local/bin/cmake --version -->
ls -l /usr/bin/cmake
sudo mv /usr/bin/cmake /usr/bin/cmake-3.10
sudo ln -s /usr/local/bin/cmake /usr/bin/cmake
cmake --version
---

protoc --version
- need libprotoc 3.4.0
cd /workspace/opt
wget https://github.com/protocolbuffers/protobuf/archive/v3.4.0.tar.gz
tar -zxvf v3.4.0.tar.gz
<!--cd .. -->
<!--rm -rf protobuf-3.4.0 -->
cd protobuf-3.4.0
mkdir -p build
cd build
cmake -Dprotobuf_BUILD_TESTS=off -Dprotobuf_BUILD_EXAMPLES=off -DBUILD_SHARED_LIBS=on ../cmake
make -j4
chmod o+rwx .
sudo make install

---
cd /workspace/opt
wget https://github.com/pybind/pybind11/archive/v2.4.3.tar.gz
tar -zxvf v2.4.3.tar.gz
cd pybind11-2.4.3
mkdir build
cd build
cmake -DPYBIND11_TEST=off -DPYBIND11_INSTALL=on ..
make
chmod o+rwx .
sudo make install

---
sudo apt update
sudo apt install automake
sudo apt-get install -y python3-dev

---
cd /workspace/opt
wget https://github.com/json-c/json-c/archive/json-c-0.13.1-20180305.tar.gz
tar -xzvf json-c-0.13.1-20180305.tar.gz
cd json-c-json-c-0.13.1-20180305
bash autogen.sh
./configure
make -j4
sudo make install

---
sudo apt install -y libopencv-dev


python -V
- Python 3.7.4
```
cd /workspace
mkdir .local
mkdir build
ls
cd /workspace/d/working

cd /workspace/d/working/unilog
./cmake.sh --type=debug --build-dir=/workspace/build/build.Debug/unilog --install-prefix=/workspace/.local/Debug

cd  /workspace/d/working/xir
./cmake.sh --build-python --clean --type=debug --build-dir=/workspace/build/build.Debug/xir --install-prefix=/workspace/.local/Debug

export LD_LIBRARY_PATH=/opt/xilinx/xrt/lib:/usr/local/lib:/usr/local/lib64:/workspace/.local/Debug/lib/workspace/.local/Debug/workspace/.local/Debug
protoc --version
cd  /workspace/d/working/vart
./cmake.sh --cmake-options=-DENABLE_DPU_RUNNER=ON --cmake-options=-DENABLE_SIM_RUNNER=OFF --cmake-options=-DENABLE_CPU_RUNNER=OFF --clean --type=debug --build-python --build-dir=/workspace/build/build.Debug/vart --install-prefix=/workspace/.local/Debug


cd /workspace
sudo tar -zxvf xilinx_model_zoo-1.0.0-Linux.tar.gz --strip-components=1  -C /
ls /usr/share/vitis_ai_library/models


ls /workspace/.local/Debug/share/cmake/vart
sudomingyue@xcosda93:/workspace/d/working/vart$ sudo
sudo: /usr/bin/sudo must be owned by uid 0 and have the setuid bit set

cd  /workspace/.local/Debug/share/cmake/vart/samples/resnet50
sudo bash build.sh
export LD_LIBRARY_PATH=$HOME/.local/Debug/lib/:/opt/xilinx/xrt/lib
env XLNX_CHECK_COMMIT_ID_ENABLE=0 ./resnet50 model_dir_for_U50/







end
