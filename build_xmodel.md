
clone source code

```
cd $HOME/d/working/aisw/
git clone ssh://gits@xcdl190260/arch/xnnc4xir
git clone ssh://gits@xcdl190260/arch/xcompiler
git clone ssh://gits@xcdl190260/aisw/unilog
git clone ssh://gits@xcdl190260/aisw/xir
git clone ssh://gits@xcdl190260/arch/target_factory
git clone ssh://gits@xcdl190260/3rd-party/pybind11
```

build xcompiler

```

cd $HOME/d/working/aisw/
cd pybind11
mkdir build
cd build
cmake -DPYBIND11_TEST=off -DPYBIND11_INSTALL=on -DCMAKE_INSTALL_PREFIX=$HOME/.local ..
make
make install

cd  $HOME/d/working/aisw/unilog
./cmake.sh

cd  $HOME/d/working/aisw/xir
git checkout 4b11298e
./cmake.sh --build-python --clean

# http://xcdl190260/arch/ci-xcompiler/tree/6cebef889c95e830565149c8c40648d751766950
cd $HOME/d/working/aisw/target_factory
git checkout 1c8e00e2
./cmake.sh

cd $HOME/d/working/aisw/xcompiler
git checkout 755d452a
./cmake.sh

cd $HOME/d/working/aisw/xnnc4xir
git checkout 5c0d499e
PIP_CONFIG_FILE=~/.config/pip/pip.conf /usr/bin/pip3 install --user "marshmallow>=3.0.0rc5" "tqdm>=4.31.1"  "numpy>=1.16.4" "graphviz>=0.11.1"  "protobuf>=3.6.1"
python3 setup.py install --user

```

```
mkdir -p d/working/aisw/run
cd  d/working/aisw/run
~/.local/bin/xnnc-run --type caffe --layout NCHW --model /group/modelzoo/internal-cooperation-models/caffe/resnet50.baseline9213_ck/fix/acc/deploy_keep_fixed_neuron/deploy.caffemodel --proto /group/modelzoo/internal-cooperation-models/caffe/resnet50.baseline9213_ck/fix/acc/deploy_keep_fixed_neuron/deploy.prototxt --out resnet50.baseline9213_ck_compiled.xmodel
```

```
cd  $HOME/d/working/
git clone gits@xcdl190260:dpdlf/model_zoo_builder
cd model_zoo_builder
ls -l
cp $HOME/d/working/aisw/unilog/cmake.sh  .
./cmake.sh

```

end