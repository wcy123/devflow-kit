# build it on xsjsda23


It seems that I have to create my own environmet, otherwise, I run
into a error as below

```
  File "/scratch/anaconda2/lib/python2.7/os.py", line 157, in makedirs
    mkdir(name, mode)
OSError: [Errno 13] Permission denied: '/scratch/anaconda2/pkgs/pybind11-2.4.3-py37hfd86e86_0'
```

```
ssh xsjsda23
source /scratch/anaconda2/etc/profile.d/conda.sh
conda create --prefix /scratch/chunywan/conda_envs
conda activate /scratch/chunywan/conda_envs
conda install -y opencv
conda install -y pybind11
conda install -y glog
conda install -y protobuf
conda install -y libprotobuf
conda list
```

after create the conda env

```
ssh xsjsda23
source /scratch/anaconda2/etc/profile.d/conda.sh
conda activate /scratch/chunywan/conda_envs
cd -P  $HOME/d/working
git clone gits@xcdl190260:vitis/conda-feedstock.git
cd  $HOME/d/working/conda-feedstock
git checkout br-for-unilog-xir-vart
conda build unilog-feedstock 2>$HOME/conda-build.stderr  | tee $HOME/conda-build.stdout
conda build target_factory-feedstock 2>&1 | tee $HOME/conda-build.stdout
conda build xir-feedstock 2>&1 | tee $HOME/conda-build.stdout
conda build vart-feedstock 2>&1 | tee $HOME/conda-build.stdout
conda build xnnc4xir-feedstock 2>&1 | tee $HOME/conda-build.stdout
conda build xcompiler-feedstock 2>&1 | tee $HOME/conda-build.stdout
emacs -nw  $HOME/conda-build.stdout
```


```
mkdir -p xnnc4xir-feedstock
git status --untracked-files
emacs -nw xcompiler-feedstock/meta.yaml
emacs -nw xcompiler-feedstock/build.sh
emacs -nw ~/d/working/xnnc4xir/requirements.txt
```
