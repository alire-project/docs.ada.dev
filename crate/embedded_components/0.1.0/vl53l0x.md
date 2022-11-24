---
crate: embedded_components
layout: gnatdoc
gnatdoc: {
name: "VL53L0X",
qualified_name: "VL53L0X",
signature: "vl53l0x",
enclosing: "",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                 Copyright (C) 2017, 2020, AdaCore                        --\n                                                                          --\n  Redistribution and use in source and binary forms, with or without      --\n  modification, are permitted provided that the following conditions are  --\n  met:                                                                    --\n     1. Redistributions of source code must retain the above copyright    --\n        notice, this list of conditions and the following disclaimer.     --\n     2. Redistributions in binary form must reproduce the above copyright --\n        notice, this list of conditions and the following disclaimer in   --\n        the documentation and/or other materials provided with the        --\n        distribution.                                                     --\n     3. Neither the name of STMicroelectronics nor the names of its       --\n        contributors may be used to endorse or promote products derived   --\n        from this software without specific prior written permission.     --\n                                                                          --\n   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS    --\n   \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT      --\n   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR  --\n   A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT   --\n   HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, --\n   SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT       --\n   LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,  --\n   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY  --\n   THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT    --\n   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE  --\n   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.   --\n                                                                          --\n                                                                          --\n  This file is based on X-CUBE-53L0A1 STM32Cube expansion                 --\n                                                                          --\n   COPYRIGHT(c) 2016 STMicroelectronics                                   --\n----------------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "VL53L0X_GPIO_Functionality",
       qualified_name: "VL53L0X.VL53L0X_GPIO_Functionality",
       signature: "vl53l0x.vl53l0x_gpio_functionality",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type VL53L0X_GPIO_Functionality is\n  (No_Interrupt,\n   Level_Low,\n   Level_High,\n   Out_Of_Window,\n   New_Sample_Ready);",
       }   ,
       {
       name: "VL53L0X_Interrupt_Polarity",
       qualified_name: "VL53L0X.VL53L0X_Interrupt_Polarity",
       signature: "vl53l0x.vl53l0x_interrupt_polarity",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type VL53L0X_Interrupt_Polarity is\n  (Polarity_Low,\n   Polarity_High);",
       }   ,
       {
       name: "VL53L0X_Ranging_Sensor",
       qualified_name: "VL53L0X.VL53L0X_Ranging_Sensor",
       signature: "vl53l0x.vl53l0x_ranging_sensor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type VL53L0X_Ranging_Sensor\n  (Port   : not null HAL.I2C.Any_I2C_Port;\n   Timing : not null HAL.Time.Any_Delays) is limited private;",
       }   ,
   ]
,constants:    [
       {
       name: "Fix_Point_16_16_Delta",
       qualified_name: "VL53L0X.Fix_Point_16_16_Delta",
       signature: "vl53l0x.fix_point_16_16_delta",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Fix_Point_16_16_Delta : constant := 1.0 / (2.0 ** 16);",
       }   ,
   ]
,}
---
