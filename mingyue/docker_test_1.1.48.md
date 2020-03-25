## CHECK DOCKER ENVIRONMENT  WITH VITIS AI LIBRARY
### Git clone vitis-ai-docker and Create work home

login vdi : XCD Asigned Linux
```
xhost +
ssh -X xsjswmtech03
cd /wrk/xsjhdnobkup6/mingyue
ls
mkdir docker_test_0317
cd docker_test_0317
rm -rf vitis-ai-docker
git clone gits@xcdl190260:vitis/vitis-ai-docker.git
cd vitis-ai-docker
docker images

docker pull xdock.xilinx.com/vitis-ai-cpu:1.1.48

cd $HOME
ls
rm docker_test_0317
ln -s /wrk/xsjhdnobkup6/mingyue/docker_test_0317/vitis-ai-docker docker_test_0317

```
### Preparing xclbin & models & samples
```
cd $HOME/docker_test_0317
ls
git clone gits@xcdl190260:aisw/unilog.git
git clone gits@xcdl190260:aisw/xir.git
git clone gits@xcdl190260:aisw/vart.git
git clone gits@xcdl190260:aisw/Vitis-AI-Library.git
git clone gits@xcdl190260:aisw/vitis-ai-library-samples-res.git
cp ~/docker_test_0311/xilinx_model_zoo-0.1.1-Linux.tar.gz ./
cp ~/docker_test_0311/libvitis_ai_library-1.1.0-Linux-build20.deb ./
cp -r ~/docker_test_0311/vart_samples ./

```
### Start docker
```
pwd
cd $HOME/docker_test_0317
docker images
#./docker_run_0301.sh xdock:5000/vitis-ai-cpu:1.1.24
cp /proj/rdi/staff/hanxuel/devops/SR-908249/docker_run.sh ./
### can compiler vart
./docker_run.sh -X vitis-ai-mingyue:latest

./docker_run.sh -X xdock.xilinx.com/vitis-ai-cpu:1.1.48
./docker_run.sh -X xdock.xilinx.com/vitis-ai-cpu:1.1.51

#### test use new vart
./docker_run.sh -X xdock.xilinx.com/vitis-ai-cpu:1.1.51_tmp

./docker_run.sh -X xdock.xilinx.com/vitis-ai-cpu:1.1.50
./docker_run.sh -X xdock.xilinx.com/vitis-ai-cpu:1.1.52
./docker_run.sh -X xdock.xilinx.com/vitis-ai-cpu:1.1.55

./docker_run.sh ubuntu-opencv-34:latest
./docker_run.sh -X xdock.xilinx.com/vitis-ai-cpu:qiuyun_tmp
```
### Check XRT&shell&xclbin
```
export INTERNAL_BUILD=1
/opt/xilinx/xrt/bin/xbutil query
sudo cp vart_samples/6E250M/* /usr/lib
cp vart_samples/6E250M/* /usr/lib
md5sum /usr/lib/dpu.xclbin /usr/lib/hbm_address_assignment.txt
/opt/xilinx/xrt/bin/xbutil program -d 1 -p  /usr/lib/dpu.xclbin


```
### Check environments
```
export LD_LIBRARY_PATH=/opt/xilinx/xrt/lib:/usr/lib:/usr/lib/x86_64-linux-gnu:/opt/vitis_ai/conda/envs/vitis-ai-tensorflow/lib/
./opendl /usr/lib/libvart-dpu-runner.so
./opendl /usr/lib/libxir.so
./opendl /usr/lib/libunilog.so


cd /workspace
sudo tar -zxvf xilinx_model_zoo-0.1.1-Linux.tar.gz --strip-components=1  -C /

ls /usr/share/vitis_ai_library/models
```

### prepare build environments
```

cmake --version
### cmake version 3.10.2  -- we need 3.12.0 +
mkdir /workspace/opt
cd /workspace/opt
wget https://github.com/Kitware/CMake/releases/download/v3.16.4/cmake-3.16.4.tar.gz
tar -zxvf cmake-3.16.4.tar.gz
cd cmake-3.16.4
rm -rf build
#export CMAKE_CXX_STANDARD=11
#export CMAKE_CXX_EXTENSIONS=OFF
mkdir build
cd build
cmake ..
make
chmod o+rwx .
sudo make install
```
>   The C++ compiler does not support C++11 (e.g.  std::unique_ptr).

solution:  build a new docker
```

ls
cd /workspace/vart
 ./cmake.sh --cmake-options=-DENABLE_DPU_RUNNER=ON --cmake-options=-DENABLE_SIM_RUNNER=OFF --cmake-options=-DENABLE_CPU_RUNNER=OFF

export LD_LIBRARY_PATH=/home/mingyue/.local/Ubuntu.18.04.x86_64.Debug/lib:$LD_LIBRARY_PATH
echo $LD_LIBRARY_PATH

ldd /home/mingyue/build/build.Ubuntu.18.04.x86_64.Debug/vart/dpu-runner/test/test_dpu_runner
cd /workspace/resnet_v1_50_tf
env  DEBUG_XRT_DEVICE_HANDLE=1 XLNX_GOLDEN_DIR=dump_results_1 XLNX_EBABLE_CLEAR=0 DEBUG_DPU_RUNNER=1 DEBUG_DPU_CONTROLLER=0 XLNX_ENABLE_DEBUG_MODE=0 XLNX_ENABLE_UPLOAD=0 XLNX_ENABLE_DUMP_PARAMTER=0 XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_ENABLE_DUMP=1 XLNX_SHOW_DPU_COUNTER=1 /home/mingyue/build/build.Ubuntu.18.04.x86_64.Debug/vart/dpu-runner/test/test_dpu_runner resnet_v1_50_tf.xmodel resnet50_v1_50_0 dump_results_1/input_aquant.bin 1 1 2>a.log 1>&2

```



### Compiler Vitis AI Library and test samples
Compiler vitis-ai-library
```
#sudo chown -R $USER:vitis-ai-users $HOME
cd  /workspace/Vitis-AI-Library
./cmake.sh --type=release --cmake-options='-DENABLE_OVERVIEW=ON'
#export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/.local/Ubuntu.18.04.x86_64.Release/lib
```
test classification
```
cd /workspace
$HOME/.local/Ubuntu.18.04.x86_64.Release/share/vitis_ai_library/samples/classification/test_jpeg_classification vgg_19_tf vitis-ai-library-samples-res/samples/classification/sample_classification.jpg
cd vitis-ai-library-samples-res/samples/classification/
$HOME/.local/Ubuntu.18.04.x86_64.Release/share/vitis_ai_library/samples/classification/test_performance_classification resnet_v1_50_tf $HOME/.local/Ubuntu.18.04.x86_64.Release/share/vitis_ai_library/samples/classification/test_performance_classification.list -t 4 -s 10

ls $HOME/.local/Ubuntu.18.04.x86_64.Release/share/vitis_ai_library/samples/classification


cd /workspace/vitis-ai-library-samples-res/samples/multitask
```
test other samples:  test_jpeg  test_performance  test_video

### Test AI Library deb

```
export LD_LIBRARY_PATH=/opt/xilinx/xrt/lib:/usr/lib:/usr/lib/x86_64-linux-gnu:/opt/vitis_ai/conda/envs/vitis-ai-tensorflow/lib/
cd /workspace
ls
sudo dpkg -i libvitis_ai_library-1.1.0-Linux-build20.deb
ls
cd vitis-ai-library-samples-res/samples/classification

/usr/share/vitis_ai_library/samples/classification/test_jpeg_classification resnet_v1_50_tf sample_classification.jpg
/usr/share/vitis_ai_library/samples/classification/test_performance_classification resnet50 /usr/share/vitis_ai_library/samples/classification/test_performance_classification.list -t 4 -s 10

cd /workspace/vitis-ai-library-samples-res/samples/multitask
/usr/share/vitis_ai_library/samples/multitask/test_performance_multitask multi_task test_performance_multitask.list -t 4 -s 10
```
Add more test:   test_jpeg  test_performance test_video and  demo

### Check resnet50 sample
```
cd /workspace/vart_samples/samples/resnet50
bash build.sh
env XLNX_CHECK_COMMIT_ID_ENABLE=0 DEBUG_XRT_DEVICE_HANDLE=1 ./resnet50 model_dir_for_U50/

cd /workspace/vart_samples/samples/resnet50_mt_py
/usr/bin/python3 resnet50.py  1 ../resnet50/model_dir_for_U50

cd  /workspace/vart_samples/samples/inception_v1_mt_py
/usr/bin/python3 inception_v1.py 1 model_dir_for_U50

cd ../
ls
cd /workspace/vart_samples/samples/segmentation
bash build.sh
./segmentation ../../videos/traffic.mp4 model_dir_for_U50

cd /workspace/vart_samples/samples/video_analysis
bash build.sh
./video_analysis ../../videos/structure.mp4 model_dir_for_U50

cd /workspace/vart_samples/samples/adas_detection
bash build.sh
ls
./adas_detection ../../videos/adas.avi model_dir_for_U50

cd ../
ls
cd /workspace/vart_samples/samples/pose_detection
bash build.sh
./pose_detection ../../videos/pose.mp4 model_dir_for_U50

```

end
