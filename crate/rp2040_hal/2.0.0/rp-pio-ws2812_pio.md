---
crate: rp2040_hal
layout: gnatdoc
gnatdoc: {
name: "RP.PIO.WS2812_PIO",
qualified_name: "RP.PIO.WS2812_PIO",
signature: "rp.pio.ws2812_pio",
enclosing: "rp.pio",
is_private: false,
documentation: "----------\n Ws2812 --\n----------",
documentation_snippet: "",
constants:    [
       {
       name: "T1",
       qualified_name: "RP.PIO.WS2812_PIO.T1",
       signature: "rp.pio.ws2812_pio.t1",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "T1 : constant := 2;",
       }   ,
       {
       name: "T2",
       qualified_name: "RP.PIO.WS2812_PIO.T2",
       signature: "rp.pio.ws2812_pio.t2",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "T2 : constant := 5;",
       }   ,
       {
       name: "T3",
       qualified_name: "RP.PIO.WS2812_PIO.T3",
       signature: "rp.pio.ws2812_pio.t3",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "T3 : constant := 3;",
       }   ,
       {
       name: "Ws2812_Wrap",
       qualified_name: "RP.PIO.WS2812_PIO.Ws2812_Wrap",
       signature: "rp.pio.ws2812_pio.ws2812_wrap",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Ws2812_Wrap        : constant := 3;",
       }   ,
       {
       name: "Ws2812_Wrap_Target",
       qualified_name: "RP.PIO.WS2812_PIO.Ws2812_Wrap_Target",
       signature: "rp.pio.ws2812_pio.ws2812_wrap_target",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Ws2812_Wrap_Target : constant := 0;",
       }   ,
   ]
,variables:    [
       {
       name: "Ws2812_Program_Instructions",
       qualified_name: "RP.PIO.WS2812_PIO.Ws2812_Program_Instructions",
       signature: "rp.pio.ws2812_pio.ws2812_program_instructions",
       enclosing: "",
       is_private: false,
       documentation: " 3: nop                    side 0 [4]\n.wrap",
       documentation_snippet: "Ws2812_Program_Instructions : RP.PIO.Program := (\n      16#6221#,\n      16#1123#,\n      16#1400#,\n      16#a442#);",
       }   ,
   ]
,}
---
