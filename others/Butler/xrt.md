## compile and debug XRT

```

git clone https://github.com/Xilinx/XRT.git
cd XRT
cd build
cat build.sh
https://github.com/Xilinx/XRT.git
source /opt/rh/devtoolset-6/enable
mkdir Debug;cd Debug
# CMake Error at /var/lib/docker/scratch/local/share/cmake-3.16/Modules/FindPackageHandleStandardArgs.cmake:146 (message):
#  Could NOT find OpenSSL, try to set the path to OpenSSL root folder in the
#  system variable OPENSSL_ROOT_DIR (missing: OPENSSL_CRYPTO_LIBRARY) (found
#  version "1.0.2k")

##   /var/lib/docker/scratch/local/share/cmake-3.16/Modules/FindOpenSSL.cmake:449 (find_package_handle_standard_args)
##  runtime_src/tools/xclbin/CMakeLists.txt:12 (find_package)

sudo yum install openssl-devel openssl-static json-glib-devel

cmake -DCMAKE_BUILD_TYPE=Debug  EXPORT_COMPILE_COMMANDS=ON  -D CMAKE_FIND_DEBUG_MODE=ON -DBUILD_SHARED_LIB=on  ../../src 2>&1 | tee config.log

cd $HOME/d/working/XRT/build/Debug
rm -fr CMakeCache.txt CMakeFiles
cmake -DCMAKE_BUILD_TYPE=Debug  EXPORT_COMPILE_COMMANDS=ON -DBUILD_SHARED_LIB=on -DOPENSSL_ROOT_DIR=/usr ../../src 2>&1 | tee config.log
make -j30
make install DESTDIR=$HOME/.local/xrt
```



```
CMake Warning at CMake/coverity.cmake:5 (message):
  -- coverity not found
Call Stack (most recent call first):
  CMake/nativeLnx.cmake:161 (include)
  CMakeLists.txt:61 (include)


CMake Error: The following variables are used in this project, but they are set to NOTFOUND.
Please set them or make sure they are set and tested correctly in the CMake files:
Z_LIB
    linked by target "xclbinutil" in directory /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/XRT/src/runtime_src/tools/xclbin
```


```
sudo yum install zlib-devel zlib-static
```

```
export LD_LIBRARY_PATH=$HOME/.local/xrt/opt/xilinx/xrt/lib:/home/chunywan/.local/lib:/usr/local/lib:/usr/local/lib64:/opt/xilinx/xrt/lib:/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib
emacs
```
