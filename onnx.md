# onnx


## checkout the source code

``` console
% cd /workspace/aisw/
% set_proxy http://localhost:9181 # if XCD
% git clone https://github.com/onnx/onnx.git
% cd /workspace/aisw/onnx
% git rev-parse HEAD
 00738d2032ca0a39d9124b02085a90adda96d018
```


## build

```
% CMAKE_ARGS="-DONNX_USE_PROTOBUF_SHARED_LIBS=ON"
% CMAKE_ARGS+=" -DCMAKE_EXPORT_COMPILE_COMMANDS=ON"
% CMAKE_ARGS+=" -DCMAKE_PREFIX_PATH=$HOME/.local/Ubuntu.20.04.x86_64.Debug"
% CMAKE_ARGS+=" -DCMAKE_INSTALL_PREFIX=$HOME/.local/Ubuntu.20.04.x86_64.Debug"
% CMAKE_ARGS+=" -DCMAKE_BUILD_TYPE=Debug"
% echo $CMAKE_ARGS
% mkdir -p  $HOME/build/onnx; cd $HOME/build/onnx; ls -l; pwd
% cmake $CMAKE_ARGS /workspace/aisw/onnx
% cmake --build . -j10
% cmake --install .
% cd /workspace/aisw/onnx
% pip install --proxy=http://localhost:9181 pytest-runner --user
% pip install --proxy=http://localhost:9181  --user -e .
```


## read source code

``` console
% cd /workspace/aisw/onnx
% cp $HOME/build/onnx/compile_commands.json  /workspace/aisw/onnx/compile_commands.json
% emacs -nw compile_commands.json
```


## tutorial 1.

``` console
% dir=/workspace/aisw/onnx/models/pytorch/super_reslution/
% mkdir -p $dir; cd $dir; ls -l;pwd
% wget https://raw.githubusercontent.com/pytorch/examples/main/super_resolution/model.py
% wget https://s3.amazonaws.com/pytorch/test_data/export/superres_epoch100-44c6958e.pth
% python eval.py
% pip3 install --proxy=http://localhost:9181 torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu --user
% env http_proxy= wget http://xcdl190260/wangchunye/work_log/raw/master/onnx/tutorials/pytorch/super_resulution/model.py
% python model.py
% ls -l super_resolution.onnx
% protoc --decode=onnx.ModelProto --proto_path /home/chunywan/build/onnx/onnx/ onnx-ml.proto < super_resolution.onnx | less -XR
```

## install onnx runtime

``` console
% pip --proxy http://localhost:9181 install onnxruntime --user
```


``` console
% dir=/workspace/aisw/onnx/models/pytorch/super_reslution/
% mkdir -p $dir; cd $dir; ls -l;pwd
% wget https://pytorch.org/tutorials/_images/cat_224x224.jpg
% env http_proxy= wget http://xcdl190260/wangchunye/work_log/raw/master/onnx/tutorials/pytorch/super_resulution/eval.py
% python eval.py
```

## install cmake 3.18

``` console
% cd /opt
% sudo mkdir -p /opt/cmake;
% sudo chmod 777 /opt/cmake;
% cd  /opt/cmake
% wget https://github.com/Kitware/CMake/releases/download/v3.23.1/cmake-3.23.1.tar.gz
% tar xvf cmake-3.23.1.tar.gz
% cd cmake-3.23.1
% ./configure
% make -j20
% sudo make install
```


## build  onnx runtime from source code.

``` console
% dir=/workspace/aisw/
% mkdir -p $dir; cd $dir; ls -l;pwd
% git clone --recursive https://github.com/Microsoft/onnxruntime
% git rev-parse HEAD
49d7050b88338dd57839159aa4ce8fb0c199b064
% cd onnxruntime
% mkdir -p  $HOME/build/onnxruntime
% cd /workspace/aisw/onnxruntime
% ./build.sh --build_dir /home/build/onnxruntime --config Debug --build_shared_lib --parallel --build_wheel --skip_tests \
   --cmake_extra_defines "CMAKE_EXPORT_COMPILE_COMMANDS=ON" \
   --cmake_extra_defines "CMAKE_PREFIX_PATH=$HOME/.local/Ubuntu.20.04.x86_64.Debug" \
   --cmake_extra_defines "CMAKE_INSTALL_PREFIX=$HOME/.local/Ubuntu.20.04.x86_64.Debug" \
   --cmake_extra_defines "onnxruntime_BUILD_SHARED_LIB=ON" \
   --cmake_extra_defines "onnxruntime_ENABLE_PYTHON=ON"
   2>&1 | tee build.log
% pip install build/Linux/Debug/dist/onnxruntime-1.12.0-cp38-cp38-linux_x86_64.whl --user
```


hack build.py

```
cd /workspace/aisw/onnxruntime; git submodule sync --recursive
cd /workspace/aisw/onnxruntime; git submodule update --init --recursive
cd /workspace/aisw/onnxruntime/build/Linux/Debug; /usr/local/bin/cmake /workspace/aisw/onnxruntime/cmake -Donnxruntime_RUN_ONNX_TESTS=OFF -Donnxruntime_BUILD_WINML_TESTS=ON -Donnxruntime_GENERATE_TEST_REPORTS=ON -DPython_EXECUTABLE=/usr/bin/python3 -DPYTHON_EXECUTABLE=/usr/bin/python3 -Donnxruntime_ROCM_VERSION= -Donnxruntime_USE_MIMALLOC=OFF -Donnxruntime_ENABLE_PYTHON=ON -Donnxruntime_BUILD_CSHARP=OFF -Donnxruntime_BUILD_JAVA=OFF -Donnxruntime_BUILD_NODEJS=OFF -Donnxruntime_BUILD_OBJC=OFF -Donnxruntime_BUILD_SHARED_LIB=ON -Donnxruntime_BUILD_APPLE_FRAMEWORK=OFF -Donnxruntime_USE_DNNL=OFF -Donnxruntime_DNNL_GPU_RUNTIME= -Donnxruntime_DNNL_OPENCL_ROOT= -Donnxruntime_USE_NNAPI_BUILTIN=OFF -Donnxruntime_USE_RKNPU=OFF -Donnxruntime_USE_OPENMP=OFF -Donnxruntime_USE_NUPHAR_TVM=OFF -Donnxruntime_USE_LLVM=OFF -Donnxruntime_ENABLE_MICROSOFT_INTERNAL=OFF -Donnxruntime_USE_VITISAI=OFF -Donnxruntime_USE_NUPHAR=OFF -Donnxruntime_USE_TENSORRT=OFF -Donnxruntime_TENSORRT_HOME= -Donnxruntime_USE_TVM=OFF -Donnxruntime_TVM_CUDA_RUNTIME=OFF -Donnxruntime_USE_MIGRAPHX=OFF -Donnxruntime_MIGRAPHX_HOME= -Donnxruntime_CROSS_COMPILING=OFF -Donnxruntime_DISABLE_CONTRIB_OPS=OFF -Donnxruntime_DISABLE_ML_OPS=OFF -Donnxruntime_DISABLE_RTTI=OFF -Donnxruntime_DISABLE_EXCEPTIONS=OFF -Donnxruntime_MINIMAL_BUILD=OFF -Donnxruntime_EXTENDED_MINIMAL_BUILD=OFF -Donnxruntime_MINIMAL_BUILD_CUSTOM_OPS=OFF -Donnxruntime_REDUCED_OPS_BUILD=OFF -Donnxruntime_ENABLE_LANGUAGE_INTEROP_OPS=OFF -Donnxruntime_USE_DML=OFF -Donnxruntime_USE_WINML=OFF -Donnxruntime_BUILD_MS_EXPERIMENTAL_OPS=OFF -Donnxruntime_USE_TELEMETRY=OFF -Donnxruntime_ENABLE_LTO=OFF -Donnxruntime_ENABLE_TRANSFORMERS_TOOL_TEST=OFF -Donnxruntime_USE_ACL=OFF -Donnxruntime_USE_ACL_1902=OFF -Donnxruntime_USE_ACL_1905=OFF -Donnxruntime_USE_ACL_1908=OFF -Donnxruntime_USE_ACL_2002=OFF -Donnxruntime_USE_ARMNN=OFF -Donnxruntime_ARMNN_RELU_USE_CPU=ON -Donnxruntime_ARMNN_BN_USE_CPU=ON -Donnxruntime_ENABLE_NVTX_PROFILE=OFF -Donnxruntime_ENABLE_TRAINING=OFF -Donnxruntime_ENABLE_TRAINING_OPS=OFF -Donnxruntime_ENABLE_TRAINING_TORCH_INTEROP=OFF -Donnxruntime_ENABLE_CPU_FP16_OPS=OFF -Donnxruntime_USE_NCCL=ON -Donnxruntime_BUILD_BENCHMARKS=OFF -Donnxruntime_USE_ROCM=OFF -Donnxruntime_ROCM_HOME= -DOnnxruntime_GCOV_COVERAGE=OFF -Donnxruntime_USE_MPI=ON -Donnxruntime_ENABLE_MEMORY_PROFILE=OFF -Donnxruntime_ENABLE_CUDA_LINE_NUMBER_INFO=OFF -Donnxruntime_BUILD_WEBASSEMBLY=OFF -Donnxruntime_BUILD_WEBASSEMBLY_STATIC_LIB=OFF -Donnxruntime_ENABLE_WEBASSEMBLY_SIMD=OFF -Donnxruntime_ENABLE_WEBASSEMBLY_EXCEPTION_CATCHING=ON -Donnxruntime_ENABLE_WEBASSEMBLY_EXCEPTION_THROWING=OFF -Donnxruntime_ENABLE_WEBASSEMBLY_THREADS=OFF -Donnxruntime_ENABLE_WEBASSEMBLY_DEBUG_INFO=OFF -Donnxruntime_ENABLE_WEBASSEMBLY_PROFILING=OFF -Donnxruntime_ENABLE_EAGER_MODE=OFF -Donnxruntime_ENABLE_EXTERNAL_CUSTOM_OP_SCHEMAS=OFF -Donnxruntime_NVCC_THREADS=0 -Donnxruntime_ENABLE_CUDA_PROFILING=OFF -DCMAKE_EXPORT_COMPILE_COMMANDS=ON -DCMAKE_PREFIX_PATH=/home/chunywan/.local/Ubuntu.20.04.x86_64.Debug -DCMAKE_INSTALL_PREFIX=/home/chunywan/.local/Ubuntu.20.04.x86_64.Debug -Donnxruntime_DEV_MODE=ON -Donnxruntime_PYBIND_EXPORT_OPSCHEMA=OFF -Donnxruntime_ENABLE_MEMLEAK_CHECKER=ON -DCMAKE_BUILD_TYPE=Debug
cd /workspace/aisw/onnxruntime/build/Linux/Debug; /usr/local/bin/cmake --build /workspace/aisw/onnxruntime/build/Linux/Debug --config Debug -- -j56
cd /workspace/aisw/onnxruntime/build/Linux/Debug; /usr/bin/python3 /workspace/aisw/onnxruntime/setup.py bdist_wheel
```


## tf model

https://github.com/onnx/tensorflow-onnx/blob/main/tutorials/keras-resnet50.ipynb


``` console
% dir=/workspace/aisw/onnx/models/tensorflow/resnet
% mkdir -p $dir; cd $dir; ls -l;pwd
% wget -q https://github.com/onnx/tensorflow-onnx/raw/master/tests/ade20k.jpg
%l
```


## install absl

``` console
% cd /home/build
% wget https://github.com/abseil/abseil-cpp/archive/refs/tags/20211102.0.zip
% unzip 20211102.0.zip
% cd abseil-cpp-20211102.0
% cmake -S /home/build/abseil-cpp-20211102.0 -B /home/build/build/abseil-cpp -DCMAKE_PREFIX_PATH=/installation/dir -DCMAKE_INSTALL_PREFIX=$HOME/.local/Ubuntu.20.04.x86_64.Debug -DABSL_ENABLE_INSTALL=ON -DABSL_USE_EXTERNAL_GOOGLETEST=ON -DABSL_FIND_GOOGLETEST=ON
% cmake --build /home/build/build/abseil-cpp -j $(nproc)
% cmake --install /home/build/build/abseil-cpp

```
