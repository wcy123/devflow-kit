```
$ cd /workspace/aisw/Vitis-AI-Library
$ unset LD_LIBRARY_PATH
$ source /opt/petalinux/2020.2/environment-setup-aarch64-xilinx-linux
$ make all
$ scp /home/build/resnet_v2_101_tf/dump_results_0/input_aquant.bin root@10.176.179.165:~/
$ scp ~/build/build.linux.2020.2.aarch64.Debug/vart/dpu-runner/test/test_dpu_runner root@10.176.179.165:~/
$ md5sum /home/build/resnet_v2_101_tf/dump_results_0/resnet_v2_101_predictions_Reshape_aquant.bin
$ ssh root@10.176.179.165
$ env DElBUG_DPU_RUNNER=1 XLNX_ENABLE_DUMP=1 ./test_dpu_runner /usr/share/vitis_ai_library/models/resnet_v2_101_tf/resnet_v2_101_tf.xmodel dpu_0 input_aquant.bin 1 1 2>a.log 1>&2
$md5sum dump/subgraph_resnet_v2_101_block1_unit_1_bottleneck_v2_add/output/0.resnet_v2_101_predictions_Reshape_aquant.bin

```
# run old xmodel
```
$ exit
$ scp /home/build/resnet_v2_101_tf/resnet_v2_101_tf.xmodel root@10.176.179.165:~/
$ ssh root@10.176.179.165
$ rm -rf dump
$ env DElBUG_DPU_RUNNER=1 XLNX_ENABLE_DUMP=1 ./test_dpu_runner resnet_v2_101_tf.xmodel dpu_0 input_aquant.bin 1 1 2>a.log 1>&2
$ md5sum dump/subgraph_resnet_v2_101_block1_unit_1_bottleneck_v2_add/output/0.resnet_v2_101_predictions_Reshape_aquant.bin


```
