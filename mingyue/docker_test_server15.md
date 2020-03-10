
mobaXterm login 10.176.178.15
```
cd /group/xbjlab/dphi_software/software/workspace/mingyue/docker_test/docker_test_0309/vitis_ai_docker

vi docker_run.sh
```
Add:
>     -e DISPLAY=$DISPLAY \   <br/>
>     -v /tmp/.X11-unix:/tmp/.X11-unix \ <br/>
>     -v $HOME/.Xauthority:$HOME/.Xauthority \ <br/>

#### start docker
```
docker images
./docker_run.sh xdock.xilinx.com/vitis-ai-cpu:1.1.31

export INTERNAL_BUILD=1
sudo cp vart_samples/6E250M/* /usr/lib
/opt/xilinx/xrt/bin/xbutil program -d 0 -p  /usr/lib/dpu.xclbin

export LD_LIBRARY_PATH=/opt/xilinx/xrt/lib:/usr/lib:/usr/lib/x86_64-linux-gnu:/opt/vitis_ai/conda/envs/vitis-ai-tensorflow/lib/


cd /workspace/vart_samples/samples/resnet50
bash build.sh
env XLNX_CHECK_COMMIT_ID_ENABLE=0 ./resnet50 model_dir_for_U50/

cd /workspace/vart_samples/samples/segmentation
bash build.sh
./segmentation ../../videos/traffic.mp4 model_dir_for_U50
```
