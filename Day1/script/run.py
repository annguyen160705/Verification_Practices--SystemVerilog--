import os


if not os.path.exists("sim"):
    os.mkdir("sim")
    print("New sim folder has been created")

# DỊCH CHUYỂN VÀO THƯ MỤC SIM
# Kể từ dòng này trở đi, mọi hành động lưu/đọc file đều diễn ra bên trong thư mục 'sim'
os.chdir("sim")


print ("1. Generating input ")
os.system("python ../script/gen_input.py")



print("2. Starting simulation ... ")

if not os.path.exists("work"):
    os.system("vlib work")
    print("New work.lib has been created")
else:
    print("work.lib was created, skip")

os.system("vlog ../tb/logic_test.sv")

#   -c                   : Chạy trên giao diện dòng lệnh (Command Line), không mở GUI.
#   -do "run -all; quit" : Tự động chạy toàn bộ thời gian mô phỏng, xong thì thoát.
#   -l log.txt           : Lưu toàn bộ nội dung in ra màn hình vào thẳng file log.txt.
#   logic_test              : Tên module bên trong file SystemVerilog của bạn.
os.system('vsim -c -do "run -all; quit" -l log.txt logic_test')

print("Simulation completed. Results have been saved into log.txt")

print ("3. Checking results")
os.system("python ../script/check.py")

print("The End")