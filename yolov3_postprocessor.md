# repeat the origin result

``` console
% cd /workspace/aisw/Vitis-AI-Library/
% ./cmake.sh
% find ~/build/build.Ubuntu.18.04.x86_64.Debug/Vitis-AI-Library/ -iname 'test_jpeg*yolo*'
% # we have to copy it to /tmp, otherwise permission denied.
% cp -av /usr/share/vitis_ai_library/samples/yolov4/images/001.png /tmp
% env DEBUG_DEMO=1 /home/chunywan/build/build.Ubuntu.18.04.x86_64.Debug/Vitis-AI-Library/overview/test_jpeg_yolov4 yolov4_leaky_spp_m /tmp/001.png
% feh /tmp/001_result.jpg
```

#

``` console

```
