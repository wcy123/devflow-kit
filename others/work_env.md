# setup dev environment

## tmux

``` console
% cd -P $HOME/build
% # install libevent
% # TODO
```

## emacs

``` console
% ./configure --without-xpm --without-jpeg --without-tiff --without-gif --without-png --without-rsvg --without-lcms2 --without-libsystemd --without-xml2 --without-imagemagick --wi
thout-xft --without-libotf --without-m17n-flt --without-toolkit-scroll-bars --with-x=no --with-xpm=no --with-png=no  --with-x-toolkit=no --prefix=$HOME/.local --with-gif=no && make && make install
```

install configuration

``` console
% ssh xsjsda153 cat /proj/xsjhdstaff6/chunywan/d/working/100ms_dot_emacs/out/100ms_dot_emacs.emacs.d.latest.tar.gz | tar -zxvf - -C ~/
```
