from Crypto.Util.number import long_to_bytes, inverse
matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]
flag = b''
for i in range(4):
    for j in range(4):
        flag = flag + long_to_bytes(matrix[i][j])
print(flag)