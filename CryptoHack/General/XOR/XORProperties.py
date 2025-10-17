#Commutative: A ⊕ B = B ⊕ A
#Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
#Identity: A ⊕ 0 = A
#Self-Inverse: A ⊕ A = 0

KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY2_KEY1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
KEY2_KEY3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
FLAG_KEY1_KEY3_KEY2 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"
bytes_KEY1 = bytes.fromhex(KEY1)
bytes_KEY1_KEY2 = bytes.fromhex(KEY2_KEY1)
bytes_KEY2_KEY3 = bytes.fromhex(KEY2_KEY3)
bytes_FLAG_KEY1_KEY2_KEY3 = bytes.fromhex(FLAG_KEY1_KEY3_KEY2)
KEY2 = b''
KEY3 = b''
FLAG = b''
for i in range (len(bytes_KEY1)):
    KEY2+= bytes([bytes_KEY1[i]^bytes_KEY1_KEY2[i]])
for i in range (len(bytes_KEY1)):
    KEY3+= bytes([KEY2[i]^bytes_KEY2_KEY3[i]])
for i in range (len(bytes_KEY1)):
    FLAG+= bytes([bytes_FLAG_KEY1_KEY2_KEY3[i]^KEY2[i]^bytes_KEY1[i]^KEY3[i]])
print(FLAG)

#KEY1 ^ KEY2 ^ KEY1 = 0 ^ KEY2
#xor among bytes return integer
