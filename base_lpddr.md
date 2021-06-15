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
% ssh b0 mkdir -p /home/wcy
% rsync -avz /opt/petalinux/2020.2/sysroots/aarch64-xilinx-linux/install/Release b0:/home/wcy/Release
% rsync -avz $(find ~/build/build.linux.2020.2.aarch64.Release/vart/ -type f  -iname 'test*' -executable) b0:/home/wcy/
% ssh b0
% cd /home/wcy/Release/Release/lib; ls -l
% env LD_LIBRARY_PATH=/home/wcy/Release/Release/lib /home/wcy/test_buffer_object 1024 1024
% env LD_LIBRARY_PATH=/home/wcy/Release/Release/lib /home/wcy/test_buffer_object $((1*1024*1024)) 1024
% env LD_LIBRARY_PATH=/home/wcy/Release/Release/lib /home/wcy/test_bin_stream /media/sd-mmcblk0p1/dpu.xclbin
% cd /home/wcy;
% scp root@10.176.179.73:/usr/share/vitis_ai_library/models/resnet50/resnet50.xmodel .
% env DEBUG_DPU_RUNNER=1 XLNX_SHOW_DPU_COUNTER=1 LD_LIBRARY_PATH=/home/wcy/Release/Release/lib /home/wcy/test_dpu_runner ./resnet50.xmodel b_0 ./resnet50.xmodel 1 1

``
`
