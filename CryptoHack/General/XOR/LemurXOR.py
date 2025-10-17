
from PIL import Image
import numpy as np

# Load 2 ảnh
img1 = Image.open("flag.png")
img2 = Image.open("lemur.png")

# Chuyển về numpy array (RGB)
arr1 = np.array(img1)
arr2 = np.array(img2)

# XOR từng pixel RGB
result = np.bitwise_xor(arr1, arr2)

# Lưu ảnh kết quả
Image.fromarray(result).save("result.png")
