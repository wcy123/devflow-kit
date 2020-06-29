# v4e edge

## build the model

``` console
% mkdir -p /var/lib/docker/scratch/chunywan/debug_v4e_edge/resnet50
% cd /var/lib/docker/scratch/chunywan/debug_v4e_edge/resnet50
% scp xcdl190253:/proj/xcdhdstaff2/jianweng/workspace/debug/ssd_vvdn_20200401/new_model/{deploy.caffemodel,deploy.prototxt} .
% ~/.local/bin/xnnc-run --type caffe --layout NCHW --model ./deploy.caffemodel --proto ./deploy.prototxt --out xnnc-run.xmodel
% $HOME/.local/Ubuntu.16.04.x86_64.Debug/bin/xcompiler -h
% $HOME/.local/Ubuntu.16.04.x86_64.Debug/bin/xcompiler -i xnnc-run.xmodel -o ssd_vvdn.xmodel  -a "0x50000000000002e"
% scp xcdl190253:/proj/xcdhdstaff2/jianweng/workspace/model_for_test/v4e/20200629_resnet_v1_50_VCK190_features_all_in/resnet_v1_50_compiled_DPUCVDX8H_PROTOTYPE_0_debug.xmodel .
```

##

``` console
% (cd /group/xbjlab/dphi_software/software/workspace/chunywan/petalinux-sdk2/sysroots/aarch64-xilinx-linux/install/Debug/ && tar -cf - lib bin) | sshpass -p root ssh root@10.176.179.54 tar -xvf - -C /home/root/wcy
% (cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/vart/xrt-device-handle/test/ && tar -cf - *) | sshpass -p root ssh root@10.176.179.54 tar -xvf - -C /home/root/wcy
```

``` console
% sshpass -p root ssh root@10.176.179.54
% mkdir -p wcy; cd wcy
% mkdir -p /group/xbjlab
% mount -t nfs -o nolock 10.176.178.33:/group_xbjlab/ /group/xbjlab
% scp chunywan@10.176.178.4:/var/lib/docker/scratch/chunywan/debug_v4e_edge/resnet50/resnet_v1_50_compiled_DPUCVDX8H_PROTOTYPE_0_debug.xmodel .
% /group/xbjlab/dphi_software/software/workspace/chunywan/petalinux-sdk2/sysroots/aarch64-xilinx-linux/install/Debug/bin/xir subgraph resnet_v1_50_compiled_DPUCVDX8H_PROTOTYPE_0_debug.xmodel | less
% /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Debug/xir/tools/xir subgraph resnet_v1_50_compiled_DPUCVDX8H_PROTOTYPE_0_debug.xmodel
% export LD_LIBRARY_PATH=/group/xbjlab/dphi_software/software/workspace/chunywan/petalinux-sdk2/sysroots/aarch64-xilinx-linux/install/Debug/lib
% env DEBUG_XRT_DEVICE_HANDLE=1 /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Debug/vart/./xrt-device-handle/test_xrt_device_handle dpu 0
% scp chunywan@10.176.178.15:/scratch/group/modelzoo/internal-cooperation-models/caffe/resnet50.baseline9213_ck/fix/acc/dump_gpu/data.bin .
% env XLNX_ENABLE_DUMP=1 XLNX_SHOW_DPU_COUNTER=1/group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Debug/vart/test/test_dpu_runner DEBUG_XRT_DEVICE_HANDLE=1 /group/xbjlab/dphi_software/software/workspace/chunywan/build/build.linux.2020.1.aarch64.Debug/vart/dpu-runner/test/test_dpu_runner resnet_v1_50_compiled_DPUCVDX8H_PROTOTYPE_0_debug.xmodel k_0 data.bin 1 1
% env DEBUG_DPU_CONTROLLER=1 DEBUG_AP_START_CU=1 XLNX_VART_FIRMARE="/media/card/package.xclbin" ~/Vitis-AI/vitis_ai_library/samples/classification/test_jpeg_classification  ~/vck-model-wj/0618/resnet_v1_50/resnet_v1_50_dpu_DPUCVDX8H-65536-1.xmodel ~/samples/classification/sample_classification.jpg
% xrt_read_register reg_cloud.conf dpu 0
% bin/xir subgraph ~/vck-model-wj/0618/resnet_v1_50/resnet_v1_50_dpu_DPUCVDX8H-65536-1.xmodel
% bin/xir dump_txt ~/vck-model-wj/0618/resnet_v1_50/resnet_v1_50_dpu_DPUCVDX8H-65536-1.xmodel a.txt
% bin/test_xrt_device_handle dpu 0
```
