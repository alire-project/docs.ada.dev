---
crate: sdlada
layout: gnatdoc
gnatdoc: {
name: "SDL.Events.Windows",
qualified_name: "SDL.Events.Windows",
signature: "sdl.events.windows",
enclosing: "sdl.events",
is_private: false,
documentation: "Window events.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Window_Event_ID",
       qualified_name: "SDL.Events.Windows.Window_Event_ID",
       signature: "sdl.events.windows.window_event_id",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Window_Event_ID is\n  (None,\n   Shown,\n   Hidden,\n   Exposed,\n   Moved,\n   Resized,\n   Size_Changed,\n   Minimised,\n   Maximised,\n   Restored,\n   Enter,\n   Leave,\n   Focus_Gained,\n   Focus_Lost,\n   Close,\n   Take_Focus,\n   Hit_Test) with\n  Convention => C;",
       }   ,
   ]
,record_types:    [
       {
       name: "Window_Events",
       qualified_name: "SDL.Events.Windows.Window_Events",
       signature: "sdl.events.windows.window_events",
       enclosing: "",
       is_private: false,
       documentation: "\n@field Event_Type\n  Will be set to Window.\n@field Time_Stamp\n@field ID\n@field Event_ID\n@field Padding_1\n@field Padding_2\n@field Padding_3\n@field Data_1\n@field Data_2",
       documentation_snippet: "type Window_Events is\n   record\n      Event_Type : Event_Types;\n      Time_Stamp : Time_Stamps;\n      ID         : SDL.Video.Windows.ID;\n      Event_ID   : Window_Event_ID;\n      Padding_1  : Padding_8;\n      Padding_2  : Padding_8;\n      Padding_3  : Padding_8;\n      Data_1     : Interfaces.Integer_32;\n      Data_2     : Interfaces.Integer_32;\n   end record with\n  Convention => C;",
       }   ,
   ]
,constants:    [
       {
       name: "System_Window_Manager",
       qualified_name: "SDL.Events.Windows.System_Window_Manager",
       signature: "sdl.events.windows.system_window_manager",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "System_Window_Manager      : constant Event_Types := Window + 1;",
       }   ,
       {
       name: "Window",
       qualified_name: "SDL.Events.Windows.Window",
       signature: "sdl.events.windows.window",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Window                     : constant Event_Types := 16#0000_0200#;",
       }   ,
   ]
,}
---
