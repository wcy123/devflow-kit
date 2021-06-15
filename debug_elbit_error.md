``` console
% rsync -avz /opt/petalinux/2021.1/sysroots/cortexa72-cortexa53-xilinx-linux/install b0:/home/wcy/
% rsync -avz $(find ~/build/build.linux.2021.1.aarch64.Release/vart/ -type f  -iname 'test*' -executable) b0:/home/wcy/
% ssh b0
% cd /home/wcy/install/Release; ls -l
% env LD_LIBRARY_PATH=/home/wcy/install/Release/lib /home/wcy/test_buffer_object 1024 1024
% env LD_LIBRARY_PATH=/home/wcy/install/Release/lib /home/wcy/test_bin_stream /media/sd-mmcblk0p1/dpu.xclbin
% cd /home/wcy;
% scp root@10.176.179.73:/usr/share/vitis_ai_library/models/resnet50/resnet50.xmodel .
% env DEBUG_DPU_RUNNER=1 XLNX_SHOW_DPU_COUNTER=1 LD_LIBRARY_PATH=/home/wcy/install/Release/lib /home/wcy/test_dpu_runner ./resnet50.xmodel b_0 ./resnet50.xmodel 1 1

```


platform1

``` console
% rsync -avz /opt/petalinux/2020.2/sysroots/aarch64-xilinx-linux/install/Release b0:/run/
% rsync -avz $(find ~/build/build.linux.2020.2.aarch64.Release/vart/ -type f  -iname 'test*' -executable) b0:/run
% ssh b0
% cd /tmp
% which xdputil
% mkdir -p /home/wcy/install
% ls -l /run/Release/lib
% /usr/bin/xdputil
% env LD_LIBRARY_PATH=/run/Release/lib xdputil run /usr/share/vitis_ai_library/models/ML-2784-elbit_224x224/ML-2784-elbit_224x224.xmodel -i 0 /group/xbjlab/dphi_software/software/workspace/qiuyuny/sft_versal_bs/workspace/sw_pipeline_debug/input_bin/golden/4c/64ee8d0de09dcf71c9d97072428021
% env DEBUG_DPU_RUNNER=1 LD_LIBRARY_PATH=/run/Release/lib xdputil run /usr/share/vitis_ai_library/models/ML-2784-elbit_224x224/ML-2784-elbit_224x224.xmodel -i 0 /group/xbjlab/dphi_software/software/workspace/qiuyuny/sft_versal_bs/workspace/sw_pipeline_debug/input_bin/golden/4c/64ee8d0de09dcf71c9d97072428021
% env DEBUG_DPU_RUNNER=1 LD_LIBRARY_PATH=/run/Release/lib /run/test_dpu_runner /usr/share/vitis_ai_library/models/ML-2784-elbit_224x224/ML-2784-elbit_224x224.xmodel b_0 /group/xbjlab/dphi_software/software/workspace/qiuyuny/sft_versal_bs/workspace/sw_pipeline_debug/input_bin/golden/4c/64ee8d0de09dcf71c9d97072428021 1 1

% mkdir -p /tmp/ref/
% cp /group/xbjlab/dphi_software/software/workspace/qiuyuny/sft_versal_bs/workspace/sw_pipeline_debug/input_bin/golden/4c/64ee8d0de09dcf71c9d97072428021 /tmp/ref/input_2_aquant.bin
```

# check model

```
% xir dump_txt /usr/share/vitis_ai_library/models/ML-2784-elbit_224x224/ML-2784-elbit_224x224.xmodel /usr/share/vitis_ai_library/models/ML-2784-elbit_224x224/ML-2784-elbit_224x224.txt
% grep 60149a483e9998edf51d80d021e740a5 /usr/share/vitis_ai_library/models/ML-2784-elbit_224x224/ML-2784-elbit_224x224.txt
%
```

# init your shell

``` console
% bash # diff <() <() requires bash
% ssh b0
% bash
% mkdir -p  /group/xbjlab; mount -t nfs -o nolock 10.176.178.33:/group_xbjlab/ /group/xbjlab
% function d() { \
    for i in $@; do  \
        md5sum $i; stat -c %s $i; xxd $i | head -n 16; \
    done \
} \

```


``` useless
% env DEBUG_DPU_RUNNER=1 LD_LIBRARY_PATH=/run/Release/lib /run/Release/share/vitis_ai_library/test/graph_runner/test_graph_runner -i 1 /usr/share/vitis_ai_library/models/ML-2784-elbit_224x224/ML-2784-elbit_224x224.xmodel ; \
```

``` console
% cd /tmp
% env DEBUG_DPU_RUNNER=1 LD_LIBRARY_PATH=/run/Release/lib xdputil run /usr/share/vitis_ai_library/models/ML-2784-elbit_224x224/ML-2784-elbit_224x224.xmodel -i 0 /group/xbjlab/dphi_software/software/workspace/qiuyuny/sft_versal_bs/workspace/sw_pipeline_debug/input_bin/golden/4c/64ee8d0de09dcf71c9d97072428021;  md5sum *.scale_out_BiasAdd_aquant.bin ; \
  diff -u <(xxd 0.scale_out_BiasAdd_aquant.bin) <(xxd 1.scale_out_BiasAdd_aquant.bin); \
  diff -u <(xxd 0.scale_out_BiasAdd_aquant.bin) <(xxd 2.scale_out_BiasAdd_aquant.bin); \
  xdputil mem -r $((0x840060000)) 78196 dump_instr_mc_sw.bin && \
  xdputil mem -r $((0x840140000)) 150528 i0.bin && \
  xdputil mem -r $((0x840180000)) 150528 i1.bin && \
  xdputil mem -r $((0x8401c0000)) 150528 i2.bin && \
  xdputil mem -r $((0x840050000)) 50176 b0.bin && \
  xdputil mem -r $((0x8400d0000)) 50176 b1.bin && \
  xdputil mem -r $((0x8400e0000)) 50176 b2.bin && \
  md5sum i0.bin i1.bin i2.bin b0.bin b1.bin b2.bin dump_instr_mc_sw.bin  *.scale_out_BiasAdd_aquant.bin
```

fix bug in `run.py`

```
% scp /workspace/aisw/Vitis-AI-Library/usefultools/python/xdputil_component/run.py b0:/usr/lib/python3.7/site-packages/xdputil_component/
```
