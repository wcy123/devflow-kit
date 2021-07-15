# hello AIE

## setup environment


``` console
% ssh chunywan@xcdchunywan41x
% cd
% cat env.sh
% export VITIS_VER=202110_1
% export _VITIS_VERSION=2021.1_weekly_latest
% source /proj/xbuilds/$_VITIS_VERSION/installs/lin64/Vitis/HEAD/settings64.sh
# import licencse server
% export XILINXD_LICENSE_FILE=2100@aiengine-eng
% export LM_LICENSE_FILE=1757@xsjlicsrvip
% export PLATFORM_REPO_PATHS=/proj/xbuilds/$_VITIS_VERSION/internal_platforms
% export PLATFORM=${PLATFORM_REPO_PATHS}/xilinx_vck190_es1_base_${VITIS_VER}/xilinx_vck190_es1_base_${VITIS_VER}.xpfm

```

``` console
% ssh chunywan@xcdchunywan41x
% mkdir -p /group/dphi_software/software/workspace/chunywan/d/working/aie_workspace/simple
% cd  /group/dphi_software/software/workspace/chunywan/d/working/aie_workspace/simple
% tree /proj/xbuilds/SWIP/2021.1_0610_2318/installs/lin64/Vitis/2021.1/samples/simple/src
% cp -av /proj/xbuilds/SWIP/2021.1_0610_2318/installs/lin64/Vitis/2021.1/samples/simple/src .
% find src -type f
% cat src/kernels.h
% cat src/kernels/kernels.cc
% cat src/kernels/include.h
% cat src/project.cpp
% cat src/project.h
% aiecompiler -platform=${PLATFORM} -include="src" --pl-axi-lite=true --pl-freq=250 --verbose -workdir=./Work src/project.cpp
% cat ./Work/ps/c_rts/aie_control.cpp
% cat ./Work/ps/c_rts/aie_control_xrt.cpp
```

# compile host

``` console
% ssh chunywan@xcdchunywan41x
% mkdir -p /group/dphi_software/software/workspace/chunywan/d/working/aie_workspace/simple
% cd  /group/dphi_software/software/workspace/chunywan/d/working/aie_workspace/simple
% mkdir -p /wrk/xcdhdnobkup1/chunywan/opt/2020.2
% /proj/xbuilds/2020.2_released/internal_platforms/sw/versal/xilinx-versal-common-v2020.2/sdk.sh -y -d /wrk/xcdhdnobkup1/chunywan/opt/2020.2
% source /wrk/xcdhdnobkup1/chunywan/opt/2020.2/environment-setup-aarch64-xilinx-linux
% ${CXX} -c -I$XILINX_VIVADO/include/ -std=c++14 -I${XILINX_VITIS}/aietools/include -I"src" -I${SDKTARGETSYSROOT}/usr/include/xrt/ -o project.o src/project.cpp
% ${CXX} -c -I$XILINX_VIVADO/include/ -std=c++14 -I${XILINX_VITIS}/aietools/include -I"src" -I${SDKTARGETSYSROOT}/usr/include/xrt/ -o aie_control_xrt.o Work/ps/c_rts/aie_control_xrt.cpp
% echo ${CXX} -o host.exe project.o aie_control_xrt.o -ladf_api_xrt -lgcc -lc -lxrt_coreutil -lxilinxopencl -lpthread -lrt -ldl -lcrypt -L/wrk/xcdhdnobkup1/chunywan/opt/2020.2/sysroots/aarch64-xilinx-linux/usr/lib/ -Wl,-O1 -Wl,--hash-style=gnu -Wl,--as-needed -ladf_api_xrt  -L/proj/xbuilds/SWIP/2021.1_0610_2318/installs/lin64/Vitis/2021.1/aietools/lib/aarch64.o/
```

``` console
% aarch64-xilinx-linux-g++  -march=armv8-a+crc -mtune=cortex-a72.cortex-a53 --sysroot=/wrk/xcdhdnobkup1/chunywan/opt/2020.2/sysroots/aarch64-xilinx-linux -o ../host.exe aie_control_xrt.o project.o -Wl,-O1 -Wl,--hash-style=gnu -Wl,--as-needed -ladf_api_xrt -lgcc -lc -lxrt_coreutil -lxilinxopencl -lpthread -lrt -ldl -lcrypt -lstdc++ -L/wrk/xcdhdnobkup1/chunywan/opt/2020.2/sysroots/aarch64-xilinx-linux/usr/lib/ --sysroot=/wrk/xcdhdnobkup1/chunywan/opt/2020.2/sysroots/aarch64-xilinx-linux -L/proj/xbuilds/SWIP/2020.2_1118_1232/installs/lin64/Vitis/2020.2/aietools/lib/aarch64.o
% aarch64-xilinx-linux-g++  -march=armv8-a+crc -mtune=cortex-a72.cortex-a53 --sysroot=/wrk/xcdhdnobkup1/chunywan/opt/2020.2/sysroots/aarch64-xilinx-linux -o ../host.exe aie_control_xrt.o   graph.o -Wl,-O1 -Wl,--hash-style=gnu -Wl,--as-needed -ladf_api_xrt -lgcc -lc -lxrt_coreutil -lxilinxopencl -lpthread -lrt -ldl -lcrypt -lstdc++ -L/wrk/xcdhdnobkup1/chunywan/opt/2020.2/sysroots/aarch64-xilinx-linux/usr/lib/ --sysroot=/wrk/xcdhdnobkup1/chunywan/opt/2020.2/sysroots/aarch64-xilinx-linux -L/proj/xbuilds/SWIP/2020.2_1118_1232/installs/lin64/Vitis/2020.2/aietools/lib/aarch64.o
```

# make package

``` console

```
