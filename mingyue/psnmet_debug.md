```
% mkdir ~/build/psmnet_debug/
% scp mingyue@xcdl190260:/group/dphi_arch/wanghong/modelzoo/psmnet_pruned_50%/*_3D.xmodel ~/build/psmnet_debug/
% scp mingyue@xcdl190260:/group/dphi_arch/wanghong/modelzoo/psmnet_pruned_80%/*_3D.xmodel ~/build/psmnet_debug/

% scp ~/build/psmnet_debug/*.xmodel root@10.176.178.116:~/test/0823/

% ssh rpot@10.176.178.116
% xdputil query
% env XLNX_SHOW_DPU_COUNTER=1 xdputil run ~/test/0823/PSMNet_0_int_50%_compiled_DPUCVDX8G_ISA1_C32B3_3D.xmodel -i 1 /home/root/test/0_50_0/PSMNet__PSMNet_QuantStub_quant1__input_1_fix.bin && rm *.bin
```
### 50%  debug mode show CYCLE
```
##
% env XLNX_SHOW_DPU_COUNTER=1 XLNX_ENABLE_DEBUG_MODE=0 xdputil run ~/test/0823/PSMNet_0_int_50%_compiled_DPUCVDX8G_ISA1_C32B3_3D.xmodel -i 1 /home/root/test/0_50_0/PSMNet__PSMNet_QuantStub_quant1__input_1_fix.bin
% env XLNX_SHOW_DPU_COUNTER=1 XLNX_ENABLE_DEBUG_MODE=1 xdputil run ~/test/0823/PSMNet_0_int_50%_compiled_DPUCVDX8G_ISA1_C32B3_3D.xmodel -i 6 /home/root/test/0_50_0/PSMNet__PSMNet_Add_add25__1837_fix.bin  /home/root/test/0_50_0/PSMNet__PSMNet_Add_add25__1837_fix.bin /home/root/test/0_50_0/PSMNet__PSMNet_Add_add25__1837_fix.bin /home/root/test/0_50_0/PSMNet__PSMNet_Add_add25__1837_fix.bin /home/root/test/0_50_0/PSMNet__PSMNet_Add_add25__1837_fix.bin /home/root/test/0_50_0/PSMNet__PSMNet_Add_add25__1837_fix.bin 2> 0_50_1.log 1>&2 && rm *.bin



% env XLNX_SHOW_DPU_COUNTER=1 XLNX_ENABLE_DEBUG_MODE=1 xdputil run ~/test/0823/PSMNet_1_int_50%_compiled_DPUCVDX8G_ISA1_C32B3_3D.xmodel -i 1 /home/root/test/1_50_0/PSMNet__PSMNet_QuantStub_quant2__input_157_fix.bin 2> 1_50_0.log 1>&2 && rm *.bin
% env XLNX_SHOW_DPU_COUNTER=1 XLNX_ENABLE_DEBUG_MODE=1 xdputil run ~/test/0823/PSMNet_1_int_50%_compiled_DPUCVDX8G_ISA1_C32B3_3D.xmodel -i 6 /home/root/test/1_50_0/PSMNet__PSMNet_Add_addvi 50__2950_fix.bin /home/root/test/1_50_0/PSMNet__PSMNet_Add_add50__2950_fix.bin /home/root/test/1_50_0/PSMNet__PSMNet_Add_add50__2950_fix.bin /home/root/test/1_50_0/PSMNet__PSMNet_Add_add50__2950_fix.bin /home/root/test/1_50_0/PSMNet__PSMNet_Add_add50__2950_fix.bin /home/root/test/1_50_0/PSMNet__PSMNet_Add_add50__2950_fix.bin 2> 1_50_1.log 1>&2 && rm *.bin

% env XLNX_SHOW_DPU_COUNTER=1 XLNX_ENABLE_DEBUG_MODE=1 xdputil run ~/test/0823/PSMNet_2_int_50%_compiled_DPUCVDX8G_ISA1_C32B3_3D.xmodel -i 1 /home/root/test/2_50/PSMNet__PSMNet_QuantStub_quant3__7990_fix.bin 2> 2_50.log 1>&2 && rm *.bin


```

### 80% debug mode show CYCLE
```
% env XLNX_SHOW_DPU_COUNTER=1 XLNX_ENABLE_DEBUG_MODE=1 xdputil run ~/test/0823/PSMNet_0_int_80%_compiled_DPUCVDX8G_ISA1_C32B3_3D.xmodel -i 1 /home/root/test/0_80/PSMNet__PSMNet_QuantStub_quant1_1__input_1_fix.bin  2>0_80_0.log 1>&2 && rm *.bin
% env XLNX_SHOW_DPU_COUNTER=1 XLNX_ENABLE_DEBUG_MODE=1 xdputil run ~/test/0823/PSMNet_0_int_80%_compiled_DPUCVDX8G_ISA1_C32B3_3D.xmodel -i 6 /home/root/test/0_80/PSMNet__PSMNet_feature_extraction_feature_extraction__Sequential_layer4__BasicBlock_2__Add_add__1475_fix.bin /home/root/test/0_80/PSMNet__PSMNet_feature_extraction_feature_extraction__Sequential_layer4__BasicBlock_2__Add_add__1475_fix.bin /home/root/test/0_80/PSMNet__PSMNet_feature_extraction_feature_extraction__Sequential_layer4__BasicBlock_2__Add_add__1475_fix.bin /home/root/test/0_80/PSMNet__PSMNet_feature_extraction_feature_extraction__Sequential_layer4__BasicBlock_2__Add_add__1475_fix.bin /home/root/test/0_80/PSMNet__PSMNet_feature_extraction_feature_extraction__Sequential_layer4__BasicBlock_2__Add_add__1475_fix.bin /home/root/test/0_80/PSMNet__PSMNet_feature_extraction_feature_extraction__Sequential_layer4__BasicBlock_2__Add_add__1475_fix.bin  2>0_80_1.log 1>&2 && rm *.bin



% env XLNX_SHOW_DPU_COUNTER=1 XLNX_ENABLE_DEBUG_MODE=1 xdputil run ~/test/0823/PSMNet_1_int_80%_compiled_DPUCVDX8G_ISA1_C32B3_3D.xmodel -i 1 /home/root/test/1_80/PSMNet__PSMNet_QuantStub_quant1_2__input_157_fix.bin  2>1_80_0.log 1>&2 && rm *.bin
% env XLNX_SHOW_DPU_COUNTER=1 XLNX_ENABLE_DEBUG_MODE=1 xdputil run ~/test/0823/PSMNet_1_int_80%_compiled_DPUCVDX8G_ISA1_C32B3_3D.xmodel -i 6 /home/root/test/1_80/PSMNet__PSMNet_feature_extraction_feature_extraction__Sequential_layer4__BasicBlock_2__Add_add__2588_fix.bin /home/root/test/1_80/PSMNet__PSMNet_feature_extraction_feature_extraction__Sequential_layer4__BasicBlock_2__Add_add__2588_fix.bin /home/root/test/1_80/PSMNet__PSMNet_feature_extraction_feature_extraction__Sequential_layer4__BasicBlock_2__Add_add__2588_fix.bin /home/root/test/1_80/PSMNet__PSMNet_feature_extraction_feature_extraction__Sequential_layer4__BasicBlock_2__Add_add__2588_fix.bin /home/root/test/1_80/PSMNet__PSMNet_feature_extraction_feature_extraction__Sequential_layer4__BasicBlock_2__Add_add__2588_fix.bin /home/root/test/1_80/PSMNet__PSMNet_feature_extraction_feature_extraction__Sequential_layer4__BasicBlock_2__Add_add__2588_fix.bin  2>1_80_1.log 1>&2 && rm *.bin

% env XLNX_SHOW_DPU_COUNTER=1 XLNX_ENABLE_DEBUG_MODE=1 xdputil run ~/test/0823/PSMNet_2_int_80%_compiled_DPUCVDX8G_ISA1_C32B3_3D.xmodel -i 1 /home/root/test/2_80/PSMNet__PSMNet_QuantStub_quant2__7620_fix.bin 2> 2_80.log 1>&2 && rm *.bin
```

### scp log file to xcd
```
% scp root@10.176.178.116:~/test/0823/*.log ./
% scp *.log mingyue@xcdl190260:/group/dphi_software/mingyue/psmnet/0823
```
