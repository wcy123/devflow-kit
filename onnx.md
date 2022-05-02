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
%
```
