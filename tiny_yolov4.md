# copy py files

``` console
% cd /workspace/aisw/debug_models/tensorflow-yolov4-tiny-master
% ls main.py
% cat main.py
% ln -s ./tensorflow-yolov4-tiny-master/quantize/quantize_results/quantize_eval_model.pb .
% ls 017.jpg
% feh 017.jpg
% file 017.jpg
% conda activate vitis-ai-tensorflow
% which python3
% python3 main.py
% ls -l *.py
% scp yolo4-tiny-test.py b0:/workspace
% scp 017.jpg coco.names  b0:/workspace
% scp b0:/workspace/output.png .
% feh output.png
```

``` console
% ssh b0
% cd /workspace
% ls *.py
% python3 yolo4-tiny-test.py >a.log
%
```
