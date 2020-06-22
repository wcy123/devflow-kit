
# build xcompile

## install prerequisites.

``` console
% /tools/xgs/bin/sudo apt-get install -y python3-dev python3-setuptools
```

python 3.5 does not work, we need python 3.6 at least.


``` console
% cd $HOME/build
% curl -Lo Python-3.8.3.tgz  https://www.python.org/ftp/python/3.8.3/Python-3.8.3.tgz
% /tools/xgs/bin/sudo apt-get install -y libffi-dev libgdbm-dev libsqlite3-dev libssl-dev zlib1g-dev
% tar xvf Python-3.8.3.tgz
% cd Python-3.8.3
% ./configure --prefix=$HOME/.local --enable-shared --enable-ipv6 LDFLAGS=-Wl,-rpath=$HOME/.lib,--disable-new-dtags --enable-optimizations
% make -j10 && make install
```

install pip

https://pip.pypa.io/en/stable/installing/

``` console
% cd $HOME/build
% curl -Lo PySocks.1.7.0.tar.gz https://github.com/Anorov/PySocks/archive/1.7.0.tar.gz
% tar xvf PySocks.1.7.0.tar.gz
% cd PySocks-1.7.0/
% $HOME/.local/bin/python3 setup.py install
% cd $HOME/build
% curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
% $HOME/.local/bin/python3 get-pip.py
% which pip
% $HOME/.local/bin/pip3 install numpy tqdm graphviz
% $HOME/.local/bin/pip3 install -Iv protobuf==3.4
```

clone source code

``` console
% ls
% mkdir -p /group/xbjlab/dphi_software/software/workspace/$USER/d/working/xcompile
% cd /group/xbjlab/dphi_software/software/workspace/$USER/d/working/xcompile
% git clone ssh://gits@xcdl190260/arch/xnnc4xir
% git clone ssh://gits@xcdl190260/arch/xcompiler
% git clone ssh://gits@xcdl190260/aisw/unilog
% git clone ssh://gits@xcdl190260/aisw/xir
% git clone ssh://gits@xcdl190260/aisw/target_factory
% git clone ssh://gits@xcdl190260/3rd-party/pybind11
# you have to install python3-dev  as below
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

## build xcompiler

```
% cd /group/xbjlab/dphi_software/software/workspace/$USER/d/working/xcompile;
% for i in unilog target_factory ; do (cd $i;bash -e ./cmake.sh --clean); done
% for i in xir ; do (cd $i;bash -e ./cmake.sh --clean --build-python); done
% for i in xcompiler ; do (cd $i;bash -e ./cmake.sh --clean); done
% cd /group/xbjlab/dphi_software/software/workspace/$USER/d/working/xcompile/xnnc4xir
% $HOME/.local/bin/pip3 install -r requirements.txt
% chmod o+rwx .
% $HOME/.local/bin/python3 setup.py install
```

## test it

```
% cd /group/xbjlab/dphi_software/software/workspace/$USER/d/working/xcompile/
% mkdir -p test/resnet50; cd test/resnet50;ls
% scp xcdl190253:/group/modelzoo/internal-cooperation-models/caffe/resnet50.baseline9213_ck/fix/acc/decrypted/deploy.caffemodel .
% scp xcdl190253:/group/modelzoo/internal-cooperation-models/caffe/resnet50.baseline9213_ck/fix/acc/deploy_keep_fixed_neuron/deploy.prototxt .
% ~/.local/bin/xnnc-run --type caffe --layout NCHW --model ./deploy.caffemodel --proto ./deploy.prototxt --out resnet50.baseline9213_ck_compiled.xmodel
% cd /group/xbjlab/dphi_software/software/workspace/$USER/d/working/xcompile/target_factory/targets
% diff -uB DPUCZDX8G_ISA0_B3136_MAX.prototxt DPUCZDX8G_ISA0_B3136_MIN.prototxt
% $HOME/.local/Ubuntu.16.04.x86_64.Debug/bin/xcompiler --help
% $HOME/.local/Ubuntu.16.04.x86_64.Debug/bin/xcompiler -i resnet50.baseline9213_ck_compiled.xmodel -o resnet50.xmodel  -a "DPUv3e B4096"
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
