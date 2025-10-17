from sympy.ntheory import sqrt_mod

# Đọc dữ liệu từ file output.txt
with open("output1.txt") as f:
    lines = f.read().splitlines()
    a = int(lines[0].split('=')[1].strip())
    p = int(lines[1].split('=')[1].strip())


# Tính căn bậc hai modulo p
roots = sqrt_mod(a, p, all_roots=True)

# Chọn nghiệm nhỏ hơn
flag = min(roots)

print("Flag:", flag)
