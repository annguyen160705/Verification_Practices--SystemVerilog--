import os

def main():
    print("\n--- BƯỚC 3: KIỂM TRA KẾT QUẢ (CHECKING) ---")
    
    input_file = "sim/input.txt"
    sv_output_file = "sim/output_sv.txt"
    
    if not os.path.exists(input_file) or not os.path.exists(sv_output_file):
        print("[!] Lỗi: Không tìm thấy file dữ liệu để kiểm tra.")
        return

    with open(input_file, "r") as fin, open(sv_output_file, "r") as fout:
        inputs = fin.readlines()
        outputs_sv = fout.readlines()

    passed = 0
    failed = 0

    for i in range(len(inputs)):
        # Tách lấy a và b từ file input
        a, b = map(int, inputs[i].split())
        
        # Kết quả chuẩn (Golden Model)
        expected = a * b 
        
        # Kết quả từ mạch RTL
        actual = int(outputs_sv[i].strip())

        if expected == actual:
            passed += 1
        else:
            print(f"[FAIL] Dòng {i+1}: a={a}, b={b} | Kỳ vọng: {expected}, Thực tế: {actual}")
            failed += 1

    print(f"[*] Tổng số test: {len(inputs)}")
    print(f"[*] PASS: {passed} | FAIL: {failed}")
    
    if failed == 0:
        print(">>> KẾT LUẬN: MẠCH HOẠT ĐỘNG CHÍNH XÁC 100% <<<")
    else:
        print(">>> KẾT LUẬN: MẠCH BỊ LỖI <<<")

if __name__ == "__main__":
    main()