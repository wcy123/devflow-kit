## login test board by ssh
```
sshpass -p root ssh root@10.176.179.54
vart_version


```
## test one image
```
## test image & xmodel : /group/xbjlab/dphi_software/software/workspace/mingyue/d/working/xvdpu
cd ~/classification
/usr/share/vitis_ai_library/samples/classification/test_jpeg_classification xvdpu_1.5_resnet_v1_50_prefetch sample_classification.jpg

```
WARNING: Logging before InitGoogleLogging() is written to STDERR
I0414 00:02:10.499278   843 process_result.hpp:25] r.index 109 brain coral, r.score 0.985991
I0414 00:02:10.499653   843 process_result.hpp:25] r.index 973 coral reef, r.score 0.0109534
I0414 00:02:10.499773   843 process_result.hpp:25] r.index 397 puffer, pufferfish, blowfish, globefish, r.score 0.000899108
I0414 00:02:10.499934   843 process_result.hpp:25] r.index 5 electric ray, crampfish, numbfish, torpedo, r.score 0.000899108
I0414 00:02:10.500095   843 process_result.hpp:25] r.index 115 sea slug, nudibranch, r.score 0.000330763

### test performance
```
/usr/share/vitis_ai_library/samples/classification/test_performance_classification xvdpu_1.5_resnet_v1_50_prefetch test_performance_classification.list -t 4 -s 60

```
root@xilinx-vck190-2020_1:~/classification# /usr/share/vitis_ai_library/samples/classification/test_performance_classification xvdpu_1.5_resnet_v1_50_prefetch test_performance_classification.list -t 4 -s 60
WARNING: Logging before InitGoogleLogging() is written to STDERR
I0414 00:06:40.583143   867 benchmark.hpp:176] writing report to <STDOUT>
I0414 00:06:41.129499   867 benchmark.hpp:203] waiting for 0/60 seconds, 4 threads running
I0414 00:06:51.129621   867 benchmark.hpp:203] waiting for 10/60 seconds, 4 threads running
I0414 00:07:01.129749   867 benchmark.hpp:203] waiting for 20/60 seconds, 4 threads running
I0414 00:07:11.129878   867 benchmark.hpp:203] waiting for 30/60 seconds, 4 threads running
I0414 00:07:21.130005   867 benchmark.hpp:203] waiting for 40/60 seconds, 4 threads running
I0414 00:07:31.130140   867 benchmark.hpp:203] waiting for 50/60 seconds, 4 threads running
I0414 00:07:41.130334   867 benchmark.hpp:211] waiting for threads terminated
FPS=1567.02
E2E_MEAN=7650.41
DPU_MEAN=5580.37

##

```
env XLNX_ENABLE_DUMP=1 ./test_dpu_runner classification/xvdpu_1.5_resnet_v1_50_prefetch/xvdpu_1.5_resnet_v1_50_prefetch.xmodel  xvdpu_1.5_resnet_v1_50_prefetch_0 subgraph_1_input_image_aquant_vart-sim-runner.bin 1 1
env XLNX_ENABLE_DUMP=1 ./test_dpu_runner xvdpu.xmodel  xvdpu_1.5_resnet_v1_50_prefetch_0 subgraph_1_input_image_aquant_vart-sim-runner.bin 1 1

env XLNX_ENABLE_DUMP=0 ./test_dpu_runner classification/xvdpu_1.5_resnet_v1_50_prefetch/xvdpu_1.5_resnet_v1_50_prefetch.xmodel  xvdpu_1.5_resnet_v1_50_prefetch_0 subgraph_1_input_image_aquant_vart-sim-runner.bin 1 10000

./xrt_read_register reg_edge_1.conf DPU 0
./xrt_read_register reg_edge.conf DPU 0
./xrt_read_register reg_xvdpu.conf D 0

./test_dpu_runner_mt classification/xvdpu_1.5_resnet_v1_50_prefetch/xvdpu_1.5_resnet_v1_50_prefetch.xmodel xvdpu_1.5_resnet_v1_50_prefetch_0 1
./test_dpu_runner_mt classification/xvdpu_1.5_resnet_v1_50_prefetch/xvdpu_1.5_resnet_v1_50_prefetch.xmodel xvdpu_1.5_resnet_v1_50_prefetch_0 4


./test_dpu_runner_mt Resnet50_v1.5_pruned_74.xmodel xvdpu_1.5_resnet_v1_50_prefetch_0 4
cd classification/

```
```
 md5sum dump/subgraph_fake_downsample_0_ReplaceConv2d/input/*.bin
 md5sum dump/subgraph_fake_downsample_0_ReplaceConv2d/output/*.bin
```


##176
```
ssh root@10.176.178.176
/group/xbjlab/dphi_software/software/workspace/mingyue/build/build.linux.2020.1.aarch64.Release/vart/


/group/xbjlab/dphi_software/software/workspace/mingyue/build/build.linux.2020.1.aarch64.Release/vart/xrt-device-handle/xrt_read_register reg_edge.conf DPU 0


sshpass -p root ssh root@10.176.179.54
cd /mnt/sd-mmcblk0p1/
cp BOOT.BIN.0909 BOOT.BIN
cp DPUCVDX8G_final_20200909.xclbin /usr/lib/dpu.xclbin
md5sum /usr/lib/dpu.xclbin /mnt/sd-mmcblk0p1/BOOT.BIN
sync
reboot


```

##pruned model test
```
## copy data from : home/mingyue/d/working/dpdlf/xvdpu/pb/Resnet50_v1.5_pruned_74/
env XLNX_ENABLE_DUMP=1 ./test_dpu_runner Resnet50_v1.5_pruned_74.xmodel Resnet50_v1.5_pruned_74_0 input_tensor_aquant.bin 1 1
./test_dpu_runner_mt Resnet50_v1.5_pruned_74.xmodel Resnet50_v1.5_pruned_74_0 1
./test_dpu_runner_mt Resnet50_v1.5_pruned_74.xmodel Resnet50_v1.5_pruned_74_0 4

cd ~/classification
/usr/share/vitis_ai_library/samples/classification/test_performance_classification Resnet50_v1.5_pruned_74 test_performance_classification.list -t 4 -s 60
```

```
cd /home/mingyue/d/working/dpdlf/xvdpu/xvdpu_bit
mkdir 0914
cd 0914
scp mingyue@xcdl190074:/group/dphi_edge/workspace/davidxu/share/versal_bootbin/xvdpu_v0_2_0_00_333M_opt_load_0914/sd_card/DPUCVDX8G_final_20200914.xclbin ./
scp mingyue@xcdl190074:/group/dphi_edge/workspace/davidxu/share/versal_bootbin/xvdpu_v0_2_0_00_333M_opt_load_0914/sd_card/BOOT.BIN ./
md5sum *
pwd
scp DPUCVDX8G_final_20200914.xclbin BOOT.BIN root@10.176.179.54:/mnt/sd-mmcblk0p1/
```



## yolov3_voc
```
scp -r mingyue@xcdl190074:/group/modelzoo/internal-cooperation-models/caffe/yolov3_voc/fix/acc/dump_gpu /home/mingyue/d/working/xvdpu/yolov3/yolov3_voc/
cp /home/mingyue/d/working/dpdlf/xvdpu/pb/yolov3_voc/yolov3_voc.xmodel /home/mingyue/d/working/xvdpu/yolov3/yolov3_voc/
scp -r /home/mingyue/d/working/xvdpu/yolov3 root@10.176.179.54:~/


env XLNX_ENABLE_FINGERPRINT_CHECK=0 XLNX_ENABLE_DUMP=1 ./test_dpu_runner yolov3/yolov3_voc/yolov3_voc.xmodel yolov3_voc_0 yolov3/yolov3_voc/dump_gpu/data_fixed.bin 1 1 2>debug.log 1>&2
md5sum dump/subgraph_layer0_conv/input/*.bin
md5sum dump/subgraph_layer0_conv/output/*.bin

env XLNX_ENABLE_FINGERPRINT_CHECK=0 XLNX_GOLDEN_DIR=yolov3/yolov3_voc/dump_gpu XLNX_ENABLE_DEBUG_MODE=1 XLNX_ENABLE_UPLOAD=0 XLNX_ENABLE_DUMP=1 ./test_dpu_runner yolov3/yolov3_voc/yolov3_voc.xmodel yolov3_voc_0 yolov3/yolov3_voc/dump_gpu/data_fixed.bin 1 1 2>debug.log 1>&2
grep 'XLNX_GOLDEN_DIR: compare data fail' debug.log

```

## yolov3_voc_tf
```
env XLNX_ENABLE_FINGERPRINT_CHECK=0 XLNX_ENABLE_DUMP=1 ./test_dpu_runner yolov3/yolov3_voc_tf/yolov3_voc_tf.xmodel yolov3_voc_0

```
