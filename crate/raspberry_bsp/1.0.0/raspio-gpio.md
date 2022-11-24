---
crate: raspberry_bsp
layout: gnatdoc
gnatdoc: {
name: "Raspio.GPIO",
qualified_name: "Raspio.GPIO",
signature: "raspio.gpio",
enclosing: "raspio",
is_private: false,
documentation: "TODO track usages of pins using controlled type, so that trying to\ncreate two overlapping pins gives a runtime error",
documentation_snippet: "",
simple_types:    [
       {
       name: "Internal_Resistor_Type",
       qualified_name: "Raspio.GPIO.Internal_Resistor_Type",
       signature: "raspio.gpio.internal_resistor_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Internal_Resistor_Type is (Off, Pull_Down, Pull_Up);",
       }   ,
       {
       name: "Mode_Type",
       qualified_name: "Raspio.GPIO.Mode_Type",
       signature: "raspio.gpio.mode_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Mode_Type is\n  (Input, Output, Alternative_5, Alternative_4, Alternative_0,\n   Alternative_1, Alternative_2, Alternative_3);",
       }   ,
       {
       name: "Pin_ID_Type",
       qualified_name: "Raspio.GPIO.Pin_ID_Type",
       signature: "raspio.gpio.pin_id_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Pin_ID_Type is\n  (GPIO_P1_03, GPIO_P1_05, GPIO_P1_07, GPIO_P1_08, GPIO_P1_10, GPIO_P1_11,\n   GPIO_P1_12, GPIO_P1_13, GPIO_P1_15, GPIO_P1_16, GPIO_P1_18, GPIO_P1_19,\n   GPIO_P1_21, GPIO_P1_22, GPIO_P1_23, GPIO_P1_24, GPIO_P1_26,\n   V2_GPIO_P1_03, V2_GPIO_P1_05, V2_GPIO_P1_07, V2_GPIO_P1_08,\n   V2_GPIO_P1_10, V2_GPIO_P1_11, V2_GPIO_P1_12, V2_GPIO_P1_13,\n   V2_GPIO_P1_15, V2_GPIO_P1_16, V2_GPIO_P1_18, V2_GPIO_P1_19,\n   V2_GPIO_P1_21, V2_GPIO_P1_22, V2_GPIO_P1_23, V2_GPIO_P1_24,\n   V2_GPIO_P1_26, V2_GPIO_P1_29, V2_GPIO_P1_31, V2_GPIO_P1_32,\n   V2_GPIO_P1_33, V2_GPIO_P1_35, V2_GPIO_P1_36, V2_GPIO_P1_37,\n   V2_GPIO_P1_38, V2_GPIO_P1_40, V2_GPIO_P5_03, V2_GPIO_P5_04,\n   V2_GPIO_P5_05, V2_GPIO_P5_06, BPLUS_GPIO_J8_03, BPLUS_GPIO_J8_05,\n   BPLUS_GPIO_J8_07, BPLUS_GPIO_J8_08, BPLUS_GPIO_J8_10, BPLUS_GPIO_J8_11,\n   BPLUS_GPIO_J8_12, BPLUS_GPIO_J8_13, BPLUS_GPIO_J8_15, BPLUS_GPIO_J8_16,\n   BPLUS_GPIO_J8_18, BPLUS_GPIO_J8_19, BPLUS_GPIO_J8_21, BPLUS_GPIO_J8_22,\n   BPLUS_GPIO_J8_23, BPLUS_GPIO_J8_24, BPLUS_GPIO_J8_26, BPLUS_GPIO_J8_29,\n   BPLUS_GPIO_J8_31, BPLUS_GPIO_J8_32, BPLUS_GPIO_J8_33, BPLUS_GPIO_J8_35,\n   BPLUS_GPIO_J8_36, BPLUS_GPIO_J8_37, BPLUS_GPIO_J8_38, BPLUS_GPIO_J8_40);",
       }   ,
       {
       name: "Pin_State",
       qualified_name: "Raspio.GPIO.Pin_State",
       signature: "raspio.gpio.pin_state",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Pin_State is (On, Off);",
       }   ,
       {
       name: "Pin_Type",
       qualified_name: "Raspio.GPIO.Pin_Type",
       signature: "raspio.gpio.pin_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Pin_Type is limited private;",
       }   ,
   ]
,}
---
