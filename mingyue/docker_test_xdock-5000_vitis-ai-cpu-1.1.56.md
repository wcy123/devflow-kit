## CHECK DOCKER ENVIRONMENT
### Git clone vitis-ai-docker and Create work home

```
ssh mingyue@xcosda93
cd /proj/xcohdstaff5/mingyue/nobkup/
mkdir docker_test_0302
cd docker_test_0302
git clone gits@xcdl190260:vitis/vitis-ai-docker.git
cd $HOME
rm docker_test_0302
ln -s /proj/xcohdstaff5/mingyue/nobkup/docker_test_0302/vitis-ai-docker docker_test_0302
```
### Preparing xclbin & models & samples
```
cd docker_test_0302
ls
mkdir -p d/working
cd d/working

scp -r mingyue@xcosda13:/proj/rdi/staff/mingyue/d/working/mingyue/cloud_test/7E100M ./
cp /home/mingyue/vitis-ai-docker/xilinx_model_zoo-1.0.0-Linux.tar.gz ./
cp -r /home/mingyue/vitis-ai-docker/d/working/vart/dpu-runner/samples ./
ls
```
### Start docker
```
cd $HOME/docker_test_0302
ls
docker images
./docker_run.sh xdock:5000/vitis-ai-cpu:1.1.56

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
export LD_LIBRARY_PATH=/usr/lib:/usr/lib/x86_64-linux-gnu:/opt/vitis_ai/conda/envs/vitis-ai-tensorflow/lib/

protoc --version
```
> mingyue@xcosda93:/usr/lib$ protoc --version <br/>
> &emsp;&emsp;libprotoc 3.0.0

```

ldd /usr/lib/libxir.so
ldd /usr/lib/libvart-runner.so
ldd /usr/lib/libunilog.so
ldd /usr/lib/libvart-util.so
```


### Check resnet50 sample
```
<!--cd /workspace
sudo mkdir my_test
sudo mkdir /usr/lib/my_test -->

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
sudo apt-cache search opencv | grep 3.2
sudo apt-cache search opencv | grep 3.2 | grep dev
for i in `sudo apt-cache search  opencv|grep 3.2|grep dev|awk '{print $1}'`; do echo $i;sudo apt-get install -y $i; done

bash build.sh

```
> mingyue@xcosda93:/workspace/d/working/samples/resnet50$ bash build.sh <br/>
> No LSB modules are available. <br/>
> No LSB modules are available. <br/>
> /usr/lib/x86_64-linux-gnu/libgdcmMSFF.so.2.8: undefined reference to `uuid_generate@UUID_1.0' <br/>
> /usr/lib/x86_64-linux-gnu/libgdcmMSFF.so.2.8: undefined reference to `uuid_parse@UUID_1.0' <br/>
> /usr/lib/x86_64-linux-gnu/libgdcmMSFF.so.2.8: undefined reference to `uuid_unparse@UUID_1.0' <br/>
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

cd /workspace/d/working/samples/resnet50
bash build.sh
ls
ldd resnet50


env XLNX_CHECK_COMMIT_ID_ENABLE=0 ./resnet50 model_dir_for_U50/
```
> mingyue@xcosda93:/workspace/d/working/samples/resnet50$ env XLNX_CHECK_COMMIT_ID_ENABLE=0 ./resnet50 model_dir_for_U50/ <br/>
> WARNING: Logging before InitGoogleLogging() is written to STDERR <br/>
> F0302 06:34:30.823110   955 dpu_runner.cpp:109] Check failed: handle != NULL cannot open library! lib=/usr/lib/libvart-dpu-runner.so;error=/usr/lib/libvart-dpu-runner.so: cannot open shared object file: No such file or directory <br/>
> *** Check failure stack trace: *** <br/>
> Aborted  <br/>



end
