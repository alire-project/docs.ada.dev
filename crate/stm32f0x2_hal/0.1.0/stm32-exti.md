---
crate: stm32f0x2_hal
layout: gnatdoc
gnatdoc: {
name: "STM32.EXTI",
qualified_name: "STM32.EXTI",
signature: "stm32.exti",
enclosing: "stm32",
is_private: false,
documentation: "Copyright 2022 (C) Marc PoulhiÃ¨s\nThis file has been adapted for the STM32F0 (ARM Cortex M4)\nBeware that most of this has been reused from Ada Drivers Library\n(https://github.com/AdaCore/Ada_Drivers_Library) and has been\ntested (as of this writing) in only one very restricted scenario.",
documentation_snippet: "",
simple_types:    [
       {
       name: "External_Line_Number",
       qualified_name: "STM32.EXTI.External_Line_Number",
       signature: "stm32.exti.external_line_number",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type External_Line_Number is\n  (EXTI_Line_0,\n   EXTI_Line_1,\n   EXTI_Line_2,\n   EXTI_Line_3,\n   EXTI_Line_4,\n   EXTI_Line_5,\n   EXTI_Line_6,\n   EXTI_Line_7,\n   EXTI_Line_8,\n   EXTI_Line_9,\n   EXTI_Line_10,\n   EXTI_Line_11,\n   EXTI_Line_12,\n   EXTI_Line_13,\n   EXTI_Line_14,\n   EXTI_Line_15,\n   EXTI_Line_16,\n   EXTI_Line_17,\n   EXTI_Line_18,\n   EXTI_Line_19,\n   EXTI_Line_20,\n   EXTI_Line_21,\n   EXTI_Line_22);",
       }   ,
       {
       name: "External_Triggers",
       qualified_name: "STM32.EXTI.External_Triggers",
       signature: "stm32.exti.external_triggers",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type External_Triggers is\n  (Interrupt_Rising_Edge, Interrupt_Falling_Edge,\n   Interrupt_Rising_Falling_Edge, Event_Rising_Edge, Event_Falling_Edge,\n   Event_Rising_Falling_Edge);",
       }   ,
   ]
,subtypes:    [
       {
       name: "Event_Triggers",
       qualified_name: "STM32.EXTI.Event_Triggers",
       signature: "stm32.exti.event_triggers",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Event_Triggers is\n  External_Triggers range Event_Rising_Edge .. Event_Rising_Falling_Edge;",
       }   ,
       {
       name: "Interrupt_Triggers",
       qualified_name: "STM32.EXTI.Interrupt_Triggers",
       signature: "stm32.exti.interrupt_triggers",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Interrupt_Triggers is\n  External_Triggers range Interrupt_Rising_Edge ..\n      Interrupt_Rising_Falling_Edge;",
       }   ,
   ]
,}
---
