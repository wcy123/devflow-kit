## software rsync by xcdsda28
```
ssh xcdsda30
cd /usr/
sudo rsync -a mingyue@xcdsda28:/usr/local .
cd /opt/rh
sudo rsync -a mingyue@xcdsda28:/opt/rh/devtoolset-9 .
sudo scp mingyue@xcdsda28:/usr/lib64/libjson* /usr/lib64/
sudo scp -r mingyue@xcdsda28:/usr/include/json* /usr/include

```


### xrt & shell install
```

sudo -i
rpm -qa | grep xilinx

yum-complete-transaction --cleanup-only;

yum remove -y xrt


yum install -y /proj/xbuilds/2020.1_0526_1/xbb/xrt/packages/xrt_202010.2.6.655_7.4.1708-x86_64-xrt.rpm
yum install -y /proj/xbuilds/2020.1_0526_1/xbb/packages/internal_platforms/cmc/u50/xilinx-cmc-u50-1.0.20-2853996.noarch.rpm  --skip-broken
yum install -y /proj/xbuilds/2020.1_0526_1/xbb/packages/internal_platforms/sc-fw/u50/xilinx-sc-fw-u50-5.0.27-2.e289be9.noarch.rpm

yum install -y /proj/xbuilds/2020.1_0526_1/xbb/packages/internal_platforms/u50lv/gen3x4_xdma/validate/xilinx-u50lv-gen3x4-xdma-validate-2-2889072.noarch.rpm
yum install -y /proj/xbuilds/2020.1_0526_1/xbb/packages/internal_platforms/u50lv/gen3x4_xdma/base/xilinx-u50lv-gen3x4-xdma-base-2-2895310.noarch.rpm
/opt/xilinx/xrt/bin/xbmgmt flash --update --shell xilinx_u50lv_gen3x4_xdma_base_2
yum install -y /proj/xbuilds/2020.1_0526_1/xbb/packages/internal_platforms/u50lv/gen3x4_xdma/2-202010-1-dev/xilinx-u50lv-gen3x4-xdma-2-202010-1-dev-1-2900293.noarch.rpm

exit
ssh mingyue@xcdengvm244021
/proj/sdxbf/prod/cmbin/util/bnreboot.py --wait xcdsda30
```
