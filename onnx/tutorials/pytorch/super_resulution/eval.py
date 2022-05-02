import onnx
import torch
import numpy as np

onnx_model = onnx.load("super_resolution.onnx")
onnx.checker.check_model(onnx_model)

import onnxruntime

ort_session = onnxruntime.InferenceSession("super_resolution.onnx")


def to_numpy(tensor):
    return tensor.detach().cpu().numpy(
    ) if tensor.requires_grad else tensor.cpu().numpy()


from PIL import Image
import torchvision.transforms as transforms

img = Image.open("./cat_224x224.jpg")

resize = transforms.Resize([224, 224])
img = resize(img)

img_ycbcr = img.convert('YCbCr')
img_y, img_cb, img_cr = img_ycbcr.split()
print(f"img_cb = {img_cb}")
print(f"img_cr = {img_cr}")
print(f"img_y = {img_y}")
to_tensor = transforms.ToTensor()
img_y = to_tensor(img_y)
img_y.unsqueeze_(0)

# compute ONNX Runtime output prediction
ort_inputs = {ort_session.get_inputs()[0].name: to_numpy(img_y)}
ort_outs = ort_session.run(None, ort_inputs)
img_out_y = ort_outs[0]

img_out_y = Image.fromarray(np.uint8((img_out_y[0] * 255.0).clip(0, 255)[0]),
                            mode='L')
print(f"img_out_y.size= {img_out_y.size}")

img_out_y_size = img_out_y.size
# get the output image follow post-processing step from PyTorch implementation
final_img = Image.merge(
    "YCbCr",
    [
        # img_out_y,
        img_out_y,
        img_cb.resize(img_out_y_size, Image.BICUBIC),
        img_cr.resize(img_out_y_size, Image.BICUBIC),
    ]).convert("RGB")

# Save the image, we will compare this with the output image from mobile device
final_img.save("./cat_superres_with_ort.jpg")
