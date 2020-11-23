#!/bin/bash
boot_bin=$1
dpu_xclbin_bin=$2
tmpdir=/tmp/$USER/xxx
mkdir -p $tmpdir/mnt/sd-mmcblk0p1/
cp -av "${boot_bin}"  $tmpdir/mnt/sd-mmcblk0p1/BOOT.BIN
mkdir -p $tmpdir/usr/lib
cp -av "${dpu_xclbin_bin}"  $tmpdir/usr/lib/dpu.xclbin
(cd $tmpdir; md5sum  mnt/sd-mmcblk0p1/BOOT.BIN usr/lib/dpu.xclbin | tee hw.md5)
(cd $tmpdir; tar -czf - mnt/sd-mmcblk0p1/BOOT.BIN usr/lib/dpu.xclbin hw.md5 |
ssh -J xcdl190074,xbjjmphost02,xbjlabdpsvr15 root@10.176.179.54 /bin/tar -zvxf - -C /)
ssh -J xcdl190074,xbjjmphost02,xbjlabdpsvr15 root@10.176.179.54 "cd /&&cat hw.md5 && md5sum -c hw.md5 && sync&&sync&&sync&& /sbin/reboot"

#ssh -J xcdl190074,xbjjmphost02,xbjlabdpsvr15 root@10.176.179.54 "bash -ex run.sh 0"
