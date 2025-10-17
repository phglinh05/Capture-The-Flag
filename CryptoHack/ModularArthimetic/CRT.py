def extended_gcd(a, b):
    # Thuật toán Euclid mở rộng để tìm nghịch đảo modular
    if b == 0:
        return a, 1, 0
    else:
        g, x, y = extended_gcd(b, a % b)
        return g, y, x - (a // b) * y

def modinv(a, m):
    # Tính nghịch đảo modular của a mod m
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise Exception('Không có nghịch đảo modular')
    else:
        return x % m

# Các phương trình đồng dư: x ≡ a_i (mod n_i)
a = [2, 3, 5]
n = [5, 11, 17]

# Tính tích N = n1 * n2 * n3 = 935
N = 1
for ni in n:
    N *= ni

x = 0
for ai, ni in zip(a, n):
    Mi = N // ni
    yi = modinv(Mi, ni)
    x += ai * Mi * yi

# Kết quả cuối cùng modulo N
x = x % N
print(f"Nghiệm nhỏ nhất x ≡ {x} mod {N}")
