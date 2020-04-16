## login U50 LV card
```
ssh mingyue@xsjcda1
ssh user@10.23.80.199

ssh mingyue@xsjcda1
ssh -L 0.0.0.0:10190:localhost:22 user@10.23.80.199

ssh -p 10190 user@xsjcda1
```
## perpare samples
```
mkdir -p d/working
cd $HOME/d/working
git clone https://github.com/Xilinx/Vitis-AI.git
```
## cp update file from xsjsda153
```
#in xsjda153
scp -P 10190 -r u50lv_xclbin user@xsjcda1:~/d/working/
scp -P 10190 vart_performance_improve_packet.tar.gz user@xsjcda1:~/d/working/Vitis-AI
```

### check Vitis-AI 1.1.1 runnable
```
cd $HOME/d/working
ls
cd Vitis-AI
./docker_run.sh xilinx/vitis-ai

wget https://www.xilinx.com/bin/public/openDownload?filename=U50_xclbin.tar.gz
mv 'openDownload?filename=U50_xclbin.tar.gz' U50_xclbin.tar.gz
tar -zxvf U50_xclbin.tar.gz
sudo cp U50_xclbin/6E250M/* /usr/lib
/opt/xilinx/xrt/bin/xbutil program -d 0 -p /usr/lib/dpu.xclbin
export LD_LIBRARY_PATH=/opt/xilinx/xrt/lib:/usr/lib:/usr/lib/x86_64-linux-gnu:/opt/vitis_ai/conda/envs/vitis-ai-tensorflow/lib/

wget https://www.xilinx.com/bin/public/openDownload?filename=vitis-ai-runtime-1.1.1.tar.gz
mv 'openDownload?filename=vitis-ai-runtime-1.1.1.tar.gz' vitis-ai-runtime-1.1.1.tar.gz
tar -zxvf vitis-ai-runtime-1.1.1.tar.gz
cd vitis-ai-runtime-1.1.1/VART/X86_64
sudo dpkg -i libvart-1.1.0-Linux-build47.deb

cd /workspace/
wget https://www.xilinx.com/bin/public/openDownload?filename=vitis_ai_runtime_r1.1_image_video.tar.gz
mv 'openDownload?filename=vitis_ai_runtime_r1.1_image_video.tar.gz' vitis_ai_runtime_r1.1_image_video.tar.gz
tar -zxvf vitis_ai_runtime_r1.1_image_video.tar.gz -C VART

cd /workspace/VART/samples/resnet50
bash -ex build.sh
./resnet50 model_dir_for_U50/

env DEBUG_DPU_RUNNER=1 DEBUG_XRT_DEVICE_HANDLE=1 DEBUG_DPU_CONTROLLER=1 ./resnet50 model_dir_for_U50/
cd resnet50_mt_py/
./resnet50.py ../resnet50/model_dir_for_U50/
/usr/bin/python3 resnet50.py 4 ../resnet50/model_dir_for_U50/

```
#### update vart & samples
```
cd /workspace/
tar -zxvf vart_performance_improve_packet.tar.gz
cd vart_performance_improve_packet
cat readme.txt
tar -zxvf VART_runtime_update.tar.gz
cd VART/X86_64
sudo dpkg -i libvart-1.1.0-Linux.deb

cd ../../
tar -zxvf VART_samples_update.tar.gz -C ../VART/

cd /workspace/VART/samples/resnet50_mt_py
/usr/bin/python3 resnet50.py 4 ../resnet50/model_dir_for_U50/



```

#### use Vitis-ai-library and test_performance for resent50
```
cd /workspace
wget https://www.xilinx.com/bin/public/openDownload?filename=vitis_ai_library_r1.1_images.tar.gz
ls
mv 'openDownload?filename=vitis_ai_library_r1.1_images.tar.gz' vitis_ai_library_r1.1_images.tar.gz
tar -xzvf vitis_ai_library_r1.1_images.tar.gz -C Vitis-AI-Library/overview

wget https://www.xilinx.com/bin/public/openDownload?filename=xilinx_model_zoo-1.1.0-Linux.deb
mv 'openDownload?filename=xilinx_model_zoo-1.1.0-Linux.deb' xilinx_model_zoo-1.1.0-Linux.deb
ls
sudo dpkg -i xilinx_model_zoo-1.1.0-Linux.deb


cd /workspace/Vitis-AI-Library
./cmake.sh --type=release --cmake-options='-DENABLE_OVERVIEW=ON'

cd /workspace/Vitis-AI-Library/overview/samples/classification
ls
~/build/build.Ubuntu.18.04.x86_64.Release/Vitis-AI-Library/overview/test_jpeg_classification resnet_v1_50_tf sample_classification.jpg
##env DEBUG_XRT_DEVICE_HANDLE=1 XLNX_GOLDEN_DIR=dump_results_1 XLNX_EBABLE_CLEAR=0 DEBUG_DPU_RUNNER=1 DEBUG_DPU_CONTROLLER=1 XLNX_ENABLE_DEBUG_MODE=0 XLNX_ENABLE_UPLOAD=0 XLNX_ENABLE_DUMP_PARAMTER=0 XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_ENABLE_DUMP=1 XLNX_SHOW_DPU_COUNTER=1

env XLNX_ENABLE_DUMP=1 XLNX_SHOW_DPU_COUNTER=1 XLNX_ENABLE_DEBUG_MODE=0 ~/build/build.Ubuntu.18.04.x86_64.Release/Vitis-AI-Library/overview/test_jpeg_classification resnet_v1_50_tf sample_classification.jpg
mv dump dump_results

env XLNX_ENABLE_DUMP=1 XLNX_SHOW_DPU_COUNTER=1 XLNX_ENABLE_DEBUG_MODE=1 ~/build/build.Ubuntu.18.04.x86_64.Release/Vitis-AI-Library/overview/test_jpeg_classification resnet_v1_50_tf sample_classification.jpg
mv dump dump_results_debug





~/build/build.Ubuntu.18.04.x86_64.Release/Vitis-AI-Library/overview/test_performance_classification resnet50 test_performance_classification.list -s 30 -t 4


```
