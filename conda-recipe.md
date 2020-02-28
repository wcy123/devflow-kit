## create a conda package


```
# on xcosda93
cd /home/chunywan/build/vitis-ai-docker
./docker_run.sh xdock.xilinx.com/vitis_conda_build_env:latest # xdock.xilinx.com/vitis-ai:tools-1.0.3-cpu # wcy_xdock
```

```
# in host
cd /home/chunywan/build/vitis-ai-docker/d/working/unilog
git checkout dev
git status
```


```
#in docker
sudo su
scp -r chunywan@xcosda93:.ssh/* ~/.ssh/
# sudo conda install -y conda-build
# sudo apt update
# sudo apt install -y openssh-client
cd /workspace/d/working/
conda build unilog  2>&1 | tee $HOME/build.log
conda build xir  2>&1 | tee $HOME/build.log
conda build vart  2>&1 | tee $HOME/build.log
conda build dpuv1  2>&1 | tee $HOME/dpuv1.build.log
vim $HOME/build.log
ZZ

cp $HOME/build.log
vim $HOME/build.clean.log
grep uuid $HOME/build.log
tar tf /home/xbuild/conda-bld/linux-64/xir-0.0.1-h1acae8b_0.tar.bz2 | less
git clone gits@xcdl190260:aisw/unilog /home/chunywan/conda-bld/git_cache/gits@xcdl190260_aisw/unilog
cat /opt/xilinx/xrt/include/version.h | grep xrt_build_version_hash # "192e706aea53163a04c574f9b3fe9ed76b6ca471"
# /opt/xilinx/xrt/lib/libxrt_core.so: undefined reference to `uuid_copy@UUID_1.0'
# /opt/xilinx/xrt/lib/libxrt_core.so: undefined reference to `memcpy@GLIBC_2.14'
```

publish meta.yaml

```
#in host
# git clone gits@xcdl190260:vitis/Vitis-AI $HOME/home/chunywan/build/vitis-ai-docker/d/working/Vitis-AI
# cd $HOME/home/chunywan/build/vitis-ai-docker/d/working/Vitis-AI
# ls -l conda-feedstock
git clone gits@xcdl190260:vitis/conda-feedstock /home/chunywan/build/vitis-ai-docker/d/working/conda-feedstock
cd /home/chunywan/build/vitis-ai-docker/d/working/conda-feedstock
git checkout -b br-for-unilog-xir-vart
mkdir -p vart-feedstock
mkdir -p unilog-feedstock
mkdir -p xir-feedstock
cp $HOME/build/vitis-ai-docker/d/working/vart/{build.sh,meta.yaml} vart-feedstock
cp $HOME/build/vitis-ai-docker/d/working/xir/{build.sh,meta.yaml} xir-feedstock
cp $HOME/build/vitis-ai-docker/d/working/unilog/{build.sh,meta.yaml} unilog-feedstock
git status --untracked-files
cd /home/chunywan/build/vitis-ai-docker
./docker_run.sh xdock.xilinx.com/vitis_conda_build_env:latest # xdock.xilinx.com/vitis-ai:tools-1.0.3-cpu # wcy_xdock
cd /workspace/d/working/conda-feedstock
conda build unilog-feedstock  2>&1 | tee $HOME/build.log
conda build xir-feedstock  2>&1 | tee $HOME/build.logo
conda build vart-feedstock  2>&1 | tee $HOME/build.log
exit
cd /home/chunywan/build/vitis-ai-docker/d/working/conda-feedstock
git status --untracked-files
```
