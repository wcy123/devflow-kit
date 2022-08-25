```

xcdl190074 copy xmodel -> xbjjmphost01 -> 10.176.178.111

% ssh mingyue@xbjjmphost01

% ssh root@10.176.178.111

show xmodel subgrahs
% xdputil xmodel -l xxx.xmodel
% env XLNX_ENABLE_FINGERPRINT_CHECK=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=1 xdputil run xxx.xmodel inout1.bin input2.bin -i 2


% mount -t nfs -o nolock 10.176.178.33:/group_xbjlab/ /group/xbjlab
% cp /group/xbjlab/dphi_edge/weizhic/20220713/C32B3/dpu.xclbin /run/media/mmcblk0p1/
% cp /group/xbjlab/dphi_edge/weizhic/20220713/C32B3/BOOT.BIN /run/media/mmcblk0p1/
% sync
% sync
% reboot

% mount -t nfs -o nolock 10.176.178.33:/group_xbjlab/ /group/xbjlab
% cp /group/xbjlab/dphi_edge/weizhic/20220713/C32B6/dpu.xclbin /run/media/mmcblk0p1/
% cp /group/xbjlab/dphi_edge/weizhic/20220713/C32B6/BOOT.BIN /run/media/mmcblk0p1/
% sync
% sync
% reboot





```
