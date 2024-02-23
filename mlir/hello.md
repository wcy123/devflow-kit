# create a hello mlir project

see start.md

# start

```
mkdir -p $W/hello-mlir;
cd $W/hello-mlir;
emacs -nw CMakeLists.txt

cmake \
    -B $BUILD/hello-mlir \
    -S $W/hello-mlir \
    -DCMAKE_EXPORT_COMPILE_COMMANDS=ON \
    -DCMAKE_PREFIX_PATH=$PREFIX

rm -fr  $BUILD/hello-mlir
ls -l $BUILD/hello-mlir
cp -av $BUILD/hello-mlir/compile_commands.json $W/hello-mlir

cmake --build $BUILD/hello-mlir

```
