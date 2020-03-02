# install gcc



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
