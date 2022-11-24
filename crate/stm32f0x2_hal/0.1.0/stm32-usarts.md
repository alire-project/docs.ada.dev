---
crate: stm32f0x2_hal
layout: gnatdoc
gnatdoc: {
name: "STM32.USARTs",
qualified_name: "STM32.USARTs",
signature: "stm32.usarts",
enclosing: "stm32",
is_private: false,
documentation: "Copyright 2022 (C) Marc PoulhiÃ¨s\nThis file has been adapted for the STM32F0 (ARM Cortex M4)\nBeware that most of this has been reused from Ada Drivers Library\n(https://github.com/AdaCore/Ada_Drivers_Library) and has been\ntested (as of this writing) in only one very restricted scenario.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Flow_Control",
       qualified_name: "STM32.USARTs.Flow_Control",
       signature: "stm32.usarts.flow_control",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Flow_Control is\n  (No_Flow_Control, RTS_Flow_Control, CTS_Flow_Control,\n   RTS_CTS_Flow_Control);",
       }   ,
       {
       name: "Internal_USART",
       qualified_name: "STM32.USARTs.Internal_USART",
       signature: "stm32.usarts.internal_usart",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Internal_USART is limited private;",
       }   ,
       {
       name: "Oversampling_Modes",
       qualified_name: "STM32.USARTs.Oversampling_Modes",
       signature: "stm32.usarts.oversampling_modes",
       enclosing: "",
       is_private: false,
       documentation: "oversampling by 16 is the default\n\n@enum Oversampling_By_8\n@enum Oversampling_By_16",
       documentation_snippet: "type Oversampling_Modes is (Oversampling_By_8, Oversampling_By_16);",
       }   ,
       {
       name: "Parities",
       qualified_name: "STM32.USARTs.Parities",
       signature: "stm32.usarts.parities",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Parities is (No_Parity, Even_Parity, Odd_Parity);",
       }   ,
       {
       name: "Stop_Bits",
       qualified_name: "STM32.USARTs.Stop_Bits",
       signature: "stm32.usarts.stop_bits",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Stop_Bits is (Stopbits_1, Stopbits_2) with\n   Size => 2;",
       }   ,
       {
       name: "UART_Modes",
       qualified_name: "STM32.USARTs.UART_Modes",
       signature: "stm32.usarts.uart_modes",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type UART_Modes is (Rx_Mode, Tx_Mode, Tx_Rx_Mode);",
       }   ,
       {
       name: "USART_Interrupt",
       qualified_name: "STM32.USARTs.USART_Interrupt",
       signature: "stm32.usarts.usart_interrupt",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type USART_Interrupt is\n  (Parity_Error, Transmit_Data_Register_Empty, Transmission_Complete,\n   Received_Data_Not_Empty, Idle_Line_Detection, Line_Break_Detection,\n   Clear_To_Send, Error);",
       }   ,
       {
       name: "USART_Status_Flag",
       qualified_name: "STM32.USARTs.USART_Status_Flag",
       signature: "stm32.usarts.usart_status_flag",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type USART_Status_Flag is\n  (Parity_Error_Indicated, Framing_Error_Indicated,\n   USART_Noise_Error_Indicated, Overrun_Error_Indicated,\n   Idle_Line_Detection_Indicated, Read_Data_Register_Not_Empty,\n   Transmission_Complete_Indicated, Transmit_Data_Register_Empty,\n   Line_Break_Detection_Indicated, Clear_To_Send_Indicated);",
       }   ,
       {
       name: "Word_Lengths",
       qualified_name: "STM32.USARTs.Word_Lengths",
       signature: "stm32.usarts.word_lengths",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Word_Lengths is (Word_Length_8, Word_Length_9);",
       }   ,
   ]
,tagged_types:    [
       {
       name: "USART",
       qualified_name: "STM32.USARTs.USART",
       signature: "stm32.usarts.usart",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type USART (Periph : not null access Internal_USART) is\n  limited new HAL.UART.UART_Port with private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Baud_Rates",
       qualified_name: "STM32.USARTs.Baud_Rates",
       signature: "stm32.usarts.baud_rates",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Baud_Rates is UInt32;",
       }   ,
   ]
,}
---
