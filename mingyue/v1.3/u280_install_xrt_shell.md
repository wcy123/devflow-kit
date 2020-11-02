###
```
ssh xcdsda24
rpm -qa | grep xrt
rpm -qa | grep xilinx

sudo yum-complete-transaction --cleanup-only
sudo yum remove -y xrt

sudo yum install -y /proj/xbuilds/2020.2_1013_1/xbb/xrt/packages/xrt_202020.2.8.606_7.4.1708-x86_64-xrt.rpm


sudo yum install -y /proj/xbuilds/2020.2_1013_1/xbb/dsabin/customer_platforms/xilinx_u280_xdma_201920_3/xilinx-u280-xdma-201920.3-2849448.noarch.rpm
sudo yum install -y /proj/xbuilds/2020.2_1013_1/xbb/dsadev/internal_platforms/xilinx_u280_xdma_201920_3/xilinx-u280-xdma-dev-201920.3-2849448.x86_64.rpm
sudo /opt/xilinx/xrt/bin/xbmgmt flash --update --shell xilinx_u50lv_gen3x4_xdma_base_2

ssh mingyue@xcdengvm244021
/proj/sdxbf/prod/cmbin/util/bnreboot.py --wait xcdsda24



cd /home/mingyue/d/working/aisw/vart-xclbins/v1.3/u280/14E300M
sudo cp 20201015/dpu.xclbin /usr/lib/
/opt/xilinx/xrt/bin/xbutil program -d 0 -p /usr/lib/dpu.xclbin
/opt/xilinx/xrt/bin/xbutil query


```
