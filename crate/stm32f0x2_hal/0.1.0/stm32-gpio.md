---
crate: stm32f0x2_hal
layout: gnatdoc
gnatdoc: {
name: "STM32.GPIO",
qualified_name: "STM32.GPIO",
signature: "stm32.gpio",
enclosing: "stm32",
is_private: false,
documentation: "type GPIO_Alternate_Function is private;",
documentation_snippet: "",
simple_types:    [
       {
       name: "GPIO_Pin",
       qualified_name: "STM32.GPIO.GPIO_Pin",
       signature: "stm32.gpio.gpio_pin",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type GPIO_Pin is\n  (Pin_0, Pin_1, Pin_2, Pin_3, Pin_4, Pin_5, Pin_6, Pin_7, Pin_8, Pin_9,\n   Pin_10, Pin_11, Pin_12, Pin_13, Pin_14, Pin_15);",
       }   ,
       {
       name: "GPIO_Port",
       qualified_name: "STM32.GPIO.GPIO_Port",
       signature: "stm32.gpio.gpio_port",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type GPIO_Port is limited private;",
       }   ,
       {
       name: "Internal_Pin_Resistors",
       qualified_name: "STM32.GPIO.Internal_Pin_Resistors",
       signature: "stm32.gpio.internal_pin_resistors",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Internal_Pin_Resistors is (Floating, Pull_Up, Pull_Down) with\n   Size => 2;",
       }   ,
       {
       name: "Pin_IO_Modes",
       qualified_name: "STM32.GPIO.Pin_IO_Modes",
       signature: "stm32.gpio.pin_io_modes",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Pin_IO_Modes is (Mode_In, Mode_Out, Mode_AF, Mode_Analog) with\n   Size => 2;",
       }   ,
       {
       name: "Pin_Output_Speeds",
       qualified_name: "STM32.GPIO.Pin_Output_Speeds",
       signature: "stm32.gpio.pin_output_speeds",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Pin_Output_Speeds is (Speed_2MHz, Speed_25MHz, Speed_50MHz) with\n   Size => 2;",
       }   ,
       {
       name: "Pin_Output_Types",
       qualified_name: "STM32.GPIO.Pin_Output_Types",
       signature: "stm32.gpio.pin_output_types",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Pin_Output_Types is (Push_Pull, Open_Drain) with\n   Size => 1;",
       }   ,
   ]
,array_types:    [
       {
       name: "GPIO_Pins",
       qualified_name: "STM32.GPIO.GPIO_Pins",
       signature: "stm32.gpio.gpio_pins",
       enclosing: "",
       is_private: false,
       documentation: "Note that, in addition to aggregates, the language-defined catenation\noperator \"&\" is available for types GPIO_Pin and GPIO_Pins, allowing one\nto construct GPIO_Pins values conveniently",
       documentation_snippet: "type GPIO_Pins is array (Positive range <>) of GPIO_Pin;",
       }   ,
       {
       name: "GPIO_Points",
       qualified_name: "STM32.GPIO.GPIO_Points",
       signature: "stm32.gpio.gpio_points",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type GPIO_Points is array (Positive range <>) of GPIO_Point;",
       }   ,
   ]
,record_types:    [
       {
       name: "GPIO_Port_Configuration",
       qualified_name: "STM32.GPIO.GPIO_Port_Configuration",
       signature: "stm32.gpio.gpio_port_configuration",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type GPIO_Port_Configuration (Mode : Pin_IO_Modes := Mode_In) is record\n   Resistors : Internal_Pin_Resistors;\n   case Mode is\n      when Mode_In | Mode_Analog =>\n         null;\n      when Mode_Out =>\n         Output_Type : Pin_Output_Types;\n         Speed       : Pin_Output_Speeds;\n      when Mode_AF =>\n         AF_Output_Type : Pin_Output_Types;\n         AF_Speed       : Pin_Output_Speeds;\n         AF             : GPIO_Alternate_Function;\n   end case;\nend record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "GPIO_Point",
       qualified_name: "STM32.GPIO.GPIO_Point",
       signature: "stm32.gpio.gpio_point",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type GPIO_Point is new HAL.GPIO.GPIO_Point with record\n   Periph : access GPIO_Port;\n   Pin : GPIO_Pin;\nend record;",
       }   ,
   ]
,constants:    [
       {
       name: "All_Pins",
       qualified_name: "STM32.GPIO.All_Pins",
       signature: "stm32.gpio.all_pins",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "All_Pins : constant GPIO_Pins :=\n  [Pin_0, Pin_1, Pin_2, Pin_3, Pin_4, Pin_5, Pin_6, Pin_7, Pin_8, Pin_9,\n   Pin_10, Pin_11, Pin_12, Pin_13, Pin_14, Pin_15];",
       }   ,
   ]
,variables:    [
       {
       name: "Speed_High",
       qualified_name: "STM32.GPIO.Speed_High",
       signature: "stm32.gpio.speed_high",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Speed_High   : Pin_Output_Speeds renames Speed_50MHz;",
       }   ,
       {
       name: "Speed_Low",
       qualified_name: "STM32.GPIO.Speed_Low",
       signature: "stm32.gpio.speed_low",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Speed_Low    : Pin_Output_Speeds renames Speed_2MHz;",
       }   ,
       {
       name: "Speed_Medium",
       qualified_name: "STM32.GPIO.Speed_Medium",
       signature: "stm32.gpio.speed_medium",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Speed_Medium : Pin_Output_Speeds renames Speed_25MHz;",
       }   ,
   ]
,}
---
