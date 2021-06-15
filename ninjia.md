# build

``` console
% mkdir -p /home/build/build_cloud_debug/unilog_ninjia
% cd  /home/build/build_cloud_debug/unilog_ninjia
% cmake -G Ninja -DBUILD_TEST=ON -DCMAKE_BUILD_TYPE=Debug -DCMAKE_EXPORT_COMPILE_COMMANDS=ON -DCMAKE_INSTALL_PREFIX=/home/chunywan/.local/Ubuntu.18.04.x86_64.Debug /workspace/aisw/unilog
% time ninja
```
