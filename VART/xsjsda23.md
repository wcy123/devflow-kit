# xsjsda23


``` console
% ssh xsjsda23
% # source /scratch/anaconda2/etc/profile.d/conda.sh # removed!
% . /wrk/xsjhdnobkup1/vincentm/anaconda2/etc/profile.d/conda.sh
% conda create --prefix /scratch/chunywan/conda_envs
% conda activate /scratch/chunywan/conda_envs
% conda install -y opencv
% conda install -y pybind11
% conda install -y glog
% conda install -y protobuf
% conda install -y libprotobuf
% conda install -y json-c
% conda install -y cmake # important ubuntu cmake version is too low
% conda install -y 'libuuid ==2.32.*' -c file://wrk/acceleration/conda-channel/ -c defaults -c omnia -c conda-forge/label/gcc7 -c conda-forge -c pytorch # important, otherwise you see strage linking error.
```


``` console
mkdir -p $HOME/d/working/aisw/
cd  $HOME/d/working/aisw/
git clone ssh://gits@xcdl190260/aisw/unilog
git clone ssh://gits@xcdl190260/aisw/xir
git clone ssh://gits@xcdl190260/aisw/vart
git clone ssh://gits@xcdl190260/aisw/target_factory
git clone ssh://gits@xcdl190260/aisw/Vitis-AI-Library
```


### build `unilog`

``` console
% cd $HOME/d/working/aisw/unilog;
% ./cmake.sh --clean --conda
```

### build `target_factory`

``` console
% cd $HOME/d/working/aisw/target_factory;
% ./cmake.sh --clean --conda
```

### build `xir`

```
% cd $HOME/d/working/aisw/xir
% ./cmake.sh --clean --pack=deb  # no need to --build-python if you don't build xcompiler
```

### build `vart`

``` console
# important, we need to hack by add `link_directories("$ENV{CONDA_PREFIX}/lib")` at the beginning of CMakeLists.
% cd $HOME/d/working/aisw/vart
% ./cmake.sh --cmake-options=-DENABLE_DPU_RUNNER=ON --cmake-options=-DENABLE_SIM_RUNNER=OFF --cmake-options=-DENABLE_CPU_RUNNER=OFF  --clean --build-python --conda
```


### run dpu test

``` console
%  export LD_LIBRARY_PATH=$HOME/.local/Ubuntu.18.04.x86_64.Debug/lib:/usr/local/lib:$CONDA_PREFIX/lib:/opt/xilinx/xrt/lib
% env XLNX_ENALBE_HBM_TXT=1 ~/build/build.Ubuntu.18.04.x86_64.Debug/vart/dpu-runner/test/test_dpu_runner  /usr/share/vitis_ai_library/models/resnet50/resnet50.xmodel k_0 /usr/share/vitis_ai_library/models/resnet50/resnet50.xmodel 1 1

```
