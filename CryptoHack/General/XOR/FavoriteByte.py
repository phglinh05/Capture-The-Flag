
#C1
from pwn import xor
hex = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
hex = bytes.fromhex(hex)
predict_flag = b'c'
print(hex[0] ^ predict_flag[0])
flag = b''
for i in hex:
    flag += bytes([16^i])
print(flag)

#C2
po_flag = ""
for i in range (256):
    ord = [i ^ o for o in hex]
    po_flag = "".join(chr(o) for o in ord)
    if po_flag.startswith("crypto"):
        flag = po_flag
        break
print(flag)