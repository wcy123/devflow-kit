## login xbjlabdpwstn11
```
#xbj-pvajmp11
ssh -L 0.0.0.0:10111:localhost:22 mingyue@xbjlabdpwstn11

ssh -p 10111 mingyue@xbj-pvapjmp11
```

### clone libs & compile
```
mkdir -p ~/d/working
cd d/working

git clone gits@xbjlabdpsvr07:aisw/unilog
git clone gits@xbjlabdpsvr07:aisw/xir
git clone gits@xbjlabdpsvr07:aisw/vart
git clone gits@xbjlabdpsvr07:aisw/Vitis-AI-Library

cd unilog
git checkout d460181c3e6c46b28e7131acdc09fbcf221d1c7f
./cmake.sh --type=release

cd ../xir
git checkout 04feb9312d88be98b81124679ee9abe1e0ef8856
./cmake.sh --type=release

cd ../vart
git checkout fd423cc9b28a0d15297e62a6d92fe550c80e6067
./cmake.sh --cmake-options=-DENABLE_DPU_RUNNER=ON --cmake-options=-DENABLE_SIM_RUNNER=OFF --cmake-options=-DENABLE_CPU_RUNNER=OFF --type=release

cd ../Vitis-AI-Library
git checkout cadf320410b11b5477ec60ae0cdd2372a4f3bda7
./cmake.sh --cmake-options='-DENABLE_OVERVIEW=ON' --type=release
```
## perpare models/images/videos
```
---
#xsjsda153
cd /wrk/xsjhdnobkup6/mingyue/docker_test_0413/Vitis-AI

scp -P 10111 vitis_ai_library_r1.1_images.tar.gz vitis_ai_library_r1.1_video.tar.gz  vitis_ai_runtime_r1.1_image_video.tar.gz xilinx_model_zoo-1.1.0-Linux.deb mingyue@xbj-pvapjmp11:/group/xbjlab/dphi_software/software/workspace/mingyue/r1.1/
---

cd /group/xbjlab/dphi_software/software/workspace/mingyue/r1.1/
dpkg -X xilinx_model_zoo-1.1.0-Linux.deb models
mv models/usr/share/vitis_ai_library ./
cd vitis_ai_library
tar -zxvf ../vitis_ai_library_r1.1_video.tar.gz
tar -zxvf ../vitis_ai_library_r1.1_images.tar.gz



```
