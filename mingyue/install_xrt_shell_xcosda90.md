

```
ssh mingyue@xcosda90
cd ~/d/working/mingyue
mkdir u50_2020.1
cd u50_2020.1
mkdir rpm
cd rpm

cp /proj/xbuilds/2020.1_daily_latest/xbb/xrt/packages/xrt_202010.2.6.655_8.1.1911-x86_64-xrt.rpm ./
cp /proj/xbuilds/2020.1_daily_latest/xbb/packages/internal_platforms/cmc/u50/xilinx-cmc-u50-1.0.20-2853996.noarch.rpm ./
cp /proj/xbuilds/2020.1_daily_latest/xbb/packages/internal_platforms/sc-fw/u50/xilinx-sc-fw-u50-5.0.27-2.e289be9.noarch.rpm ./
cp /proj/xbuilds/2020.1_0526_1/xbb/packages/internal_platforms/u50/gen3x4_xdma/validate/xilinx-u50-gen3x4-xdma-validate-2-2889074.noarch.rpm ./
cp /proj/xbuilds/2020.1_0526_1/xbb/packages/internal_platforms/u50/gen3x4_xdma/base/xilinx-u50-gen3x4-xdma-base-2-2895184.noarch.rpm ./
cp /proj/xbuilds/2020.1_0526_1/xbb/packages/internal_platforms/u50/gen3x4_xdma/2-202010-1-dev/xilinx-u50-gen3x4-xdma-2-202010-1-dev-1-2895797.noarch.rpm ./


/tools/xgs/bin/sudo -i
rpm -qa | grep xilinx

yum-complete-transaction --cleanup-only; yum remove -y xrt
cd /home/mingyue/d/working/mingyue/u50_2020.1/rpm

ls
yum install -y xrt_202010.2.6.655_8.1.1911-x86_64-xrt.rpm --skip-broken
yum install -y xilinx-cmc-u50-1.0.20-2853996.noarch.rpm
yum install -y xilinx-sc-fw-u50-5.0.27-2.e289be9.noarch.rpm
yum install -y xilinx-u50-gen3x4-xdma-validate-2-2889074.noarch.rpm
yum install -y xilinx-u50-gen3x4-xdma-base-2-2895184.noarch.rpm
yum install -y xilinx-u50-gen3x4-xdma-2-202010-1-dev-1-2895797.noarch.rpm

/opt/xilinx/xrt/bin/xbmgmt flash --update --shell xilinx_u50_gen3x4_xdma_base_2

exit
ssh mingyue@xcosdxbf
/proj/sdxbf/prod/cmbin/util/bnreboot.py xcosda90 --wait


ssh xcosda90
cd /home/mingyue/d/working/mingyue/u50_2020.1/xclbin
scp mingyue@xcdl190074:/group/dphi_cloud/workspace/v3e_rel/vai1.2_for_u50/dpu_vitis_2020shell/rtl_kernels/rtl_v3e/dpu.xclbin ./
scp mingyue@xcdl190074:/group/dphi_cloud/workspace/v3e_rel/vai1.2_for_u50/dpu_vitis_2020shell/rtl_kernels/rtl_v3e/hbm_address_assignment.txt ./
/tools/xgs/bin/sudo /opt/xilinx/xrt/bin/xbutil flash scan
ls
/opt/xilinx/xrt/bin/xbutil program -d 0 -p dpu.xclbin

```

## software rsync by xcosda142
```
cd /usr/
/tools/xgs/bin/sudo rsync -a mingyue@xcosda142:/usr/local .
cd /opt/rh
/tools/xgs/bin/sudo rsync -a mingyue@xcosda142:/opt/rh/devtoolset-9 .
/tools/xgs/bin/sudo scp mingyue@xcosda142:/usr/lib64/libjson* /usr/lib64/
/tools/xgs/bin/sudo scp -r mingyue@xcosda142:/usr/include/json* /usr/include

```
