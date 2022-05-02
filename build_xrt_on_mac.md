

``` console
% cd ~/d/working/
% git clone https://github.com/Xilinx/XRT.git
% cd XRT
% git remote -v show
% cd build
% env PKG_CONFIG_PATH="/usr/local/opt/openssl@1.1/lib/pkgconfig" cmake ../src
% make VERBOSE=1
```
