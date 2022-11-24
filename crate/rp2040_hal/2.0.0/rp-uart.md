---
crate: rp2040_hal
layout: gnatdoc
gnatdoc: {
name: "RP.UART",
qualified_name: "RP.UART",
signature: "rp.uart",
enclosing: "rp",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "FIFO_IRQ_Level",
       qualified_name: "RP.UART.FIFO_IRQ_Level",
       signature: "rp.uart.fifo_irq_level",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type FIFO_IRQ_Level is (Lvl_Eighth,\n                        Lvl_Quarter,\n                        Lvl_Half,\n                        Lvl_Three_Quarter,\n                        Lvl_Seven_Eighth);",
       }   ,
       {
       name: "UART_FIFO_Status",
       qualified_name: "RP.UART.UART_FIFO_Status",
       signature: "rp.uart.uart_fifo_status",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type UART_FIFO_Status is (Empty, Not_Full, Full, Busy, Invalid);",
       }   ,
       {
       name: "UART_IRQ_Flag",
       qualified_name: "RP.UART.UART_IRQ_Flag",
       signature: "rp.uart.uart_irq_flag",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type UART_IRQ_Flag is\n  (Modem_RI, Modem_CTS, Modem_DCD, Modem_DSR,\n   Receive,\n   Transmit,\n   Receive_Timeout,\n   Framing_Error,\n   Parity_Error,\n   Break_Error,\n   Overrun_Error);",
       }   ,
       {
       name: "UART_Parity_Type",
       qualified_name: "RP.UART.UART_Parity_Type",
       signature: "rp.uart.uart_parity_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type UART_Parity_Type is (Even, Odd);",
       }   ,
   ]
,record_types:    [
       {
       name: "UART_Configuration",
       qualified_name: "RP.UART.UART_Configuration",
       signature: "rp.uart.uart_configuration",
       enclosing: "",
       is_private: false,
       documentation: "\n@field Baud\n@field Word_Size\n@field Parity\n@field Stop_Bits\n@field Parity_Type\n  has no effect when Parity = False\n@field Frame_Length\n  Words per frame. Used to calculate break timing.\n@field Loopback\n@field Enable_FIFOs\n  Enable TX and RX FIFOs",
       documentation_snippet: "type UART_Configuration is record\n   Baud         : Hertz := 115_200;\n   Word_Size    : UART_Word_Size := 8;\n   Parity       : Boolean := False;\n   Stop_Bits    : UART_Stop_Bits := 1;\n   Parity_Type  : UART_Parity_Type := Even;\n   Frame_Length : Positive := 1;\n   Loopback     : Boolean := False;\n   Enable_FIFOs : Boolean := True;\nend record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "UART_Port",
       qualified_name: "RP.UART.UART_Port",
       signature: "rp.uart.uart_port",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type UART_Port\n   (Num    : UART_Number;\n    Periph : not null access RP2040_SVD.UART.UART_Peripheral)\nis new HAL.UART.UART_Port with record\n   Config : UART_Configuration;\nend record;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Microseconds",
       qualified_name: "RP.UART.Microseconds",
       signature: "rp.uart.microseconds",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Microseconds is Integer;",
       }   ,
       {
       name: "UART_Number",
       qualified_name: "RP.UART.UART_Number",
       signature: "rp.uart.uart_number",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype UART_Number is Natural range 0 .. 1;",
       }   ,
       {
       name: "UART_Stop_Bits",
       qualified_name: "RP.UART.UART_Stop_Bits",
       signature: "rp.uart.uart_stop_bits",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype UART_Stop_Bits is Integer range 1 .. 2;",
       }   ,
       {
       name: "UART_Word_Size",
       qualified_name: "RP.UART.UART_Word_Size",
       signature: "rp.uart.uart_word_size",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype UART_Word_Size is Integer range 5 .. 8;",
       }   ,
   ]
,constants:    [
       {
       name: "Default_UART_Configuration",
       qualified_name: "RP.UART.Default_UART_Configuration",
       signature: "rp.uart.default_uart_configuration",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Default_UART_Configuration : constant UART_Configuration := (others => <>);",
       }   ,
   ]
,}
---
