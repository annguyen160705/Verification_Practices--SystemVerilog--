module traffic_lights (
    input  logic clk,
    input  logic rst_n,
    output logic red,
    output logic yellow,
    output logic green
);

    // Định nghĩa các trạng thái
    typedef enum logic [1:0] {
        RED,
        GREEN,
        YELLOW
    } state_t;

    state_t state, next_state;

    // Thanh ghi trạng thái
    always_ff @(posedge clk or negedge rst_n) begin
        if (!rst_n)
            state <= RED;
        else
            state <= next_state;
    end

    // Logic chuyển trạng thái
    always_comb begin
        case (state)
            RED:    next_state = GREEN;
            GREEN:  next_state = YELLOW;
            YELLOW: next_state = RED;
            default: next_state = RED;
        endcase
    end

    // Logic điều khiển đèn
    always_comb begin
        // Tắt tất cả trước
        red    = 1'b0;
        yellow = 1'b0;
        green  = 1'b0;

        case (state)
            RED:    red    = 1'b1;
            GREEN:  green  = 1'b1;
            YELLOW: yellow = 1'b1;
        endcase
    end

endmodule