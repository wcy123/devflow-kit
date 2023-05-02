'# install clangd

## download

https://releases.llvm.org/download.html

```
mkdir ~/build/llvm
cd ~/build/llvm
ls -l
curl -sLo llvm-10.0.0.src.tar.xz https://github.com/llvm/llvm-project/releases/download/llvmorg-10.0.0/llvm-10.0.0.src.tar.xz
curl -sLo clang-10.0.0.src.tar.xz https://github.com/llvm/llvm-project/releases/download/llvmorg-10.0.0/clang-10.0.0.src.tar.xz
curl -sLo compiler-rt-10.0.0.src.tar.xz https://github.com/llvm/llvm-project/releases/download/llvmorg-10.0.0/compiler-rt-10.0.0.src.tar.xz
# curl -sLo libcxx-10.0.0.src.tar.xz https://github.com/llvm/llvm-project/releases/download/llvmorg-10.0.0/libcxx-10.0.0.src.tar.xz
# curl -sLo libcxxabi-10.0.0.src.tar.xz https://github.com/llvm/llvm-project/releases/download/llvmorg-10.0.0/libcxxabi-10.0.0.src.tar.xz
# curl -sLo lldb-10.0.0.src.tar.xz https://github.com/llvm/llvm-project/releases/download/llvmorg-10.0.0/lldb-10.0.0.src.tar.xz
# curl -sLo clang-tools-extra-10.0.0.src.tar.xz https://github.com/llvm/llvm-project/releases/download/llvmorg-10.0.0/clang-tools-extra-10.0.0.src.tar.xz

curl -sLo lld-10.0.0.src.tar.xz https://github.com/llvm/llvm-project/releases/download/llvmorg-10.0.0/lld-10.0.0.src.tar.xz
```


## extract, build and install

https://shaharmike.com/cpp/build-clang/

```
cd  ~/build/llvm
pwd
tar xf llvm-10.0.0.src.tar.xz
tar xf clang-10.0.0.src.tar.xz -C llvm-10.0.0.src/tools/
mv ./clang-10.0.0.src/tools/clang-10.0.0.src llvm-10.0.0.src/projects/clang-10.0.0.src/tools/clang
tar xf clang-tools-extra-10.0.0.src.tar.xz -C llvm-10.0.0.src/tools/clang/tools
mv llvm-10.0.0.src/tools/clang/tools/clang-tools-extra-10.0.0 llvm-10.0.0.src/tools/clang/tools/clang-tools-extra
tar xf compiler-rt-10.0.0.src.tar.xz -C llvm-10.0.0.src/projects/
tar xf lld-10.0.0.src.tar.xz -C   llvm-10.0.0.src/projects/
mkdir build_out
cd build_out
source /opt/rh/devtoolset-6/enable
cmake -DCMAKE_INSTALL_PREFIX=$HOME/.local -DCMAKE_BUILD_TYPE=MINSIZEREL -DBUILD_SHARED_LIBS=on  ../llvm-10.0.0.src 2>&1 | tee config.log
env LANG=C make VERBOSE=0  -j20 2>&1 | tee build.log && make install
make install
```

## setup project

### install `bear`

```
cd ~/build
git clone https://github.com/rizsotto/Bear.git
cd Bear
source /opt/rh/devtoolset-6/enable
cmake -DCMAKE_INSTALL_PREFIX=$HOME/.local ; make all -j20 && make install
```

###  setup project for `Butler`

```
cd ~/d/working/XIP/Butler/src
make clean
bear make DEBUG=1
```

## `eglot`


ls -l ../llvm-10.0.0.src/tools/clang/tools/ | grep clang-tools-extra
# it maybe a bug, we have to modify ../llvm-10.0.0.src/tools/clang/tools/CMakeLists.txt
# change add_llvm_external_project(clang-tools-extra extra)
# into add_llvm_external_project(clang-tools-extra)
##
ls -l tools/clang/tools/ | grep clang-tools-extra # make sure it is there.
emacs config.log
env LANG=C make VERBOSE=0  -j20 2>&1 | tee build.log && make install
emacs build.log
