---
crate: stm32f0x2_hal
layout: gnatdoc
gnatdoc: {
name: "STM32.RCC",
qualified_name: "STM32.RCC",
signature: "stm32.rcc",
enclosing: "stm32",
is_private: false,
documentation: "Copyright 2022 (C) Marc PoulhiÃ¨s\nThis file has been adapted for the STM32F0 (ARM Cortex M4)\nBeware that most of this has been reused from Ada Drivers Library\n(https://github.com/AdaCore/Ada_Drivers_Library) and has been\ntested (as of this writing) in only one very restricted scenario.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Sys_Clock_Source",
       qualified_name: "STM32.RCC.Sys_Clock_Source",
       signature: "stm32.rcc.sys_clock_source",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Sys_Clock_Source is (HSI, HSE, HSI48);",
       }   ,
       {
       name: "Usb_Clock_Source",
       qualified_name: "STM32.RCC.Usb_Clock_Source",
       signature: "stm32.rcc.usb_clock_source",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Usb_Clock_Source is (HSI48, PLL);",
       }   ,
   ]
,record_types:    [
       {
       name: "Rcc_Cfgr",
       qualified_name: "STM32.RCC.Rcc_Cfgr",
       signature: "stm32.rcc.rcc_cfgr",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Rcc_Cfgr is record\n   Hclk         : Natural          := 0;\n   Pclk         : Natural          := 0;\n   Sysclk       : Natural          := 0;\n   Clock_Source : Sys_Clock_Source := HSI;\n   Usb_Source   : Usb_Clock_Source := HSI48;\n   Use_Crs      : Boolean          := False;\nend record;",
       }   ,
   ]
,constants:    [
       {
       name: "HSI48_Freq",
       qualified_name: "STM32.RCC.HSI48_Freq",
       signature: "stm32.rcc.hsi48_freq",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "HSI48_Freq : constant Positive := 48_000_000;",
       }   ,
       {
       name: "HSI_Freq",
       qualified_name: "STM32.RCC.HSI_Freq",
       signature: "stm32.rcc.hsi_freq",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "HSI_Freq   : constant Positive := 8_000_000;",
       }   ,
   ]
,variables:    [
       {
       name: "HSE_Freq",
       qualified_name: "STM32.RCC.HSE_Freq",
       signature: "stm32.rcc.hse_freq",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "HSE_Freq   : Positive          := Positive'Last;",
       }   ,
   ]
,}
---
