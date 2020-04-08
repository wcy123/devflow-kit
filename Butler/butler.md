# setup environment


follow [XBulter](https://confluence.xilinx.com/display/~vincentm/XButler)

## XRT

it is already installed.

## anaconda

nNOTE: refer to [anaconda](../VART/anaconda_env.md)

due to lib confilctions, we cannto use it, refer to [](butler.bak.md) for your reference.

## prerequites

```
sudo yum -y install jsoncpp-devel
```


## XIP/XButler

### prepare

```
which g++
g++ --version # make sure it is gcc6 or above
source /opt/rh/devtoolset-6/enable
g++ --version # make sure it is gcc6 or above
make clean
make
```

### make

```
cd $HOME/d/working/XIP/Butler/src
# make clean &&
make DEBUG=1
```

### prepare dsa files
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

it seems that we must ensure `XILINX_XRT=/opt/xilinx/xrt/`, at least, we must run `source /opt/xilinx/xrt/setup.sh`

### start server
```
export XILINX_XRT=/opt/xilinx/xrt/
export LD_LIBRARY_PATH=/group/xbjlab/dphi_software/software/workspace/chunywan/d/working/XIP/Butler/src/lib/:/usr/local/lib:/usr/local/lib64:/opt/xilinx/xrt/lib
cd $HOME/d/working/XIP/Butler/src
export BUTLER_VERBOSE=1
export GLOG_logtostderr=1
bin/xbutler

```

### start client

```
export XILINX_XRT=/opt/xilinx/xrt/
export LD_LIBRARY_PATH=/group/xbjlab/dphi_software/software/workspace/chunywan/d/working/XIP/Butler/src/lib/:/usr/local/lib:/usr/local/lib64:/opt/xilinx/xrt/lib
cd $HOME/d/working/XIP/Butler/src
export BUTLER_VERBOSE=1
export GLOG_logtostderr=1
bin/test_xbutler
```

end mark
