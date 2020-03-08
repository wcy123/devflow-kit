### use root login
```
/tools/xgs/bin/sudo -i
```
### install emacs 25.3.1

```
yum remove -y emacs

wget ftp://ftp.gnu.org/pub/gnu/emacs/emacs-25.3.tar.gz
tar -zxvf emacs-25.3.tar.gz
cd emacs-25.3/
./configure
make && make install
```

### install tmux 3a
```
yum remove -y tmux
mkdir tmux_install
cd tmux_install
```
install libevent & ncurses.tar.gz
```
wget https://github.com/libevent/libevent/releases/download/release-2.1.11-stable/libevent-2.1.11-stable.tar.gz
tar -zxvf libevent-2.1.11-stable.tar.gz
cd libevent-2.1.11-stable/
./configure --prefix=/usr/local --enable-shared
make && make install


cd ../
wget ftp://ftp.invisible-island.net/ncurses/ncurses.tar.gz
tar -zxvf ncurses.tar.gz
cd ncurses-6.2/
./configure --prefix=/usr/local --with-shared --enable-pc-files --with-pkg-config-libdir=/usr/local/lib/pkgconfig
make && make install

```
install tmux
```
cd ..
wget https://github.com/tmux/tmux/releases/download/3.0a/tmux-3.0a.tar.gz
tar -zxvf tmux-3.0a.tar.gz
cd tmux-3.0a/
PKG_CONFIG_PATH=/usr/local/lib/pkgconfig ./configure --prefix=/usr/local
make && make install


ln -s /usr/bin/tmux /usr/local/bin/tmux
exit

tmux -V
emacs --version
```

end
