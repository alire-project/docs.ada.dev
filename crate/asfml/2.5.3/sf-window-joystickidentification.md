---
crate: asfml
layout: gnatdoc
gnatdoc: {
name: "Sf.Window.JoystickIdentification",
qualified_name: "Sf.Window.JoystickIdentification",
signature: "sf.window.joystickidentification",
enclosing: "sf.window",
is_private: false,
documentation: "//////////////////////////////////////////////////////////\n//////////////////////////////////////////////////////////\n/ sfJoystickIdentification holds a joystick's identification\n//////////////////////////////////////////////////////////",
documentation_snippet: "",
record_types:    [
       {
       name: "sfJoystickIdentification",
       qualified_name: "Sf.Window.JoystickIdentification.sfJoystickIdentification",
       signature: "sf.window.joystickidentification.sfjoystickidentification",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfJoystickIdentification is record\n   name : Interfaces.C.Strings.chars_ptr;\n   vendorId : aliased sfUint32;\n   productId : aliased sfUint32;\nend record;",
       }   ,
   ]
,}
---
