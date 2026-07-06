import os
import subprocess
import sys

def run_cmd(cmd):
    print(f"\n[*] Đang chạy: {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"[!] LỖI: Lệnh thất bại với mã lỗi {result.returncode}")
        sys.exit(1)

def main():
    print("="*50)
    print("   KHỞI ĐỘNG LUỒNG MÔ PHỎNG MODELSIM")
    print("="*50)

    # Tối ưu: Tạo thư mục 'sim' để chứa dữ liệu mô phỏng rác/kết quả
    if not os.path.exists("sim"):
        os.makedirs("sim")
        print("[*] Đã tạo thư mục 'sim' để giữ sạch project.")

    # ---------------------------------------------------------
    # CHỖ CHÈN 1: BƯỚC 0 - Tạo dữ liệu test trước khi làm mọi thứ
    # ---------------------------------------------------------
    print("\n--- BƯỚC 0: TẠO DỮ LIỆU TEST ---")
    run_cmd("python script/gen_input.py")

    # 1. Tạo thư viện làm việc 'work'
    if not os.path.exists("work"):
        run_cmd("vlib work")

    # 2. Biên dịch mã nguồn (Compile)
    print("\n--- BƯỚC 1: BIÊN DỊCH (COMPILE) ---")
    compile_cmd = "vlog -sv +incdir+rtl rtl/multiplier.sv tb/multiplier_tb.sv"
    run_cmd(compile_cmd)

    # 3. Chạy mô phỏng (Simulate)
    print("\n--- BƯỚC 2: MÔ PHỎNG (SIMULATE) ---")
    sim_cmd = 'vsim -c -voptargs="+acc" -do "run -all; quit" work.multiplier_tb'
    run_cmd(sim_cmd)

    print("\n" + "="*50)
    print("   MÔ PHỎNG HOÀN TẤT THÀNH CÔNG!")
    print("="*50)

    # ---------------------------------------------------------
    # CHỖ CHÈN 2: BƯỚC 3 - Kiểm tra kết quả ngay sau khi chạy xong
    # ---------------------------------------------------------
    run_cmd("python script/check.py")

    # Dọn dẹp file log của ModelSim
    if os.path.exists("transcript"):
        os.replace("transcript", "sim/transcript")
        
    # 4. Chuyển đổi và xem sóng (Waveform)
    view_wave = input("\nBạn có muốn mở ModelSim để xem sóng không? (y/n): ")
    if view_wave.lower() == 'y':
        print("[*] Đang chuẩn bị dữ liệu sóng...")
        convert_cmd = "vcd2wlf sim/waveform.vcd sim/waveform.wlf"
        run_cmd(convert_cmd)
        
        print("[*] Đang mở giao diện ModelSim...")
        view_cmd = "vsim -gui -logfile sim/transcript_gui -view sim/waveform.wlf"
        subprocess.Popen(view_cmd, shell=True)

if __name__ == "__main__":
    main()