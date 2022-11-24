---
crate: hal
layout: gnatdoc
gnatdoc: {
name: "HAL.SPI",
qualified_name: "HAL.SPI",
signature: "hal.spi",
enclosing: "hal",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                     Copyright (C) 2015-2016, AdaCore                     --\n                                                                          --\n  Redistribution and use in source and binary forms, with or without      --\n  modification, are permitted provided that the following conditions are  --\n  met:                                                                    --\n     1. Redistributions of source code must retain the above copyright    --\n        notice, this list of conditions and the following disclaimer.     --\n     2. Redistributions in binary form must reproduce the above copyright --\n        notice, this list of conditions and the following disclaimer in   --\n        the documentation and/or other materials provided with the        --\n        distribution.                                                     --\n     3. Neither the name of the copyright holder nor the names of its     --\n        contributors may be used to endorse or promote products derived   --\n        from this software without specific prior written permission.     --\n                                                                          --\n   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS    --\n   \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT      --\n   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR  --\n   A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT   --\n   HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, --\n   SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT       --\n   LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,  --\n   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY  --\n   THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT    --\n   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE  --\n   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.   --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "SPI_Data_Size",
       qualified_name: "HAL.SPI.SPI_Data_Size",
       signature: "hal.spi.spi_data_size",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SPI_Data_Size is\n  (Data_Size_8b,\n   Data_Size_16b);",
       }   ,
       {
       name: "SPI_Status",
       qualified_name: "HAL.SPI.SPI_Status",
       signature: "hal.spi.spi_status",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SPI_Status is\n  (Ok,\n   Err_Error,\n   Err_Timeout,\n   Busy);",
       }   ,
   ]
,array_types:    [
       {
       name: "SPI_Data_16b",
       qualified_name: "HAL.SPI.SPI_Data_16b",
       signature: "hal.spi.spi_data_16b",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SPI_Data_16b is array (Natural range <>) of UInt16;",
       }   ,
       {
       name: "SPI_Data_8b",
       qualified_name: "HAL.SPI.SPI_Data_8b",
       signature: "hal.spi.spi_data_8b",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SPI_Data_8b is array (Natural range <>) of UInt8;",
       }   ,
   ]
,interface_types:    [
       {
       name: "SPI_Port",
       qualified_name: "HAL.SPI.SPI_Port",
       signature: "hal.spi.spi_port",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SPI_Port is limited interface;",
       }   ,
   ]
,access_types:    [
       {
       name: "Any_SPI_Port",
       qualified_name: "HAL.SPI.Any_SPI_Port",
       signature: "hal.spi.any_spi_port",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Any_SPI_Port is access all SPI_Port'Class;",
       }   ,
   ]
,}
---
