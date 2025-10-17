# Fermat's Little Theorem 
## I. Nội dung của định lý
Nếu p là một số nguyên tố và a là một số nguyên bất kỳ không chia hết cho p (tức là gcd(a,p) = 1) thì:
 a^(p-1) ≡ 1 (mod p)

## II. Example:
Tính 10^12 mod 13:
`10 mod 13 = 10`
`10^2 mod 13 = 100 mod 13 = 9`
`10^4 mod 13 = (10^2)^2 mod 13 = 9^2 mod 13 = 81 mod 13 = 3`
`10^12 mod 13 = (10^4)^3 mod 13 = 3^3 mod 13 = 27 mod 13 = 1`

Kết quả: `10^12 ≡ 1 (mod 13)`.

---

## III. Ứng dụng:
1. **Tính lũy thừa nhanh**: Thay vì tính trực tiếp `a^b mod p`, Fermat's Little Theorem giúp rút gọn lũy thừa với `p` là số nguyên tố.
2. **Mã hóa RSA**: Fermat's Little Theorem được dùng để tính số mũ ngược trong trường hợp đặc biệt.
3. **Kiểm tra tính nguyên tố**: Định lý là cơ sở cho các thuật toán như kiểm tra Fermat (Fermat primality test).


### Lưu ý:
Fermat's Little Theorem chỉ áp dụng khi `p` là số nguyên tố. Nếu `p` không phải số nguyên tố, thì định lý không đảm bảo kết quả đúng.
