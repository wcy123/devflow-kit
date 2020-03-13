# Getting  started with VMSS.

`NOTE`: working in progress, it only works on xbjlabdpsvr15
environment. You might need minor tweaks for your environment.

# external prerequistes

## install and start `mongodb`

TODO: install `mongodb`

### start mongodb

```
systemctl start mongod
systemctl status mongod
```

```
mongo -version
MongoDB shell version v4.2.3
git version: 6874650b362138df74be53d366bbefc321ea32d4
OpenSSL version: OpenSSL 1.0.1e-fips 11 Feb 2013
allocator: tcmalloc
modules: none
build environment:
    distmod: rhel70
    distarch: x86_64
    target_arch: x86_64
```
## internal prerequites

## build `Vitis-AI-Library`

please refert to [build Vitis AI Library](../VART/build_unilog_xir_vart_ailib.md)

## build vmss server

```
mkdir -p $HOME/d/working/vmss/
cd $HOME/d/working/vmss/
git clone https://gitenterprise.xilinx.com/ips-video-ml/VMSS.git
cd VMSS
export VMSS_HOME=$HOME/d/working/vmss/VMSS
git submodule update --init
make DEBUG=1
```


## build DPU plugsins

```
mkdir -p $HOME/d/working/vmss/
cd $HOME/d/working/vmss/
git clone gits@xcdl190260:wangchunye/VMSS_DPU_Plugins.git
cd $HOME/d/working/vmss/VMSS_DPU_Plugins
./cmake.sh
```

## install the plugins


```
build_type=Debug  ;\
os=`lsb_release -a | grep "Distributor ID" | sed 's/^.*:\s*//'`  ;\
os_version=`lsb_release -a | grep "Release" | sed 's/^.*:\s*//'` ;\
arch=`uname -p`  ;\
target_info=${os}.${os_version}.${arch}  ;\
VMSS_HOME=/group/xbjlab/dphi_software/software/workspace/chunywan/d/working/vmss/my_vmss
ln -sf $HOME/.local/${target_info}.${build_type}/lib/libdpuMLPreProcPlg.so $VMSS_HOME/server/plugins
ln -sf $HOME/.local/${target_info}.${build_type}/lib/libdpuMLInferencePlg.so $VMSS_HOME/server/plugins
ln -sf $HOME/.local/${target_info}.${build_type}/lib/libdpuMLPostProcPlg.so $VMSS_HOME/server/plugins
ls -l $VMSS_HOME/server/plugins
```


## debug vmss server

```
cd $VMSS_HOME/server
export LD_LIBRARY_PATH=/usr/local/lib:/usr/local/lib64:/opt/xilinx/xrt/lib:/home/$USER/.local/${target_info}.${build_type}/lib:$VMSS_HOME/server/libs:$VMSS_HOME/server/libs/extern:$VMSS_HOME/server/libs/extern/ml-suite-py3
gdb vmss_server
```

in the gdb session

```
start conf
continue
```

open request for resnet50

```
export VMSS_HOME=$HOME/d/working/vmss/my_vmss
export LD_LIBRARY_PATH=/usr/local/lib:/usr/local/lib64:/opt/xilinx/xrt/lib:/home/$USER/.local/${target_info}.${build_type}/lib:$VMSS_HOME/server/libs:$VMSS_HOME/server/libs/extern:$VMSS_HOME/server/libs/extern/ml-suite-py3
./vmss_client 127.0.0.1 8001 data/commands/vmss_open_jpeg_resnet_request.txt
# now a subshell is forked
```


send image

```
# in the forked subshell
./scripts/gst_send_rtp.sh -rd 10 -w 224 -h 224 -f  data/classification/beagle.jpg
# after tesing
exit
# exit will close the session.
```


<!-- close request -->

<!-- ``` -->
<!-- export VMSS_HOME=$HOME/d/working/vmss/my_vmss -->
<!-- export LD_LIBRARY_PATH=/usr/local/lib:/usr/local/lib64:/opt/xilinx/xrt/lib:/home/$USER/.local/${target_info}.${build_type}/lib:$VMSS_HOME/server/libs:$VMSS_HOME/server/libs/extern:$VMSS_HOME/server/libs/extern/ml-suite-py3 -->
<!-- ./vmss_client 127.0.0.1 8001 data/commands/vmss_close_request.txt -->
<!-- ## -->
<!-- ``` -->



open request for retail, a cascade network

```
./vmss_client 127.0.0.1 8001 data/commands/vmss_open_jpeg_retail_request.txt

```


again in the forked subshell

```
./scripts/gst_send_rtp.sh -rd 10 -w 416 -h 416 -f  data/classification/beagle.j
```





for cascade network

```
I0312 14:24:02.776981 174841 dpuMLPreProcPlg.cpp:68] ctx network-ctxt@0x6b4000[name=resnet50] session 5e69c8db7719fb23f0591f7a00000000 input->image_data ImageData[
    roi=InfR[
        classification=CHOCOLATE
        confidence= 0.999255
        bbox= 226x326@(106,57)
        next=InfR[
            classification=null
            confidence= 0
            bbox= 0x0@(101,0)
            next=InfR[
                classification=null
                confidence= 0
                bbox= 0x0@(0,0)
                next=null
            ]
        ]
    ]
    pts=4134799567
    timestamp=1583994239
    ts_us_offset=497507
    frame=1
    fourcc=0
    dim=0x0
    size=0
    org_img=0
    out_img=0
    src=ImageData[
        roi=null
        pts=4134799567
        timestamp=1583994239
        ts_us_offset=497507
        frame=1
        fourcc=0
        dim=0x0
        size=0
        org_img=0
        out_img=0
        src=ImageData[
            roi=null
            pts=4134799567
            timestamp=1583994239
            ts_us_offset=497507
            frame=1
            fourcc=5392194
            dim=416x416
            size=519168
            org_img=0x7fff700de350
            out_img=0
            src=ImageData[null]
        ]
    ]
]
```
