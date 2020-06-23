
## install anaconda

I found the most easy way to setup xcompiler environment is to use
anaconda. please take to look at [install anaconda](anaconda_env.md)
otherwise, you will run into errors, like, "No Python.h found", etc.


##  install dependencies

```
conda install -y glog libprotobuf protobuf pybind11 cmake
conda install -y 'marshmallow' 'tqdm>=4.31.1' 'numpy>=1.16.4' 'python-graphviz'
```

note: python-graphviz version is 0.8.3, which is lower than than the required version 0.11.1.
marshmallow is 3.0.0b8, not as same as 3.0.0rc5.

I will try to install them via pip.
[How to install python, pip, pypi packages in XCD](https://confluence.xilinx.com/display/XCD/How+to+install+python%2C+pip%2C+pypi+packages+in+XCD)



```
which python # make sure python is /wrk/xcdhdnobkup1/chunywan/local/anaconda3/bin/python, provided by anaconda
python -m pip install -r $HOME/d/working/aisw/xnnc4xir/requirements.txt
```

clone source code

```
% ls
% mkdir -p /group/xbjlab/dphi_software/software/workspace/$USER/d/working/xcompile
% cd /group/xbjlab/dphi_software/software/workspace/$USER/d/working/xcompile
% git clone ssh://gits@xcdl190260/arch/xnnc4xir
% git clone ssh://gits@xcdl190260/arch/xcompiler
% git clone ssh://gits@xcdl190260/aisw/unilog
% git clone ssh://gits@xcdl190260/aisw/xir
% git clone ssh://gits@xcdl190260/arch/target_factory
% git clone ssh://gits@xcdl190260/3rd-party/pybind11
# you have to install python3-dev  as below
# /tools/xgs/bin/sudo apt-get install -y python3-dev
```

## pybind11

``` console
% cd /group/xbjlab/dphi_software/software/workspace/$USER/d/working/xcompile/pybind11
% mkdir build;cd build;
% cmake -DCMAKE_INSTALL_PREFIX=$HOME/.local -DPYBIND11_TEST=off -DPYBIND11_INSTALL=on ..
% cmake  -DPYBIND11_TEST=off -DPYBIND11_INSTALL=on ..
% make
% chmod o+rwx .
% make install
```

build xcompiler

```
cd  $HOME/d/working/aisw/unilog
git checkout br-conda-build
./cmake.sh --cmake-options=-DCMAKE_PREFIX_PATH=$CONDA_PREFIX --clean  # TODO consider to make it default options

cd  $HOME/d/working/aisw/xir
git checkout br-conda-build
./cmake.sh --build-python --cmake-options=-DPYTHON_EXECUTABLE=$CONDA_PYTHON_EXE --cmake-options=-DCMAKE_PREFIX_PATH=$CONDA_PREFIX --clean

# http://xcdl190260/arch/ci-xcompiler/tree/6cebef889c95e830565149c8c40648d751766950
cd $HOME/d/working/aisw/target_factory
git fetch --all
git checkout br-conda-build
./cmake.sh --cmake-options=-DCMAKE_PREFIX_PATH=$CONDA_PREFIX --clean

cd $HOME/d/working/aisw/xcompiler
git fetch --all
git checkout br-conda-build
./cmake.sh --cmake-options=-DCMAKE_PREFIX_PATH=$CONDA_PREFIX --clean

cd $HOME/d/working/aisw/xnnc4xir
git fetch --all
git checkout br-conda-build
$CONDA_PYTHON_EXE setup.py install

```

```
mkdir -p $HOME/d/working/aisw/run
cd  $HOME/d/working/aisw/run
export LD_LIBRARY_PATH=$CONDA_PREFIX/lib:/home/chunywan/.local/Ubuntu.18.04.x86_64.Debug/lib
~/.local/bin/xnnc-run --type caffe --layout NCHW --model /group/modelzoo/internal-cooperation-models/caffe/resnet50.baseline9213_ck/fix/acc/decrypted/deploy.caffemodel --proto /group/modelzoo/internal-cooperation-models/caffe/resnet50.baseline9213_ck/fix/acc/deploy_keep_fixed_neuron/deploy.prototxt --out resnet50.baseline9213_ck_compiled.xmodel
~/.local/Ubuntu.18.04.x86_64.Debug/bin/xcompiler -i resnet50.baseline9213_ck_compiled.xmodel -o resnet50.xmodel  -a "DPUv3e B4096"
```

```
cd  $HOME/d/working/
git clone gits@xcdl190260:dpdlf/model_zoo_builder
cd model_zoo_builder
ls -l
cp $HOME/d/working/aisw/unilog/cmake.sh  .
./cmake.sh

```


build the model zoo

```
mkdir -p d/working/aisw
git clone gits@xcdl190260:dpdlf/model_zoo_builder
git checkout br-xcompiler
./cmake.sh --pack=tgz --clean
```

to extract the models to docker

```
tar -zxvf xilinx_model_zoo-1.0.0-Linux.tar.gz --strip-components=1  -C /tmp/tmp/usr/share/vitis_ai_library/.models/resnet50_acc/meta.json
```
end
