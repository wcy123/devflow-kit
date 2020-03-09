## CHECK DOCKER ENVIRONMENT
### Git clone vitis-ai-docker and Create work home
login vdi : XCD Asigned Linux
```
xhost +
ssh -X xcosda143
cd /proj/xcohdstaff5/$USER/nobkup/
ls
mkdir docker_test_0309
cd docker_test_0309
rm -rf vitis-ai-docker
git clone gits@xcdl190260:vitis/vitis-ai-docker.git
cd vitis-ai-docker
docker images

ls
cd $HOME
ls
rm docker_test_0309
ln -s /proj/xcohdstaff5/$USER/nobkup/docker_test_0309/vitis-ai-docker docker_test_0309
```
### Preparing xclbin & models & samples
```
cd $HOME/docker_test_0309
ls
scp -r $USER@xcosda13:/proj/rdi/staff/$USER/d/working/$USER/cloud_test/7E100M ./
scp -r $USER@xcdl190256:/group/dphi_software/vitis_ai_library/r1.1/vart_samples.tar.gz ./
tar -zxvf vart_samples.tar.gz

```
### Start docker
```
cd $HOME/docker_test_0309
ls
docker images
ls
./docker_run.sh xdock.xilinx.com/vitis-ai-cpu:1.1.30

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
```


### Check resnet50 sample
```
cd /workspace/vart_samples/samples/resnet50
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
