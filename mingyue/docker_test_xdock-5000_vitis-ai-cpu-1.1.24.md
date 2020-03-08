## CHECK DOCKER ENVIRONMENT
### Git clone vitis-ai-docker and Create work home
```
ssh $USER@xcosda93
cd /tmp/docker_test/vitis-ai-docker
pwd
mkdir mingyue
docker images
cd mingyue
pwd

<!--/tmp/docker_test/vitis-ai-docker/mingyue -->

<!--ls
cd $HOME
rm docker_test_0304
ln -s /proj/xcohdstaff5/$USER/nobkup/docker_test_0304/vitis-ai-docker docker_test_0304 -->
```
### Preparing xclbin & models & samples
```
cd /tmp/docker_test/vitis-ai-docker/mingyue

scp -r $USER@xcosda13:/proj/rdi/staff/$USER/d/working/$USER/cloud_test/7E100M ./
cp /proj/xcohdstaff5/mingyue/nobkup/docker_test_0302/vitis-ai-docker/d/working/xilinx_model_zoo-1.0.0-Linux.tar.gz ./
##cp -r /proj/xcohdstaff5/mingyue/nobkup/docker_test_0302/vitis-ai-docker/d/working/samples ./
scp -r mingyue@xsjsda153:/home/mingyue/d/working/mingyue/vart/dpu-runner/samples ./
ls
```
### Start docker
```
cd /tmp/docker_test/vitis-ai-docker
ls
docker images
./docker_run.sh xdock:5000/vitis-ai-cpu:1.1.24

```
### Check XRT&shell&xclbin
```
export INTERNAL_BUILD=1
/opt/xilinx/xrt/bin/xbutil query
sudo cp mingyue/7E100M/* /usr/lib
md5sum /usr/lib/dpu.xclbin /usr/lib/hbm_address_assignment.txt
/opt/xilinx/xrt/bin/xbutil program -d 0 -p  /usr/lib/dpu.xclbin

```
### Check environments
```
export LD_LIBRARY_PATH=/opt/xilinx/xrt/lib:/usr/lib:/usr/lib/x86_64-linux-gnu:/opt/vitis_ai/conda/envs/vitis-ai-tensorflow/lib/

sudo ldconfig
sudo find / -iname libprotobuf.so.14

```
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
cd /workspace/mingyue/
ls
sudo tar -zxvf xilinx_model_zoo-1.0.0-Linux.tar.gz --strip-components=1  -C /
ls /usr/share/vitis_ai_library/models/inception_v1_tf
cp /usr/share/vitis_ai_library/models/resnet50/resnet50.xmodel /workspace/mingyue/samples/resnet50/model_dir_for_U50/
ls /workspace/mingyue/samples/
cp /usr/share/vitis_ai_library/models/inception_v1_tf/inception_v1_tf.xmodel /workspace/mingyue/samples/inception_v1_mt_py/model_dir_for_U50/


cd /workspace/mingyue/samples/resnet50
ls
bash build.sh
```

```
cd /workspace/d/working/samples/resnet50
ls
bash build.sh
pwd

env XLNX_CHECK_COMMIT_ID_ENABLE=0 ./resnet50 model_dir_for_U50/

cd ../
ls
cd /workspace/mingyue/samples/resnet50_mt_py
ls
#sudo apt install python-opencv
#sudo pip install opencv-python
<!--python3
python3 resnet50.py  1 ../resnet50/model_dir_for_U50
pip3 install --user opencv-python
export PYTHONPATH=/usr/local/lib/python2.7/dist-packages:$PYTHONPATH
echo $PYTHONPATH  #/opt/vitis_ai/compiler
export PYTHONPATH=/opt/xilinx/xrt/lib:/usr/lib:/usr/lib/x86_64-linux-gnu:/opt/vitis_ai/conda/envs/vitis-ai-tensorflow/lib/:$PYTHONPATH
-->
/usr/bin/python3 resnet50.py  1 ../resnet50/model_dir_for_U50

cd ..
ls
cd inception_v1_mt_py
/usr/bin/python3 inception_v1.py 1 model_dir_for_U50
ls


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
