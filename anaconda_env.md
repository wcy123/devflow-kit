## install anaconda


```
cd ~/bulid
curl -Lo Anaconda3-2019.10-Linux-x86_64.sh https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh
```

you can copy if from `/wrk/xcdhdnobkup1/chunywan/build/Anaconda3-2019.10-Linux-x86_64.sh`

```
chmod +x Anaconda3-2019.10-Linux-x86_64.sh
./Anaconda3-2019.10-Linux-x86_64.sh -p /wrk/xcdhdnobkup1/chunywan/local/anaconda3
```

The installation will modify your `~/.bashrc`, you have to logout and login again to use `conda`.

if you use xcd environment, please have look at https://confluence.xilinx.com/display/XCD/How+to+install+conda%2C+anaconda+packages+in+XCD

```
conda config --add channels https://xcdconda/defaults/
conda config --add channels https://xcdconda/bioconda/
conda config --add channels https://xcdconda/conda-forge/
conda config --add channels https://xcdconda/pytorch/
conda config --remove channels defaults
conda config --set show_channel_urls yes
conda config --set ssl_verify /etc/ssl/certs/ca-certificates.crt
cat ~/.condarc
```
