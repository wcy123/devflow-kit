


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
source /proj/xbuilds/HEAD_plus_daily_latest/installs/lin64/Vitis/HEAD/settings64.sh

cd /workspace/mllib/L1/regression/element_wise/ElementWise_MAX_0
make PYTHON_PATH=`which python` x86sim

emacs -nw /workspace/mllib/L1/regression/inc/test_element_wise.h
emacs -nw /workspace/mllib/L1/regression/inc/single_layer_overlay_element_wise.h
emacs -nw /workspace/mllib/L1/regression/src/test_element_wise.cpp
emacs -nw /workspace/mllib/L1/regression/src/test_element_wise.cpp
emacs -nw /workspace/mllib/L1/regression/src/test_element_wise.cpp


x86simulator --pkg-dir=./Work --input-dir=./ --output-dir=./

head data/output.txt  data/output_ref.txt
cmp data/output.txt  data/output_ref.txt

x86simulator --pkg-dir=./Work --input-dir=./ --output-dir=./  --gdb
l max.h:1
l
b max.h:79
c
x /64db ia
x /64db ib

! ls data/
! head -n16 data/input_int_a.txt data/input_int_b.txt

n

x /64db &a
x /64db &b

n

x /&no last window

```


double check the final results

```
timeout 1200 aiesimulator --pkg-dir=./Work  --input-dir=./ --output-dir=./ --profile || exit 0
bash -ex /workspace/mllib/L1/regression/common/time.sh SIM_END
bash -ex /workspace/mllib/L1/regression/common/func_status.sh /workspace/mllib/L1/regression/element_wise/ElementWise_MAX_0/data/output.txt /workspace/mllib/L1/regression/element_wise/ElementWise_MAX_0/data/output_ref.txt /workspace/mllib/L1/regression/element_wise/ElementWise_MAX_0/data
bash -ex /workspace/mllib/L1/regression/common/rerun.sh /workspace/mllib ElementWise 1200 5
bash -ex /workspace/mllib/L1/regression/common/get_testinfo.sh /workspace/mllib /workspace/mllib/L1/regression/element_wise/ElementWise_MAX_0 ElementWise
bash -ex /workspace/mllib/L1/regression/common/parameter_mining.sh conv2d
```


git commit

```
cd /workspace/mllib/
git status
git add L1/regression/common/rerun.sh
git add L1/include/element_wise/
git add L1
git status
git reset L1/regression/element_wise/ElementWise_MAX_0/trace
git status
git add internal/models/python/mllib/dump.py
git add internal/models/python/testcases/ElementWise.json internal/models/python/tv_gen_element_wise.py
git commit -m 'support max(a,b) kernels'
git status
git remote -v show
git push -u origin add_element_wise_kernel
```
;;(local-set-key (kbd "C-b") tmux-cc-key-map)
