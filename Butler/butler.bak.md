# setup environment


follow [XBulter](https://confluence.xilinx.com/display/~vincentm/XButler)

## XRT

it is already installed.

## anaconda

NOTE: refer to [anaconda](VART/anaconda_env.md)

due to lib confilctions, we cannto use it.
## create anaconda mirror from xcd environment to bjlab

refer to [how to create a mirror for conda repo](https://docs.anaconda.com/anaconda-repository/admin-guide/install/config/mirrors/mirror-anaconda-repository/)

I don't know the version of the xcd repos version, lets' go anyway.

according to https://docs.anaconda.com/anaconda-repository/admin-guide/install/requirements/#repo-hardware-reqs,
and

```
(base) chunywan@xbjlabdpsvr15:~% env LANG=C df -h /scratch/
Filesystem                 Size  Used Avail Use% Mounted on
/dev/mapper/vg00-dockerlv  744G  269G  476G  37% /var/lib/docker
```
It seems that we don't have enough storage, even for local disk.

But without local mirrors and slow network, it is very challenging.

```

the content of `~/.condarc`

```yaml
channels:
  - conda-forge
  - defaults
```

```bash
function init_conda() {
    __conda_setup="$('/scratch/chunywan/anoconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
    if [ $? -eq 0 ]; then
          eval "$__conda_setup"
    else
          if [ -f "/scratch/chunywan/anoconda3/etc/profile.d/conda.sh" ]; then
                 . "/scratch/chunywan/anoconda3/etc/profile.d/conda.sh"
          else
                 export PATH="/scratch/chunywan/anoconda3/bin:$PATH"
         fi
   fi
}
```

```sh
init_conda
```


```
rsync -a -e 'ssh -p 10152' localhost:/wrk/acceleration/conda-channel /scratch/chunywan
rmdir /scratch/chunywan/conda
mv -v $HOME/.conda /scratch/chunywan/conda
mkdir -p /scratch/chunywan/conda
ln -s /scratch/chunywan/conda $HOME/.conda
conda create -y -n butler python=3.7 \
    libuuid glog protobuf pybind11 jsoncpp xip \
    -c file://scratch/chunywan/conda-channel/ -c defaults -c conda-forge/label/gcc7

conda activate butler
conda list | grep xip
```

```
xip                       2.0.4                    py37_0    file://scratch/chunywan/conda-channel
(butler) chunywan@xbjlabdpsvr15:~%
```


## prerequites

```
sudo yum -y install jsoncpp-devel
```


## XIP/XButler


```
which enable-xbutler-process.sh

/scratch/chunywan/anoconda3/envs/butler/bin/enable-xbutler-process.sh

enable-xbutler-process.sh
(butler) chunywan@xbjlabdpsvr15:~% enable-xbutler-process.sh
XILINX_XRT      : /opt/xilinx/xrt
PATH            : /opt/xilinx/xrt/bin:/scratch/chunywan/anoconda3/envs/butler/bin:/scratch/chunywan/anoconda3/bin:/scratch/chunywan/anoconda3/condabin:/home/chunywan/.cargo/bin:/home/chunywan/.local/bin:/home/chunywan/.cargo/bin:/home/chunywan/.cargo/bin:/home/chunywan/.local/bin:/home/chunywan/.cargo/bin:/usr/lib64/qt-3.3/bin:/usr/lib64/ccache:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/opt/puppetlabs/bin:/home/chunywan/.fzf/bin:/home/chunywan/.local/bin:/home/chunywan/bin:/home/chunywan/.local/bin:/home/chunywan/bin
LD_LIBRARY_PATH : /opt/xilinx/xrt/lib:/home/chunywan/.local/lib:/usr/local/lib:/usr/local/lib64:/opt/xilinx/xrt/lib:/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib
PYTHONPATH     : /opt/xilinx/xrt/python:
Validating Arguments... passed!
Multi-process is not running!...
Multi-process is now running!
Starting Butler...
------------
Version Info
------------
Butler Version: 2.0.4
Butler Build Version Date: Oct  8 2019
Butler Build Version Time: 23:47:56
-----------
-----------
System Info
-----------
FPGA #0: xilinx_u50_xdma_201920_1
-----------
Safe Mode Enabled.
Starting Server Thread...
Starting PID Thread...
Done Starting Butler!

cat ${CONDA_PREFIX}/metadata/xip/butler/xbutler.config
NOTE: no config file
```


clone the source code.



```
cd $HOME/d/working/
git clone ssh://gits@localhost:10260/vitis/XIP.git
cd $HOME/d/working/XIP
head ./Butler/packages/common/xbutler.config
etags $(find . -iname '*.c' -or -iname '*.h' -or -iname '*.hpp' -or -iname '*.cpp')
fd
```

```
conda install protobuf
test_xbutler.sh

(butler) chunywan@xbjlabdpsvr15:XIP% test_xbutler.sh
-------------------------------
Validating Arguments... passed!
-------------------------------

----------------------
Verifying XILINX_XRT
----------------------
XILINX_XRT not defined!
XILINX_XRT      : /opt/xilinx/xrt
PATH            : /opt/xilinx/xrt/bin:/scratch/chunywan/anoconda3/envs/butler/bin:/scratch/chunywan/anoconda3/bin:/scratch/chunywan/anoconda3/bin:/scratch/chunywan/anoconda3/condabin:/home/chunywan/.cargo/bin:/home/chunywan/.local/bin:/home/chunywan/.cargo/bin:/home/chunywan/.cargo/bin:/home/chunywan/.local/bin:/home/chunywan/.cargo/bin:/usr/lib64/qt-3.3/bin:/usr/lib64/ccache:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/opt/puppetlabs/bin:/home/chunywan/.fzf/bin:/home/chunywan/.local/bin:/home/chunywan/bin:/home/chunywan/.local/bin:/home/chunywan/bin
LD_LIBRARY_PATH : /opt/xilinx/xrt/lib:
PYTHONPATH     : /opt/xilinx/xrt/python:
Pass!
test_xbutler: error while loading shared libraries: libprotobuf.so.20: cannot open shared object file: No such file or directory

```


`libprotobuf.so.20` is required but `libprotobuf.so.22` is installed.

```
(butler) chunywan@xbjlabdpsvr15:XIP% find /scratch/chunywan/anoconda3/envs/butler/lib | grep protobuf.so
/scratch/chunywan/anoconda3/envs/butler/lib/libprotobuf.so
/scratch/chunywan/anoconda3/envs/butler/lib/libprotobuf.so.22
/scratch/chunywan/anoconda3/envs/butler/lib/libprotobuf.so.22.0.4
```



```
(butler) chunywan@xbjlabdpsvr15:XIP% conda list protobuf
# packages in environment at /scratch/chunywan/anoconda3/envs/butler:
#
# Name                    Version                   Build  Channel
libprotobuf               3.11.4               hd408876_0
protobuf                  3.11.4           py37he1b5a44_0    conda-forge
```

```
conda remove protobuf
conda install 'protobuf==3.9'
conda install xip -c file://scratch/chunywan/conda-channel
test_xbutler.sh
-------------------------------
Validating Arguments... passed!
-------------------------------

----------------------
Verifying CONDA_PREFIX
----------------------
----------------------
Verifying XILINX_XRT
----------------------
XILINX_XRT not defined!
XILINX_XRT      : /opt/xilinx/xrt
PATH            : /opt/xilinx/xrt/bin:/scratch/chunywan/anoconda3/bin:/scratch/chunywan/anoconda3/bin:/scratch/chunywan/anoconda3/envs/butler/bin:/scratch/chunywan/anoconda3/bin:/scratch/chunywan/anoconda3/bin:/scratch/chunywan/anoconda3/condabin:/home/chunywan/.cargo/bin:/home/chunywan/.local/bin:/home/chunywan/.cargo/bin:/home/chunywan/.cargo/bin:/home/chunywan/.local/bin:/home/chunywan/.cargo/bin:/usr/lib64/qt-3.3/bin:/usr/lib64/ccache:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/opt/puppetlabs/bin:/home/chunywan/.fzf/bin:/home/chunywan/.local/bin:/home/chunywan/bin:/home/chunywan/.local/bin:/home/chunywan/bin
LD_LIBRARY_PATH : /opt/xilinx/xrt/lib:
PYTHONPATH     : /opt/xilinx/xrt/python:
Pass!
test_xbutler: /scratch/chunywan/anoconda3/envs/butler/lib/libuuid.so.1: no version information available (required by /opt/xilinx/xrt/lib/libxilinxopencl.so.2)
test_xbutler: /scratch/chunywan/anoconda3/envs/butler/lib/libuuid.so.1: no version information available (required by /opt/xilinx/xrt/lib/libxrt_core.so.2)

-----------------------
     Version Info
-----------------------
Butler Version: 2.0.4
Butler Build Version Date: Oct  8 2019
Butler Build Version Time: 23:47:54

-----------------------
   Starting Test...
-----------------------

ERROR: Did not find any xclbins!
```



```
xbutler_backdoor.sh -b
xbutler_backdoor.sh -s
```


```
export BUTLER_VERBOSE=1
export BUTLER_VERBOSE_STDOUT=1
```

compile from source code

```
cd $HOME/d/working/XIP/Butler/src
# we got protoc error, version mismatch
# so  I have to reinstall protobuf
conda remove protobuf
conda install xip protobuf -c file://scratch/chunywan/conda-channel/
make
# then we've got the error
# undefined reference to symbol '_ZNKSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE7compareEPKc'
# it seems that we use the wrong version of g++
g++ --version
g++ (GCC) 4.8.5 20150623 (Red Hat 4.8.5-36)
conda install gxx_linux-64 -c defaults -c conda-forge/label/gcc7
make CXX=x86_64-conda_cos6-linux-gnu-g++
```

then we've got the error

```
common/butler_xocl_util.h:26:10: fatal error: CL/opencl.h: No such file or directory
 #include <CL/opencl.h>
```


```
sudo yum install opencl-headers
Package opencl-headers-2.2-1.20180306gite986688.el7.noarch already installed and latest version
Nothing to do

rpm -ql opencl-headers
```


it seems that the `gxx` in conda does not search for include directories in system.


```
x86_64-conda_cos6-linux-gnu-g++ -xc -E -v -
cp -av /usr/include/CL $CONDA_PREFIX/x86_64-conda_cos6-linux-gnu/sysroot/usr/include
```

```
make CXX=x86_64-conda_cos6-linux-gnu-g++
```

we got the link error as below

```
/opt/xilinx/xrt//lib/libxilinxopencl.so: undefined reference to `undefined reference to `boost::filesystem::detail:
```

copy the boost libararies to  sysroot

```
cp -av /usr/lib64/*boost_filesystem* /usr/include/CL $CONDA_PREFIX/x86_64-conda_cos6-linux-gnu/sysroot/usr/lib
```

make it again

```
make CXX=x86_64-conda_cos6-linux-gnu-g++
```

we got the link error as below

```
/opt/xilinx/xrt//lib/libxilinxopencl.so: undefined reference to `uuid_copy@UUID_1.0'
```

```
ldd /opt/xilinx/xrt//lib/libxilinxopencl.so
cp -av /usr/lib64/libuuid* $CONDA_PREFIX/x86_64-conda_cos6-linux-gnu/sysroot/usr/lib
```

make it again

```
make CXX=x86_64-conda_cos6-linux-gnu-g++
```

we got the link error as below


```
/var/lib/docker/scratch/chunywan/anoconda3/envs/butler/bin/../lib/gcc/x86_64-conda_cos6-linux-gnu/7.3.0/../../../../x86_64-conda_cos6-linux-gnu/bin/ld: /opt/xilinx/xrt//lib/libxilinxopencl.so: undefined reference to `memcpy@GLIBC_2.14'
/var/lib/docker/scratch/chunywan/anoconda3/envs/butler/bin/../lib/gcc/x86_64-conda_cos6-linux-gnu/7.3.0/../../../../x86_64-conda_cos6-linux-gnu/bin/ld: /opt/xilinx/xrt//lib/libxilinxopencl.so: undefined reference to `boost::system::system_category()'
/var/lib/docker/scratch/chunywan/anoconda3/envs/butler/bin/../lib/gcc/x86_64-conda_cos6-linux-gnu/7.3.0/../../../../x86_64-conda_cos6-linux-gnu/bin/ld: /opt/xilinx/xrt//lib/libxilinxopencl.so: undefined reference to `boost::system::generic_category()
```

it seems that we cannot use conda gxx to compile it, use local gcc

```
source /opt/rh/devtoolset-6/enable
make clean
make
```

we got the link error as below

```
butler_config_file_parser_util.cpp:(.text+0x13f): undefined reference to `Json::Value::operator[](std::string const&)'
butler_config_file_parser_util.cpp:(.text+0x167): undefined reference to `Json::Value::asString() const'
```


```
make
```

we got many link errors, give up.

switch to a non conda environment.

```
make
```

we got the following compilation error.

```
common/butler_config_file.h:47:13: error: ‘Json’ has not been declared
  ConfigFile(Json::Value& root);
```

it seems that because the jsoncpp and jsonc confliction

```
rpm -ql jsoncpp-devel | grep json.h
grep '^#.*json' a.cpp.e
# 1 "/usr/local/include/json/json.h" 1 3

```

```
make CXXFLAGS
```


```
python3 -c "import distutils.sysconfig; print(distutils.sysconfig.get_config_vars())" ## useless
python3 -c "import sysconfig;print(sysconfig.get_config_vars())"
python3-config --libs --includes --ldflags

/tools/xgs/bin/sudo -i
rsync -av /home/liyunzhi/Python-3.8.1 /scratch/
chown -R chunywan: /scratch/Python-3.8.1
exit
cd /scratch/Python-3.8.1
source /opt/rh/devtoolset-6/enable
./configure --enable-shared
make -j10
/tools/xgs/bin/sudo make install
python3-config  --ldflags
```

```
emacs
xgud-gdb
set env LD_LIBRARY_PATH /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/XIP/Butler/src/lib/:/usr/local/lib:/usr/local/lib64
```

```
mkdir -p /opt/xilinx/dsa/
sudo cp -av /usr/lib/dpu.xclbin /opt/xilinx/dsa/verify.xclbin
ssh xbjlabdpsvr15 ls -l /opt/xilinx/dsa/
ls -la /opt/xilinx/dsa/
sudo chmod o+rw /opt/xilinx/dsa/
scp xbjlabdpsvr15:/opt/xilinx/dsa/dpu.xclbin.vitis.1.1 /opt/xilinx/dsa/
cp /opt/xilinx/dsa/dpu.xclbin.vitis.1.1 /opt/xilinx/dsa/verify.xclbin
md5sum /opt/xilinx/dsa/dpu.xclbin.vitis.1.1 /opt/xilinx/dsa/verify.xclbin
# it should be b7229999dca837511de0ac716d904870
/opt/xilinx/xrt/bin/xbutil query | less
```

cannot detect any cards.

rollback to origin version.

```
conda search xip --info -c file://scratch/chunywan/conda-channel/
mkdir ~/tmp/xip.tar.gz
tar -xvf /scratch/chunywan/conda-channel/linux-64/xip-2.0.5-py36_0.tar.bz2 -C ~/tmp/xip.tar.gz
cd ~/tmp/xip.tar.gz/
cat info/git

cd ~/tmp/
git clone ssh://gits@localhost:10260/vitis/XIP.git
cd ~/tmp/XIP
git checkout a6880c08f731ef9a132b3c3a2610fbae0e1563b9
cd Butler/src
source /opt/rh/devtoolset-6/enable
make clean
make DEBUG=1 -j30
```

it seems that we must ensure `XILINX_XRT=/opt/xilinx/xrt/`, at least, we must run `source /opt/xilinx/xrt/setup.sh`

try again

```
export XILINX_XRT=/opt/xilinx/xrt/
export LD_LIBRARY_PATH=/group/xbjlab/dphi_software/software/workspace/chunywan/d/working/XIP/Butler/src/lib/:/usr/local/lib:/usr/local/lib64:/opt/xilinx/xrt/lib
cd $HOME/d/working/XIP/Butler/src
export BUTLER_VERBOSE=1
export GLOG_logtostderr=1
bin/xbutler

```

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

sudo yum install openssl-devel
cmake -DCMAKE_BUILD_TYPE=Debug  EXPORT_COMPILE_COMMANDS=ON --trace-source=FindOpenSSL.cmake -D CMAKE_FIND_DEBUG_MODE=ON --trace-expand -DBUILD_SHARED_LIB=on  ../../src 2>&1 | tee config.log
cmake -DCMAKE_BUILD_TYPE=Debug  EXPORT_COMPILE_COMMANDS=ON --trace-source=FindOpenSSL.cmake -D CMAKE_FIND_DEBUG_MODE=ON -DBUILD_SHARED_LIB=on  ../../src 2>&1 | tee config.log
cmake -DCMAKE_BUILD_TYPE=Debug  EXPORT_COMPILE_COMMANDS=ON  -D CMAKE_FIND_DEBUG_MODE=ON -DBUILD_SHARED_LIB=on  ../../src 2>&1 | tee config.log
strace -f -o a.log cmake -DCMAKE_BUILD_TYPE=Debug  EXPORT_COMPILE_COMMANDS=ON -DBUILD_SHARED_LIB=on -DOPENSSL_ROOT_DIR=/usr ../../src 2>&1 | tee config.log

sudo yum install openssl-static
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
end mark
