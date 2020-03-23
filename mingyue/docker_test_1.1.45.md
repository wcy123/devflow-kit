## CHECK DOCKER ENVIRONMENT  WITH VITIS AI LIBRARY
### Git clone vitis-ai-docker and Create work home

login vdi : XCD Asigned Linux
```
xhost +
ssh -X xsjsda153
cd /wrk/xsjhdnobkup6/mingyue
ls
mkdir docker_test_0311
cd docker_test_0311
rm -rf vitis-ai-docker
git clone gits@xcdl190260:vitis/vitis-ai-docker.git
cd vitis-ai-docker
docker images
#git checkout gui
#docker pull xdock.xilinx.com/vitis-ai-cpu:1.1.37

ls
cd $HOME
ls
rm docker_test_0311
ln -s /wrk/xsjhdnobkup6/mingyue/docker_test_0311/vitis-ai-docker docker_test_0311

```
### Preparing xclbin & models & samples
```
cd $HOME/docker_test_0311
ls
git clone gits@xcdl190260:aisw/Vitis-AI-Library.git
git clone gits@xcdl190260:aisw/vitis-ai-library-samples-res.git
scp mingyue@xsjsda152:/tmp/xilinx_model_zoo-0.1.1-Linux.tar.gz ./
scp mingyue@xcosda143:/proj/xbuilds/VitisAI/0308_0750/Vitis-AI-Library/X86_64/libvitis_ai_library-1.1.0-Linux-build20.deb ./


scp -r $USER@xcdl190256:/group/dphi_software/vitis_ai_library/r1.1/vart_samples.tar.gz ./
tar -zxvf vart_samples.tar.gz

```
### Start docker
```
pwd
cd $HOME/docker_test_0311
docker images
./docker_run.sh -X xdock.xilinx.com/vitis-ai-cpu:1.1.45
./docker_run.sh -X xdock.xilinx.com/vitis-ai-cpu:1.1.50
./docker_run.sh -X xdock.xilinx.com/vitis-ai-cpu:1.1.46


#./docker_run.sh xdock.xilinx.com/vitis-ai-cpu:1.1.44
#./docker_run.sh -X hanxue-test:latest
#./docker_run.sh xdock.xilinx.com/vitis-ai-cpu:1.1.37

```
### Check XRT&shell&xclbin
```
export INTERNAL_BUILD=1
/opt/xilinx/xrt/bin/xbutil query
sudo cp vart_samples/6E250M/* /usr/lib
md5sum /usr/lib/dpu.xclbin /usr/lib/hbm_address_assignment.txt
/opt/xilinx/xrt/bin/xbutil program -d 0 -p  /usr/lib/dpu.xclbin

```
### Check environments
```
export LD_LIBRARY_PATH=/opt/xilinx/xrt/lib:/usr/lib:/usr/lib/x86_64-linux-gnu:/opt/vitis_ai/conda/envs/vitis-ai-tensorflow/lib/

sudo tar -zxvf xilinx_model_zoo-0.1.1-Linux.tar.gz --strip-components=1  -C /
ls /usr/share/vitis_ai_library/models
```
### Compiler Vitis AI Library and test samples
Compiler vitis-ai-library
```
#sudo chown -R $USER:vitis-ai-users $HOME
cd  /workspace/Vitis-AI-Library
./cmake.sh --type=release
#export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/.local/Ubuntu.18.04.x86_64.Release/lib
```
test classification
```
cd /workspace
$HOME/.local/Ubuntu.18.04.x86_64.Release/share/vitis_ai_library/samples/classification/test_jpeg_classification vgg_19_tf vitis-ai-library-samples-res/samples/classification/sample_classification.jpg
cd vitis-ai-library-samples-res/samples/classification/
$HOME/.local/Ubuntu.18.04.x86_64.Release/share/vitis_ai_library/samples/classification/test_performance_classification resnet_v1_50_tf $HOME/.local/Ubuntu.18.04.x86_64.Release/share/vitis_ai_library/samples/classification/test_performance_classification.list -t 4 -s 10

ls $HOME/.local/Ubuntu.18.04.x86_64.Release/share/vitis_ai_library/samples/classification

cd vitis-ai-library-samples-res/samples/multitask

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

```
Add more test:   test_jpeg  test_performance test_video and  demo

### Check resnet50 sample
```
cd /workspace/vart_samples/samples/resnet50
sh -x ./build.sh
bash build.sh
env XLNX_CHECK_COMMIT_ID_ENABLE=0 ./resnet50 model_dir_for_U50/

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
