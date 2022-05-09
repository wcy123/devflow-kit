# onnx xnnc 需要做的事情

1. 融合 `QLinear` 和 `DeQLinear` 编成一个 `fix` op
2. layout 转换，这部分比较难。 按照 TVM 的思路，分成几种 Op.
   1. layout 敏感 例如 Conv ， weight/bias
   2. layout 中度敏感 例如 transpose
   3. layout 不敏感的 例如 relu sigmoid
3. 转换 onnx 模型到 xmodel 上。难点
   1. 属性映射。
      1. xmodel 不支持 graph 属性。
   2. 不认识的 op 统一成为 customized op 。
