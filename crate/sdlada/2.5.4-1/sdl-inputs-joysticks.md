---
crate: sdlada
layout: gnatdoc
gnatdoc: {
name: "SDL.Inputs.Joysticks",
qualified_name: "SDL.Inputs.Joysticks",
signature: "sdl.inputs.joysticks",
enclosing: "sdl.inputs",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "All_Devices",
       qualified_name: "SDL.Inputs.Joysticks.All_Devices",
       signature: "sdl.inputs.joysticks.all_devices",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type All_Devices is range 0 .. 2 ** 31 - 1 with\n  Convention => C,\n  Size       => 32;",
       }   ,
       {
       name: "GUID_Element",
       qualified_name: "SDL.Inputs.Joysticks.GUID_Element",
       signature: "sdl.inputs.joysticks.guid_element",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type GUID_Element is range 0 .. 255 with\n  convention => C,\n  Size       => 8;",
       }   ,
       {
       name: "Instances",
       qualified_name: "SDL.Inputs.Joysticks.Instances",
       signature: "sdl.inputs.joysticks.instances",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Instances is range 0 .. 2 ** 31 - 1 with\n  Convention => C,\n  Size       => 32;",
       }   ,
   ]
,array_types:    [
       {
       name: "GUID_Array",
       qualified_name: "SDL.Inputs.Joysticks.GUID_Array",
       signature: "sdl.inputs.joysticks.guid_array",
       enclosing: "",
       is_private: false,
       documentation: "Pack       => True;",
       documentation_snippet: "type GUID_Array is array (1 .. 16) of aliased GUID_Element with\n  Convention => C;",
       }   ,
   ]
,record_types:    [
       {
       name: "GUIDs",
       qualified_name: "SDL.Inputs.Joysticks.GUIDs",
       signature: "sdl.inputs.joysticks.guids",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type GUIDs is\n   record\n      Data : GUID_Array;\n   end record with\n  Convention => C_Pass_By_Copy;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Joystick",
       qualified_name: "SDL.Inputs.Joysticks.Joystick",
       signature: "sdl.inputs.joysticks.joystick",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Joystick is new Ada.Finalization.Limited_Controlled with private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Devices",
       qualified_name: "SDL.Inputs.Joysticks.Devices",
       signature: "sdl.inputs.joysticks.devices",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Devices is All_Devices range All_Devices'First + 1 .. All_Devices'Last;",
       }   ,
   ]
,constants:    [
       {
       name: "Null_Joystick",
       qualified_name: "SDL.Inputs.Joysticks.Null_Joystick",
       signature: "sdl.inputs.joysticks.null_joystick",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Null_Joystick : constant Joystick;",
       }   ,
   ]
,}
---
