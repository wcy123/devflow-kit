# MLIR tutorial

# download

https://serene-lang.org

```
cd /workspace
git clone https://devheroes.codes/serene/serene
cd /workspace/serene;
ls -l
git clone https://devheroes.codes/Serene/bootstrap-toolchain
cd /workspace/bootstrap-toolchain;
ls -l
```

#

```
cmake \
    -B $BUILD/serene \
    -S $W/serene \
    -DCMAKE_EXPORT_COMPILE_COMMANDS=ON \
    -DCMAKE_PREFIX_PATH=$PREFIX

cp -av $BUILD/serene/compile_commands.json $W/serene
```
