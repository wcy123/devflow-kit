

```
cd /workspace/
git clone https://github.com/onnx/onnx-mlir
cd /workspace/onnx-mlir
git submodule update --init
cmake -G Ninja \
  -S /workspace/onnx-mlir \
  -DMLIR_DIR=$BUILD/llvm-project/lib/cmake/mlir \
  -DLLVM_ENABLE_PROJECTS="mlir;clang" \
  -DLLVM_TARGETS_TO_BUILD="host" \
  -DLLVM_ENABLE_ASSERTIONS=ON \
    -DCMAKE_C_COMPILER=clang \
    -DLLVM_ENABLE_LLD=OFF \
    -DCMAKE_CXX_COMPILER=clang++ \
  -DCMAKE_BUILD_TYPE=DEBUG  \
  -DLLVM_USE_LINKER=lld \
  -B $BUILD/onnx-mlir

(cd /workspace/llvm-project; git checkout b2cdf3cc4c08729d0ff582d55e40793a20bbcdcc)
cmake -E time cmake --build $BUILD/onnx-mlir -j $(nproc)

```


```
ls $BUILD/onnx-mlir/DEBUG/bin
find $BUILD/onnx-mlir/ -iname onnx-mlir
 /workspaceon./third_party/onnx/onnx/backend/test/data/node/test_add/model.onnx
```
