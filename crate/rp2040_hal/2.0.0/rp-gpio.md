---
crate: rp2040_hal
layout: gnatdoc
gnatdoc: {
name: "RP.GPIO",
qualified_name: "RP.GPIO",
signature: "rp.gpio",
enclosing: "rp",
is_private: false,
documentation: "\nCopyright 2021 (C) Jeremy Grosser\n\nSPDX-License-Identifier: BSD-3-Clause",
documentation_snippet: "",
simple_types:    [
       {
       name: "GPIO_Config_Mode",
       qualified_name: "RP.GPIO.GPIO_Config_Mode",
       signature: "rp.gpio.gpio_config_mode",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type GPIO_Config_Mode is (Input, Output, Analog);",
       }   ,
       {
       name: "GPIO_Drive",
       qualified_name: "RP.GPIO.GPIO_Drive",
       signature: "rp.gpio.gpio_drive",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type GPIO_Drive is (Drive_2mA, Drive_4mA, Drive_8mA, Drive_12mA);",
       }   ,
       {
       name: "GPIO_Function",
       qualified_name: "RP.GPIO.GPIO_Function",
       signature: "rp.gpio.gpio_function",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type GPIO_Function is\n   (SPI, UART, I2C, PWM, SIO, PIO0, PIO1, CLOCK, USB, HI_Z);",
       }   ,
       {
       name: "GPIO_Pin",
       qualified_name: "RP.GPIO.GPIO_Pin",
       signature: "rp.gpio.gpio_pin",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type GPIO_Pin is range 0 .. 29;",
       }   ,
       {
       name: "GPIO_Pull_Mode",
       qualified_name: "RP.GPIO.GPIO_Pull_Mode",
       signature: "rp.gpio.gpio_pull_mode",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type GPIO_Pull_Mode is (Floating, Pull_Up, Pull_Down, Pull_Both);",
       }   ,
       {
       name: "Interrupt_Triggers",
       qualified_name: "RP.GPIO.Interrupt_Triggers",
       signature: "rp.gpio.interrupt_triggers",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Interrupt_Triggers is (Low_Level, High_Level, Falling_Edge, Rising_Edge)\n   with Size => 4;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "GPIO_Point",
       qualified_name: "RP.GPIO.GPIO_Point",
       signature: "rp.gpio.gpio_point",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type GPIO_Point is new HAL.GPIO.GPIO_Point with\n   record\n      Pin : GPIO_Pin;\n   end record;",
       }   ,
   ]
,subtypes:    [
       {
       name: "ADC_Pin",
       qualified_name: "RP.GPIO.ADC_Pin",
       signature: "rp.gpio.adc_pin",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype ADC_Pin is GPIO_Pin range 26 .. 29;",
       }   ,
   ]
,}
---
