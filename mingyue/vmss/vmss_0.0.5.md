## git clone VMSS release/0.0.5
```
cd /home/mingyue/d/working
mkdir VMSS_0.0.5
cd VMSS_0.0.5
git clone git@gitenterprise.xilinx.com:ips-video-ml/VMSS.git
git checkout release/0.0.5

cd VMSS
#vi .git/config  change https://gitenterprise.xilinx.com/ips-video-ml/VMSS_Lib.git to git@gitenterprise.xilinx.com:ips-video-ml/VMSS_Lib.git

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

```
## build VMSS server
```
cd $HOME/d/working/VMSS_0.0.5/VMSS
export VMSS_HOME=$HOME/d/working/VMSS_0.0.5/VMSS

make DEBUG=1
```
*********************************************************
              CALLING MAKE  FOR mlplugin
***********************************************************
make -C /home/mingyue/d/working/VMSS_0.0.5/VMSS/./extern/VMSS_Plugins/ml/XDNN_ML_Interface_Plugin -e -j1
make[2]: Entering directory '/group/xbjlab/dphi_software/software/workspace/mingyue/d/working/VMSS_0.0.5/VMSS/extern/VMSS_Plugins/ml/XDNN_ML_Interface_Plugin'
mkdir -p build/obj
g++ -I /home/mingyue/d/working/VMSS_0.0.5/VMSS/./extern/VMSS_Lib/include -Ilibs -Ilibs/MLsuite/xfdnn/rt/xdnn_cpp -I/opt/xilinx/xrt/include -I/opt/xilinx/xrt/include/CL -I./anaconda2/envs/ml-suite-py3/include -I./anaconda2/envs/ml-suite-py3/include/xip/butler -Ilibs/MLsuite/xfdnn/rt/vitis/include --std=c++11 -Wall -Wno-unknown-pragmas -Wfatal-errors -fPIC -fpermissive -O0 -g -c src/xdnnMLsuiteIntf.cpp -o build/obj/xdnnMLsuiteIntf.o
src/xdnnMLsuiteIntf.cpp:27:10: fatal error: xdnn.h: No such file or directory
   27 | #include "xdnn.h"
      |          ^~~~~~~~
compilation terminated.
make[2]: *** [Makefile:106: build/obj/xdnnMLsuiteIntf.o] Error 1
make[2]: Leaving directory '/group/xbjlab/dphi_software/software/workspace/mingyue/d/working/VMSS_0.0.5/VMSS/extern/VMSS_Plugins/ml/XDNN_ML_Interface_Plugin'
make[1]: *** [Makefile:100: mlplugin] Error 2
make[1]: Leaving directory '/group/xbjlab/dphi_software/software/workspace/mingyue/d/working/VMSS_0.0.5/VMSS/server'
make: [Makefile:41: /home/mingyue/d/working/VMSS_0.0.5/VMSS/server] Error 2 (ignored)
```
#update server/env.sh  server/Makefile
vi server/Makefile
vi server/env.sh
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
make DEBUG=1
```

***********************************************************
              CALLING MAKE  FOR dbplugin
***********************************************************
make -C /home/mingyue/d/working/VMSS_0.0.5/VMSS/./extern/VMSS_Plugins/database/VMSS_MongoDB_Conn_Plugin -e -j1
make[2]: Entering directory '/group/xbjlab/dphi_software/software/workspace/mingyue/d/working/VMSS_0.0.5/VMSS/extern/VMSS_Plugins/database/VMSS_MongoDB_Conn_Plugin'
mkdir -p build/obj
Package libmongoc-1.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `libmongoc-1.0.pc'
to the PKG_CONFIG_PATH environment variable
No package 'libmongoc-1.0' found
gcc -I/home/mingyue/d/working/VMSS_0.0.5/VMSS/./extern/VMSS_Lib/include  -Wall -fPIC -O0 -g -c src/vmssDBconn.c -o build/obj/vmssDBconn.o
src/vmssDBconn.c:18:10: fatal error: mongoc.h: No such file or directory
   18 | #include <mongoc.h>
      |          ^~~~~~~~~~
compilation terminated.
make[2]: *** [Makefile:89: build/obj/vmssDBconn.o] Error 1
make[2]: Leaving directory '/group/xbjlab/dphi_software/software/workspace/mingyue/d/working/VMSS_0.0.5/VMSS/extern/VMSS_Plugins/database/VMSS_MongoDB_Conn_Plugin'
make[1]: *** [Makefile:121: dbplugin] Error 2
make[1]: Leaving directory '/group/xbjlab/dphi_software/software/workspace/mingyue/d/working/VMSS_0.0.5/VMSS/server'
make: [Makefile:41: /home/mingyue/d/working/VMSS_0.0.5/VMSS/server] Error 2 (ignored)
