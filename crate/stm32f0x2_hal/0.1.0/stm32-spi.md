---
crate: stm32f0x2_hal
layout: gnatdoc
gnatdoc: {
name: "STM32.SPI",
qualified_name: "STM32.SPI",
signature: "stm32.spi",
enclosing: "stm32",
is_private: false,
documentation: "Copyright 2022 (C) Marc PoulhiÃ¨s\nThis file has been adapted for the STM32F0 (ARM Cortex M4)\nBeware that most of this has been reused from Ada Drivers Library\n(https://github.com/AdaCore/Ada_Drivers_Library) and has been\ntested (as of this writing) in only one very restricted scenario.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Internal_SPI_Port",
       qualified_name: "STM32.SPI.Internal_SPI_Port",
       signature: "stm32.spi.internal_spi_port",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Internal_SPI_Port is private;",
       }   ,
       {
       name: "SPI_Baud_Rate_Prescaler",
       qualified_name: "STM32.SPI.SPI_Baud_Rate_Prescaler",
       signature: "stm32.spi.spi_baud_rate_prescaler",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SPI_Baud_Rate_Prescaler is\n  (BRP_2, BRP_4, BRP_8, BRP_16, BRP_32, BRP_64, BRP_128, BRP_256);",
       }   ,
       {
       name: "SPI_Clock_Phase",
       qualified_name: "STM32.SPI.SPI_Clock_Phase",
       signature: "stm32.spi.spi_clock_phase",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SPI_Clock_Phase is (P1Edge, P2Edge);",
       }   ,
       {
       name: "SPI_Clock_Polarity",
       qualified_name: "STM32.SPI.SPI_Clock_Polarity",
       signature: "stm32.spi.spi_clock_polarity",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SPI_Clock_Polarity is (High, Low);",
       }   ,
       {
       name: "SPI_Data_Direction",
       qualified_name: "STM32.SPI.SPI_Data_Direction",
       signature: "stm32.spi.spi_data_direction",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SPI_Data_Direction is\n  (D2Lines_FullDuplex, D2Lines_RxOnly, D1Line_Rx, D1Line_Tx);",
       }   ,
       {
       name: "SPI_First_Bit",
       qualified_name: "STM32.SPI.SPI_First_Bit",
       signature: "stm32.spi.spi_first_bit",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SPI_First_Bit is (MSB, LSB);",
       }   ,
       {
       name: "SPI_Mode",
       qualified_name: "STM32.SPI.SPI_Mode",
       signature: "stm32.spi.spi_mode",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SPI_Mode is (Master, Slave);",
       }   ,
       {
       name: "SPI_Slave_Management",
       qualified_name: "STM32.SPI.SPI_Slave_Management",
       signature: "stm32.spi.spi_slave_management",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SPI_Slave_Management is (Software_Managed, Hardware_Managed);",
       }   ,
   ]
,array_types:    [
       {
       name: "UInt8_Buffer",
       qualified_name: "STM32.SPI.UInt8_Buffer",
       signature: "stm32.spi.uint8_buffer",
       enclosing: "",
       is_private: false,
       documentation: "The alignment is set to 2 because we treat component pairs as half_word\nvalues when sending/receiving in 16-bit mode.",
       documentation_snippet: "type UInt8_Buffer is array (Natural range <>) of UInt8 with\n   Alignment => 2;",
       }   ,
   ]
,record_types:    [
       {
       name: "SPI_Configuration",
       qualified_name: "STM32.SPI.SPI_Configuration",
       signature: "stm32.spi.spi_configuration",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SPI_Configuration is record\n   Direction           : SPI_Data_Direction;\n   Mode                : SPI_Mode;\n   Data_Size           : HAL.SPI.SPI_Data_Size;\n   Clock_Polarity      : SPI_Clock_Polarity;\n   Clock_Phase         : SPI_Clock_Phase;\n   Slave_Management    : SPI_Slave_Management;\n   Baud_Rate_Prescaler : SPI_Baud_Rate_Prescaler;\n   First_Bit           : SPI_First_Bit;\n   CRC_Poly            : UInt16;\nend record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "SPI_Port",
       qualified_name: "STM32.SPI.SPI_Port",
       signature: "stm32.spi.spi_port",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SPI_Port (Periph : not null access Internal_SPI_Port) is\n  limited new HAL.SPI.SPI_Port with private;",
       }   ,
   ]
,}
---
