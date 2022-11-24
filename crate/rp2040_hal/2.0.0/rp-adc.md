---
crate: rp2040_hal
layout: gnatdoc
gnatdoc: {
name: "RP.ADC",
qualified_name: "RP.ADC",
signature: "rp.adc",
enclosing: "rp",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "ADC_Mode",
       qualified_name: "RP.ADC.ADC_Mode",
       signature: "rp.adc.adc_mode",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type ADC_Mode is (One_Shot, Free_Running);",
       }   ,
       {
       name: "ADC_Sample_Bits",
       qualified_name: "RP.ADC.ADC_Sample_Bits",
       signature: "rp.adc.adc_sample_bits",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type ADC_Sample_Bits is new Positive\n   with Dynamic_Predicate => ADC_Sample_Bits in 8 | 12;",
       }   ,
       {
       name: "Celsius",
       qualified_name: "RP.ADC.Celsius",
       signature: "rp.adc.celsius",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Celsius is new Integer;",
       }   ,
       {
       name: "Microvolts",
       qualified_name: "RP.ADC.Microvolts",
       signature: "rp.adc.microvolts",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Microvolts is new Integer;",
       }   ,
   ]
,array_types:    [
       {
       name: "ADC_Channels",
       qualified_name: "RP.ADC.ADC_Channels",
       signature: "rp.adc.adc_channels",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type ADC_Channels is array (ADC_Channel) of Boolean\n   with Component_Size => 1,\n        Size           => 5;",
       }   ,
   ]
,subtypes:    [
       {
       name: "ADC_Channel",
       qualified_name: "RP.ADC.ADC_Channel",
       signature: "rp.adc.adc_channel",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype ADC_Channel is Natural range 0 .. 4;",
       }   ,
       {
       name: "Analog_Value",
       qualified_name: "RP.ADC.Analog_Value",
       signature: "rp.adc.analog_value",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Analog_Value is HAL.UInt12;",
       }   ,
   ]
,constants:    [
       {
       name: "ADC_Divider_Fraction",
       qualified_name: "RP.ADC.ADC_Divider_Fraction",
       signature: "rp.adc.adc_divider_fraction",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "ADC_Divider_Fraction : constant := 1.0 / (2.0 ** 8);",
       }   ,
       {
       name: "Temperature_Sensor",
       qualified_name: "RP.ADC.Temperature_Sensor",
       signature: "rp.adc.temperature_sensor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Temperature_Sensor : constant ADC_Channel := 4;",
       }   ,
   ]
,}
---
