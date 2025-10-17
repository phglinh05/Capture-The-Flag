from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes, bytes_to_long
iv = "5b3d6c0e06bb8c2a573d08303a01f0d7"
ciphertext1 ="6875549949d204e7aaecd80dd4070c4f"
ciphertext2 = "511ab68862534cdcf52d1bd9d0444ba9"

de_ciphertext1 = "384f157e72d4f719345f57054f629be2"
de_ciphertext2 = "374122a978b65bd69db3f92cf5262d32"

print(long_to_bytes(bytes_to_long(bytes.fromhex(de_ciphertext1))^bytes_to_long(bytes.fromhex(iv))))
print(long_to_bytes(bytes_to_long(bytes.fromhex(ciphertext1))^bytes_to_long(bytes.fromhex(de_ciphertext2))))