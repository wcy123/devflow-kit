# hello AIE

## setup environment


``` console
% ssh chunywan@xcdl190253
% cd
% export VITIS_VER=202020_1
% export _VITIS_VERSION=2020.2_released
% export VITIS_SDK_VER=v2020.2
% source /proj/xbuilds/$_VITIS_VERSION/installs/lin64/Vitis/HEAD/settings64.sh
# import licencse server
% export XILINXD_LICENSE_FILE=2100@aiengine-eng
% export LM_LICENSE_FILE=1757@xsjlicsrvip
% export PLATFORM_REPO_PATHS=/proj/xbuilds/$_VITIS_VERSION/internal_platforms
% export PLATFORM=${PLATFORM_REPO_PATHS}/xilinx_vck190_es1_base_${VITIS_VER}/xilinx_vck190_es1_base_${VITIS_VER}.xpfm

```

## build AIE kernel

``` console
% ssh chunywan@xcdl190253
% mkdir -p /group/dphi_software/software/workspace/chunywan/d/working/aie_workspace/simple
% cd  /group/dphi_software/software/workspace/chunywan/d/working/aie_workspace/simple
% tree /proj/xbuilds/SWIP/2021.1_0610_2318/installs/lin64/Vitis/2021.1/samples/simple/src
% tree /proj/xbuilds/SWIP/2021.1_0610_2318/installs/lin64/Vitis/2021.1/samples/simple/
% cp -av /proj/xbuilds/SWIP/2021.1_0610_2318/installs/lin64/Vitis/2021.1/samples/simple/src .
% find src -type f
% cat src/kernels.h
% cat src/kernels/kernels.cc
% cat src/kernels/include.h
% cat src/project.cpp
% cat src/project.h
% aiecompiler -platform=${PLATFORM} -include="src" --pl-axi-lite=true --pl-freq=250 --verbose -workdir=./Work src/project.cpp
```

## simulate

``` console
% ssh chunywan@xcdl190253
% mkdir -p /group/dphi_software/software/workspace/chunywan/d/working/aie_workspace/simple
% cd  /group/dphi_software/software/workspace/chunywan/d/working/aie_workspace/simple
% aiesimulator --help --pkg-dir=./Work
AIEsim feature license is found.
USAGE: aiesim [options]

OPTIONS:

AIE Simulator Options:

  --dump-vcd=<file>                   - Dump VCD to a file. e.g. --dump_vcd=foo
  --enable-memory-check               - Enable runtime program and data memory boundary access check. Any violation access will be reported as [WARNING] message. Default is disabled.
  --online                            - Call vcdanalyze to parse VCD on-the-fly, to optionally produce CTF (-ctf) or WDB (-wdb)
  --pkg-dir=<dir>                     - Set the package directory. e.g. --pkg-dir=Work
  --profile                           - Generate profiling data. use --profile argument to get profiling data for all used cores, or --profile="(col,row)(col,row)..."to get profiling data for specified cores
  --simulation-cycle-timeout=<cycles> - Run the simulator for a given number of cycles. e.g. --simulation-cycle-timeout=10000

Generic Options:

  --help-list                         - Display list of available options (--help-list-hidden for more)

% cp -av /proj/xbuilds/SWIP/2021.1_0610_2318/installs/lin64/Vitis/2021.1/samples/simple/data .
% aiesimulator --pkg-dir=./Work --profile --dump-vcd=aiesim_vcd_dump
% bash -ex `which aiesimulator` --pkg-dir=./Work --profile --dump-vcd=aiesim_vcd_dump
```

hack

``` console
% export XILINX_VITIS_AIETOOLS=/proj/xbuilds/SWIP/2020.2_1118_1232/installs/lin64/Vitis/2020.2/aietools
% setsid bash -ex /proj/xbuilds/SWIP/2020.2_1118_1232/installs/lin64/Vitis/2020.2/aietools/bin/loader -exec aiesim_dbg --pkg-dir=./Work --profile --dump-vcd=aiesim_vcd_dump
```

## ref

``` console
% ssh chunywan@xcdl190253
% mkdir -p /group/dphi_software/software/workspace/chunywan/d/working/aie_workspace/simple
% cd /group/dphi_software/software/workspace/chunywan/d/working/aie_workspace/vai_library_aie_task/aie_demo
% cd /group/dphi_software/software/workspace/chunywan/d/working/aie_workspace/vai_library_aie_task/mean_scale_gmio
% cd /group/dphi_software/software/workspace/chunywan/d/working/aie_workspace/vai_library_aie_task/; ls -l
% cat env.sh
% cat Makefile
% source env.sh
% make aiesim
% aiesimulator --pkg-dir=./Work
```

## compile host

``` console
% ssh chunywan@xcdl190253
% mkdir -p /group/dphi_software/software/workspace/chunywan/d/working/aie_workspace/simple
% cd  /group/dphi_software/software/workspace/chunywan/d/working/aie_workspace/simple
% mkdir -p /wrk/xcdhdnobkup1/chunywan/opt/2020.2
% /proj/xbuilds/2020.2_released/internal_platforms/sw/versal/xilinx-versal-common-v2020.2/sdk.sh -y -d /wrk/xcdhdnobkup1/chunywan/opt/2020.2
% source /wrk/xcdhdnobkup1/chunywan/opt/2020.2/environment-setup-aarch64-xilinx-linux
% cat ./Work/ps/c_rts/aie_control.cpp
% cat ./Work/ps/c_rts/aie_control_xrt.cpp
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
