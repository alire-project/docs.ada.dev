---
crate: microbit_bsp
layout: gnatdoc
gnatdoc: {
name: "MicroBit.Servos",
qualified_name: "MicroBit.Servos",
signature: "microbit.servos",
enclosing: "microbit",
is_private: false,
documentation: "Servo-motors control",
documentation_snippet: "",
simple_types:    [
       {
       name: "Servo_Set_Point",
       qualified_name: "MicroBit.Servos.Servo_Set_Point",
       signature: "microbit.servos.servo_set_point",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Servo_Set_Point is range 0 .. 180;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Servo_Pin_Id",
       qualified_name: "MicroBit.Servos.Servo_Pin_Id",
       signature: "microbit.servos.servo_pin_id",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Servo_Pin_Id is Pin_Id\n  with Predicate => Supports (Servo_Pin_Id, Analog);",
       }   ,
   ]
,}
---
