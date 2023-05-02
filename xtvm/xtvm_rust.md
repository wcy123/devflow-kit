# compiler Vitis AI
```
$ cd /workspace/aisw/Vitis-AI-Library
$ make all
```
# compiler xcompiler for MR-598
```
$ cd /workspace/aisw/xcompiler
$ git fetch origin refs/merge-requests/598/head
$ git checkout FETCH_HEAD
$ ../Vitis-AI-Library/cmake.sh --project=xcompiler
```

# compiler tvm  for branch 'br-squash'
```
$ cd /workspace/aisw
$ git clone gits@xcdl190260:aisw/tvm.git
$ cd /workspace/aisw/tvm
$ git checkout br-squash

$ git submodule init
$ git submodule update

$ rm -rf /home/build/build.Ubuntu.20.04.x86_64.Debug/tvm
$ mkdir -p /home/build/build.Ubuntu.20.04.x86_64.Debug/tvm
$ cp /workspace/aisw/tvm/cmake/config.cmake /home/build/build.Ubuntu.20.04.x86_64.Debug/tvm/
```
append /workspace/aisw/tvm/cmake/config.cmake :
     set(USE_LLVM ON)
     set(INSTALL_DEV ON)

```
$ ../Vitis-AI-Library/cmake.sh --project=tvm
```

# compiler xcompiler_tvm for branch create-rust-relay-representation-for-pattern-matching
```
$ cd /workspace/aisw/xcompiler_tvm
$ git checkout create-rust-relay-representation-for-pattern-matching
$ ../Vitis-AI-Library/cmake.sh --project=xcompiler_tvm

```
# run resnet50 sample
```
$ env PYTHONPATH=/workspace/aisw/tvm/python LD_LIBRARY_PATH=/home/local/Ubuntu.20.04.x86_64.Debug/lib:/usr/local/lib python /workspace/aisw/xcompiler_tvm/tests/test_resnet_v1_50.py

```

# for rust
## frist add cargo config file
$ cat /workspace/aisw/.cargo/config
[build]
target-dir= "/home/local/tvm-rust"

```
$ cd /workspace/aisw/tvm
$ ln -s  $(realpath ~/build/build.Ubuntu.20.04.x86_64.Debug/tvm) build

$ export TVM_HOME=/workspace/aisw/tvm
$ export LD_LIBRARY_PATH=/home/local/Ubuntu.20.04.x86_64.Debug/lib:$LD_LIBRARY_PATH

$ cd /workspace/aisw/tvm/rust
$ cargo build

$ cd /workspace/aisw/xcompiler_tvm/rust
$ cargo build
$ make
```


# for CXX
```
$ unset LD_LIBRARY_PATH; source /opt/petalinux/2021.1/environment-setup-cortexa72-cortexa53-xilinx-linux

$ cd /workspace/aisw/Vitis-AI-Library
$ make all

$ cd  /workspace/aisw/tvm
$ ../Vitis-AI-Library/cmake.sh --project=tvm --cmake-options=-DMACHINE_NAME=aarch64-linux-gnu

$ cd /workspace/aisw/xcompiler_tvm
$ ../Vitis-AI-Library/cmake.sh --project=xcompiler_tvm

```
