`timescale 1ns/1ps

module multiplier_tb;

parameter WIDTH = 8;

logic [WIDTH-1:0] a;
logic [WIDTH-1:0] b;
logic [(2*WIDTH)-1:0] product;

// Khai báo DUT
multiplier #(
    .WIDTH(WIDTH)
) dut (
    .a(a),
    .b(b),
    .product(product)
);

initial begin
    // Khai báo biến xử lý file
    int file_in, file_out;
    int status;
    
    // Cấu hình lưu file sóng vào thư mục sim/
    $dumpfile("sim/waveform.vcd");
    $dumpvars(0, multiplier_tb);

    // Mở file input (để đọc) và file output (để ghi)
    file_in = $fopen("sim/input.txt", "r");
    file_out = $fopen("sim/output_sv.txt", "w");

    if (file_in == 0 || file_out == 0) begin
        $display("[!] LOI: Khong the mo file du lieu."); // Đã bỏ dấu
        $finish;
    end

    $display("-----------------------------------");
    $display("     MO PHONG VOI FILE DU LIEU"); // Đã bỏ dấu
    $display("-----------------------------------");

    // Đọc từng dòng cho đến khi hết file input.txt
    while (!$feof(file_in)) begin
        // Quét lấy 2 giá trị a và b từ mỗi dòng
        status = $fscanf(file_in, "%d %d\n", a, b);
        
        #1; // Đợi mạch tổ hợp (multiplier) tính toán

        // Ghi kết quả product vừa tính được ra file output_sv.txt
        $fdisplay(file_out, "%d", product);
    end

    // Đóng file để giải phóng bộ nhớ
    $fclose(file_in);
    $fclose(file_out);

    $display("     MO PHONG HOAN TAT"); // Đã bỏ dấu
    $display("-----------------------------------");
    $finish;
end

endmodule