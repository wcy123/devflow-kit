# sync data from xbjlabdpsvr16

``` console
% ssh xbjlabdpsvr04
```

#

``` console
% function sync() { local a=$1; rsync -av xbjlabdpsvr16:/scratch/$USER/$a /scratch/$USER/; rm -fr $HOME/$a || true; ln -s /scratch/$USER/$a $HOME/; }
% for i in \
        .bashrc \
        build \
        .cache \
        .cargo \
        .ccache \
        .cgdb \
        .clangd \
        .cmake \
        conda \
        .conda \
        conda-channel \
        .condarc \
        .config \
        .dbshell \
        .dbus \
        debug_resnet50 \
        dpu_bsp \
        .emacs \
        .emacs.d \
        .fzf \
        .fzf.bash \
        .gitconfig \
        .gitignore \
        .ipython \
        .kshrc \
        .local \
        .rustup \
        .tmux.conf \
        .z.lua \
        .zshrc \
        ; do \
        sync $i; done
```

# install tmux

``` console
% ssh xbjlabdpsvr04
% cd ~/build
% pwd;ls
% tar xvf libevent.2.1.11.tar.gz
% cd libevent-release-2.1.11-stable
% bash autogen.sh
% ./configure --prefix=$HOME/.local && make -j10 && make install
% tar xvf tmux-3.0a.tar.gz
% cd tmux-3.0a/
% bash autogen.sh
% /tools/xgs/bin/sudo apt-get install -y  bison flex
% env PKG_CONFIG_PATH=$HOME/.local/lib/pkgconfig ./configure --prefix=$HOME/.local && make -j10 && make install
```

# install emacs

``` console
% cd ~/build;
% tar xvf emacs-26.3.tar.xz
% cd emacs-26.3
% ./configure --without-xpm  --with-gnutls=no --without-jpeg --without-tiff --without-gif --without-png --without-rsvg --without-lcms2 --without-libsystemd --without-xml2 --without-imagemagick --without-xft --without-libotf --without-m17n-flt --without-toolkit-scroll-bars --with-x=no --with-xpm=no --with-png=no  --with-x-toolkit=no --prefix=$HOME/.local --with-gif=no && make && make install
```
