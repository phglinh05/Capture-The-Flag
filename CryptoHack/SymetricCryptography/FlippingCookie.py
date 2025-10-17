from Crypto.Util.number import long_to_bytes, bytes_to_long
from pwn import xor
cookie = "8951e256f44bd526bd13c6e56d87ba15e4c682dbc601874e5c457a42246d5a9f1f566e79260b0e6658bea45f618f0922"
iv_new = xor(bytes.fromhex(cookie[:32]),b'admin=False',b'admin=True;').hex()


ciphertext = cookie[32:]

print(iv_new, ciphertext)
