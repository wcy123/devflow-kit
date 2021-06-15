
platform1

``` console
% rsync -avz /opt/petalinux/2020.2/sysroots/aarch64-xilinx-linux/install/Release b0:/run/
% rsync -avz $(find ~/build/build.linux.2020.2.aarch64.Release/vart/ -type f  -executable) b0:/run
% rsync -avz /workspace/aisw/vart/xrt-device-handle/test/reg_xvdpu_hack.conf b0:/run/a.conf
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
% xir dump_bin /usr/share/vitis_ai_library/models/ML-2784-elbit_224x224/ML-2784-elbit_224x224.xmodel bin
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
% env DEBUG_DPU_RUNNER=1  xdputil run /usr/share/vitis_ai_library/models/ML-2784-elbit_224x224/ML-2784-elbit_224x224.xmodel -i 0 \
 /group/xbjlab/dphi_software/software/workspace/qiuyuny/sft_versal_bs/workspace/sw_pipeline_debug/input_bin/golden/4c/64ee8d0de09dcf71c9d97072428021 &&  \
 md5sum *.scale_out_BiasAdd_aquant.bin ;

% env XLNX_XRT_CU_DRY_RUN=0 DEBUG_DPU_RUNNER=1  /run/test_dpu_runner /usr/share/vitis_ai_library/models/ML-2784-elbit_224x224/ML-2784-elbit_224x224.xmodel b_0 /group/xbjlab/dphi_software/software/workspace/qiuyuny/sft_versal_bs/workspace/sw_pipeline_debug/input_bin/golden/4c/64ee8d0de09dcf71c9d97072428021 1 1

% env DEBUG_BUFFER_OBJECT=4 XLNX_XRT_CU_DRY_RUN=1 DEBUG_DPU_RUNNER=1  xdputil run /usr/share/vitis_ai_library/models/ML-2784-elbit_224x224/ML-2784-elbit_224x224.xmodel -i 0 \
 /group/xbjlab/dphi_software/software/workspace/qiuyuny/sft_versal_bs/workspace/sw_pipeline_debug/input_bin/golden/4c/64ee8d0de09dcf71c9d97072428021 &&  \
 md5sum *.scale_out_BiasAdd_aquant.bin ;



% diff -u <(xxd 0.scale_out_BiasAdd_aquant.bin) <(xxd 1.scale_out_BiasAdd_aquant.bin); \
  diff -u <(xxd 0.scale_out_BiasAdd_aquant.bin) <(xxd 2.scale_out_BiasAdd_aquant.bin); \


% xdputil mem -r $((0x840060000)) 78196 dump_instr_mc_sw.bin && \
  xdputil mem -r $((0x840140000)) 150528 i0.bin && \
  xdputil mem -r $((0x840180000)) 150528 i1.bin && \
  xdputil mem -r $((0x8401c0000)) 150528 i2.bin && true

% xdputil mem -r $((0x840050000)) 50176 b0.bin && \
  xdputil mem -r $((0x8400d0000)) 50176 b1.bin && \
  xdputil mem -r $((0x8400e0000)) 50176 b2.bin && md5sum  b0.bin b1.bin b2.bin

% md5sum i0.bin i1.bin i2.bin b0.bin b1.bin b2.bin dump_instr_mc_sw.bin  *.scale_out_BiasAdd_aquant.bin

% diff -u <(xxd dump_instr_mc_sw.bin) <(xxd right_code.bin)
```

fix bug in `run.py`

```
% scp /workspace/aisw/Vitis-AI-Library/usefultools/python/xdputil_component/run.py b0:/usr/lib/python3.7/site-packages/xdputil_component/
```

``` console
% env DEBUG_BUFFER_OBJECT=1 /run/test_buffer_object 78196 196608 6573744 6573744 6573744 150528 150528 150528 50176 50176 50176 2>&1 | grep error_code
```


``` console
%  env XLNX_ENABLE_CLEAR=0 XLNX_ENABLE_DUMP=0 XLNX_XRT_CU_DRY_RUN=0 DEBUG_DPU_RUNNER=1  /run/test_dpu_runner /usr/share/vitis_ai_library/models/ML-2784-elbit_224x224/ML-2784-elbit_224x224.xmodel b_0 /group/xbjlab/dphi_software/software/workspace/qiuyuny/sft_versal_bs/workspace/sw_pipeline_debug/input_bin/golden/4c/64ee8d0de09dcf71c9d97072428021 1 1 && \
  xdputil mem -r $((0x840050000)) 50176 b0.bin && \
  xdputil mem -r $((0x8400d0000)) 50176 b1.bin && \
  xdputil mem -r $((0x8400e0000)) 50176 b2.bin && md5sum  b0.bin b1.bin b2.bin && \
  cat /proc/interrupts  | grep zocl && \
  xrt_read_register /run/a.conf D 0
```


``` console
%  env XLNX_ENABLE_DUMP=0 XLNX_XRT_CU_DRY_RUN=0 DEBUG_DPU_RUNNER=1  /run/test_dpu_runner /usr/share/vitis_ai_library/models/ML-2784-elbit_224x224/ML-2784-elbit_224x224.xmodel b_0 /group/xbjlab/dphi_software/software/workspace/qiuyuny/sft_versal_bs/workspace/sw_pipeline_debug/input_bin/golden/4c/64ee8d0de09dcf71c9d97072428021 1 1 && \
  xdputil mem -r $((0x840060000)) 78196 dump_instr_mc_sw.bin && \
  xdputil mem -r $((0x840050000)) 50176 b0.bin && \
  xdputil mem -r $((0x8400d0000)) 50176 b1.bin && \
  xdputil mem -r $((0x8400e0000)) 50176 b2.bin && md5sum  b0.bin b1.bin b2.bin dump_instr_mc_sw.bin && \
  cat /proc/interrupts  | grep zocl && \
  xrt_read_register /run/a.conf D 0

```

``` console
% /run/test_dpu_controller_cloud && \
  xdputil mem -r $((0x840050000)) 50176 b0.bin && \
  xdputil mem -r $((0x8400d0000)) 50176 b1.bin && \
  xdputil mem -r $((0x8400e0000)) 50176 b2.bin && md5sum  b0.bin b1.bin b2.bin && \
  cat /proc/interrupts  | grep zocl && \
  xrt_read_register /run/a.conf D 0
```

``` console

% cp /group/xbjlab/dphi_software/software/workspace/qiuyuny/sft_versal_bs/workspace/sw_pipeline_debug/input_bin/golden/4c/64ee8d0de09dcf71c9d97072428021 input1.bin
% xxd input1.bin | sed 's/00000000: 1d/00000000: 2d/g' | xxd -r >input2.bin
% xxd input1.bin | sed 's/00000000: 1d/00000000: 3d/g' | xxd -r >input3.bin
% md5sum input*.bin
4c64ee8d0de09dcf71c9d97072428021  input1.bin
45b9c2f4c7e0db55d76f9c3cd0d2bcae  input2.bin
c9cea8c22033b23e74eeb1fc4250e454  input3.bin

% xdputil mem -w $((0x840060000)) 78196 bin/subgraph_conv2d_1_1/Conv2D.mc && \
  xdputil mem -w $((0x840100000)) 196544 bin/REG_0.bin && \
  xdputil mem -w $((0x840140000)) 150528 input1.bin && \
  xdputil mem -w $((0x840180000)) 150528 input1.bin && \
  xdputil mem -w $((0x8401c0000)) 150528 input1.bin &&

  devmem 0x80000040 32 1 && \
  devmem 0x80000044 32 1 && \
  devmem 0x80000000 32 1  && \
  xdputil mem -r $((0x840050000)) 50176 b0.bin && \
  xdputil mem -r $((0x8400d0000)) 50176 b1.bin && \
  xdputil mem -r $((0x8400e0000)) 50176 b2.bin && md5sum  b0.bin b1.bin b2.bin && \
  cat /proc/interrupts  | grep zocl && \
  xrt_read_register /run/a.conf D 0
```
