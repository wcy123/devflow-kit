

```
ssh xcosda143
cd /proj/rdi/staff/chunywan/d/working/aisw/xdock-vitis-ai-sw/workspace/
git clone https://gitenterprise.xilinx.com/FaaSApps/runtime_control_translator
cd runtime_control_translator
cd tests/sample_test
export XILINXD_LICENSE_FILE=2100@aiengine-eng
export LM_LICENSE_FILE=1757@xsjlicsrvip
make all
```

```
# setting setenv.rc
set VER = '9999.0'
#setenv BUILD CustTA/2021.2_2021_1109_1353
#setenv BUILD ${VER}_INT_daily_latest
#setenv BUILD ${VER}_INT_0504_2148
setenv BUILD ${VER}_INT_0519_2210
#setenv BUILD ${VER}_2022_0420_0528
setenv XILINX_VITIS /proj/xbuilds/$BUILD/installs/lin64/Vitis/HEAD
setenv XILINX_VITIS_AIETOOLS ${XILINX_VITIS}/aietools
setenv PATH ${XILINX_VITIS_AIETOOLS}/bin:$PATH
setenv PATH /proj/xcohdstaff6/yud/gcc-inst-6.4.0/bin:$PATH
source ${XILINX_VITIS}/settings64.csh
setenv XILINXD_LICENSE_FILE 2100@aiengine-eng
setenv LM_LICENSE_FILE 1757@xsjlicsrvip
setenv aiecompiler $XILINX_VITIS_AIETOOLS/bin/aiecompiler
```

```
cp /proj/xcohdstaff6/yud/simnow-linux64-internal-20230419-f9b6332fa7.zip /proj/xcohdstaff5/chunywan

unzip simnow-linux64-internal-20230419-f9b6332fa7.zip

```

```

```
