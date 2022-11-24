---
crate: openglada_glfw
layout: gnatdoc
gnatdoc: {
name: "Glfw.Monitors",
qualified_name: "Glfw.Monitors",
signature: "glfw.monitors",
enclosing: "glfw",
is_private: false,
documentation: "part of OpenGLAda, (c) 2017 Felix Krause\nreleased under the terms of the MIT license, see the file \"COPYING\"",
documentation_snippet: "",
simple_types:    [
       {
       name: "Event",
       qualified_name: "Glfw.Monitors.Event",
       signature: "glfw.monitors.event",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Event is (Connected, Disconnected);",
       }   ,
   ]
,array_types:    [
       {
       name: "Gamma_Value_Array",
       qualified_name: "Glfw.Monitors.Gamma_Value_Array",
       signature: "glfw.monitors.gamma_value_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Gamma_Value_Array is array (Positive range <>) of aliased\n  Interfaces.C.unsigned_short;",
       }   ,
       {
       name: "Monitor_List",
       qualified_name: "Glfw.Monitors.Monitor_List",
       signature: "glfw.monitors.monitor_list",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Monitor_List is array (Positive range <>) of Monitor;",
       }   ,
       {
       name: "Video_Mode_List",
       qualified_name: "Glfw.Monitors.Video_Mode_List",
       signature: "glfw.monitors.video_mode_list",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Video_Mode_List is array (Positive range <>) of aliased Video_Mode;",
       }   ,
   ]
,record_types:    [
       {
       name: "Gamma_Ramp",
       qualified_name: "Glfw.Monitors.Gamma_Ramp",
       signature: "glfw.monitors.gamma_ramp",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Gamma_Ramp (Size : Positive) is record\n   Red, Green, Blue : Gamma_Value_Array (1 .. Size);\nend record;",
       }   ,
       {
       name: "Video_Mode",
       qualified_name: "Glfw.Monitors.Video_Mode",
       signature: "glfw.monitors.video_mode",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Video_Mode is record\n   Width, Height : Interfaces.C.int;\n   Red_Bits, Green_Bits, Blue_Bits : Interfaces.C.int;\n   Refresh_Rate : Interfaces.C.int;\nend record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Monitor",
       qualified_name: "Glfw.Monitors.Monitor",
       signature: "glfw.monitors.monitor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Monitor is tagged private;",
       }   ,
   ]
,constants:    [
       {
       name: "No_Monitor",
       qualified_name: "Glfw.Monitors.No_Monitor",
       signature: "glfw.monitors.no_monitor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Monitor : constant Monitor;",
       }   ,
   ]
,}
---
