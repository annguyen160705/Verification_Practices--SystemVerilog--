import random
import os

def main():
    # Đảm bảo thư mục sim tồn tại
    os.makedirs("sim", exist_ok=True)
    
    # Mở file để ghi dữ liệu
    with open("sim/input.txt", "w") as f:
        for _ in range(100): # Tạo 100 test case
            a = random.randint(0, 255)
            b = random.randint(0, 255)
            # Ghi vào file, mỗi dòng 2 số cách nhau bởi dấu cách
            f.write(f"{a} {b}\n")
            
    print("[*] Đã sinh 100 test cases vào sim/input.txt")

if __name__ == "__main__":
    main()