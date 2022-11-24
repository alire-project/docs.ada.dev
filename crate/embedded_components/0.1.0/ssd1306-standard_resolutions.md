---
crate: embedded_components
layout: gnatdoc
gnatdoc: {
name: "SSD1306.Standard_Resolutions",
qualified_name: "SSD1306.Standard_Resolutions",
signature: "ssd1306.standard_resolutions",
enclosing: "ssd1306",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                        Copyright (C) 2017, AdaCore                       --\n                                                                          --\n  Redistribution and use in source and binary forms, with or without      --\n  modification, are permitted provided that the following conditions are  --\n  met:                                                                    --\n     1. Redistributions of source code must retain the above copyright    --\n        notice, this list of conditions and the following disclaimer.     --\n     2. Redistributions in binary form must reproduce the above copyright --\n        notice, this list of conditions and the following disclaimer in   --\n        the documentation and/or other materials provided with the        --\n        distribution.                                                     --\n     3. Neither the name of the copyright holder nor the names of its     --\n        contributors may be used to endorse or promote products derived   --\n        from this software without specific prior written permission.     --\n                                                                          --\n   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS    --\n   \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT      --\n   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR  --\n   A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT   --\n   HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, --\n   SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT       --\n   LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,  --\n   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY  --\n   THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT    --\n   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE  --\n   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.   --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
tagged_types:    [
       {
       name: "SSD1306_128x32_Screen",
       qualified_name: "SSD1306.Standard_Resolutions.SSD1306_128x32_Screen",
       signature: "ssd1306.standard_resolutions.ssd1306_128x32_screen",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SSD1306_128x32_Screen\n  (Port             : not null Any_I2C_Port;\n   RST              : not null Any_GPIO_Point;\n   Time             : not null HAL.Time.Any_Delays)\nis new SSD1306_Screen ((128 * 32) / 8, 128, 32, Port, RST, Time) with null record;",
       }   ,
       {
       name: "SSD1306_128x64_Screen",
       qualified_name: "SSD1306.Standard_Resolutions.SSD1306_128x64_Screen",
       signature: "ssd1306.standard_resolutions.ssd1306_128x64_screen",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SSD1306_128x64_Screen\n  (Port             : not null Any_I2C_Port;\n   RST              : not null Any_GPIO_Point;\n   Time             : not null HAL.Time.Any_Delays)\nis new SSD1306_Screen ((128 * 64) / 8, 128, 64, Port, RST, Time) with null record;",
       }   ,
       {
       name: "SSD1306_96x16_Screen",
       qualified_name: "SSD1306.Standard_Resolutions.SSD1306_96x16_Screen",
       signature: "ssd1306.standard_resolutions.ssd1306_96x16_screen",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SSD1306_96x16_Screen\n  (Port             : not null Any_I2C_Port;\n   RST              : not null Any_GPIO_Point;\n   Time             : not null HAL.Time.Any_Delays)\nis new SSD1306_Screen ((96 * 16) / 8, 96, 16, Port, RST, Time) with null record;",
       }   ,
   ]
,}
---
