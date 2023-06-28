
# build all

```
cd /workspace/vai-rt
python main.py --dev-mode --exclude-project test_onnx_runner
```


# build vaip

```
cd /workspace/vai-rt
python main.py --dev-mode --project vaip
```


# build onnxruntime

```
cd /workspace/vai-rt
python main.py --dev-mode --project onnxruntime
```



# run a specific case

```
cd /workspace/vaip
python ci/main.py run 5
emacs -nw ci/main.py
```


```
cd /workspace/vaip
git s
git checkout -b untrack-svg
git commit -m 'untrack svg files'
git ll
git rvs
git push -u fork untrack-svg
# create pr and merged
dev
python /workspace/vai-rt/main.py --dev-mode --project vaip
python /workspace/vaip/ci/main.py run 5
rm -fr /tmp/chunywan/vaip/.cache/d111d3ee33c942c0b6f1134bc6a0f56b
```


## debug issue https://gitenterprise.xilinx.com/VitisAI/vaip/issues/561

```
cd /workspace/vaip
env ENABLE_OPT=0 python /workspace/vaip/ci/main.py run CrossViT_int

ls -l "/tmp/chunywan/vaip/.cache/654ea89a5ecc633269882b8c3112dd64/"
```

## debug issue https://gitenterprise.xilinx.com/VitisAI/vaip/issues/557

```
env ENABLE_OPT=0 python /workspace/vaip/ci/main.py run "mvitv2_small"

md5sum /home/chunywan/build/vaip_regression/mvitv2_small/MultiScaleVit_int.onnx
b2692b7d083124a9590ef03cbfe58bf3

ls -l /tmp/chunywan/vaip/.cache/b2692b7d083124a9590ef03cbfe58bf3 | grep xmodel
/opt/netron/squashfs-root/AppRun netron --no-sandbox /tmp/chunywan/vaip/.cache/b2692b7d083124a9590ef03cbfe58bf3/compiled.DPUCZDX8G_ISA1_B4096.xmodel

xdputil xmodel -t /tmp/chunywan/vaip/.cache/b2692b7d083124a9590ef03cbfe58bf3/compiled.DPUCZDX8G_ISA1_B4096.txt /tmp/chunywan/vaip/.cache/b2692b7d083124a9590ef03cbfe58bf3/compiled.DPUCZDX8G_ISA1_B4096.xmodel

xdputil xmodel -l  /tmp/chunywan/vaip/.cache/b2692b7d083124a9590ef03cbfe58bf3/compiled.DPUCZDX8G_ISA1_B4096.xmodelzh

xdputil xmodel -s  /tmp/chunywan/vaip/.cache/b2692b7d083124a9590ef03cbfe58bf3/compiled.DPUCZDX8G_ISA1_B4096.svg  /tmp/chunywan/vaip/.cache/b2692b7d083124a9590ef03cbfe58bf3/compiled.DPUCZDX8G_ISA1_B4096.xmodel

scp -P 10022  localhost:/tmp/chunywan/vaip/.cache/b2692b7d083124a9590ef03cbfe58bf3/compiled.DPUCZDX8G_ISA1_B4096.svg ~/tmp

firefox ~/tmp/compiled.DPUCZDX8G_ISA1_B4096.svg

view /tmp/chunywan/vaip/.cache/b2692b7d083124a9590ef03cbfe58bf3/compiled.DPUCZDX8G_ISA1_B4096.txt
```

## debug issue https://gitenterprise.xilinx.com/VitisAI/vaip/issues/

```
env ENABLE_OPT=0 python /workspace/vaip/ci/main.py run "EfficientNet_int"
```
