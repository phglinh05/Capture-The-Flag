# Modular Inverting
Nghịch đảo modulo của một số a (mod n) là một số x thỏa mãn:
a.x ≡ 1(mod n)
Điều này có nghĩa là khi nhân a với x và lấy phần dư chia cho n, ta sẽ được kết quả là 1.

Điều kiện tồn tại:
Nghịch đảo modulo của a theo n chỉ tồn tại nếu: gcd(a,n)=1
Tức là a và n phải nguyên tố cùng nhau (không có ước chung lớn hơn 1).

**Fermat's Little Theorem** có thể được sử dụng để tìm nghịch đảo modulo của một số a khi mô-đun p là một số nguyên tố.

Theo định lý này, nếu p là một số nguyên tố và a là một số nguyên không chia hết cho p, thì:

a^(p−1) ≡ 1(mod p)
Từ đây, suy ra:

a^(p−2) ≡ a^(-1) (mod p)

Do đó, số nghịch đảo modulo của a theo p là:

a^(−1) = a^(p−2) (mod p)