# setup environment


follow [XBulter](https://confluence.xilinx.com/display/~vincentm/XButler)

## XRT

it is already installed.

## anaconda

refer to [anaconda](VART/anaconda_env.md)


## create anaconda mirror from xcd environment to bjlab

refer to [how to create a mirror for conda repo](https://docs.anaconda.com/anaconda-repository/admin-guide/install/config/mirrors/mirror-anaconda-repository/)

I don't know the version of the xcd repos version, lets' go anyway.

according to https://docs.anaconda.com/anaconda-repository/admin-guide/install/requirements/#repo-hardware-reqs,
and

```
(base) chunywan@xbjlabdpsvr15:~% env LANG=C df -h /scratch/
Filesystem                 Size  Used Avail Use% Mounted on
/dev/mapper/vg00-dockerlv  744G  269G  476G  37% /var/lib/docker
```
It seems that we don't have enough storage, even for local disk.

But without local mirrors and slow network, it is very challenging.

```

the content of `~/.condarc`

```yaml
channels:
  - conda-forge
  - defaults
```

```
rsync -a -e 'ssh -p 10152' localhost:/wrk/acceleration/conda-channel /scratch/chunywan
rmdir /scratch/chunywan/conda
mv -v $HOME/.conda /scratch/chunywan/conda
mkdir -p /scratch/chunywan/conda
ln -s /scratch/chunywan/conda $HOME/.conda
conda create -y -n butler python=3.7 \
    libuuid glog protobuf pybind11 jsoncpp xip \
    -c file://scratch/chunywan/conda-channel/ -c defaults -c conda-forge/label/gcc7
```


```

## XIP/XButler

```bash
function init_conda() {
    __conda_setup="$('/scratch/chunywan/anoconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
    if [ $? -eq 0 ]; then
          eval "$__conda_setup"
    else
          if [ -f "/scratch/chunywan/anoconda3/etc/profile.d/conda.sh" ]; then
                 . "/scratch/chunywan/anoconda3/etc/profile.d/conda.sh"
          else
                 export PATH="/scratch/chunywan/anoconda3/bin:$PATH"
         fi
   fi
}
```

```
init_conda
```
