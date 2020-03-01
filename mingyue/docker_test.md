## CHECK DOCKER ENVIRONMENT
### clone vitis-ai-docker and create work home
```
ssh mingyue@xcosda93
cd /proj/xcohdstaff5/mingyue/nobkup/
mkdir docker_test_0301
cd docker_test_0301
git clone gits@xcdl190260:vitis/vitis-ai-docker.git
cd $HOME
ln -s /proj/xcohdstaff5/mingyue/nobkup/docker_test_0301/vitis-ai-docker docker_test_0301
```
### prepare xclbin & models & samples
```
cd docker_test_0301
ls
mkdir -p d/working
cd d/working

scp -r mingyue@xcosda13:/proj/rdi/staff/mingyue/d/working/mingyue/cloud_test/7E100M ./
cp /home/mingyue/vitis-ai-docker/xilinx_model_zoo-1.0.0-Linux.tar.gz ./
cp -r /home/mingyue/vitis-ai-docker/d/working/vart/dpu-runner/samples ./
ls
```
> mingyue@xcosda93:working% ls <br/>
> 7E100M  samples  xilinx_model_zoo-1.0.0-Linux.tar.gz

### start docker
```
cd $HOME/docker_test_0301
ls
docker images
./docker_run.sh xdock.xilinx.com/vitis-ai-cpu:1.1.45

```
### check XRT&shell&xclbin
```
export INTERNAL_BUILD=1
/opt/xilinx/xrt/bin/xbutil query
cd /workspace
ls
sudo cp d/working/7E100M/* /usr/lib
md5sum /usr/lib/dpu.xclbin /usr/lib/hbm_address_assignment.txt
/opt/xilinx/xrt/bin/xbutil program -d 0 -p  /usr/lib/dpu.xclbin
```
> mingyue@xcosda93:/workspace$ /opt/xilinx/xrt/bin/xbutil program -d 0 -p  /usr/lib/dpu.xclbin <br/>
> INFO: Found total 1 card(s), 1 are usable <br/>
> INFO: xbutil program succeeded. <br/>

---

### check protobuf version
```
protoc --version
```
> mingyue@xcosda93:/usr/lib$ protoc --version <br/>
> &emsp;&emsp;libprotoc 3.0.0

```
cd /usr/lib
ls
ldd libxir.so
```
> mingyue@xcosda93:/usr/lib$ ldd libxir.so <br/>
> &emsp;&emsp;        linux-vdso.so.1 (0x00007ffd36103000)<br/>
> &emsp;&emsp;        <span style="color:red;">libprotobuf.so.22 => not found </span><br/>
> &emsp;&emsp;        libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007f60d51fa000)<br/>
> &emsp;&emsp;        libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007f60d4ff6000)<br/>
> &emsp;&emsp;        libcrypto.so.1.1 => /usr/lib/x86_64-linux-gnu/libcrypto.so.1.1 (0x00007f60d4b2b000)<br/>
> &emsp;&emsp;        libunilog.so.0 => /usr/lib/libunilog.so.0 (0x00007f60d4921000)<br/>
> &emsp;&emsp;        libglog.so.0 => /usr/lib/x86_64-linux-gnu/libglog.so.0 (0x00007f60d46f0000)<br/>
> &emsp;&emsp;        libstdc++.so.6 => /usr/lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007f60d4365000)<br/>
> &emsp;&emsp;        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007f60d414d000)<br/>
> &emsp;&emsp;        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f60d3d5c000)<br/>
> &emsp;&emsp;        /lib64/ld-linux-x86-64.so.2 (0x000055ee7de3c000)<br/>
> &emsp;&emsp;        libgflags.so.2.2 => /usr/lib/x86_64-linux-gnu/libgflags.so.2.2 (0x00007f60d3b37000)<br/>
> &emsp;&emsp;        libunwind.so.8 => /usr/lib/x86_64-linux-gnu/libunwind.so.8 (0x00007f60d391c000)<br/>
> &emsp;&emsp;        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f60d357e000)<br/>
> &emsp;&emsp;        liblzma.so.5 => /lib/x86_64-linux-gnu/liblzma.so.5 (0x00007f60d3356000)<br/>

---

check json-c
```
ldd libvart-runner.so
```
> mingyue@xcosda93:/usr/lib$ ldd libvart-runner.so <br/>
> &emsp;&emsp;        linux-vdso.so.1 (0x00007fff04e54000) <br/>
> &emsp;&emsp;        libglog.so.0 => /usr/lib/x86_64-linux-gnu/libglog.so.0 (0x00007ff2e152d000) <br/>
> &emsp;&emsp;        <span style="color:red;">libjson-c.so.4 => not found </span><br/>
> &emsp;&emsp;        libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007ff2e1329000)<br/>
> &emsp;&emsp;        libstdc++.so.6 => /usr/lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007ff2e0fa0000)<br/>
> &emsp;&emsp;        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007ff2e0d88000)<br/>
> &emsp;&emsp;        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007ff2e0997000)<br/>
> &emsp;&emsp;        libgflags.so.2.2 => /usr/lib/x86_64-linux-gnu/libgflags.so.2.2 (0x00007ff2e0770000) <br/>
> &emsp;&emsp;        libunwind.so.8 => /usr/lib/x86_64-linux-gnu/libunwind.so.8 (0x00007ff2e0555000)<br/>
> &emsp;&emsp;        libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007ff2e0336000)<br/>
> &emsp;&emsp;        /lib64/ld-linux-x86-64.so.2 (0x0000564484095000)<br/>
> &emsp;&emsp;        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007ff2dff98000) <br/>
> &emsp;&emsp;        liblzma.so.5 => /lib/x86_64-linux-gnu/liblzma.so.5 (0x00007ff2dfd72000)<br/>

```
ldd libunilog.so
ldd libvart-util.so
```

### check opencv version
```
pkg-config opencv --modversion
cd /usr
sudo find . -iname "libopencv_imgproc*"
```
> mingyue@xcosda93:/usr$ sudo find . -iname "libopencv_imgproc*" <br/>
> ./lib/x86_64-linux-gnu/libopencv_imgproc.so.3.2.0 <br/>
> ./lib/x86_64-linux-gnu/libopencv_imgproc.so.3.2 <br/>

<span style="color:red;">note: must opencv3.4 ?? </span>

### check glog
```
cd /usr
sudo find . -iname "libglog.so"
```
> mingyue@xcosda93:/usr$ sudo find . -iname "libglog.so" <br/>
> ./lib/x86_64-linux-gnu/libglog.so <br/>

### check gflags
```
sudo find . -iname "libgflags.so"
```
> mingyue@xcosda93:/usr$ sudo find . -iname "libgflags.so" <br/>
> ./lib/x86_64-linux-gnu/libgflags.so <br/>

---

### check resnet50 sample
```
cd /workspace/d/working/samples/resnet50
ls
sudo bash build.sh
<!-- sudo find / -iname "opencv.hpp" -->
```
> mingyue@xcosda93:/workspace/d/working/samples/resnet50$ sudo bash build.sh <br/>
> No LSB modules are available. <br/>
> No LSB modules are available. <br/>
> In file included from /workspace/d/working/samples/resnet50/src/main.cc:32:0: <br/>
> /workspace/d/working/samples/resnet50/../common/common.h:22:10: <span style="color:red;">fatal error: </span>opencv2/opencv.hpp: No such file or directory <br/>
>  #include<span style="color:red"> <opencv2/opencv.hpp> </span><br/>
>          ^~~~~~~~~~~~~~~~~~~~ <br/>
> compilation terminated.<br/>
> In file included from /workspace/d/working/samples/resnet50/../common/common.cpp:17:0:<br/>
> /workspace/d/working/samples/resnet50/../common/common.h:22:10: <span style="color:red;">fatal error:</span> opencv2/opencv.hpp: No such file or directory <br/>
>  #include <span style="color:red;"><opencv2/opencv.hpp></span> <br/>
> &emsp;&emsp;         ^~~~~~~~~~~~~~~~~~~~   <br/>
> compilation terminated.<br/>





end
