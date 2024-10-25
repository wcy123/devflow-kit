# polygeist


Polygeist: Affine C in MLIR [MLIR Open Design Meeting 02/11/2021]
https://www.youtube.com/watch?v=GF45kitd3nY


```
cd /workspace/
git clone --recursive https://github.com/llvm/Polygeist
cd /workspace/Polygeist

cmake -G Ninja \
  -S /workspace/Polygeist/llvm-project/llvm \
  -DLLVM_ENABLE_PROJECTS="mlir;clang" \
  -DLLVM_TARGETS_TO_BUILD="host" \
  -DLLVM_ENABLE_ASSERTIONS=ON \
    -DCMAKE_C_COMPILER=clang \
    -DLLVM_ENABLE_LLD=OFF \
    -DCMAKE_CXX_COMPILER=clang++ \
  -DCMAKE_BUILD_TYPE=DEBUG  \
  -DLLVM_USE_LINKER=lld \
  -B $BUILD/Polygeist

cmake -E time cmake --build $BUILD/Polygeist -j $(nproc) && \
cmake -E time cmake --build $BUILD/Polygeist -j $(nproc) check-polygeist-opt && \
cmake -E time cmake --build $BUILD/Polygeist check-cgeist
```
