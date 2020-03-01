clone vitis-ai-docker and create work home
```
ssh mingyue@xcosda93
cd /proj/xcohdstaff5/mingyue/nobkup/
mkdir docker_test_0301
cd docker_test_0301
git clone gits@xcdl190260:vitis/vitis-ai-docker.git
cd $HOME
ln -s /proj/xcohdstaff5/mingyue/nobkup/docker_test_0301/vitis-ai-docker docker_test_0301
```
prepare xclbin and models
```
cd docker_test_0301
ls
mkdir -p d/working
cd d/working

scp -r mingyue@xcosda13:/proj/rdi/staff/mingyue/d/working/mingyue/cloud_test/7E100M ./
cp /home/mingyue/vitis-ai-docker/xilinx_model_zoo-1.0.0-Linux.tar.gz ./
ls
```
start docker
```
cd $HOME/docker_test_0301
ls
docker images
./docker_run.sh xdock.xilinx.com/vitis-ai-cpu:1.1.45
```
check protobuf version
```
ls
protoc --version
> mingyue@xcosda93:/usr/lib$ protoc --version
> libprotoc 3.0.0


cd /usr/lib
ls
ldd libxir.so
```


end
