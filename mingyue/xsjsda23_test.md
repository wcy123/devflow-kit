## reproduce issue of double free
```
ssh xsjsda23
. /wrk/xsjhdnobkup1/vincentm/anaconda2/etc/profile.d/conda.sh
conda --version
conda activate /wrk/xsjhdnobkup1/vincentm/anaconda2/envs/vart-sandbox

cd /proj/xsjhdstaff6/mingyue/d/working/aisw/cloud_test
g++ -std=c++17 -g -O0 -ggdb -o test_dpu_runner /wrk/xsjhdnobkup1/vincentm/Projects/ML/vart-sandbox/vart/dpu-runner/test/test_dpu_runner.cpp -I${CONDA_PREFIX}/include -L${CONDA_PREFIX}/lib -lvart-dpu-runner -lvart-buffer-object -lvart-runner -lvart-elf-util -lvart-mem-manager -lvart-util -lvart-xclbinutil -lglog
export LD_LIBRARY_PATH=${CONDA_PREFIX}/lib:$LD_LIBRARY_PATH
env DEBUG_DPU_RUNNER=1 XLNX_ENABLE_DUMP=1 XLNX_SHOW_DPU_COUNTER=1 XLNX_DPU_CORE_ID=0 DEBUG_XRT_DEVICE_HANDLE=0 XLNX_ENABLE_DEVICES=0 ./test_dpu_runner resnet_v1_50_tf/resnet_v1_50_tf.xmodel k_0 resnet_v1_50_tf/resnet_v1_50_tf.xmodel 1 1

```
ok, issue reproduced

## check vart & xir version
```
cd /proj/xsjhdstaff6/mingyue/d/working/aisw/cloud_test
g++ -fpermissive -o opendl opendl.c -ldl

./opendl /wrk/xsjhdnobkup1/vincentm/anaconda2/envs/vart-sandbox/lib/libvart-dpu-runner.so
./opendl /wrk/xsjhdnobkup1/vincentm/anaconda2/envs/vart-sandbox/lib/libxir.so
```
(vart-sandbox) mingyue@xsjsda23:cloud_test% ./opendl /wrk/xsjhdnobkup1/vincentm/anaconda2/envs/vart-sandbox/lib/libvart-dpu-runner.so<br/>
Xilinx vart Version: vart- 2020-07-20-23:40:06<br/>
(vart-sandbox) mingyue@xsjsda23:cloud_test% ./opendl /wrk/xsjhdnobkup1/vincentm/anaconda2/envs/vart-sandbox/lib/libxir.so<br/><br/>
Xilinx xir Version: xir- 2020-07-20-23:31:42<br/>

The vart&xir version(git commitID) is not displayed here, it is impossible to determine whether the version is correct<br/><br/>

so , I will compile locally using source code, libxir*,libunilog*,libvart* will be reinstalled to /wrk/xsjhdnobkup1/vincentm/anaconda2/envs/vart-sandbox/lib/<br/>
```
git clone ssh://gits@xcdl190260/aisw/unilog
git clone ssh://gits@xcdl190260/aisw/xir
git clone ssh://gits@xcdl190260/aisw/vart
git clone ssh://gits@xcdl190260/aisw/target_factory
git clone ssh://gits@xcdl190260/aisw/Vitis-AI-Library

cd /proj/xsjhdstaff6/mingyue/d/working/aisw
cd unilog
./cmake.sh --clean --conda

cd ../xir
./cmake.sh --clean --conda

cd ../target_factory
./cmake.sh --clean --conda

cd ../vart
./cmake.sh --cmake-options=-DENABLE_DPU_RUNNER=ON --cmake-options=-DENABLE_SIM_RUNNER=OFF --cmake-options=-DENABLE_CPU_RUNNER=OFF  --clean  --conda

```

```
export
cd /proj/xsjhdstaff6/mingyue/d/working/aisw/cloud_test
g++ -fpermissive -o opendl opendl.c -ldl

export LD_LIBRARY_PATH=~/.local/Ubuntu.18.04.x86_64.Debug/lib:$LD_LIBRARY_PATH
./opendl ~/.local/Ubuntu.18.04.x86_64.Debug/lib/libvart-dpu-runner.so
./opendl ~/.local/Ubuntu.18.04.x86_64.Debug/lib/libxir.so
```
(vart-sandbox) mingyue@xsjsda23:cloud_test% ./opendl ~/.local/Ubuntu.18.04.x86_64.Debug/lib/libvart-dpu-runner.so<br/>
Xilinx vart Version: vart-a7c2c728f661c6b68c8ba50de344feb574f36265 2020-07-21-06:28:11<br/>
(vart-sandbox) mingyue@xsjsda23:cloud_test% ./opendl ~/.local/Ubuntu.18.04.x86_64.Debug/lib/libxir.so<br/>
Xilinx xir Version: xir-7c53644ff94dbb7a871cc970469261637e2a34c9 2020-07-21-06:23:16<br/>

but:
```
./opendl /wrk/xsjhdnobkup1/vincentm/anaconda2/envs/vart-sandbox/lib/libvart-dpu-runner.so
./opendl /wrk/xsjhdnobkup1/vincentm/anaconda2/envs/vart-sandbox/lib/libxir.so
```

and during compilation, some binary files under the /wrk/xsjhdnobkup1/vincentm/anaconda2/envs/vart-sandbox/lib/ reinstalled.<br/>
but :
```
md5sum /wrk/xsjhdnobkup1/vincentm/anaconda2/envs/vart-sandbox/lib/libvart-dpu-runner.so
md5sum ~/.local/Ubuntu.18.04.x86_64.Debug/lib/libvart-dpu-runner.so
```
compiler log , a small fragment:<br/>
-- Set runtime path of "/home/mingyue/.local/Ubuntu.18.04.x86_64.Debug/lib/libvart-dpu-runner.so.1.2.0" to "/wrk/xsjhdnobkup1/vincentm/anaconda2/envs/vart-sandbox/lib" <br/>
I don't understand what happened.<br/>
<br/>

Modify LD_LIBRARY_PATH, binary files under runtime link ~/.local/Ubuntu.18.04.x86_64.Debug/lib/*<br/>
```
export LD_LIBRARY_PATH=~/.local/Ubuntu.18.04.x86_64.Debug/lib:$LD_LIBRARY_PATH
g++ -std=c++17 -g -O0 -ggdb -o test_dpu_runner /wrk/xsjhdnobkup1/vincentm/Projects/ML/vart-sandbox/vart/dpu-runner/test/test_dpu_runner.cpp -I${CONDA_PREFIX}/include -L${CONDA_PREFIX}/lib -lvart-dpu-runner -lvart-buffer-object -lvart-runner -lvart-elf-util -lvart-mem-manager -lvart-util -lvart-xclbinutil -lglog


env DEBUG_DPU_RUNNER=1 XLNX_ENABLE_DUMP=1 XLNX_SHOW_DPU_COUNTER=1 XLNX_DPU_CORE_ID=0 DEBUG_XRT_DEVICE_HANDLE=0 XLNX_ENABLE_DEVICES=0 ./test_dpu_runner resnet_v1_50_tf/resnet_v1_50_tf.xmodel k_0 resnet_v1_50_tf/resnet_v1_50_tf.xmodel 1 1

```
double free issue no recurrence.
