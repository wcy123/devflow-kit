## CHECK DOCKER ENVIRONMENT
### Git clone vitis-ai-docker and Create work home
```
ssh $USER@xcosda93
cd /proj/xcohdstaff5/$USER/nobkup/
ls
mkdir docker_test_0304
cd docker_test_0304
rm -rf vitis-ai-docker
git clone gits@xcdl190260:vitis/vitis-ai-docker.git
docker images
ls
cd $HOME
rm docker_test_0304
ln -s /proj/xcohdstaff5/$USER/nobkup/docker_test_0304/vitis-ai-docker docker_test_0304
```
### Preparing xclbin & models & samples
```
cd $HOME/docker_test_0304
ls
mkdir -p d/working
cd d/working
pwd
scp -r $USER@xcosda13:/proj/rdi/staff/$USER/d/working/$USER/cloud_test/7E100M ./
cp /proj/xcohdstaff5/mingyue/nobkup/docker_test_0302/vitis-ai-docker/d/working/xilinx_model_zoo-1.0.0-Linux.tar.gz ./
##cp -r /proj/xcohdstaff5/mingyue/nobkup/docker_test_0302/vitis-ai-docker/d/working/samples ./
scp -r mingyue@xsjsda153:/home/mingyue/d/working/mingyue/vart/dpu-runner/samples ./
ls
```
### Start docker
```
cd $HOME/docker_test_0304
ls
docker images
./docker_run.sh xdock:5000/vitis-ai-cpu:1.1.69
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

ldd /usr/lib/libvart-dpu-controller.so
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
#sudo apt install python-opencv
#sudo pip install opencv-python
python3
python3 resnet50.py  1 ../resnet50/model_dir_for_U50
pip3 install --user opencv-python
export PYTHONPATH=/usr/local/lib/python2.7/dist-packages:$PYTHONPATH
echo $PYTHONPATH  #/opt/vitis_ai/compiler
export PYTHONPATH=/opt/xilinx/xrt/lib:/usr/lib:/usr/lib/x86_64-linux-gnu:/opt/vitis_ai/conda/envs/vitis-ai-tensorflow/lib/:$PYTHONPATH

/usr/bin/python3 resnet50.py  1 ../resnet50/model_dir_for_U50

```
> mingyue@xcosda93:/workspace/d/working/samples/resnet50_mt_py$ /usr/bin/python3 resnet50.py  1 ../resnet50/model_dir_for_U50 <br/>
> Traceback (most recent call last): <br/>
>  File "resnet50.py", line 20, in <module> <br/>
>    import runner  <br/>
> ModuleNotFoundError: No module named 'runner' <br/>

```
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
```




<!--opencv_version -V
opencv --verion -->

end
