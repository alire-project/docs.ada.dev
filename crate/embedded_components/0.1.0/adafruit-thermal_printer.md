---
crate: embedded_components
layout: gnatdoc
gnatdoc: {
name: "AdaFruit.Thermal_Printer",
qualified_name: "AdaFruit.Thermal_Printer",
signature: "adafruit.thermal_printer",
enclosing: "adafruit",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                     Copyright (C) 2015-2017, AdaCore                     --\n                                                                          --\n  Redistribution and use in source and binary forms, with or without      --\n  modification, are permitted provided that the following conditions are  --\n  met:                                                                    --\n     1. Redistributions of source code must retain the above copyright    --\n        notice, this list of conditions and the following disclaimer.     --\n     2. Redistributions in binary form must reproduce the above copyright --\n        notice, this list of conditions and the following disclaimer in   --\n        the documentation and/or other materials provided with the        --\n        distribution.                                                     --\n     3. Neither the name of the copyright holder nor the names of its     --\n        contributors may be used to endorse or promote products derived   --\n        from this software without specific prior written permission.     --\n                                                                          --\n   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS    --\n   \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT      --\n   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR  --\n   A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT   --\n   HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, --\n   SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT       --\n   LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,  --\n   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY  --\n   THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT    --\n   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE  --\n   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.   --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Character_Set",
       qualified_name: "AdaFruit.Thermal_Printer.Character_Set",
       signature: "adafruit.thermal_printer.character_set",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Character_Set is (USA, France, Germany, UK, Denmark1, Sweden, Italy,\n                       Spain1, Japan, Norway, Denmark2, Spain2,\n                       Latin_Americam, Korea);",
       }   ,
       {
       name: "Text_Align",
       qualified_name: "AdaFruit.Thermal_Printer.Text_Align",
       signature: "adafruit.thermal_printer.text_align",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Text_Align is (Right, Center, Left);",
       }   ,
   ]
,array_types:    [
       {
       name: "Thermal_Printer_Bitmap",
       qualified_name: "AdaFruit.Thermal_Printer.Thermal_Printer_Bitmap",
       signature: "adafruit.thermal_printer.thermal_printer_bitmap",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Thermal_Printer_Bitmap is array (Natural range <>,\n                                      Natural range <>) of Boolean\n  with Pack;",
       }   ,
   ]
,record_types:    [
       {
       name: "Printer_Settings",
       qualified_name: "AdaFruit.Thermal_Printer.Printer_Settings",
       signature: "adafruit.thermal_printer.printer_settings",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Printer_Settings is record\n   Max_Printing_Dots : UInt8;\n   Heating_Time      : UInt8;\n   Heating_Interval  : UInt8;\nend record;",
       }   ,
       {
       name: "Printer_Status",
       qualified_name: "AdaFruit.Thermal_Printer.Printer_Status",
       signature: "adafruit.thermal_printer.printer_status",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Printer_Status is record\n   Paper       : Boolean;\n   Voltage     : Integer;\n   Temperature : Integer;\nend record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "TP_Device",
       qualified_name: "AdaFruit.Thermal_Printer.TP_Device",
       signature: "adafruit.thermal_printer.tp_device",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type TP_Device (Port : not null HAL.UART.Any_UART_Port;\n                Time : not null HAL.Time.Any_Delays) is\n  tagged private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Underline_Height",
       qualified_name: "AdaFruit.Thermal_Printer.Underline_Height",
       signature: "adafruit.thermal_printer.underline_height",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Underline_Height is UInt8 range 0 .. 2;",
       }   ,
   ]
,}
---
