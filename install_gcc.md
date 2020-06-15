# install gcc


``` console
% yum install yum-downloadonly
% yumdownloader centos-release-scl-2-2.el7.centos.noarch.rpm
% sudo rpm --nodeps -i ~/build/centos-release-scl-2-2.el7.centos.noarch.rpm
% yum install centos-release-scl
% scp /etc/yum.repos.d/CentOS-SCLo-scl-rh.repo to som /etc/yum.repos.d/CentOS-SCLo-scl-rh.repo
% sudo yum install -y devtoolset-9
```

enable gcc9

```  console
% source /opt/rh/devtoolset-9/enable
```



# install gcc7.4 from source code

```
cd $HOME/build
curl -Logcc-7.4.0.tar.gz  http://ftp.mirrorservice.org/sites/sourceware.org/pub/gcc/releases/gcc-7.4.0/gcc-7.4.0.tar.gz
tar xvf gcc-7.4.0.tar.gz
cd  gcc-7.4.0
sudo  yum install -y gmp-devel mpfr-devel libmpc-devel
./configure --disable-multilib --enable-languages=c,c++
make -j 4
sudo make install
```
