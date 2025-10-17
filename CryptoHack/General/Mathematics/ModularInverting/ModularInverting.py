# Sử dụng Fermat's Little Theorem
def modular_inverse(a, n):
    return pow(a, n-2, n) # Chỉ dùng được nếu n là số nguyên tố

a = 3
n = 13
print(modular_inverse(3, 13))