---
crate: rp2040_hal
layout: gnatdoc
gnatdoc: {
name: "RP.SPI",
qualified_name: "RP.SPI",
signature: "rp.spi",
enclosing: "rp",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "SPI_FIFO_Status",
       qualified_name: "RP.SPI.SPI_FIFO_Status",
       signature: "rp.spi.spi_fifo_status",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SPI_FIFO_Status is (Empty, Not_Full, Busy, Full, Invalid);",
       }   ,
       {
       name: "SPI_IRQ_Flag",
       qualified_name: "RP.SPI.SPI_IRQ_Flag",
       signature: "rp.spi.spi_irq_flag",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SPI_IRQ_Flag is\n  (Receive_Overrun,\n   Receive_FIFO_Not_Empty,\n   Receive_FIFO_Half_Full,\n   Transmit_FIFO_Half_Empty);",
       }   ,
       {
       name: "SPI_Phase",
       qualified_name: "RP.SPI.SPI_Phase",
       signature: "rp.spi.spi_phase",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SPI_Phase is (Rising_Edge, Falling_Edge);",
       }   ,
       {
       name: "SPI_Polarity",
       qualified_name: "RP.SPI.SPI_Polarity",
       signature: "rp.spi.spi_polarity",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SPI_Polarity is (Active_Low, Active_High);",
       }   ,
       {
       name: "SPI_Role",
       qualified_name: "RP.SPI.SPI_Role",
       signature: "rp.spi.spi_role",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SPI_Role is (Master, Slave);",
       }   ,
   ]
,record_types:    [
       {
       name: "SPI_Configuration",
       qualified_name: "RP.SPI.SPI_Configuration",
       signature: "rp.spi.spi_configuration",
       enclosing: "",
       is_private: false,
       documentation: "\n@field Role\n@field Baud\n@field Data_Size\n@field Polarity\n@field Phase\n@field Blocking\n  Wait for Transmit FIFO to be empty before returning\n@field Loopback",
       documentation_snippet: "type SPI_Configuration is record\n   Role      : SPI_Role := Master;\n   Baud      : Hertz := 1_000_000;\n   Data_Size : SPI_Data_Size := Data_Size_8b;\n   Polarity  : SPI_Polarity := Active_Low;\n   Phase     : SPI_Phase := Rising_Edge;\n   Blocking  : Boolean := True;\n   Loopback  : Boolean := False;\nend record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "SPI_Port",
       qualified_name: "RP.SPI.SPI_Port",
       signature: "rp.spi.spi_port",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SPI_Port\n   (Num    : SPI_Number;\n    Periph : not null access RP2040_SVD.SPI.SPI_Peripheral)\nis new HAL.SPI.SPI_Port with record\n   Blocking : Boolean := True;\nend record;",
       }   ,
   ]
,subtypes:    [
       {
       name: "SPI_Number",
       qualified_name: "RP.SPI.SPI_Number",
       signature: "rp.spi.spi_number",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype SPI_Number is Natural range 0 .. 1;",
       }   ,
   ]
,constants:    [
       {
       name: "Default_SPI_Configuration",
       qualified_name: "RP.SPI.Default_SPI_Configuration",
       signature: "rp.spi.default_spi_configuration",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Default_SPI_Configuration : constant SPI_Configuration := (others => <>);",
       }   ,
   ]
,}
---
