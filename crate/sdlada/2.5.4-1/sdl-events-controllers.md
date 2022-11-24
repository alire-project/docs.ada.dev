---
crate: sdlada
layout: gnatdoc
gnatdoc: {
name: "SDL.Events.Controllers",
qualified_name: "SDL.Events.Controllers",
signature: "sdl.events.controllers",
enclosing: "sdl.events",
is_private: false,
documentation: "Game controller events.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Axes",
       qualified_name: "SDL.Events.Controllers.Axes",
       signature: "sdl.events.controllers.axes",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Axes is (Invalid,\n              Left_X,\n              Left_Y,\n              Right_X,\n              Right_Y,\n              Left_Trigger,\n              Right_Trigger) with\n  Convention => C;",
       }   ,
       {
       name: "Axes_Values",
       qualified_name: "SDL.Events.Controllers.Axes_Values",
       signature: "sdl.events.controllers.axes_values",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Axes_Values is range -32768 .. 32767 with\n  Convention => C,\n  Size       => 16;",
       }   ,
       {
       name: "Buttons",
       qualified_name: "SDL.Events.Controllers.Buttons",
       signature: "sdl.events.controllers.buttons",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum Invalid\n@enum A\n@enum B\n@enum X\n@enum Y\n@enum Back\n@enum Guide\n@enum Start\n@enum Left_Stick\n@enum Right_Stick\n@enum Left_Shoulder\n@enum Right_Shoulder\n@enum Pad_Up\n  Direction pad buttons.\n@enum Pad_Down\n@enum Pad_Left\n@enum Pad_Right",
       documentation_snippet: "type Buttons is (Invalid,\n                 A,\n                 B,\n                 X,\n                 Y,\n                 Back,\n                 Guide,\n                 Start,\n                 Left_Stick,\n                 Right_Stick,\n                 Left_Shoulder,\n                 Right_Shoulder,\n                 Pad_Up,\n                 Pad_Down,\n                 Pad_Left,\n                 Pad_Right) with\n  Convention => C;",
       }   ,
   ]
,record_types:    [
       {
       name: "Axis_Events",
       qualified_name: "SDL.Events.Controllers.Axis_Events",
       signature: "sdl.events.controllers.axis_events",
       enclosing: "",
       is_private: false,
       documentation: "\n@field Event_Type\n  Will be set to Axis_Motion.\n@field Time_Stamp\n@field Which\n@field Axis\n@field Padding_1\n@field Padding_2\n@field Padding_3\n@field Value\n@field Padding_4",
       documentation_snippet: "type Axis_Events is\n   record\n      Event_Type : Event_Types;\n      Time_Stamp : Time_Stamps;\n      Which      : SDL.Events.Joysticks.IDs;\n      Axis       : Axes;\n      Padding_1  : Padding_8;\n      Padding_2  : Padding_8;\n      Padding_3  : Padding_8;\n      Value      : Axes_Values;\n      Padding_4  : Padding_16;\n   end record with\n  Convention => C;",
       }   ,
       {
       name: "Button_Events",
       qualified_name: "SDL.Events.Controllers.Button_Events",
       signature: "sdl.events.controllers.button_events",
       enclosing: "",
       is_private: false,
       documentation: "\n@field Event_Type\n  Will be set to Button_Down or Button_Up.\n@field Time_Stamp\n@field Which\n@field Button\n@field State\n@field Padding_1\n@field Padding_2",
       documentation_snippet: "type Button_Events is\n   record\n      Event_Type : Event_Types;\n      Time_Stamp : Time_Stamps;\n      Which      : SDL.Events.Joysticks.IDs;\n      Button     : Buttons;\n      State      : Button_State;\n      Padding_1  : Padding_8;\n      Padding_2  : Padding_8;\n   end record with\n  Convention => C;",
       }   ,
       {
       name: "Device_Events",
       qualified_name: "SDL.Events.Controllers.Device_Events",
       signature: "sdl.events.controllers.device_events",
       enclosing: "",
       is_private: false,
       documentation: "\n@field Event_Type\n  Will be set to Device_Added, Device_Removed or Device_Remapped.\n@field Time_Stamp\n@field Which",
       documentation_snippet: "type Device_Events is\n   record\n      Event_Type : Event_Types;\n      Time_Stamp : Time_Stamps;\n      Which      : SDL.Events.Joysticks.IDs;\n   end record with\n  Convention => C;",
       }   ,
   ]
,constants:    [
       {
       name: "Axis_Motion",
       qualified_name: "SDL.Events.Controllers.Axis_Motion",
       signature: "sdl.events.controllers.axis_motion",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Axis_Motion     : constant Event_Types := 16#0000_0650#;",
       }   ,
       {
       name: "Button_Down",
       qualified_name: "SDL.Events.Controllers.Button_Down",
       signature: "sdl.events.controllers.button_down",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Button_Down     : constant Event_Types := Axis_Motion + 1;",
       }   ,
       {
       name: "Button_Up",
       qualified_name: "SDL.Events.Controllers.Button_Up",
       signature: "sdl.events.controllers.button_up",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Button_Up       : constant Event_Types := Axis_Motion + 2;",
       }   ,
       {
       name: "Device_Added",
       qualified_name: "SDL.Events.Controllers.Device_Added",
       signature: "sdl.events.controllers.device_added",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Device_Added    : constant Event_Types := Axis_Motion + 3;",
       }   ,
       {
       name: "Device_Remapped",
       qualified_name: "SDL.Events.Controllers.Device_Remapped",
       signature: "sdl.events.controllers.device_remapped",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Device_Remapped : constant Event_Types := Axis_Motion + 5;",
       }   ,
       {
       name: "Device_Removed",
       qualified_name: "SDL.Events.Controllers.Device_Removed",
       signature: "sdl.events.controllers.device_removed",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Device_Removed  : constant Event_Types := Axis_Motion + 4;",
       }   ,
   ]
,}
---