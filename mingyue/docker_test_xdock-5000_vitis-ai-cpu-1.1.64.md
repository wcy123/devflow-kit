## CHECK DOCKER ENVIRONMENT
### Git clone vitis-ai-docker and Create work home
```
ssh $USER@xcosda93
cd /proj/xcohdstaff5/$USER/nobkup/
ls
mkdir docker_test_0303
cd docker_test_0303
rm -rf vitis-ai-docker
git clone gits@xcdl190260:vitis/vitis-ai-docker.git
docker images
ls
cd $HOME
rm docker_test_0303
ln -s /proj/xcohdstaff5/$USER/nobkup/docker_test_0303/vitis-ai-docker docker_test_0303
```
### Preparing xclbin & models & samples
```
cd $HOME/docker_test_0303
ls
mkdir -p d/working
cd d/working
pwd
scp -r $USER@xcosda13:/proj/rdi/staff/$USER/d/working/$USER/cloud_test/7E100M ./
cp /proj/xcohdstaff5/mingyue/nobkup/docker_test_0302/vitis-ai-docker/d/working/xilinx_model_zoo-1.0.0-Linux.tar.gz ./
##cp -r /proj/xcohdstaff5/mingyue/nobkup/docker_test_0302/vitis-ai-docker/d/working/samples ./
scp -r mingyue@xcosda13:/home/mingyue/d/working/mingyue/vart/dpu-runner/samples ./
ls
```
### Start docker
```
cd $HOME/docker_test_0303
ls
docker images
<!--docker pull xdock:5000/vitis-ai-cpu:1.1.56
docker pull xdock.xilinx.com/vitis-ai-cpu:1.1.59 -->

./docker_run.sh xdock:5000/vitis-ai-cpu:1.1.64
```
### Check XRT&shell&xclbin
```
export INTERNAL_BUILD=1
/opt/xilinx/xrt/bin/xbutil query
sudo cp d/working/7E100M/* /usr/lib
md5sum /usr/lib/dpu.xclbin /usr/lib/hbm_address_assignment.txt
/opt/xilinx/xrt/bin/xbutil program -d 0 -p  /usr/lib/dpu.xclbin

```
### Check environments
```
export LD_LIBRARY_PATH=/opt/xilinx/xrt/lib:/usr/lib:/usr/lib/x86_64-linux-gnu:/opt/vitis_ai/conda/envs/vitis-ai-tensorflow/lib/

protoc --version
```
> $USER@xcosda93:/usr/lib$ protoc --version <br/>
> &emsp;&emsp;libprotoc 3.0.0

```
ls /usr/lib/
ldd /usr/lib/libxir.so
ldd /usr/lib/libvart-runner.so
ldd /usr/lib/libunilog.so
ldd /usr/lib/libvart-util.so
ldd /usr/lib/libvart-buffer-object.so
ldd /usr/lib/libvart-dpu-runner.so
```
> $USER@xcosda93:/workspace$ ldd /usr/lib/libvart-buffer-object.so<br/>
>         linux-vdso.so.1 (0x00007ffc2f4e5000)<br/>
>         libglog.so.0 => /usr/lib/x86_64-linux-gnu/libglog.so.0 (0x00007fcea9dd6000)<br/>
>         libxrt_core.so.2 => not found<br/>
>         libstdc++.so.6 => /usr/lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007fcea9a33000)<br/>
>        libgcc_s.so.1 => /opt/vitis_ai/conda/envs/vitis-ai-tensorflow/lib/libgcc_s.so.1 (0x00007fcea9a1f000)<br/>
>         libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fcea962e000)<br/>
>         libgflags.so.2.2 => /usr/lib/x86_64-linux-gnu/libgflags.so.2.2 (0x00007fcea9407000)<br/>
>         libunwind.so.8 => /usr/lib/x86_64-linux-gnu/libunwind.so.8 (0x00007fcea91ec000)<br/>
>         libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007fcea8fcd000)<br/>
>         libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007fcea8c2f000)<br/>
>         /lib64/ld-linux-x86-64.so.2 (0x000055728dadd000)<br/>
>         liblzma.so.5 => /opt/vitis_ai/conda/envs/vitis-ai-tensorflow/lib/liblzma.so.5 (0x00007fcea8a09000) <br/>
>         librt.so.1 => /lib/x86_64-linux-gnu/librt.so.1 (0x00007fcea87ff000)<br/>

```
 ls /usr/lib
 ldd /usr/lib/libvart-buffer-object.so
 ldd /usr/lib/libvart-dpu-controller.so
 ldd /usr/lib/libvart-dpu-runner.so
 ldd /usr/lib/libvart-elf-util.so
 ldd /usr/lib/libvart-xrt-device-handle.so
```


### Check resnet50 sample
```
cd /workspace/d/working
sudo tar -zxvf xilinx_model_zoo-1.0.0-Linux.tar.gz --strip-components=1  -C /
cp /usr/share/vitis_ai_library/models/resnet50/resnet50.xmodel /workspace/d/working/samples/resnet50/model_dir_for_U50/

cd /workspace/d/working/samples/resnet50
ls
bash build.sh
```


> mingyue@xcosda93:/workspace/d/working/samples/resnet50$ sudo bash build.sh <br/>
> No LSB modules are available. <br/>
> No LSB modules are available. <br/>
> In file included from /workspace/d/working/samples/resnet50/src/main.cc:32:0: <br/>
> /workspace/d/working/samples/resnet50/../common/common.h:22:10: <font color=red>fatal error: </font>opencv2/opencv.hpp: No such file or directory <br/>
>  #include <font style="color:red"> <opencv2/opencv.hpp> </font><br/>
> &emsp;&emsp;&emsp;&emsp;         ^~~~~~~~~~~~~~~~~~~~ <br/>
> compilation terminated.<br/>
> In file included from /workspace/d/working/samples/resnet50/../common/common.cpp:17:0:<br/>
> /workspace/d/working/samples/resnet50/../common/common.h:22:10: <font color=red>fatal error:</font> opencv2/opencv.hpp: No such file or directory <br/>
>  #include <font color=red><opencv2/opencv.hpp></font> <br/>
> &emsp;&emsp;&emsp;&emsp;         ^~~~~~~~~~~~~~~~~~~~   <br/>
> compilation terminated.<br/>

### Use solution from Jennifer
```
sudo apt-get update
<!--sudo apt-cache search opencv | grep 3.2
sudo apt-cache search opencv | grep 3.2 | grep dev -->
for i in `sudo apt-cache search  opencv|grep 3.2|grep dev|awk '{print $1}'`; do echo $i;sudo apt-get install -y $i; done
bash build.sh
```

> mingyue@xcosda93:/workspace/d/working/samples/resnet50$ bash build.sh <br/>
> No LSB modules are available. <br/>
> No LSB modules are available. <br/>
> /usr/lib/x86_64-linux-gnu/libgdcmMSFF.so.2.8: undefined reference to 'uuid_generate@UUID_1.0' <br/>
> /usr/lib/x86_64-linux-gnu/libgdcmMSFF.so.2.8: undefined reference to 'uuid_parse@UUID_1.0' <br/>
> /usr/lib/x86_64-linux-gnu/libgdcmMSFF.so.2.8: undefined reference to 'uuid_unparse@UUID_1.0' <br/>
> collect2: error: ld returned 1 exit status <br/>

----
solution from Jennifer:

> https://blog.csdn.net/qq_35170720/article/details/102636253
```
ldd /usr/lib/x86_64-linux-gnu/libgdcmMSFF.so.2.8
```
> libuuid.so.1 => /opt/vitis_ai/conda/envs/vitis-ai-tensorflow/lib/libuuid.so.1 (0x00007f5ad289a000)
```
cd /opt/vitis_ai/conda/envs/vitis-ai-tensorflow/lib/
sudo mkdir backup.libuuid
sudo mv libuuid* backup.libuuid
```
----

```
cd /workspace/d/working/samples/resnet50
bash build.sh
env XLNX_CHECK_COMMIT_ID_ENABLE=0 ./resnet50 model_dir_for_U50/

cd ../
ls
cd /workspace/d/working/samples/resnet50_mt_py
ls
sudo apt install python-opencv
sudo pip install opencv-python
python3
python3 resnet50.py  1 ../resnet50/model_dir_for_U50


```
<!--opencv_version -V
opencv --verion -->

end
