
https://jeremykun.com/2023/08/10/mlir-running-and-testing-a-lowering/


```
cd /workspace/llvm-project
grep -r convert-ctlz /workspace/llvm-project/mlir
bat /workspace/llvm-project/mlir/test/Conversion/MathToFuncs/ctlz.mlir
```


```
mlir-opt /workspace/llvm-project/mlir/test/Dialect/Affine/affine-loop-normalize.mlir -affine-loop-normalize -split-input-file | bat
```


Polygeist: Affine C in MLIR [MLIR Open Design Meeting 02/11/2021]
https://www.youtube.com/watch?v=GF45kitd3nY


```
mlir-opt --
```
