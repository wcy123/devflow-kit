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
protoc --version
```
> mingyue@xcosda93:/usr/lib$ protoc --version
> libprotoc 3.0.0

```
cd /usr/lib
ls
ldd libxir.so
```
> mingyue@xcosda93:/usr/lib$ ldd libxir.so
>        linux-vdso.so.1 (0x00007ffd36103000)
>        libprotobuf.so.22 => not found
>        libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007f60d51fa000)
>        libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007f60d4ff6000)
>        libcrypto.so.1.1 => /usr/lib/x86_64-linux-gnu/libcrypto.so.1.1 (0x00007f60d4b2b000)
>        libunilog.so.0 => /usr/lib/libunilog.so.0 (0x00007f60d4921000)
>        libglog.so.0 => /usr/lib/x86_64-linux-gnu/libglog.so.0 (0x00007f60d46f0000)
>        libstdc++.so.6 => /usr/lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007f60d4365000)
>        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007f60d414d000)
>        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f60d3d5c000)
>        /lib64/ld-linux-x86-64.so.2 (0x000055ee7de3c000)
>        libgflags.so.2.2 => /usr/lib/x86_64-linux-gnu/libgflags.so.2.2 (0x00007f60d3b37000)
>        libunwind.so.8 => /usr/lib/x86_64-linux-gnu/libunwind.so.8 (0x00007f60d391c000)
>        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f60d357e000)
>        liblzma.so.5 => /lib/x86_64-linux-gnu/liblzma.so.5 (0x00007f60d3356000)

---

check json-c
```
ldd libvart-runner.so
```
mingyue@xcosda93:/usr/lib$ ldd libvart-runner.so
        linux-vdso.so.1 (0x00007fff04e54000)
        libglog.so.0 => /usr/lib/x86_64-linux-gnu/libglog.so.0 (0x00007ff2e152d000)
        libjson-c.so.4 => not found
        libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007ff2e1329000)
        libstdc++.so.6 => /usr/lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007ff2e0fa0000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007ff2e0d88000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007ff2e0997000)
        libgflags.so.2.2 => /usr/lib/x86_64-linux-gnu/libgflags.so.2.2 (0x00007ff2e0770000)
        libunwind.so.8 => /usr/lib/x86_64-linux-gnu/libunwind.so.8 (0x00007ff2e0555000)
        libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007ff2e0336000)
        /lib64/ld-linux-x86-64.so.2 (0x0000564484095000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007ff2dff98000)
        liblzma.so.5 => /lib/x86_64-linux-gnu/liblzma.so.5 (0x00007ff2dfd72000)


end
