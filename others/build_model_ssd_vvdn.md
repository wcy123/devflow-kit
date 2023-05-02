# build model for u30 vvdn ssd

``` console
% cd /group/xbjlab/dphi_software/software/workspace/$USER/d/working/xcompile/
% mkdir -p U50_ssd;cd U50_ssd; pwd;ls
% scp xcdl190253:/proj/xcdhdstaff2/jianweng/workspace/debug/ssd_vvdn_20200401/new_model/{deploy.caffemodel,deploy.prototxt} .
% ~/.local/bin/xnnc-run --type caffe --layout NCHW --model ./deploy.caffemodel --proto ./deploy.prototxt --out xnnc-run.xmodel
% cd /group/xbjlab/dphi_software/software/workspace/$USER/d/working/xcompile/target_factory/targets
% diff -uB DPUCZDX8G_ISA0_B3136_MAX.prototxt DPUCZDX8G_ISA0_B3136_MIN.prototx t
% $HOME/.local/Ubuntu.16.04.x86_64.Debug/bin/xcompiler --help
% $HOME/.local/Ubuntu.16.04.x86_64.Debug/bin/xcompiler -i xnnc-run.xmodel -o ssd_vvdn.xmodel  -a "DPUCZDX8G_ISA0_B3136_MAX_BG2"
% export VMSS_HOME=$HOME/d/working/vmss/VMSS
% cp -av ssd_vvdn.xmodel $VMSS_HOME/extern/VMSS_Plugins/ml/DPU/models/ssd_U30;ls
% ~/build/build.Ubuntu.16.04.x86_64.Debug/xir/tools/xir dump_txt ssd_vvdn.xmodel ssd_vvdn.txt
% cd  $VMSS_HOME/extern/VMSS_Plugins/ml/DPU/models/ssd_U30;ls
% cp $VMSS_HOME/extern/VMSS_Plugins/ml/DPU/models/ssd/ssd_vvdn.prototxt .
% cp $VMSS_HOME/extern/VMSS_Plugins/ml/DPU/models/ssd_U30/1024-736-max.jpg .
% env DEBUG_DPBASE=1 ~/build/build.Ubuntu.16.04.x86_64.Debug/Vitis-AI-Library/overview/test_jpeg_ssd ssd_vvdn.xmodel 1024-736-max.jpg

```
DPUCZDX8G_ISA0_B3136_MAX.prototxt
