

```
ssh mingyue@xsjsda23
cat /proc/version
/tools/xgs/bin/sudo -i
apt-get remove xrt
# wget https://www.xilinx.com/bin/public/openDownload?filename=dpuv3e_u50_platform_vai1.2.tgz -O shell.tgz
# tar xfz shell.tgz

apt-get install /proj/xbuilds/2020.1_0529_1/xbb/xrt/packages/xrt_202010.2.6.655_18.04-amd64-xrt.deb
apt-get install /proj//xbuilds/2020.1_0529_1/xbb/packages/internal_platforms/cmc/u50/xilinx-cmc-u50_1.0.20-2853996_all_18.04.deb
apt-get install /proj//xbuilds/2020.1_0529_1/xbb/packages/internal_platforms/sc-fw/u50/xilinx-sc-fw-u50-5.0.27-2.e289be9_18.04.deb
apt-get install /proj/xbuilds/2020.1_0521_1/xbb/packages/internal_platforms/u50/gen3x4_xdma/validate/xilinx-u50-gen3x4-xdma-vali
date_2-2889074_all_18.04.deb
apt-get install /proj/xbuilds/2020.1_0521_1/xbb/packages/internal_platforms/u50/gen3x4_xdma/base/xilinx-u50-gen3x4-xdma-base_2-2895184_all_18.04.deb
/opt/xilinx/xrt/bin/xbmgmt flash --update --shell xilinx_u50_gen3x4_xdma_base_2
apt-get install /proj/xbuilds/2020.1_0521_1/xbb/packages/internal_platforms/u50/gen3x4_xdma/2-202010-1-dev/xilinx-u50-gen3x4-xdma-2-202010-1-dev_1-2895797_all_18.04.deb

#cold reboot xsjsda23
ssh mingyue@xsjsdxbf
/proj/sdxbf/prod/cmbin/util/bnreboot.py xsjsda23 --wait

/opt/xilinx/xrt/bin/xbutil program -d 0 -p /usr/lib/dpu.xclbin

```
