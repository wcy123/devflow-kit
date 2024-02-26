

```
cd /workspace
set_proxy http://localhost:9181
git clone https://github.com/llvm/llvm-project.git
cd /workspace/llvm-project
mkdir -p ~/build/llvm-project/
sudo -E apt-get install -y lld

cmake -G Ninja  \
   -DLLVM_ENABLE_PROJECTS='mlir;lld' \
   -DLLVM_BUILD_EXAMPLES=ON \
   -DLLVM_TARGETS_TO_BUILD="Native;NVPTX;AMDGPU" \
   -DCMAKE_BUILD_TYPE=Debug \
   -DLLVM_ENABLE_LLD=ON \
   -DCMAKE_EXPORT_COMPILE_COMMANDS=ON \
   -DLLVM_ENABLE_ASSERTIONS=ON \
   -S /workspace/llvm-project/llvm \
   -B $BUILD/llvm-project

cp -av $BUILD/llvm-project/compile_commands.json /workspace/llvm-project/

# Using clang and lld speeds up the build, we recommend adding:
#  -DCMAKE_C_COMPILER=clang -DCMAKE_CXX_COMPILER=clang++ -DLLVM_ENABLE_LLD=ON
# CCache can drastically speed up further rebuilds, try adding:
#  -DLLVM_CCACHE_BUILD=ON
# Optionally, using ASAN/UBSAN can find bugs early in development, enable with:
# -DLLVM_USE_SANITIZER="Address;Undefined"
# Optionally, enabling integration tests as well
# -DMLIR_INCLUDE_INTEGRATION_TESTS=ON
cmake --build $BUILD/llvm-project  --target check-mlir -j $(nproc)&& \
cmake --build $BUILD/llvm-project -j $(nproc) && \
cmake --install $BUILD/llvm-project   --prefix $PREFIX
grep cmake $BUILD/llvm-project/install_manifest.txt
```
