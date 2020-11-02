###
```
ssh xcdsda27
rpm -qa | grep xrt
rpm -qa | grep xilinx

sudo yum-complete-transaction --cleanup-only
sudo yum remove -y xrt

sudo yum install -y /proj/xbuilds/2020.2_1013_1/xbb/xrt/packages/xrt_202020.2.8.606_7.4.1708-x86_64-xrt.rpm
sudo yum install -y /proj/xbuilds/2020.2_1013_1/xbb/packages/internal_platforms/cmc/u50/xilinx-cmc-u50-1.0.26-3021399.noarch.rpm
sudo yum install -y /proj/xbuilds/2020.2_1013_1/xbb/packages/internal_platforms/sc-fw/u50/xilinx-sc-fw-u50-5.1.7-1.f121ae9.noarch.rpm
sudo yum install -y /proj/xbuilds/2020.2_1013_1/xbb/packages/internal_platforms/u50lv/gen3x4_xdma/validate/xilinx-u50lv-gen3x4-xdma-validate-2-2902115.noarch.rpm
sudo yum install -y /proj/xbuilds/2020.2_1013_1/xbb/packages/internal_platforms/u50lv/gen3x4_xdma/base/xilinx-u50lv-gen3x4-xdma-base-2-2902115.noarch.rpm
sudo /opt/xilinx/xrt/bin/xbmgmt flash --update --shell xilinx_u50lv_gen3x4_xdma_base_2
sudo yum install -y /proj/xbuilds/2020.2_1013_1/xbb/packages/internal_platforms/u50lv/gen3x4_xdma/2-202010-1-dev/xilinx-u50lv-gen3x4-xdma-2-202010-1-dev-1-2902115.noarch.rpm

ssh mingyue@xcdengvm244021
/proj/sdxbf/prod/cmbin/util/bnreboot.py --wait xcdsda23

/tools/xgs/bin/sudo /opt/xilinx/xrt/bin/xbmgmt flash --scan
/tools/xgs/bin/sudo /opt/xilinx/xrt/bin/xbmgmt flash --factory_reset

cd /home/mingyue/d/working/aisw/vart-xclbins/v1.3/u50lv/9E275M
sudo cp 20201015/dpu.xclbin /usr/lib/
/opt/xilinx/xrt/bin/xbutil program -d 0 -p dpu.xclbin
/opt/xilinx/xrt/bin/xbutil query



```
