# create a hello mlir project

see start.md

# start

```
mkdir -p $W/loong;
cd $W/loong;
emacs -nw CMakeLists.txt

cmake -E time cmake -G Ninja \
    -B $BUILD/loong \
    -S $W/loong \
    -DCMAKE_EXPORT_COMPILE_COMMANDS=ON \
    -DCMAKE_C_COMPILER=clang \
    -DCMAKE_CXX_COMPILER=clang++ \
    -DCMAKE_PREFIX_PATH=$PREFIX

rm -fr  $BUILD/loong
ls -l $BUILD/loong
cp -av $BUILD/loong/compile_commands.json $W/loong

cmake --build $BUILD/loong

```
