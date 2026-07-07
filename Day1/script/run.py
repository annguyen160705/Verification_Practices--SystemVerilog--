import os


if not os.path.exists("sim"):
    os.mkdir("sim")
    print("New sim folder has been created")

# DỊCH CHUYỂN VÀO THƯ MỤC SIM
# Kể từ dòng này trở đi, mọi hành động lưu/đọc file đều diễn ra bên trong thư mục 'sim'
os.chdir("sim")

#==================Generating inputs==========================#
print("=" * 50)
print("Generating input . . . ")
print("=" * 50)

status = os.system("python ../script/gen_input.py")
if(status != 0):
    print("Input generation failed. Please check the gen_input.py script.")
    exit(1)

#==================Simulation==========================#
print("=" * 50)
print("Starting simulation . . . ")
print("=" * 50)


if not os.path.exists("work"):
    os.system("vlib work")
    print("New work.lib has been created")
else:
    print("work.lib was created, skip")

compile_ok = (
    os.system("vlog ../tb/*.sv") == 0
)

if not compile_ok:
    print("Compilation failed.")
    exit(1)

#   -c                   : Chạy trên giao diện dòng lệnh (Command Line), không mở GUI.
#   -do "run -all; quit" : Tự động chạy toàn bộ thời gian mô phỏng, xong thì thoát.
#   -l log.txt           : Lưu toàn bộ nội dung in ra màn hình vào thẳng file log.txt.
#   logic_test              : Tên module bên trong file SystemVerilog của bạn.
os.system('vsim -c -do "run -all; quit" -l log.txt logic_test')

print("Simulation completed. Results have been saved into log.txt")

#==================Results check==========================#

results_check = input ("Do you want to check the results y/n: ")

if results_check.lower() == 'y':
    print("=" * 50)
    print("Checking results . . .")
    print("=" * 50)
    os.system("python ../script/check.py")
else:
    print("The End")