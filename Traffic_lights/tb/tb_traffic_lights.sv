//~ `New testbench
`timescale  1ns / 1ns

module tb_traffic_lights;

// traffic_lights Parameters
parameter PERIOD  = 10;


// traffic_lights Inputs
 logic clk                            = 0 ;
 logic rst_n                          = 0 ;

// traffic_lights Outputs
 logic red                            ;
 logic yellow                         ;
 logic green                          ;


initial
begin
    forever #(PERIOD/2)  clk=~clk;
end

initial
begin
    rst_n  =  1;
end

traffic_lights  u_traffic_lights (
    .clk               ( clk      ),
    .rst_n             ( rst_n    ),

    .red               ( red      ),
    .yellow            ( yellow   ),
    .green             ( green    )
);



endmodule