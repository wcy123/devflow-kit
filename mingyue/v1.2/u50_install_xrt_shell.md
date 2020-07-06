###
```
rpm -qa | grep xrt
rpm -qa | grep xilinx
/tools/xgs/bin/sudo  -i
rpm -e xilinx-u50-gen3x4-xdma-base-2-2895184.noarch
rpm -e xilinx-u50-gen3x4-xdma-validate-2-2889074.noarch
rpm -e xilinx-u50-gen3x4-xdma-2-202010-1-dev-1-2895797.noarch

#sudo yum-complete-transaction --cleanup-only
#sudo yum remove -y xrt

#sudo yum install -y /proj/xbuilds/2020.1_0527_1/xbb/xrt/packages/xrt_202010.2.6.655_7.4.1708-x86_64-xrt.rpm
#sudo yum install -y /proj/xbuilds/2020.1_0622_1910/xbb/packages/internal_platforms/cmc/u50/xilinx-cmc-u50-1.0.20-2853996.noarch.rpm
#sudo yum install -y /proj/xbuilds/2020.1_0622_1910/xbb/packages/internal_platforms/sc-fw/u50/xilinx-sc-fw-u50-5.0.27-2.e289be9.noarch.rpm

yum install -y /proj/xbuilds/2020.1_0622_1910/xbb/packages/internal_platforms/u50/gen3x4_xdma/validate/xilinx-u50-gen3x4-xdma-validate-2-2902115.noarch.rpm
yum install -y /proj/xbuilds/2020.1_0622_1910/xbb/packages/internal_platforms/u50/gen3x4_xdma/base/xilinx-u50-gen3x4-xdma-base-2-2902115.noarch.rpm
yum install -y /proj/xbuilds/2020.1_0622_1910/xbb/packages/internal_platforms/u50/gen3x4_xdma/2-202010-1-dev/xilinx-u50-gen3x4-xdma-2-202010-1-dev-1-2902115.noarch.rpm
/opt/xilinx/xrt/bin/xbmgmt flash --update --shell xilinx_u50_gen3x4_xdma_base_2


```
