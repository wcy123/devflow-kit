## git clone VMSS release/0.0.5
```
cd /home/mingyue/d/working
mkdir VMSS_0.0.5
cd VMSS_0.0.5
git clone git@gitenterprise.xilinx.com:ips-video-ml/VMSS.git
git checkout release/0.0.5
#commit id : 4d31cbf7e1451f1b5129a79f7fd230d5ab03e605

cd VMSS
git submodule update --init
```
## compiler VAI 1.2 (br-u30)
```
cd /home/mingyue/d/working/aisw/br-u30

cd unilog
./cmake.sh


cd ../target_factory
./cmake.sh

cd ../xir
./cmake.sh

cd ../vart
./cmake.sh --cmake-options=-DENABLE_DPU_RUNNER=ON --cmake-options=-DENABLE_SIM_RUNNER=OFF --cmake-options=-DENABLE_CPU_RUNNER=OFF

cd ../Vitis-AI-Library/
./cmake.sh --cmake-options='-DENABLE_OVERVIEW=ON'

```
## build VMSS server
```
cd $HOME/d/working/VMSS_0.0.5/VMSS
export VMSS_HOME=$HOME/d/working/VMSS_0.0.5/VMSS

#update server/env.sh  server/Makefile
vi server/Makefile
vi server/env.sh
```
### git diff
```
mingyue@xbjlabdpsvr15:VMSS% git diff
diff --git a/server/Makefile b/server/Makefile
index 4cd3a62..7693476 100644
--- a/server/Makefile
+++ b/server/Makefile
@@ -44,8 +44,8 @@ endif
 export LIBXFDNN_PREFIX

 # Used by PostProc plugin
-NMS_INC=$(PWD)/extern/VMSS_Plugins/ml/XDNN_ML_Interface_Plugin/libs/MLsuite/apps/yolo/nms/nms_20180209/include/
-export NMS_INC
+#NMS_INC=$(PWD)/extern/VMSS_Plugins/ml/XDNN_ML_Interface_Plugin/libs/MLsuite/apps/yolo/nms/nms_20180209/include/
+#export NMS_INC

 LDFLAGS= -ldl -lm -pthread -L/usr/lib/x86_64-linux-gnu $(EXTERN_LIBS) -L$(LIBXFDNN_PREFIX) -lVMSSserver
 CFLAGS= -Wall -Iinclude -I$(VMSS_LIB)/include -I$(EXTERN_FLAGS)
@@ -55,9 +55,8 @@ CFLAGS+=-O0 -g
 endif

 PHONY= env clean clearsc all update libs server server_clean lib_clean
-PLG_TARGETS= mlplugin preprocplugin postprocplugin dbplugin
-PLG_CLEAN = mlplugin_clean preprocplugin_clean
-PLG_CLEAN += postprocplugin_clean dbplugin_clean
+PLG_TARGETS= dbplugin
+PLG_CLEAN == dbplugin_clean

 .PHONY: $(PHONY) $(PLG_TARGETS) $(PLG_CLEAN)

diff --git a/server/env.sh b/server/env.sh
index aacbf94..ba50ac3 100755
--- a/server/env.sh
+++ b/server/env.sh
@@ -18,8 +18,8 @@
 export LD_LIBRARY_PATH=$PWD/libs:$PWD/libs/extern:$PWD/libs/extern/ml-suite-py3:/usr/local/lib:$LD_LIBRARY_PATH
 export GST_DEBUG_DUMP_DOT_DIR=.

-sudo cp conf/log/rsyslog/vmss.conf /etc/rsyslog.d/
-sudo cp conf/log/rotate/vmss_server /etc/logrotate.d/
-sudo service rsyslog restart
+#sudo cp conf/log/rsyslog/vmss.conf /etc/rsyslog.d/
+#sudo cp conf/log/rotate/vmss_server /etc/logrotate.d/
+#sudo service rsyslog restart

-sudo cp extern/VMSS_Plugins/preproc/XDNN_ML_PreProcess_Plugin/lib/libmlscaler.so /opt/xilinx/xma/plugins/
+#sudo cp extern/VMSS_Plugins/preproc/XDNN_ML_PreProcess_Plugin/lib/libmlscaler.so /opt/xilinx/xma/plugins/
```

```
export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig:/usr/local/lib64/pkgconfig
make DEBUG=1
```
vmss server compiler success!!!

## build DPU plugin
```
cd /home/mingyue/d/working/VMSS_0.0.5/
git clone git@gitenterprise.xilinx.com:chunywan/VMSS_Plugins.git
# commit is : c9224a00111b2676173090ba7aa875975ccc0429

cp -r $HOME/d/working/VMSS_0.0.5/VMSS_Plugins/ml/DPU $HOME/d/working/VMSS_0.0.5/VMSS_DPU_Plugins
cd $HOME/d/working/VMSS_0.0.5/VMSS_DPU_Plugins/
./cmake.sh --clean --cmake-options=-DCMAKE_EXPORT_COMPILE_COMMANDS=ON
```
#### DPU Plugin build error
```
/group/xbjlab/dphi_software/software/workspace/mingyue/d/working/VMSS_0.0.5/VMSS_DPU_Plugins/dpu_plugin_common/src/util.cpp: In function ‘std::string to_string(const VmssInfResult*, int)’:
/group/xbjlab/dphi_software/software/workspace/mingyue/d/working/VMSS_0.0.5/VMSS_DPU_Plugins/dpu_plugin_common/src/util.cpp:132:58: error: ‘const VmssInfResult’ {aka ‘const struct VmssInfResult’} has no member named ‘meta_cnt’
  132 |            << "next=" << to_string(result->next, result->meta_cnt, level + 1)
      |                                                          ^~~~~~~~
/group/xbjlab/dphi_software/software/workspace/mingyue/d/working/VMSS_0.0.5/VMSS_DPU_Plugins/dpu_plugin_common/src/util.cpp: In function ‘bool get_roi_rec(const VmssInfResult*, const VmssInfResult*, std::vector<cv::Rect_<int> >&)’:
/group/xbjlab/dphi_software/software/workspace/mingyue/d/working/VMSS_0.0.5/VMSS_DPU_Plugins/dpu_plugin_common/src/util.cpp:218:55: error: ‘const VmssInfResult’ {aka ‘const struct VmssInfResult’} has no member named ‘meta_cnt’
  218 |   auto found = get_roi_rec(dst, result->next, result->meta_cnt, ret);
      |                                                       ^~~~~~~~
/group/xbjlab/dphi_software/software/workspace/mingyue/d/working/VMSS_0.0.5/VMSS_DPU_Plugins/dpu_plugin_common/src/util.cpp: At global scope:
/group/xbjlab/dphi_software/software/workspace/mingyue/d/working/VMSS_0.0.5/VMSS_DPU_Plugins/dpu_plugin_common/src/util.cpp:193:13: error: ‘bool get_roi_rec(const VmssInfResult*, VmssMetaData**, uint16_t, std::vector<cv::Rect_<int> >&)’ defined but not used [-Werror=unused-function]
  193 | static bool get_roi_rec(const VmssInfResult *dst, VmssMetaData **result,
      |             ^~~~~~~~~~~
cc1plus: all warnings being treated as errors
make[2]: *** [dpu_plugin_common/CMakeFiles/dpu_plugin_common.dir/build.make:63: dpu_plugin_common/CMakeFiles/dpu_plugin_common.dir/src/util.cpp.o] Error 1
```
