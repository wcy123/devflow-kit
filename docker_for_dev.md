# docker for development



``` console
% ssh xsjsda153
xsjsda153:~% cd $HOME/d/working/
xsjsda153:working% git clone gits@xcdl190260:devops/vitis-ai-dev-docker.git
xsjsda153:working% cd vitis-ai-dev-docker
xsjsda153:vitis-ai-dev-docker% ./docker_run.sh xdock.xilinx.com/vitis-ai-dev:latest
chunywan@xsjsda153:/workspace $ ls
```

## for cloud

``` console
chunywan@xsjsda153:/workspace $ build_type=Debug  ;\
os=`lsb_release -a | grep "Distributor ID" | sed 's/^.*:\s*//'`  ;\
os_version=`lsb_release -a | grep "Release" | sed 's/^.*:\s*//'` ;\
arch=`uname -p`  ;\
target_info=${os}.${os_version}.${arch};

chunywan@xsjsda153:/workspace $ git clone ssh://gits@xcdl190260/aisw/unilog
chunywan@xsjsda153:/workspace $ cd unilog
chunywan@xsjsda153:/workspace $ ./cmake.sh --build-dir--pack=deb --clean
chunywan@xsjsda153:/workspace $  git clone ssh://gits@xcdl190260/aisw/xir
chunywan@xsjsda153:/workspace $  git clone ssh://gits@xcdl190260/aisw/vart
chunywan@xsjsda153:/workspace $  git clone ssh://gits@xcdl190260/aisw/Vitis-AI-Library
```

## for edge

``` console

```
