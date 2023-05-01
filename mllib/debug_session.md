
;;(local-set-key (kbd "C-b") tmux-cc-key-map)

```
% ssh -p 10022 localhost
% ipython
```

```
import numpy as np
seed = 100
np.random.seed(seed)
batch_size = 1
h = 5
w = 16
ic = 256
oc = 32
ifm = np.random.randint(-127, 128,
    size=[batch_size, h, w, ic],
    dtype=np.int8).astype(np.float32)

kh = 1
kw = 1
kernel = np.random.randint(-127, 128, size=[oc, kh, kw, ic],
                               dtype=np.int8).astype(np.float32)

ifm[0,0,0,0:16]
kernel[0,0,0,0:16]
```


```
cd /workspace/mllib/L1/regression/conv/Conv_DPU_0
x86simulator --pkg-dir=./Work --input-dir=./ --output-dir=./ --gdb
l conv_dpu.h:163
b conv_dpu.h:163
cont

# view channel 4x16,  w=0:2, ic=0:16
x /64bd &Abuff0


l conv_dpu.h:133
l
b conv_dpu.h:160
x /64bd pIn
x /bd p_ifm

# 4x16
x /64bd &Abuff0
ifm[0,0,0:4,0:16]

x /64bd &Abuff1
ifm[0,0,4:8,0:16]

# 16x16
x /128bd &Bbuff0
x /128bd &Bbuff1

kernel[0:8,0,0,0:16]

kernel[8:15,0,0,0:16]


x /32wd &C0.data

[ np.dot(ifm[0,0,0,0:16], kernel[i,0,0,0:16]) for i in range(8)]
[ np.dot(ifm[0,0,1,0:16], kernel[i,0,0,0:16]) for i in range(8)]
[ np.dot(ifm[0,0,2,0:16], kernel[i,0,0,0:16]) for i in range(8)]
[ np.dot(ifm[0,0,3,0:16], kernel[i,0,0,0:16]) for i in range(8)]

x /32wd &C1.data
[ np.dot(ifm[0,0,0,0:32], kernel[i,0,0,0:32]) for i in range(8)]

x /32wd &C2.data
x /32wd &C3.data


x /64dw tdm_buff

iter 2

x /64bd &Abuff0
ifm[0,0,0:4,32:64]

x /128bd &Bbuff0
kernel[0:7,0,0,32:48]

```

check memory

```
l conv_dpu.h:316
b conv_dpu.h:316
r
x /32xb p_wgt
dump memory data/w_0.dat p_wgt p_wgt+1024
cont
dump memory data/w_1.dat p_wgt p_wgt+1024
```

final test

```
l conv_dpu.h:160
l

l conv_dpu.h:243
l
b conv_dpu.h:252
r

x /128dw &C0.data

[ np.dot(ifm[0,0,0,0:256], kernel[i,0,0,0:256]) for i in range(8)]

kernel[0:7,0,0,0:16]
```

optimization test

```
b conv_dpu.h:252
cont

x /16wd pTdm32out
[ np.dot(ifm[0,0,0,0:256], kernel[i,0,0,0:256]) for i in range(8)]

n
# 4x8  W * OC
x /32wd &C0.data
np.array([np.dot(ifm[0,0,w,0:256], kernel[oc,0,0,0:256]) for w in range(4) for oc in range(8)]).reshape((4,8))

x /32wd &C1.data
np.array([np.dot(ifm[0,0,w+4,0:256], kernel[oc,0,0,0:256]) for w in range(4) for oc in range(8)]).reshape((4,8))

x /32wd &C2.data
np.array([np.dot(ifm[0,0,w,0:256], kernel[oc+8,0,0,0:256]) for w in range(4) for oc in range(8)]).reshape((4,8))

x /32wd &C3.data
np.array([np.dot(ifm[0,0,w+4,0:256], kernel[oc+8,0,0,0:256]) for w in range(4) for oc in range(8)]).reshape((4,8))



x /32wd &C2.data
x /32wd &C3.data

```


```
cd /workspace/mllib/L1/regression/conv/Conv_DPU_0
ls -l data/
cmp data/ofm32.txt data/ofm32_ref.txt || paste data/ofm32.txt data/ofm32_ref.txt | head
emacs -nw "/workspace/mllib/internal/models/python/tv_gen_dpu.py"
python /workspace/mllib/internal/models/python/tv_gen_dpu.py --use_json /workspace/mllib/internal/models/python/testcases/Conv2D.json
```


```
git status
git checkout -b conv_dpu_improve_0
git add -p

git commit -m 'use as_type(float32) and prohibit inline for more accurate mearsurement'
git rvs
git push -u origin conv_dpu_improve_0
```

```
ls -l | grep in
emacs -nw profile_instr_0_0.txt
```
