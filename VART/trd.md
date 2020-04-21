# software for trd.

## replace driver


```
sshpass -p root ssh root@10.176.178.108
mkdir /home/root/wcy;
cd /home/root/wcy;
rmmod dpu; # remove dpu 2.0
```

on host

```
sshpass -p root scp /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/dpu_bsp/dpu/files/dpu.ko root@10.176.178.108:/home/root/wcy
```

on board

```
insmod /home/root/wcy/dpu.ko
dmesg
ls -l /sys/module/dpu # if you see parameters, you are on the right track
cat /sys/module/dpu/parameters/version # double confirm
# DPU Driver version 3.0.0
# Build Label: Mar 25 2020 04:46:51
```


## install models

on host

```
sshpass -p root  scp /scratch/chunywan/vitis_ai_model_ZCU102_2019.2-r1.1.0.deb root@10.176.178.108:/home/root/wcy
```


on board
```
cd /home/root/wcy
dpkg -i vitis_ai_model_ZCU102_2019.2-r1.1.0.deb
```

## run the samples

on host

```
sshpass -p root scp  /home/chunywan/build/build.linux.2019.2.aarch64.Debug/vart/dpu-runner/test/resnet50.tar.gz root@10.176.178.108:/home/root/wcy
sshpass -p root scp /scratch/chunywan/images/samples/classification/sample_classification.jpg root@10.176.178.108:/home/root/wcy

```

on board

```
cd /home/root/wcy
tar -zxvf resnet50.tar.gz

cd /home/root//wcy/samples/bin
cp -av /usr/share/vitis_ai_library/models/resnet50/resnet50.elf .


% env LD_LIBRARY_PATH=../lib ./resnet50 /home/root/wcy/sample_classification.jpg
score[109]  =  0.982666     text: brain coral,
score[973]  =  0.00850172   text: coral reef,
score[955]  =  0.00662115   text: jackfruit, jak, jack,
score[397]  =  0.000543497  text: puffer, pufferfish, blowfish, globefish,
score[390]  =  0.000329648  text: eel,

~/wcy/samples/bin# cat /proc/interrupts | grep dpu
 51:          2          0          0          0     GICv2 138 Edge      dpu_isr
 52:          0          0          0          0     GICv2 139 Edge      dpu_isr
 53:          0          0          0          0     GICv2 140 Edge      dpu_isr
 59:          0          0          0          0     GICv2 142 Edge      dpu_smfc
```


``` console
% sshpass -p root ssh root@10.176.178.107
% cd ~/xdd/samples/bin;ls
% cp -av ../lib/libvart-dpu-controller.* /usr/lib
% cd /home/root/xdd/overview/samples/facedetect;ls
% ./test_jpeg_facedetect densebox_640_360 sample_facedetect.jpg
```
end mark
