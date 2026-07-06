module logic_test;

    logic [3:0] my_data;
    logic en;

    initial begin
        $display ("my_data = 0x%0h en=%0b", my_data, en);
        my_data = 4'hB;
        $display ("my_data = 0x%0h en=%0b", my_data, en);
        #1;
        $display ("my_data = 0x%0h en=%0b", my_data, en);
    end


endmodule