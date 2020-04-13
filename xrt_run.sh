#!/bin/bash -e

BRANCH=2018.3
MODE=Debug
XCLBIN=/home/yangenshan/mls_release/u280_3627d1_v3me_826d68_2019年06月19日_Freq300.000.from_loc.xdc.xclbin
DIR=$(readlink -f $(dirname ${BASH_SOURCE[0]}))

debug()
{
    sudo dmesg -n8
    sudo bash -c "echo 0xfffffff > /sys/module/drm/parameters/debug"
    #cat /sys/bus/pci/devices/0000:08:00.0/*
    #cat /sys/bus/pci/devices/0000:08:00.1/*
}

query()
{
    read -p "Do you want to replace XRT (y/n)" ans
    while [ $ans != "y" ] && [ $ans != "n" ]
    do
        read -p "Do you want to replace XRT (y/n)" ans
    done
}

xrt()
{
    echo -e "\n====================Build XRT=============================="
    dkms status
    query
    if [ "$ans" == "y" ];then
        [ ! -d XRT ] && git clone https://github.com/Xilinx/XRT.git
        cd XRT
        ver=$(git branch | head -n1 | awk '{print $2}')
        if [ "$ver" != "${BRANCH}" ];then
            git checkout -b "${BRANCH}" origin/"${BRANCH}" || exit
        fi
        ${DIR}/XRT/build/build.sh || exit 1;
        sudo cp -rvf ${DIR}/XRT/build/${MODE}/usr/src/xrt-2.1.0 /usr/src || exit 1;
        sudo cp -rvf ${DIR}/XRT/build/${MODE}/opt/xilinx/xrt /opt/xilinx/xrt || exit 1
        sync && sync
        #sudo rm -rvf /var/lib/dkms/xrt
        #sudo dkms install -m xrt -v 2.1.0
        sudo ${DIR}/XRT/build/${MODE}/postinst || exit 1
        cd "$cur"
        dkms status
    fi
}

SECONDS=0
cur="$DIR"
debug

#echo -e "\n====================LOAD XCLBIN=============================="
#echo "xbutil program -d 0 -p $XCLBIN"
#xbutil program -d 0 -p $XCLBIN || exit

echo -e "\n====================RUN DPU=================================="
cat /proc/interrupts | head -n1
cat /proc/interrupts |grep cl | sed /"          0          0          0          0          0          0          0          0  "/d

if [ ! -e ./run_dpu ]
    then
    make  || exit
fi
./run_dpu || exit

cat /proc/interrupts | head -n1
cat /proc/interrupts |grep cl | sed /"          0          0          0          0          0          0          0          0  "/d

echo "Elapsed: $(( SECONDS / 3600 ))h:$((( SECONDS / 60) % 60 ))m:$(( SECONDS % 60))s"
