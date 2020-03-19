
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
cd $HOME/d/working/aisw/
git clone ssh://gits@xcdl190260/vitis/Vitis-AI
cd Vitis-AI
git pull upstream master
git submodule deinit --all -f
git submodule update --init  --depth 1 xnnc4xir xcompiler target_factory unilog  XIR
```

build xcompiler

```
cd  $HOME/d/working/aisw/Vitis-AI/unilog
# ./cmake.sh --cmake-options=-DCMAKE_PREFIX_PATH=$CONDA_PREFIX --clean  # TODO consider to make it default options

cd  $HOME/d/working/aisw/Vitis-AI/XIR
./cmake.sh --build-python --cmake-options=-DPYTHON_EXECUTABLE=$CONDA_PYTHON_EXE --cmake-options=-DCMAKE_PREFIX_PATH=$CONDA_PREFIX --clean

# http://xcdl190260/arch/ci-xcompiler/tree/6cebef889c95e830565149c8c40648d751766950
cd $HOME/d/working/aisw/Vitis-AI/target_factory
./cmake.sh --cmake-options=-DCMAKE_PREFIX_PATH=$CONDA_PREFIX --clean

cd $HOME/d/working/aisw/Vitis-AI/xcompiler
./cmake.sh --cmake-options=-DCMAKE_PREFIX_PATH=$CONDA_PREFIX --clean

cd $HOME/d/working/aisw/xnnc4xir
$CONDA_PYTHON_EXE setup.py install

```

```
mkdir -p $HOME/d/working/aisw/run
cd  $HOME/d/working/aisw/run
export LD_LIBRARY_PATH=$CONDA_PREFIX/lib:/home/chunywan/.local/Ubuntu.18.04.x86_64.Debug/lib
model=/group/modelzoo/vmss_models/Tiny_yolov3_A004/quantize_results/deploy.caffemodel
proto=/group/modelzoo/vmss_models/Tiny_yolov3_A004/quantize_results/deploy.prototxt
# we must convert for a wired reason
ssh xcdl190091
cd  $HOME/d/working/
git clone gits@xcdl190260:vitis/vitis-ai-docker.git
cd $HOME/d/working/vitis-ai-docker
mkdir tinyyolov3; cd tinyyolov3
cp -av /group/dphi_software/software/workspace/max/Tiny_yolov3_A004/quantize_results /group/dphi_software/software/workspace/chunywan/d/working/vitis-ai-docker/tinyyolov3
cd $HOME/d/working/vitis-ai-docker
./docker_run.sh xdock:5000/vitis-ai-cpu:1.1.50
cd /workspace/tinyyolov3/quantize_results ; ls -l
env DECENT_DEBUG=1  /opt/vitis_ai/compression/vai_q_caffe deploy -keep_fixed_neuron -model quantize_train_test.prototxt -weights quantize_train_test.caffemodel
exit
cd $HOME/d/working/vitis-ai-docker/tinyyolov3/
ls quantize_results -l
model=$HOME/d/working/vitis-ai-docker/tinyyolov3/quantize_results/deploy.caffemodel
proto=$HOME/d/working/vitis-ai-docker/tinyyolov3/quantize_results/quantize_results/deploy.prototxt
export LD_LIBRARY_PATH=$CONDA_PREFIX/lib:/home/chunywan/.local/Ubuntu.18.04.x86_64.Debug/lib
~/.local/bin/xnnc-run --type caffe --layout NCHW --model $model --proto $proto --out tiny_yolov3.xnnc4xir.xmodel
~/.local/Ubuntu.18.04.x86_64.Debug/bin/xcompiler -i tiny_yolov3.xnnc4xir.xmodel -o tiny_yolov3.xmodel  -a "DPUv3e B4096"
/home/chunywan/build/build.Ubuntu.18.04.x86_64.Debug/model_zoo_builder/xcompiler/xmodel_info $HOME/d/working/vitis-ai-docker/tinyyolov3/tiny_yolov3.xmodel
rsync --exclude decent_debug  -av -e 'ssh -p 10115'  $HOME/d/working/vitis-ai-docker/tinyyolov3/tiny_yolov3.xmodel localhost:/group/xbjlab/dphi_software/software/workspace/chunywan/d/working/vmss/VMSS_DPU_Plugins/models/tinyyolov3/
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
