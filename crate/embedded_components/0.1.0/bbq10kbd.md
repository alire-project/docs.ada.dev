---
crate: embedded_components
layout: gnatdoc
gnatdoc: {
name: "BBQ10KBD",
qualified_name: "BBQ10KBD",
signature: "bbq10kbd",
enclosing: "",
is_private: false,
documentation: "Driver for the Blackberry Q10 Keyboard I2C interface from solder.party\nhttps://github.com/arturo182/bbq10kbd_i2c_sw",
documentation_snippet: "",
simple_types:    [
       {
       name: "Key_State_Kind",
       qualified_name: "BBQ10KBD.Key_State_Kind",
       signature: "bbq10kbd.key_state_kind",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Key_State_Kind is (Pressed, Held_Pressed, Released, Error);",
       }   ,
   ]
,record_types:    [
       {
       name: "KBD_Status",
       qualified_name: "BBQ10KBD.KBD_Status",
       signature: "bbq10kbd.kbd_status",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type KBD_Status is record\n   Numlock   : Boolean;\n   Capslock  : Boolean;\n   Key_Count : HAL.UInt5;\nend record;",
       }   ,
       {
       name: "Key_State",
       qualified_name: "BBQ10KBD.Key_State",
       signature: "bbq10kbd.key_state",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Key_State is record\n   Kind : Key_State_Kind;\n   Code : HAL.UInt8;\nend record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "BBQ10KBD_Device",
       qualified_name: "BBQ10KBD.BBQ10KBD_Device",
       signature: "bbq10kbd.bbq10kbd_device",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type BBQ10KBD_Device (Port : not null HAL.I2C.Any_I2C_Port)\nis tagged private;",
       }   ,
   ]
,}
---
