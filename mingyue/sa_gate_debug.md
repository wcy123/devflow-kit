### board b0: 10.176.178.111
## copy  run.py to support multipule inputs
```
$ scp /workspace/aisw/Vitis-AI-Library/usefultools/python/xdputil_component/run.py root@b0:/usr/lib/python3.7/site-packages/xdputil_component/run.py
```
## ssh b0
```
$ sshpass -p root ssh root@b0
$ mkdir -p  /group/xbjlab; mount -t nfs -o nolock 10.176.178.33:/group_xbjlab/ /group/xbjlab
```
## test
### golden dir b0: ~/lgd/SA_gate_golden && compare data
```
$ xdputil xmodel -l /usr/share/vitis_ai_library/models/SA_gate_pt/SA_gate_pt.xmodel
$ mkdir -p ~/test/01 && cd ~/test/01
$ env XLNX_ENABLE_FINGERPRINT_CHECK=0 XLNX_ENABLE_DUMP=1 xdputil run /usr/share/vitis_ai_library/models/SA_gate_pt/SA_gate_pt.xmodel  ~/lgd/SA_gate_golden/DeepLab__input_0_fix.bin  ~/lgd/SA_gate_golden/DeepLab__input_1_fix.bin && md5sum * && md5sum  ~/lgd/SA_gate_golden/DeepLab__DeepLab_45974_fix.bin
$ md5sum dump/subgraph_DeepLab__DeepLab_45974/input/*
```

>98fefdfba1798105190c3cbb6a2ad6c6  0.DeepLab__DeepLab_45974_fix.bin
>98fefdfba1798105190c3cbb6a2ad6c6  1.DeepLab__DeepLab_45974_fix.bin
>98fefdfba1798105190c3cbb6a2ad6c6  2.DeepLab__DeepLab_45974_fix.bin
>98fefdfba1798105190c3cbb6a2ad6c6  3.DeepLab__DeepLab_45974_fix.bin
>98fefdfba1798105190c3cbb6a2ad6c6  4.DeepLab__DeepLab_45974_fix.bin
>98fefdfba1798105190c3cbb6a2ad6c6  /home/root/lgd/SA_gate_golden/DeepLab__DeepLab_45974_fix.bin


>244395187e5c7b98fb729251f80cf677  dump/subgraph_DeepLab__DeepLab_45974/input/0.DeepLab__input_0_fix.bin
>7cca8a1df6280ff178cddad6f71f03ef  dump/subgraph_DeepLab__DeepLab_45974/input/0.DeepLab__input_1_fix.bin
>244395187e5c7b98fb729251f80cf677  dump/subgraph_DeepLab__DeepLab_45974/input/1.DeepLab__input_0_fix.bin
>7cca8a1df6280ff178cddad6f71f03ef  dump/subgraph_DeepLab__DeepLab_45974/input/1.DeepLab__input_1_fix.bin
>244395187e5c7b98fb729251f80cf677  dump/subgraph_DeepLab__DeepLab_45974/input/2.DeepLab__input_0_fix.bin
>7cca8a1df6280ff178cddad6f71f03ef  dump/subgraph_DeepLab__DeepLab_45974/input/2.DeepLab__input_1_fix.bin
>244395187e5c7b98fb729251f80cf677  dump/subgraph_DeepLab__DeepLab_45974/input/3.DeepLab__input_0_fix.bin
>7cca8a1df6280ff178cddad6f71f03ef  dump/subgraph_DeepLab__DeepLab_45974/input/3.DeepLab__input_1_fix.bin
>244395187e5c7b98fb729251f80cf677  dump/subgraph_DeepLab__DeepLab_45974/input/4.DeepLab__input_0_fix.bin
>7cca8a1df6280ff178cddad6f71f03ef  dump/subgraph_DeepLab__DeepLab_45974/input/4.DeepLab__input_1_fix.bin

compare data success

### update input
```
$ mkdir -p ~/test/10 && cd ~/test/10
$ env XLNX_ENABLE_FINGERPRINT_CHECK=0 XLNX_ENABLE_DUMP=1 xdputil run /usr/share/vitis_ai_library/models/SA_gate_pt/SA_gate_pt.xmodel  ~/lgd/SA_gate_golden/DeepLab__input_1_fix.bin  ~/lgd/SA_gate_golden/DeepLab__input_0_fix.bin && md5sum *
$ md5sum dump/subgraph_DeepLab__DeepLab_45974/input/*
```
>40f8b985ae9ad54645a4ad535d2a14ee  0.DeepLab__DeepLab_45974_fix.bin
>40f8b985ae9ad54645a4ad535d2a14ee  1.DeepLab__DeepLab_45974_fix.bin
>40f8b985ae9ad54645a4ad535d2a14ee  2.DeepLab__DeepLab_45974_fix.bin
>40f8b985ae9ad54645a4ad535d2a14ee  3.DeepLab__DeepLab_45974_fix.bin
>40f8b985ae9ad54645a4ad535d2a14ee  4.DeepLab__DeepLab_45974_fix.bin


>7cca8a1df6280ff178cddad6f71f03ef  dump/subgraph_DeepLab__DeepLab_45974/input/0.DeepLab__input_0_fix.bin
>244395187e5c7b98fb729251f80cf677  dump/subgraph_DeepLab__DeepLab_45974/input/0.DeepLab__input_1_fix.bin
>7cca8a1df6280ff178cddad6f71f03ef  dump/subgraph_DeepLab__DeepLab_45974/input/1.DeepLab__input_0_fix.bin
>244395187e5c7b98fb729251f80cf677  dump/subgraph_DeepLab__DeepLab_45974/input/1.DeepLab__input_1_fix.bin
>7cca8a1df6280ff178cddad6f71f03ef  dump/subgraph_DeepLab__DeepLab_45974/input/2.DeepLab__input_0_fix.bin
>244395187e5c7b98fb729251f80cf677  dump/subgraph_DeepLab__DeepLab_45974/input/2.DeepLab__input_1_fix.bin
>7cca8a1df6280ff178cddad6f71f03ef  dump/subgraph_DeepLab__DeepLab_45974/input/3.DeepLab__input_0_fix.bin
>244395187e5c7b98fb729251f80cf677  dump/subgraph_DeepLab__DeepLab_45974/input/3.DeepLab__input_1_fix.bin
>7cca8a1df6280ff178cddad6f71f03ef  dump/subgraph_DeepLab__DeepLab_45974/input/4.DeepLab__input_0_fix.bin
>244395187e5c7b98fb729251f80cf677  dump/subgraph_DeepLab__DeepLab_45974/input/4.DeepLab__input_1_fix.bin
```
$ mkdir -p ~/test/0110 && cd ~/test/0110
$ env XLNX_ENABLE_FINGERPRINT_CHECK=0 XLNX_ENABLE_DUMP=1 xdputil run /usr/share/vitis_ai_library/models/SA_gate_pt/SA_gate_pt.xmodel  ~/lgd/SA_gate_golden/DeepLab__input_0_fix.bin  ~/lgd/SA_gate_golden/DeepLab__input_1_fix.bin  ~/lgd/SA_gate_golden/DeepLab__input_1_fix.bin  ~/lgd/SA_gate_golden/DeepLab__input_0_fix.bin  && md5sum *

$ md5sum dump/subgraph_DeepLab__DeepLab_45974/input/*
```
>98fefdfba1798105190c3cbb6a2ad6c6  0.DeepLab__DeepLab_45974_fix.bin
>5440e073c3b34dfc978ecf7447bc48c0  1.DeepLab__DeepLab_45974_fix.bin
>98fefdfba1798105190c3cbb6a2ad6c6  2.DeepLab__DeepLab_45974_fix.bin
>5440e073c3b34dfc978ecf7447bc48c0  3.DeepLab__DeepLab_45974_fix.bin
>98fefdfba1798105190c3cbb6a2ad6c6  4.DeepLab__DeepLab_45974_fix.bin


>244395187e5c7b98fb729251f80cf677  dump/subgraph_DeepLab__DeepLab_45974/input/0.DeepLab__input_0_fix.bin
>7cca8a1df6280ff178cddad6f71f03ef  dump/subgraph_DeepLab__DeepLab_45974/input/0.DeepLab__input_1_fix.bin
>7cca8a1df6280ff178cddad6f71f03ef  dump/subgraph_DeepLab__DeepLab_45974/input/1.DeepLab__input_0_fix.bin
>244395187e5c7b98fb729251f80cf677  dump/subgraph_DeepLab__DeepLab_45974/input/1.DeepLab__input_1_fix.bin
>244395187e5c7b98fb729251f80cf677  dump/subgraph_DeepLab__DeepLab_45974/input/2.DeepLab__input_0_fix.bin
>7cca8a1df6280ff178cddad6f71f03ef  dump/subgraph_DeepLab__DeepLab_45974/input/2.DeepLab__input_1_fix.bin
>7cca8a1df6280ff178cddad6f71f03ef  dump/subgraph_DeepLab__DeepLab_45974/input/3.DeepLab__input_0_fix.bin
>244395187e5c7b98fb729251f80cf677  dump/subgraph_DeepLab__DeepLab_45974/input/3.DeepLab__input_1_fix.bin
>244395187e5c7b98fb729251f80cf677  dump/subgraph_DeepLab__DeepLab_45974/input/4.DeepLab__input_0_fix.bin
>7cca8a1df6280ff178cddad6f71f03ef  dump/subgraph_DeepLab__DeepLab_45974/input/4.DeepLab__input_1_fix.bin

```
$ mkdir -p ~/test/1001 && cd ~/test/1001
$ env XLNX_ENABLE_FINGERPRINT_CHECK=0 XLNX_ENABLE_DUMP=1 xdputil run /usr/share/vitis_ai_library/models/SA_gate_pt/SA_gate_pt.xmodel  ~/lgd/SA_gate_golden/DeepLab__input_1_fix.bin  ~/lgd/SA_gate_golden/DeepLab__input_0_fix.bin  ~/lgd/SA_gate_golden/DeepLab__input_0_fix.bin  ~/lgd/SA_gate_golden/DeepLab__input_1_fix.bin  && md5sum *
$ md5sum dump/subgraph_DeepLab__DeepLab_45974/input/*
```
>40f8b985ae9ad54645a4ad535d2a14ee  0.DeepLab__DeepLab_45974_fix.bin
>c7630d3a632665cd539b00cb67d914b4  1.DeepLab__DeepLab_45974_fix.bin
>40f8b985ae9ad54645a4ad535d2a14ee  2.DeepLab__DeepLab_45974_fix.bin
>c7630d3a632665cd539b00cb67d914b4  3.DeepLab__DeepLab_45974_fix.bin
>40f8b985ae9ad54645a4ad535d2a14ee  4.DeepLab__DeepLab_45974_fix.bin

>7cca8a1df6280ff178cddad6f71f03ef  dump/subgraph_DeepLab__DeepLab_45974/input/0.DeepLab__input_0_fix.bin
>244395187e5c7b98fb729251f80cf677  dump/subgraph_DeepLab__DeepLab_45974/input/0.DeepLab__input_1_fix.bin
>244395187e5c7b98fb729251f80cf677  dump/subgraph_DeepLab__DeepLab_45974/input/1.DeepLab__input_0_fix.bin
>7cca8a1df6280ff178cddad6f71f03ef  dump/subgraph_DeepLab__DeepLab_45974/input/1.DeepLab__input_1_fix.bin
>7cca8a1df6280ff178cddad6f71f03ef  dump/subgraph_DeepLab__DeepLab_45974/input/2.DeepLab__input_0_fix.bin
>244395187e5c7b98fb729251f80cf677  dump/subgraph_DeepLab__DeepLab_45974/input/2.DeepLab__input_1_fix.bin
>244395187e5c7b98fb729251f80cf677  dump/subgraph_DeepLab__DeepLab_45974/input/3.DeepLab__input_0_fix.bin
>7cca8a1df6280ff178cddad6f71f03ef  dump/subgraph_DeepLab__DeepLab_45974/input/3.DeepLab__input_1_fix.bin
>7cca8a1df6280ff178cddad6f71f03ef  dump/subgraph_DeepLab__DeepLab_45974/input/4.DeepLab__input_0_fix.bin
>244395187e5c7b98fb729251f80cf677  dump/subgraph_DeepLab__DeepLab_45974/input/4.DeepLab__input_1_fix.bin


### diff data
```
$ xxd ~/test/10/0.DeepLab__DeepLab_45974_fix.bin | head
$ xxd ~/test/0110/1.DeepLab__DeepLab_45974_fix.bin | head
```

```
$ xxd ~/test/01/0.DeepLab__DeepLab_45974_fix.bin | head
$ xxd ~/test/1001/1.DeepLab__DeepLab_45974_fix.bin | head
```


### run graph runner
```
$ scp  ~/build/build.linux.2020.2.aarch64.Debug/Vitis-AI-Library/graph_runner/test_graph_runner root@b0:~/graph_test/
$ sshpass -p root ssh root@b0
$ mkdir -p ~/graph_test/ref
$ cp ~/lgd/SA_gate_golden/DeepLab__input_*fix.bin ~/graph_test/ref
$ cd ~/graph_test
```

#### 01 all input is 0 1
```
$ mkdir ~/graph_test/01 && cd ~/graph_test/01
$ cp -r ~/graph_test/ref ./

$ cd ~/graph_test/01/ref
$ cp DeepLab__input_0_fix.bin DeepLab__input_0_fix_0.bin
$ cp DeepLab__input_0_fix.bin DeepLab__input_0_fix_1.bin
$ cp DeepLab__input_0_fix.bin DeepLab__input_0_fix_2.bin
$ cp DeepLab__input_0_fix.bin DeepLab__input_0_fix_3.bin
$ cp DeepLab__input_0_fix.bin DeepLab__input_0_fix_4.bin

$ cp DeepLab__input_1_fix.bin DeepLab__input_1_fix_0.bin
$ cp DeepLab__input_1_fix.bin DeepLab__input_1_fix_1.bin
$ cp DeepLab__input_1_fix.bin DeepLab__input_1_fix_2.bin
$ cp DeepLab__input_1_fix.bin DeepLab__input_1_fix_3.bin
$ cp DeepLab__input_1_fix.bin DeepLab__input_1_fix_4.bin

$ cd ~/graph_test/01
$ env XLNX_ENABLE_FINGERPRINT_CHECK=0 DEBUG_DPU_RUNNER=0  ~/graph_test/test_graph_runner /usr/share/vitis_ai_library/models/SA_gate_pt/SA_gate_pt.xmodel -i 2 && md5sum *
```

### 10 all input is 1 0

```
$ mkdir -p ~/graph_test/10 && cd ~/graph_test/10
$ cp -r ~/graph_test/ref ./

$ cd ~/graph_test/10/ref
$ cp DeepLab__input_0_fix.bin DeepLab__input_1_fix_0.bin
$ cp DeepLab__input_0_fix.bin DeepLab__input_1_fix_1.bin
$ cp DeepLab__input_0_fix.bin DeepLab__input_1_fix_2.bin
$ cp DeepLab__input_0_fix.bin DeepLab__input_1_fix_3.bin
$ cp DeepLab__input_0_fix.bin DeepLab__input_1_fix_4.bin

$ cp DeepLab__input_1_fix.bin DeepLab__input_0_fix_0.bin
$ cp DeepLab__input_1_fix.bin DeepLab__input_0_fix_1.bin
$ cp DeepLab__input_1_fix.bin DeepLab__input_0_fix_2.bin
$ cp DeepLab__input_1_fix.bin DeepLab__input_0_fix_3.bin
$ cp DeepLab__input_1_fix.bin DeepLab__input_0_fix_4.bin
$ cd ~/graph_test/10
$ env XLNX_ENABLE_FINGERPRINT_CHECK=0 DEBUG_DPU_RUNNER=0  ~/graph_test/test_graph_runner /usr/share/vitis_ai_library/models/SA_gate_pt/SA_gate_pt.xmodel -i 2 && md5sum *.bin
```

### 0110
```
$ mkdir -p ~/graph_test/0110 && cd ~/graph_test/0110
$ cp -r ~/graph_test/ref ./
$ cd ~/graph_test/0110/ref
$ cp DeepLab__input_0_fix.bin DeepLab__input_0_fix_0.bin
$ cp DeepLab__input_1_fix.bin DeepLab__input_0_fix_1.bin
$ cp DeepLab__input_0_fix.bin DeepLab__input_0_fix_2.bin
$ cp DeepLab__input_1_fix.bin DeepLab__input_0_fix_3.bin
$ cp DeepLab__input_0_fix.bin DeepLab__input_0_fix_4.bin

$ cp DeepLab__input_1_fix.bin DeepLab__input_1_fix_0.bin
$ cp DeepLab__input_0_fix.bin DeepLab__input_1_fix_1.bin
$ cp DeepLab__input_1_fix.bin DeepLab__input_1_fix_2.bin
$ cp DeepLab__input_0_fix.bin DeepLab__input_1_fix_3.bin
$ cp DeepLab__input_1_fix.bin DeepLab__input_1_fix_4.bin

$ cd ~/graph_test/0110
$ env XLNX_ENABLE_FINGERPRINT_CHECK=0 DEBUG_DPU_RUNNER=0  ~/graph_test/test_graph_runner /usr/share/vitis_ai_library/models/SA_gate_pt/SA_gate_pt.xmodel -i 2 && md5sum *.bin
```
```
$ env XLNX_ENABLE_DUMP=1 XLNX_ENABLE_FINGERPRINT_CHECK=0 ./test_jpeg_RGBDsegmentation SA_gate_pt sample_rgbdsegmentation_bgr.jpg sample_rgbdsegmentation_hha.jpg
$ md5sum dump/subgraph_DeepLab__DeepLab_45974/input/0*

$ cp -r ~/graph_test/01 ~/graph_test/01_1
$ cd ~/graph_test/01_1
$ env XLNX_ENABLE_FINGERPRINT_CHECK=0 DEBUG_DPU_RUNNER=0  ~/graph_test/test_graph_runner /usr/share/vitis_ai_library/models/SA_gate_pt/SA_gate_pt.xmodel -i 2 && md5sum *.bin
```
<pre>
98fefdfba1798105190c3cbb6a2ad6c6  0.DeepLab__DeepLab_45974_fix.bin
98fefdfba1798105190c3cbb6a2ad6c6  1.DeepLab__DeepLab_45974_fix.bin
98fefdfba1798105190c3cbb6a2ad6c6  2.DeepLab__DeepLab_45974_fix.bin
98fefdfba1798105190c3cbb6a2ad6c6  3.DeepLab__DeepLab_45974_fix.bin
98fefdfba1798105190c3cbb6a2ad6c6  4.DeepLab__DeepLab_45974_fix.bin
</pre>
```
$ (cd ref; md5sum DeepLab__input_0_fix_0.bin DeepLab__input_1_fix_0.bin  DeepLab__input_0_fix_1.bin DeepLab__input_1_fix_1.bin DeepLab__input_0_fix_2.bin DeepLab__input_1_fix_2.bin DeepLab__input_0_fix_3.bin DeepLab__input_1_fix_3.bin DeepLab__input_0_fix_4.bin DeepLab__input_1_fix_4.bin)
```
>244395187e5c7b98fb729251f80cf677  DeepLab__input_0_fix_0.bin <br/>
>7cca8a1df6280ff178cddad6f71f03ef  DeepLab__input_1_fix_0.bin <br/>
>244395187e5c7b98fb729251f80cf677  DeepLab__input_0_fix_1.bin <br/>
>7cca8a1df6280ff178cddad6f71f03ef  DeepLab__input_1_fix_1.bin <br/>
>244395187e5c7b98fb729251f80cf677  DeepLab__input_0_fix_2.bin <br/>
>7cca8a1df6280ff178cddad6f71f03ef  DeepLab__input_1_fix_2.bin <br/>
>244395187e5c7b98fb729251f80cf677  DeepLab__input_0_fix_3.bin <br/>
>7cca8a1df6280ff178cddad6f71f03ef  DeepLab__input_1_fix_3.bin <br/>
>244395187e5c7b98fb729251f80cf677  DeepLab__input_0_fix_4.bin <br/>
>7cca8a1df6280ff178cddad6f71f03ef  DeepLab__input_1_fix_4.bin <br/>


### update batch 0 input
```
$ cp ~/graph_test/dump/subgraph_DeepLab__DeepLab_45974/input/0.DeepLab__input_0_fix.bin ref/DeepLab__input_0_fix_0.bin
$ cp ~/graph_test/dump/subgraph_DeepLab__DeepLab_45974/input/0.DeepLab__input_1_fix.bin ref/DeepLab__input_1_fix_0.bin
$ (cd ref; md5sum DeepLab__input_0_fix_0.bin DeepLab__input_1_fix_0.bin  DeepLab__input_0_fix_1.bin DeepLab__input_1_fix_1.bin DeepLab__input_0_fix_2.bin DeepLab__input_1_fix_2.bin DeepLab__input_0_fix_3.bin DeepLab__input_1_fix_3.bin DeepLab__input_0_fix_4.bin DeepLab__input_1_fix_4.bin)
```
>a1e6c241c01dee0b476db338b0d5137d  DeepLab__input_0_fix_0.bin <br/>
>4902901688ce4c7240d22dc909b06ed9  DeepLab__input_1_fix_0.bin <br/>
>244395187e5c7b98fb729251f80cf677  DeepLab__input_0_fix_1.bin <br/>
>7cca8a1df6280ff178cddad6f71f03ef  DeepLab__input_1_fix_1.bin <br/>
>244395187e5c7b98fb729251f80cf677  DeepLab__input_0_fix_2.bin <br/>
>7cca8a1df6280ff178cddad6f71f03ef  DeepLab__input_1_fix_2.bin <br/>
>244395187e5c7b98fb729251f80cf677  DeepLab__input_0_fix_3.bin <br/>
>7cca8a1df6280ff178cddad6f71f03ef  DeepLab__input_1_fix_3.bin <br/>
>244395187e5c7b98fb729251f80cf677  DeepLab__input_0_fix_4.bin <br/>
>7cca8a1df6280ff178cddad6f71f03ef  DeepLab__input_1_fix_4.bin <br/>

```
$ env XLNX_ENABLE_FINGERPRINT_CHECK=0 DEBUG_DPU_RUNNER=0  ~/graph_test/test_graph_runner /usr/share/vitis_ai_library/models/SA_gate_pt/SA_gate_pt.xmodel -i 2 && md5sum *.bin
```
>84e6c96b441d2e0527f3fa4817beb082  0.DeepLab__DeepLab_45974_fix.bin <br/>
>0d6c0b0a6759adc50cec9e4fa946d9bb  1.DeepLab__DeepLab_45974_fix.bin <br/>
>0d6c0b0a6759adc50cec9e4fa946d9bb  2.DeepLab__DeepLab_45974_fix.bin <br/>
>0d6c0b0a6759adc50cec9e4fa946d9bb  3.DeepLab__DeepLab_45974_fix.bin <br/>
>0d6c0b0a6759adc50cec9e4fa946d9bb  4.DeepLab__DeepLab_45974_fix.bin <br/>

```
$ cp ~/graph_test/ref/DeepLab__input_0_fix.bin ref/DeepLab__input_0_fix_0.bin
$ cp ~/graph_test/ref/DeepLab__input_1_fix.bin ref/DeepLab__input_1_fix_0.bin
$ env XLNX_ENABLE_FINGERPRINT_CHECK=0 DEBUG_DPU_RUNNER=0  ~/graph_test/test_graph_runner /usr/share/vitis_ai_library/models/SA_gate_pt/SA_gate_pt.xmodel -i 2 && md5sum *.bin
``
