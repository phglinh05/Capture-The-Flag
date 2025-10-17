# Extended GCD
a.u + b.v = gcd(a, b)

## Giải thích thuật toán Euclid mở rộng

1. Gọi r = a - q.b, thay vào phương trình:
   b.x1 + r.y1 = GCD(b, r)

2. Thay r vào, ta được:
   b.x1 + (a - q.b).y1 = GCD(a, b)

3. Khai triển:
   b.x1 + a.y1 - q.b.y1 = GCD(a, b)

4. Gom nhóm theo a và b:
   a.y1 + b.(x1 - q.y1) = GCD(a, b)

5. Kết luận:
   - x = y1
   - y = x1 - q.y1
 

