from Crypto.Cipher import AES
import hashlib
ciphertext = "c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66"
ciphertext = bytes.fromhex(ciphertext)
with open("words.txt", 'r') as f:
    for chuoi in f:
      keyword = chuoi.strip()
      KEY = hashlib.md5(keyword.encode()).digest()
      cipher = AES.new(KEY, AES.MODE_ECB)
      decrypted = cipher.decrypt(ciphertext)
      if b'crypto' in decrypted:
         print(decrypted)