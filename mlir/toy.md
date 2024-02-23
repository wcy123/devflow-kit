# toy

## prepare

link https://mlir.llvm.org/docs/Tutorials/Toy/


```
cd /workspace
git clone https://github.com/joker-eph/llvm-project-with-mlir.git
cd llvm-project-with-mlir
```

```
cd /workspace
git clone https://github.com/llvm/llvm-project.git
```



```
cd /workspace
set_proxy http://localhost:9181
git clone https://github.com/llvm/llvm-project.git
cd /workspace/llvm-project
mkdir -p ~/build/llvm-project/

cmake -G Ninja  \
   -DLLVM_ENABLE_PROJECTS=mlir \
   -DLLVM_BUILD_EXAMPLES=ON \
   -DLLVM_TARGETS_TO_BUILD="Native;NVPTX;AMDGPU" \
   -DCMAKE_BUILD_TYPE=Release \
   -DLLVM_ENABLE_ASSERTIONS=ON \
   -DCMAKE_EXPORT_COMPILE_COMMANDS=ON \
   -S /workspace/llvm-project/llvm \
   -B $HOME/build/llvm-project

# Using clang and lld speeds up the build, we recommend adding:
#  -DCMAKE_C_COMPILER=clang -DCMAKE_CXX_COMPILER=clang++ -DLLVM_ENABLE_LLD=ON
# CCache can drastically speed up further rebuilds, try adding:
#  -DLLVM_CCACHE_BUILD=ON
# Optionally, using ASAN/UBSAN can find bugs early in development, enable with:
# -DLLVM_USE_SANITIZER="Address;Undefined"
# Optionally, enabling integration tests as well
# -DMLIR_INCLUDE_INTEGRATION_TESTS=ON
cmake --build $HOME/build/llvm-project  --target check-mlir
```

## ch1

```
cd /workspace/llvm-project/mlir/examples/toy/Ch1
tree .
cat CMakeLists.txt

cd /workspace/llvm-project/mlir
cat test/Examples/Toy/Ch1/ast.toy
$HOME/build/llvm-project/bin/toyc-ch1 test/Examples/Toy/Ch1/ast.toy -emit=ast
```


## ch2



```
cmake --build ~/build/llvm-project/ --target toyc-ch2 --verbose
[1/8] cd /home/chunywan/build/llvm-project && /home/chunywan/build/llvm-project/bin/mlir-tblgen -gen-dialect-defs -I /workspace/llvm-project/mlir/examples/toy/Ch2/include/toy -I/home/chunywan/build/llvm-project/include -I/workspace/llvm-project/llvm/include -I/workspace/llvm-project/mlir/include -I/home/chunywan/build/llvm-project/tools/mlir/include /workspace/llvm-project/mlir/examples/toy/Ch2/include/toy/Ops.td --write-if-changed -o tools/mlir/examples/toy/Ch2/include/toy/Dialect.cpp.inc -d tools/mlir/examples/toy/Ch2/include/toy/Dialect.cpp.inc.d
[2/8] cd /home/chunywan/build/llvm-project && /home/chunywan/build/llvm-project/bin/mlir-tblgen -gen-dialect-decls -I /workspace/llvm-project/mlir/examples/toy/Ch2/include/toy -I/home/chunywan/build/llvm-project/include -I/workspace/llvm-project/llvm/include -I/workspace/llvm-project/mlir/include -I/home/chunywan/build/llvm-project/tools/mlir/include /workspace/llvm-project/mlir/examples/toy/Ch2/include/toy/Ops.td --write-if-changed -o tools/mlir/examples/toy/Ch2/include/toy/Dialect.h.inc -d tools/mlir/examples/toy/Ch2/include/toy/Dialect.h.inc.d
[3/8] cd /home/chunywan/build/llvm-project && /home/chunywan/build/llvm-project/bin/mlir-tblgen -gen-op-defs -I /workspace/llvm-project/mlir/examples/toy/Ch2/include/toy -I/home/chunywan/build/llvm-project/include -I/workspace/llvm-project/llvm/include -I/workspace/llvm-project/mlir/include -I/home/chunywan/build/llvm-project/tools/mlir/include /workspace/llvm-project/mlir/examples/toy/Ch2/include/toy/Ops.td --write-if-changed -o tools/mlir/examples/toy/Ch2/include/toy/Ops.cpp.inc -d tools/mlir/examples/toy/Ch2/include/toy/Ops.cpp.inc.d
[4/8] cd /home/chunywan/build/llvm-project && /home/chunywan/build/llvm-project/bin/mlir-tblgen -gen-op-decls -I /workspace/llvm-project/mlir/examples/toy/Ch2/include/toy -I/home/chunywan/build/llvm-project/include -I/workspace/llvm-project/llvm/include -I/workspace/llvm-project/mlir/include -I/home/chunywan/build/llvm-project/tools/mlir/include /workspace/llvm-project/mlir/examples/toy/Ch2/include/toy/Ops.td --write-if-changed -o tools/mlir/examples/toy/Ch2/include/toy/Ops.h.inc -d tools/mlir/examples/toy/Ch2/include/toy/Ops.h.inc.d
```

```
cd /workspace/llvm-project/mlir
$HOME/build/llvm-project/bin/toyc-ch2 test/Examples/Toy/Ch2/codegen.toy -emit=mlir -mlir-print-debuginfo
$HOME/build/llvm-project/bin/toyc-ch2 test/Examples/Toy/Ch2/codegen.toy -emit=mlir -mlir-print-debuginfo | mlir-opt -mlir-print-op-generic

:mlir chunywan % $HOME/build/llvm-project/bin/toyc-ch2 test/Examples/Toy/Ch2/codegen.toy -emit=mlir -mlir-print-debuginfo
module {
  toy.func @multiply_transpose(%arg0: tensor<*xf64> loc("test/Examples/Toy/Ch2/codegen.toy":4:1), %arg1: tensor<*xf64> loc("test/Examples/Toy/Ch2/codegen.toy":4:1)) -> tensor<*xf64> {
    %0 = toy.transpose(%arg0 : tensor<*xf64>) to tensor<*xf64> loc("test/Examples/Toy/Ch2/codegen.toy":5:10)
    %1 = toy.transpose(%arg1 : tensor<*xf64>) to tensor<*xf64> loc("test/Examples/Toy/Ch2/codegen.toy":5:25)
    %2 = toy.mul %0, %1 : tensor<*xf64> loc("test/Examples/Toy/Ch2/codegen.toy":5:25)
    toy.return %2 : tensor<*xf64> loc("test/Examples/Toy/Ch2/codegen.toy":5:3)
  } loc("test/Examples/Toy/Ch2/codegen.toy":4:1)
  toy.func @main() {
    %0 = toy.constant dense<[[1.000000e+00, 2.000000e+00, 3.000000e+00], [4.000000e+00, 5.000000e+00, 6.000000e+00]]> : tensor<2x3xf64> loc("test/Examples/Toy/Ch2/codegen.toy":9:17)
    %1 = toy.reshape(%0 : tensor<2x3xf64>) to tensor<2x3xf64> loc("test/Examples/Toy/Ch2/codegen.toy":9:3)
    %2 = toy.constant dense<[1.000000e+00, 2.000000e+00, 3.000000e+00, 4.000000e+00, 5.000000e+00, 6.000000e+00]> : tensor<6xf64> loc("test/Examples/Toy/Ch2/codegen.toy":10:17)
    %3 = toy.reshape(%2 : tensor<6xf64>) to tensor<2x3xf64> loc("test/Examples/Toy/Ch2/codegen.toy":10:3)
    %4 = toy.generic_call @multiply_transpose(%1, %3) : (tensor<2x3xf64>, tensor<2x3xf64>) -> tensor<*xf64> loc("test/Examples/Toy/Ch2/codegen.toy":11:11)
    %5 = toy.generic_call @multiply_transpose(%3, %1) : (tensor<2x3xf64>, tensor<2x3xf64>) -> tensor<*xf64> loc("test/Examples/Toy/Ch2/codegen.toy":12:11)
    toy.print %5 : tensor<*xf64> loc("test/Examples/Toy/Ch2/codegen.toy":13:3)
    toy.return loc("test/Examples/Toy/Ch2/codegen.toy":8:1)
  } loc("test/Examples/Toy/Ch2/codegen.toy":8:1)
} loc(unknown)
:mlir chunywan % $HOME/build/llvm-project/bin/toyc-ch2 test/Examples/Toy/Ch2/codegen.toy -emit=mlir -mlir-print-debuginfo | mlir-opt -mlir-print-op-generic
module {
  toy.func @multiply_transpose(%arg0: tensor<*xf64> loc("test/Examples/Toy/Ch2/codegen.toy":4:1), %arg1: tensor<*xf64> loc("test/Examples/Toy/Ch2/codegen.toy":4:1)) -> tensor<*xf64> {
    %0 = toy.transpose(%arg0 : tensor<*xf64>) to tensor<*xf64> loc("test/Examples/Toy/Ch2/codegen.toy":5:10)
    %1 = toy.transpose(%arg1 : tensor<*xf64>) to tensor<*xf64> loc("test/Examples/Toy/Ch2/codegen.toy":5:25)
    %2 = toy.mul %0, %1 : tensor<*xf64> loc("test/Examples/Toy/Ch2/codegen.toy":5:25)
    toy.return %2 : tensor<*xf64> loc("test/Examples/Toy/Ch2/codegen.toy":5:3)
  } loc("test/Examples/Toy/Ch2/codegen.toy":4:1)
  toy.func @main() {
    %0 = toy.constant dense<[[1.000000e+00, 2.000000e+00, 3.000000e+00], [4.000000e+00, 5.000000e+00, 6.000000e+00]]> : tensor<2x3xf64> loc("test/Examples/Toy/Ch2/codegen.toy":9:17)
    %1 = toy.reshape(%0 : tensor<2x3xf64>) to tensor<2x3xf64> loc("test/Examples/Toy/Ch2/codegen.toy":9:3)
    %2 = toy.constant dense<[1.000000e+00, 2.000000e+00, 3.000000e+00, 4.000000e+00, 5.000000e+00, 6.000000e+00]> : tensor<6xf64> loc("test/Examples/Toy/Ch2/codegen.toy":10:17)
    %3 = toy.reshape(%2 : tensor<6xf64>) to tensor<2x3xf64> loc("test/Examples/Toy/Ch2/codegen.toy":10:3)
    %4 = toy.generic_call @multiply_transpose(%1, %3) : (tensor<2x3xf64>, tensor<2x3xf64>) -> tensor<*xf64> loc("test/Examples/Toy/Ch2/codegen.toy":11:11)
    %5 = toy.generic_call @multiply_transpose(%3, %1) : (tensor<2x3xf64>, tensor<2x3xf64>) -> tensor<*xf64> loc("test/Examples/Toy/Ch2/codegen.toy":12:11)
    toy.print %5 : tensor<*xf64> loc("test/Examples/Toy/Ch2/codegen.toy":13:3)
    toy.return loc("test/Examples/Toy/Ch2/codegen.toy":8:1)
  } loc("test/Examples/Toy/Ch2/codegen.toy":8:1)
} loc(unknown)
"builtin.module"() ({
^bb0:
}) : () -> ()
```

```
$HOME/build/llvm-project/bin/toyc-ch2 test/Examples/Toy/Ch2/codegen.toy -emit=ast
```



```
// A function that returns its argument twice:
func.func @count(%x: i64) -> (i64, i64)
           {
  return %x, %x: i64, i64
}
```

```
mlir-opt 3.mlir -mlir-print-op-generic
```


```
"builtin.module"() ({
  "func.func"() <{function_type = (i64) -> (i64, i64), sym_name = "count"}> ({
  ^bb0(%arg0: i64):
    "func.return"(%arg0, %arg0) : (i64, i64) -> ()
  }) : () -> ()
}) : () -> ()
```
