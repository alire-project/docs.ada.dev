---
crate: hal
layout: gnatdoc
gnatdoc: {
name: "HAL.GPIO",
qualified_name: "HAL.GPIO",
signature: "hal.gpio",
enclosing: "hal",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                     Copyright (C) 2015-2018, AdaCore                     --\n                                                                          --\n  Redistribution and use in source and binary forms, with or without      --\n  modification, are permitted provided that the following conditions are  --\n  met:                                                                    --\n     1. Redistributions of source code must retain the above copyright    --\n        notice, this list of conditions and the following disclaimer.     --\n     2. Redistributions in binary form must reproduce the above copyright --\n        notice, this list of conditions and the following disclaimer in   --\n        the documentation and/or other materials provided with the        --\n        distribution.                                                     --\n     3. Neither the name of the copyright holder nor the names of its     --\n        contributors may be used to endorse or promote products derived   --\n        from this software without specific prior written permission.     --\n                                                                          --\n   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS    --\n   \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT      --\n   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR  --\n   A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT   --\n   HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, --\n   SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT       --\n   LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,  --\n   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY  --\n   THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT    --\n   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE  --\n   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.   --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Capability",
       qualified_name: "HAL.GPIO.Capability",
       signature: "hal.gpio.capability",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum Unknown_Mode\n  Mode\n@enum Input\n  Mode\n@enum Output\n  Mode\n@enum Floating\n@enum Pull_Up\n@enum Pull_Down\n  Resistor",
       documentation_snippet: "type Capability is (Unknown_Mode, Input, Output,\n                    Floating, Pull_Up, Pull_Down);",
       }   ,
   ]
,interface_types:    [
       {
       name: "GPIO_Point",
       qualified_name: "HAL.GPIO.GPIO_Point",
       signature: "hal.gpio.gpio_point",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type GPIO_Point is limited interface;",
       }   ,
   ]
,access_types:    [
       {
       name: "Any_GPIO_Point",
       qualified_name: "HAL.GPIO.Any_GPIO_Point",
       signature: "hal.gpio.any_gpio_point",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Any_GPIO_Point is access all GPIO_Point'Class;",
       }   ,
   ]
,subtypes:    [
       {
       name: "GPIO_Config_Mode",
       qualified_name: "HAL.GPIO.GPIO_Config_Mode",
       signature: "hal.gpio.gpio_config_mode",
       enclosing: "",
       is_private: false,
       documentation: "Modes a GPIO point can be configured in",
       documentation_snippet: "subtype GPIO_Config_Mode is GPIO_Mode range Input .. Output;",
       }   ,
       {
       name: "GPIO_Mode",
       qualified_name: "HAL.GPIO.GPIO_Mode",
       signature: "hal.gpio.gpio_mode",
       enclosing: "",
       is_private: false,
       documentation: "Possible modes for a GPIO point. Unknown_Mode means that the point\nis configured in a mode that is not described in this interface. For\ninstance alternate function mode on an STM32 micro-controller.",
       documentation_snippet: "subtype GPIO_Mode is Capability range Unknown_Mode .. Output;",
       }   ,
       {
       name: "GPIO_Pull_Resistor",
       qualified_name: "HAL.GPIO.GPIO_Pull_Resistor",
       signature: "hal.gpio.gpio_pull_resistor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype GPIO_Pull_Resistor is Capability range Floating .. Pull_Down;",
       }   ,
   ]
,}
---
