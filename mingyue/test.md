ssh mingyue@xcosda14
mkdir $HOME/d/working/mingyue/xcompiler
cd $HOME/d/working/mingyue/xcompiler
ls
git clone ssh://gits@xcdl190260/arch/xnnc4xir
git clone ssh://gits@xcdl190260/arch/xcompiler
git clone ssh://gits@xcdl190260/aisw/unilog
git clone ssh://gits@xcdl190260/aisw/xir
git clone ssh://gits@xcdl190260/arch/target_factory
git clone ssh://gits@xcdl190260/3rd-party/pybind11

#build pybind11
cd pybind11
mkdir build
cd build
cmake -DPYBIND11_TEST=off -DPYBIND11_INSTALL=on -DCMAKE_INSTALL_PREFIX=$HOME/.local/xcompiler.Debug ..
make
make install

#build unilog
cd $HOME/d/working/mingyue/xcompiler/unilog
./cmake.sh --build-dir=$HOME/build/build.xcompiler.Debug/unilog --install-prefix=$HOME/.local/xcompiler.Debug

#build xir
cd $HOME/d/working/mingyue/xcompiler/xir
git checkout 4b11298e
./cmake.sh --build-python --clean --build-dir=$HOME/build/build.xcompiler.Debug/xir --install-prefix=$HOME/.local/xcompiler.Debug

##




end
