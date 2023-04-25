


```
ssh -p 10022 localhost
cd /workspace/mllib
git status
git diff df4381483bcac3eb5892dbea90aee86a1a626e0d origin/conv_dpu  --stat
mkdir -p L1/include/element_wise
ls L1/include/element_wise
git show origin/conv_dpu:L1/include/conv/conv_dpu.h >L1/include/element_wise/

mkdir -p L1/regression/element_wise/ElementWise_MAX_0
git show origin/conv_dpu:L1/regression/conv/Conv_DPU_0/Makefile >L1/regression/element_wise/ElementWise_MAX_0/Makefile
git show origin/conv_dpu:L1/regression/conv/Conv_DPU_0/utils.mk >L1/regression/element_wise/ElementWise_MAX_0/utils.mk
git show origin/conv_dpu:L1/regression/inc/single_layer_overlay_conv_dpu.h >L1/regression/inc/single_layer_overlay_element_wise.h
git show origin/conv_dpu:L1/regression/inc/test_conv_dpu.h >L1/regression/inc/test_element_wise.h
git show origin/conv_dpu:L1/regression/inc/tiling_dpu.h >L1/regression/inc/tiling_element_wise.h
git show origin/conv_dpu:L1/regression/src/conv_dpu_wrapper.cpp >L1/regression/src/element_wise_wrapper.cpp
git show origin/conv_dpu:L1/regression/src/test_conv_dpu.cpp >L1/regression/src/test_element_wise.cpp
touch internal/models/python/testcases/ElementWise.json
git show origin/conv_dpu:internal/models/python/tv_gen_dpu.py >internal/models/python/tv_gen_element_wise.py
```


```
sed -e 's/conv_dpu/element_wise/g' -i L1/regression/element_wise/ElementWise_MAX_0/Makefile
```


```
no update L1/regression/element_wise/ElementWise_MAX_0/utils.mk
```

```
sed -e 's/conv_dpu/element_wise/g' -i L1/regression/inc/single_layer_overlay_element_wise.h
grep conv_dpu L1/regression/inc/single_layer_overlay_element_wise.h
```


```
sed -e 's/conv_dpu/element_wise/g' -i  L1/regression/inc/test_element_wise.h
```

```
grep conv_dpu L1/regression/inc/tiling_element_wise.h
```

```
grep conv_dpu L1/regression/src/element_wise_wrapper.cpp
sed -e 's/conv_dpu/element_wise/g' -i  L1/regression/src/element_wise_wrapper.cpp
```


```
grep conv_dpu L1/regression/src/test_element_wise.cpp
sed -e 's/conv_dpu/element_wise/g' -i L1/regression/src/test_element_wise.cpp
```

```
emacs -nw internal/models/python/tv_gen_element_wise.py
ls -l /workspace/mllib/internal/models/python/testcases/
cd /workspace/mllib/L1/regression/element_wise/ElementWise_MAX_0
python /workspace/mllib/internal/models/python/tv_gen_element_wise.py --use_json /workspace/mllib/internal/models/python/testcases/ElementWise.json --key Element_Wise_0 && cat data/testcase.h
ls -l data/
paste data/input_int_a.txt data/input_int_b.txt  data/output_int_ref.txt | head
emacs -nw /workspace/mllib/internal/models/python/testcases/ElementWise.json
emacs -nw /workspace/mllib/internal/models/python/tv_gen_element_wise.py
```



```
source /workspace/mllib/internal/examples/test/tools_setup.sh
cd /workspace/mllib/L1/regression/element_wise/ElementWise_MAX_0
make PYTHON_PATH=`which python` x86sim

emacs -nw /workspace/mllib/L1/regression/inc/test_element_wise.h
emacs -nw /workspace/mllib/L1/regression/inc/single_layer_overlay_element_wise.h
emacs -nw /workspace/mllib/L1/regression/src/test_element_wise.cpp
emacs -nw /workspace/mllib/L1/regression/src/test_element_wise.cpp
emacs -nw /workspace/mllib/L1/regression/src/test_element_wise.cpp
```

;;(local-set-key (kbd "C-b") tmux-cc-key-map)
