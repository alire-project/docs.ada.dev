---
crate: rp2040_hal
layout: gnatdoc
gnatdoc: {
name: "RP.PWM",
qualified_name: "RP.PWM",
signature: "rp.pwm",
enclosing: "rp",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "PWM_Channel",
       qualified_name: "RP.PWM.PWM_Channel",
       signature: "rp.pwm.pwm_channel",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type PWM_Channel is (A, B);",
       }   ,
       {
       name: "PWM_Divider_Mode",
       qualified_name: "RP.PWM.PWM_Divider_Mode",
       signature: "rp.pwm.pwm_divider_mode",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum Free_Running\n@enum Gated\n  Slice counter only runs while channel B is high\n@enum Rising_Edge\n  Slice counter increments on channel B rising edge\n@enum Falling_Edge\n  Slice counter increments on channel B falling edge",
       documentation_snippet: "type PWM_Divider_Mode is\n   (Free_Running,\n    Gated,\n    Rising_Edge,\n    Falling_Edge);",
       }   ,
       {
       name: "PWM_Slice",
       qualified_name: "RP.PWM.PWM_Slice",
       signature: "rp.pwm.pwm_slice",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type PWM_Slice is range 0 .. 7;",
       }   ,
   ]
,array_types:    [
       {
       name: "PWM_Slice_Array",
       qualified_name: "RP.PWM.PWM_Slice_Array",
       signature: "rp.pwm.pwm_slice_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type PWM_Slice_Array is array (PWM_Slice) of Boolean;",
       }   ,
   ]
,record_types:    [
       {
       name: "PWM_Point",
       qualified_name: "RP.PWM.PWM_Point",
       signature: "rp.pwm.pwm_point",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type PWM_Point is record\n   Slice   : PWM_Slice;\n   Channel : PWM_Channel;\nend record;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Period",
       qualified_name: "RP.PWM.Period",
       signature: "rp.pwm.period",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Period is UInt16;",
       }   ,
   ]
,constants:    [
       {
       name: "Divider_Fraction",
       qualified_name: "RP.PWM.Divider_Fraction",
       signature: "rp.pwm.divider_fraction",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Divider_Fraction : constant := 1.0 / (2.0 ** 4);",
       }   ,
   ]
,variables:    [
       {
       name: "Initialized",
       qualified_name: "RP.PWM.Initialized",
       signature: "rp.pwm.initialized",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Initialized : Boolean := False;",
       }   ,
   ]
,}
---
