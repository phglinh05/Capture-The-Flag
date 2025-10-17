from binascii import hexlify
import requests
import json
from string import printable

def encrypt(cipher):
    cipher = hexlify(cipher).decode()
    url = "https://aes.cryptohack.org/ecb_oracle/encrypt/" + cipher
    x = requests.get(url)
    ciphertext = x.text[15:-3]
    return ciphertext

def bruteforce():
    flag = ''
    total = 32 - 1
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-~!?#%&@{}'

    while True:
        payload = '1' * (total - len(flag))
        ciphertext_1 = encrypt(payload.encode())  
        for c in chars:
            ciphertext_2 = encrypt((payload + flag + c).encode())  
            # So sánh các block ở giữa ([32:64]) của mỗi văn bản đã mã hóa
            if ciphertext_2[32:64] == ciphertext_1[32:64]:
                flag += c
                break
    print(flag)

bruteforce()