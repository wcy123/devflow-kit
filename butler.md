# setup environment


follow [XBulter](https://confluence.xilinx.com/display/~vincentm/XButler)

## XRT

it is already installed.

## anaconda

refer to [anaconda](VART/anaconda_env.md)


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
sudo yum install jsoncpp-devel
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
end mark
