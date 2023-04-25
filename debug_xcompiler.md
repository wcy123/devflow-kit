# debug xcompiler

``` console
% cd /workspace/aisw/xcompiler
% ./cmake.sh --clean
% ../Vitis-AI-Library/cmake.sh --project $(basename $PWD)
```


``` console
% mkdir -p ~/.local/debug_xcompiler
% cd  ~/.local/debug_xcompiler
% ls -l /workspace/aisw/onnx_models/quantized_resnet50
% ls -l /workspace/aisw/onnx/models/pytorch/quantized_resnet50/ResNet_int.xmodel
% cp -av /workspace/aisw/onnx/models/pytorch/quantized_resnet50/ResNet_int.xmodel ~/.local/debug_xcompiler
```

``` console
% export  LD_LIBRARY_PATH=$HOME/.local/Ubuntu.20.04.x86_64.Debug/lib
% PATH=$PATH:$HOME/.local/Ubuntu.20.04.x86_64.Debug/bin
% which xcompiler;
% cd  ~/.local/debug_xcompiler
% xcompiler -h
% xcompiler -i ResNet_int.xmodel -o ResNet_compiled.xmodel -t DPUCVDX8G_ISA3_C32B3 -d
```
