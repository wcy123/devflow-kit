##



```
cd $HOME/d/working/XIP/Butler/src
../Scripts/enable-xbutler-process.sh
```

but it fails with the following messge.

```
XILINX_XRT      : /opt/xilinx/xrt
PATH            : /opt/xilinx/xrt/bin:/home/chunywan/.cargo/bin:/home/chunywan/.local/usr/local/bin:/home/chunywan/.local/bin:/home/chunywan/.cargo/bin:/home/chunywan/.local/usr/local/bin:/home/chunywan/.local/bin:/home/chunywan/.cargo/bin:/usr/lib64/qt-3.3/bin:/usr/lib64/ccache:/usr/local/bin:/usr/bin:/opt/puppetlabs/bin:/home/chunywan/.fzf/bin:/usr/local/sbin:/usr/sbin:/home/chunywan/.local/bin:/home/chunywan/bin
LD_LIBRARY_PATH : /opt/xilinx/xrt/lib:/group/xbjlab/dphi_software/software/workspace/chunywan/d/working/XIP/Butler/src/lib/:/usr/local/lib:/usr/local/lib64:/opt/xilinx/xrt/lib
PYTHONPATH     : /opt/xilinx/xrt/python:
Validating Arguments... passed!
Multi-process is not running!...
Multi-process is now running!
nohup: failed to run command 'xbutler': No such file or directory
```

I change PATH and run it again.

```
cd $HOME/d/working/XIP/Butler/src
export PATH=$HOME/d/working/XIP/Butler/src/bin:$PATH
../Scripts/enable-xbutler-process.sh
chunywan@xbjlabdpsvr15:src% ../Scripts/enable-xbutler-process.sh
XILINX_XRT      : /opt/xilinx/xrt
PATH            : /opt/xilinx/xrt/bin:/home/chunywan/d/working/XIP/Butler/src/bin:/home/chunywan/.cargo/bin:/home/chunywan/.local/usr/local/bin:/home/chunywan/.local/bin:/home/chunywan/.cargo/bin:/home/chunywan/.local/usr/local/bin:/home/chunywan/.local/bin:/home/chunywan/.cargo/bin:/usr/lib64/qt-3.3/bin:/usr/lib64/ccache:/usr/local/bin:/usr/bin:/opt/puppetlabs/bin:/home/chunywan/.fzf/bin:/usr/local/sbin:/usr/sbin:/home/chunywan/.local/bin:/home/chunywan/bin
LD_LIBRARY_PATH : /opt/xilinx/xrt/lib:/home/chunywan/.local/lib:/home/chunywan/.local/usr/local/lib:/usr/local/lib:/usr/local/lib64:/opt/xilinx/xrt/lib:/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib
PYTHONPATH     : /opt/xilinx/xrt/python:
Validating Arguments... passed!
Multi-process is not running!...
Multi-process is now running!
Starting Butler...
------------
Version Info
------------
Butler Version: 9000.0.0
Butler Build Version Date: Mar 30 2020
Butler Build Version Time: 10:12:26

-----------
------------
Config File
------------
Error reading config file from: /etc/xbutler/xbutler.config
-----------
System Info
-----------
FPGA #0: xilinx_u50_xdma_201920_1
-----------
Safe Mode Enabled.
Starting Server Thread...
Done Starting Butler!
```

for client side

```
cp /usr/lib/dpu.xclbins /opt/xilinx/dsa/verify.xclbin
cd $HOME/d/working/XIP/Butler/src
export PATH=$HOME/d/working/XIP/Butler/src/bin:$PATH
../Scripts/test_xbutler_cpp.sh
```

I've got the following error

```
chunywan@xbjlabdpsvr15:src% ../Scripts/test_xbutler_cpp.sh
-------------------------------
Validating Arguments... passed!
-------------------------------

----------------------
Verifying CONDA_PREFIX
----------------------
CONDA_PREFIX not defined!
Are you in a conda environment?...
```

Because libraries conflicts and there is no internet connection, I cannot setup environment for conda


```
bin/test_xbutler
```

I've got the following error

```
chunywan@xbjlabdpsvr15:src% bin/test_xbutler
bin/test_xbutler: error while loading shared libraries: libbutler.so: cannot open shared object file: No such file or directory
```

I export the 'LD_LIBRARY' and run it again.

```
export LD_LIBRARY_PATH=$HOME/d/working/XIP/Butler/src/lib:/opt/xilinx/xrt/lib:/home/chunywan/.local/lib:/home/chunywan/.local/usr/local/lib:/usr/local/lib:/usr/local/lib64:/opt/xilinx/xrt/lib:/home/chunywan/.local/CentOS.7.6.1810.x86_64.Debug/lib
export XILINX_XRT=/opt/xilinx/xrt/
export BUTLER_VERBOSE=1
export GLOG_logtostderr=1
bin/test_xbutler
```

I've got the following log from client side.

```
chunywan@xbjlabdpsvr15:src% bin/test_xbutler

-----------------------
     Version Info
-----------------------
Butler Version: 9000.0.0
Butler Build Version Date: Mar 30 2020
Butler Build Version Time: 10:12:23


-----------------------
   Starting Test...
-----------------------

-------------------------------------
In Ping
Ping: connected.
Ping: Sending message...
Ping: Sending User Name...
Ping: User Name is: chunywan.
Ping: Receiving response...
Ping: response is: SUCCESS.
-------------------------------------

-----------------------
       Ping Test
-----------------------
Passed!


-----------------------
   Acquire FPGA Test
-----------------------
-------------------------------------
In acquireFPGA
acquireFPGA: Reading XCLBIN(s) from path...
acquireFPGA: connected.
acquireFPGA: UDF Mode.
acquireFPGA: Sending message...
acquireFPGA: Sending User Name...
acquireFPGA: User Name is: chunywan.
acquireFPGA: Sending XCLBINs...
acquireFPGA: Receiving System...
acquireFPGA: Executing Algo.
acquireFPGA: Sending UDF Result...
acquireFPGA: UDF Result is: 0x7ffe0f49de10.
acquireFPGA: Receiving response...
acquireFPGA: response is: GET_NUM_KERNEL_ARGS_ERROR.
acquireFPGA: Receiving handle...
acquireFPGA: handle is: 0.
acquireFPGA: Receiving CUs...
-------------------------------------
ERROR: No CUs acquired.

-----------------------
     Release Test
-----------------------


-----------------------
    Acquire CU Test
-----------------------
-------------------------------------
In acquireCU
acquireCU: connected.
acquireCU: non-UDF Mode.
acquireCU: Sending message...
acquireCU: Sending User Name...
acquireCU: User Name is: chunywan.
acquireCU: Sending Kernel Name...
acquireCU: Kernel Name is: hello.
acquireCU: Sending XCLBINs...
acquireCU: Receiving response...
acquireCU: response is: INVALID.
acquireCU: Receiving handle...
acquireCU: handle is: 0.
acquireCU: Receiving CUs...
-------------------------------------
ERROR: No CUs acquired.

-----------------------
     Release Test
-----------------------

```

this is the log from server side

```
Running on machine: xbjlabdpsvr15
Log line format: [IWEF]mmdd hh:mm:ss.uuuuuu threadid file:line] msg
-------------------------------------
In Ping
Ping: connected.
Ping: Sending message...
Ping: Sending User Name...
Ping: User Name is: chunywan.
Ping: Receiving response...
Ping: response is: SUCCESS.
-------------------------------------
-------------------------------------
In acquireFPGA
acquireFPGA: Reading XCLBIN(s) from path...
```


I modified the source code, as below, otherwise, I don't think it is
meaningful. It is not even to try program the xclbin.

```
+      butler::FPGASelectionPriorityDSANameFPGA0 algo;
+      acquireResult = client.acquireFPGA(xclbin, nullptr, &algo);
```


log from server side

```
chunywan@xbjlabdpsvr15:src% bin/xbutler
Starting Butler...
------------
Version Info
------------
Butler Version: 9000.0.0
Butler Build Version Date: Mar 30 2020
Butler Build Version Time: 10:12:26

-----------
------------
Config File
------------
Error reading config file from: /etc/xbutler/xbutler.config
-----------
System Info
-----------
FPGA #0: xilinx_u50_xdma_201920_1
-----------
Safe Mode Enabled.
Starting Server Thread...
Done Starting Butler!
AcquireFPGA: Sending system...
AcquireFPGA: Receiving UDF result...
AcquireFPGA: UDF result is:
0x7fb7e0b024d0
AcquireFPGA: Validating UDF result...
AcquireFPGA: UDF result is valid.
AcquireFPGA: Programming FPGA...
XRT build version: 2.3.0
Build hash: 192e706aea53163a04c574f9b3fe9ed76b6ca471
Build date: 2020-03-30 17:10:12
Git branch: HEAD
PID: 359095
UID: 30870
[Tue Mar 31 13:15:52 2020]
HOST: xbjlabdpsvr15
EXE: /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/XIP/Butler/src/bin/xbutler
[XRT] ERROR: Wrong kernel argument index: 63
[XRT] ERROR: kernel is nullptr
AcquireFPGA: Sending response...
AcquireFPGA: Response is: GET_NUM_KERNEL_ARGS_ERROR
AcquireFPGA: Sending handle...
AcquireFPGA: Handle is: 0
AcquireFPGA: Sending result...
Finishing AcquireFPGA.
-------------------------------------
-------------------------------------
        New Message From Client
-------------------------------------
Server: got connection on Tue Mar 31 13:15:52 2020
Server: got connection from 127.0.0.1 port 48120
ServerBooklet: Already exist socket: 5.
ServerBooklet: Already exist port: 63675.
Servicing PID 359172
-------------------------------------
Starting AcquireCU...
AcquireCU: Safe Mode Enabled.
AcquireCU: Receiving user name...
AcquireCU: user name is: chunywan
ServerBooklet: Already exist socket: 5.
ServerBooklet: Already exist username: chunywan.
AcquireCU: Receiving kernel name...
AcquireCU: Kernel name is: hello
AcquireCU: Receiving xclbin batch...
AcquireCU: Non-UDF Mode.
AcquireCU: executing algo.
ERROR: AcquireCU: FAILED!
AcquireCU: Sending response...
AcquireCU: Response is: INVALID
AcquireCU: Sending handle...
AcquireCU: Handle is: 0
AcquireCU: Sending result...
Finishing AcquireCU.
-------------------------------------
-------------------------------------
        New Message From Client
-------------------------------------
Server: got connection on Tue Mar 31 13:15:52 2020
Server: got connection from 127.0.0.1 port 48120
ServerBooklet: Already exist socket: 5.
ServerBooklet: Already exist port: 63675.
-------------------------------------
      Detected Dead Connection
Removing socket: 5
ServerBooklet: Removing socket: 5.
-------------------------------------

```
