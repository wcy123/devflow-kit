###
```
ssh xcdsda27
rpm -qa | grep xrt
rpm -qa | grep xilinx

sudo yum-complete-transaction --cleanup-only
sudo yum remove -y xrt

sudo yum install -y /proj/xbuilds/2020.1_0527_1/xbb/xrt/packages/xrt_202010.2.6.655_7.4.1708-x86_64-xrt.rpm
sudo yum install -y /proj/xbuilds/2020.1_0622_1910/xbb/packages/internal_platforms/cmc/u50/xilinx-cmc-u50-1.0.20-2853996.noarch.rpm
sudo yum install -y /proj/xbuilds/2020.1_0622_1910/xbb/packages/internal_platforms/sc-fw/u50/xilinx-sc-fw-u50-5.0.27-2.e289be9.noarch.rpm
sudo yum install -y /proj/xbuilds/2020.1_0622_1910/xbb/packages/internal_platforms/u50lv/gen3x4_xdma/validate/xilinx-u50lv-gen3x4-xdma-validate-2-2902115.noarch.rpm
sudo yum install -y /proj/xbuilds/2020.1_0622_1910/xbb/packages/internal_platforms/u50lv/gen3x4_xdma/base/xilinx-u50lv-gen3x4-xdma-base-2-2902115.noarch.rpm
sudo /opt/xilinx/xrt/bin/xbmgmt flash --update --shell xilinx_u50lv_gen3x4_xdma_base_2
sudo yum install -y /proj/xbuilds/2020.1_0622_1910/xbb/packages/internal_platforms/u50lv/gen3x4_xdma/2-202010-1-dev/xilinx-u50lv-gen3x4-xdma-2-202010-1-dev-1-2902115.noarch.rpm

ssh mingyue@xcdengvm244021
/proj/sdxbf/prod/cmbin/util/bnreboot.py --wait xcdsda30

cd /home/mingyue/d/working/aisw/vart-xclbins/v1.2/u50lv/9E275M
mkdir 20200706
cd 20200706
cp /group/dphi_cloud/workspace/v3e_rel/U50LV/dpu_vitis_9e_65p_0622shell/rtl_kernels/rtl_v3e/dpuhack.xclbin dpu.xclbin
cp /group/dphi_cloud/workspace/v3e_rel/U50LV/dpu_vitis_9e_65p_0622shell/rtl_kernels/rtl_v3e/hbm_address_assignment.txt ./
ls
md5sum * > md5sum.txt
/opt/xilinx/xrt/bin/xbutil program -d 0 -p dpu.xclbin
sudo cp dpu.xclbin hbm_address_assignment.txt /usr/lib/

xcdsda28: 10E
cd ../../
cd 10E275M
mkdir 20200706
cd 20200706
cp /group/dphi_cloud/workspace/v3e_rel/U50LV/dpu_vitis_10e_159p_0622shell/rtl_kernels/rtl_v3e/dpuhack.xclbin dpu.xclbin
cp /group/dphi_cloud/workspace/v3e_rel/U50LV/dpu_vitis_10e_159p_0622shell/rtl_kernels/rtl_v3e/hbm_address_assignment.txt ./
md5sum * >md5sum.txt

/opt/xilinx/xrt/bin/xbutil program -d 0 -p dpu.xclbin
sudo cp dpu.xclbin hbm_address_assignment.txt /usr/lib/
```
