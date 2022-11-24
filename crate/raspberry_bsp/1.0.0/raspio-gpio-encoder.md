---
crate: raspberry_bsp
layout: gnatdoc
gnatdoc: {
name: "Raspio.GPIO.Encoder",
qualified_name: "Raspio.GPIO.Encoder",
signature: "raspio.gpio.encoder",
enclosing: "raspio.gpio",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Diff_Type",
       qualified_name: "Raspio.GPIO.Encoder.Diff_Type",
       signature: "raspio.gpio.encoder.diff_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Diff_Type is range -1 .. 1;",
       }   ,
       {
       name: "Encoder_Type",
       qualified_name: "Raspio.GPIO.Encoder.Encoder_Type",
       signature: "raspio.gpio.encoder.encoder_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Encoder_Type is limited private;",
       }   ,
   ]
,array_types:    [
       {
       name: "Encoder_Pin_Values",
       qualified_name: "Raspio.GPIO.Encoder.Encoder_Pin_Values",
       signature: "raspio.gpio.encoder.encoder_pin_values",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Encoder_Pin_Values is array (1 .. Encoder_Size) of Pin_State;",
       }   ,
       {
       name: "Encoder_Pins",
       qualified_name: "Raspio.GPIO.Encoder.Encoder_Pins",
       signature: "raspio.gpio.encoder.encoder_pins",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Encoder_Pins is array (1 .. Encoder_Size) of Pin_Type;",
       }   ,
   ]
,constants:    [
       {
       name: "Encoder_Size",
       qualified_name: "Raspio.GPIO.Encoder.Encoder_Size",
       signature: "raspio.gpio.encoder.encoder_size",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Encoder_Size : constant := 2;",
       }   ,
   ]
,}
---
