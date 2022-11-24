---
crate: embedded_components
layout: gnatdoc
gnatdoc: {
name: "STMPE1600",
qualified_name: "STMPE1600",
signature: "stmpe1600",
enclosing: "",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                    Copyright (C) 2017-2018, AdaCore                      --\n                                                                          --\n  Redistribution and use in source and binary forms, with or without      --\n  modification, are permitted provided that the following conditions are  --\n  met:                                                                    --\n     1. Redistributions of source code must retain the above copyright    --\n        notice, this list of conditions and the following disclaimer.     --\n     2. Redistributions in binary form must reproduce the above copyright --\n        notice, this list of conditions and the following disclaimer in   --\n        the documentation and/or other materials provided with the        --\n        distribution.                                                     --\n     3. Neither the name of the copyright holder nor the names of its     --\n        contributors may be used to endorse or promote products derived   --\n        from this software without specific prior written permission.     --\n                                                                          --\n   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS    --\n   \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT      --\n   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR  --\n   A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT   --\n   HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, --\n   SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT       --\n   LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,  --\n   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY  --\n   THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT    --\n   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE  --\n   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.   --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "STMPE1600_Expander",
       qualified_name: "STMPE1600.STMPE1600_Expander",
       signature: "stmpe1600.stmpe1600_expander",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type STMPE1600_Expander (Port : not null HAL.I2C.Any_I2C_Port;\n                         Addr : HAL.I2C.I2C_Address) is limited private;",
       }   ,
       {
       name: "STMPE1600_Pin_Direction",
       qualified_name: "STMPE1600.STMPE1600_Pin_Direction",
       signature: "stmpe1600.stmpe1600_pin_direction",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type STMPE1600_Pin_Direction is (Input, Output) with Size => 1;",
       }   ,
       {
       name: "STMPE1600_Pin_Number",
       qualified_name: "STMPE1600.STMPE1600_Pin_Number",
       signature: "stmpe1600.stmpe1600_pin_number",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type STMPE1600_Pin_Number is range 0 .. 15;",
       }   ,
       {
       name: "STMPE1600_Pin_Polarity",
       qualified_name: "STMPE1600.STMPE1600_Pin_Polarity",
       signature: "stmpe1600.stmpe1600_pin_polarity",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type STMPE1600_Pin_Polarity is (Low, High) with Size => 1;",
       }   ,
   ]
,array_types:    [
       {
       name: "STMPE1600_Pins",
       qualified_name: "STMPE1600.STMPE1600_Pins",
       signature: "stmpe1600.stmpe1600_pins",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type STMPE1600_Pins is array (STMPE1600_Pin_Number) of Boolean\n  with Pack, Size => 16;",
       }   ,
       {
       name: "STMPE1600_Pins_Direction",
       qualified_name: "STMPE1600.STMPE1600_Pins_Direction",
       signature: "stmpe1600.stmpe1600_pins_direction",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type STMPE1600_Pins_Direction is\n  array (STMPE1600_Pin_Number) of STMPE1600_Pin_Direction\n  with Pack, Size => 16;",
       }   ,
   ]
,access_types:    [
       {
       name: "Any_STMPE1600_Expander",
       qualified_name: "STMPE1600.Any_STMPE1600_Expander",
       signature: "stmpe1600.any_stmpe1600_expander",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Any_STMPE1600_Expander is access all STMPE1600_Expander;",
       }   ,
   ]
,}
---
