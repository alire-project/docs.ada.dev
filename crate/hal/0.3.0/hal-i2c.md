---
crate: hal
layout: gnatdoc
gnatdoc: {
name: "HAL.I2C",
qualified_name: "HAL.I2C",
signature: "hal.i2c",
enclosing: "hal",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                     Copyright (C) 2015-2016, AdaCore                     --\n                                                                          --\n  Redistribution and use in source and binary forms, with or without      --\n  modification, are permitted provided that the following conditions are  --\n  met:                                                                    --\n     1. Redistributions of source code must retain the above copyright    --\n        notice, this list of conditions and the following disclaimer.     --\n     2. Redistributions in binary form must reproduce the above copyright --\n        notice, this list of conditions and the following disclaimer in   --\n        the documentation and/or other materials provided with the        --\n        distribution.                                                     --\n     3. Neither the name of the copyright holder nor the names of its     --\n        contributors may be used to endorse or promote products derived   --\n        from this software without specific prior written permission.     --\n                                                                          --\n   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS    --\n   \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT      --\n   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR  --\n   A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT   --\n   HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, --\n   SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT       --\n   LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,  --\n   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY  --\n   THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT    --\n   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE  --\n   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.   --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "I2C_Memory_Address_Size",
       qualified_name: "HAL.I2C.I2C_Memory_Address_Size",
       signature: "hal.i2c.i2c_memory_address_size",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type I2C_Memory_Address_Size is\n  (Memory_Size_8b,\n   Memory_Size_16b);",
       }   ,
       {
       name: "I2C_Status",
       qualified_name: "HAL.I2C.I2C_Status",
       signature: "hal.i2c.i2c_status",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type I2C_Status is\n  (Ok,\n   Err_Error,\n   Err_Timeout,\n   Busy);",
       }   ,
   ]
,interface_types:    [
       {
       name: "I2C_Port",
       qualified_name: "HAL.I2C.I2C_Port",
       signature: "hal.i2c.i2c_port",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type I2C_Port is limited interface;",
       }   ,
   ]
,access_types:    [
       {
       name: "Any_I2C_Port",
       qualified_name: "HAL.I2C.Any_I2C_Port",
       signature: "hal.i2c.any_i2c_port",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Any_I2C_Port is access all I2C_Port'Class;",
       }   ,
   ]
,subtypes:    [
       {
       name: "I2C_Address",
       qualified_name: "HAL.I2C.I2C_Address",
       signature: "hal.i2c.i2c_address",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype I2C_Address is UInt10;",
       }   ,
       {
       name: "I2C_Data",
       qualified_name: "HAL.I2C.I2C_Data",
       signature: "hal.i2c.i2c_data",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype I2C_Data is UInt8_Array;",
       }   ,
   ]
,}
---
