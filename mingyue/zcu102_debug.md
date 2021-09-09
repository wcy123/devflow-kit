## compile Vitis AI
##  b0： 10.176.179.62  /etc/hosts
```

$ cd /workspace/aisw/Vitis-AI-Library
$ unset LD_LIBRARY_PATH
$ source /opt/petalinux/2021.1/environment-setup-cortexa72-cortexa53-xilinx-linux
$ bash -ex build_all.sh --type=release

```

## copy BOOT.BIN & dpu.xclbin
```
% cd ~/build
% scp mingyue@xcdl190260:/proj/rdi/staff/jiaz/scout/temp/xdpu_mingyue/prj/Vitis/binary_container_1/sd_card/dpu.xclbin zcu102_debug/
% scp mingyue@xcdl190260:/proj/rdi/staff/jiaz/scout/temp/xdpu_mingyue/prj/Vitis/binary_container_1/sd_card/BOOT.BIN zcu102_debug/

% md5sum zcu102_debug/*
% scp zcu102_debug/* root@b0:~/0625/
```

## update BOOT.BIN & dpu.xclbin
```
% sshpass -p root ssh root@b0
% md5sum ~/0625/*
% cd /mnt/sd-mmcblk0p1/
% mv BOOT.BIN BOOT.BIN.OLD
% mv dpu.xclbin dpu.xclbin.old
% cp ~/0625/* .
% md5sum dpu.xclbin BOOT.BIN
% sync
% reboot
```

## test  FPN_Res18_Medical_segmentation
```
% sshpass -p root ssh root@b0
% xdputil query
% env LOG_ERROR_COUNTER=1 SAVE_ERROR_OUTPUT_TO_FILE=1 SAVE_INPUT_TO_FILE=1 SAME_INPUT=1 xdputil benchmark /usr/share/vitis_ai_library/models/FPN-resnet18_Endov/FPN-resnet18_Endov.xmodel -i 0 1

% bash
%

```
