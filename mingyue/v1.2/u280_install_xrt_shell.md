###
```
rpm -qa | grep xrt
rpm -qa | grep xilinx

sudo yum-complete-transaction --cleanup-only
sudo yum remove -y xrt

cd /home/mingyue/d/working/aisw/u280_rpm/pengbo
cp  /group/dphi_cloud/workspace/zhengpengbo/to_jennifer/* ./
ls
sudo yum install -y xrt_202010.2.6.655_7.4.1708-x86_64-xrt.rpm
sudo yum install -y xilinx-u280-xdma-201920.3-2789161.x86_64.rpm
sudo /opt/xilinx/xrt/bin/xbmgmt flash --update --shell xilinx_u280_xdma_201920_3
sudo yum install -y xilinx-u280-xdma-dev-201920.3-2789161.x86_64.rpm

cd ../
ls
sudo yum install -y /proj/xbuilds/2019.2_0409_1/xbb/dsabin/internal_platforms/xilinx_u280_xdma_201920_1/xilinx-u280-xdma-201920.1-2699728.x86_64.rpm

```






```
cd /proj/rdi/staff/mingyue/d/working/aisw/u280_rpm/v1.2_2020.1_xrt
ls
cp /proj/xbuilds/2020.1_0526_1/xbb/xrt/packages/xrt_202010.2.6.655_7.4.1708-x86_64-xrt.rpm ./
cp /proj/xbuilds/2020.1_0526_1/xbb/packages/internal_platforms/cmc/u50/xilinx-cmc-u50-1.0.20-2853996.noarch.rpm ./
cp /proj/xbuilds/2020.1_0526_1/xbb/packages/internal_platforms/sc-fw/u50/xilinx-sc-fw-u50-5.0.27-2.e289be9.noarch.rpm ./

#ls /proj/xbuilds/2020.1*/xbb/dsadev/opt/xilinx/platforms/*u280*201920_3/ -d1
cp /proj/xbuilds/2020.1_0526_1/xbb/dsabin/internal_platforms/xilinx_u280_xdma_201920_3/xilinx-u280-xdma-201920.3-2849448.x86_64.rpm ./
cp /proj/xbuilds/2020.1_0526_1/xbb/dsadev/internal_platforms/xilinx_u280_xdma_201920_3/xilinx-u280-xdma-dev-201920.3-2849448.x86_64.rpm ./

```
