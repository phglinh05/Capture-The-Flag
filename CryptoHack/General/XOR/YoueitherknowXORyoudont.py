from pwn import*
encode_flag = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
encode_flag = bytes.fromhex(encode_flag)
flag_format = b'crypto{'
secretkey = b'myXORkey'
print(xor(encode_flag, flag_format))
print(xor(encode_flag, secretkey))