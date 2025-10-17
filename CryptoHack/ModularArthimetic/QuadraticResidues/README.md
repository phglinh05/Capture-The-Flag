# Square root modul

**Square root modulo (căn bậc hai modulo)** là bài toán tìm số x sao cho:

*x^2 ≡ a (mod n)*
với a, n là các số nguyên cho trước.

Nói cách khác, số x là căn bậc hai modulo của a theo modulo n nếu khi bình phương x rồi lấy phần dư chia n, ta được a.

**Điều kiện tồn tại căn bậc hai modulo:**
1. Modulo n là số nguyên tố:
   - a là quadratic residue modulo p (tồn tại x sao cho 
*x^2 ≡ a(mod p)*) nếu và chỉ nếu: 
*a^((p−1)/2) ≡ 1(mod p)*
Explain:
 

2. Modulo n là hợp số:
   - Xử lý phức tạp hơn và thường phải phân tích n thành các thừa số nguyên tố, sau đó giải bài toán với từng modulo nguyên tố (theo Chinese Remainder Theorem).
