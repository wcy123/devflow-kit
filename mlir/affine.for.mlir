func.func @loop_with_unknown_upper_bound(%arg0: memref<?x?xf32>, %arg1: index) {
  %c0 = arith.constant 0 : index
  %0 = memref.dim %arg0, %c0 : memref<?x?xf32>
  affine.for %i0 = 2 to %0 step 32 {
    affine.for %i1 = 0 to %arg1 step 2 {
      "test.foo"(%i0, %i1) : (index, index) -> ()
    }
  }
  return
}