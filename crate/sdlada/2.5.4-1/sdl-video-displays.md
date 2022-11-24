---
crate: sdlada
layout: gnatdoc
gnatdoc: {
name: "SDL.Video.Displays",
qualified_name: "SDL.Video.Displays",
signature: "sdl.video.displays",
enclosing: "sdl.video",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Display_Indices",
       qualified_name: "SDL.Video.Displays.Display_Indices",
       signature: "sdl.video.displays.display_indices",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Display_Indices is new Positive;",
       }   ,
       {
       name: "Refresh_Rates",
       qualified_name: "SDL.Video.Displays.Refresh_Rates",
       signature: "sdl.video.displays.refresh_rates",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Refresh_Rates is range 0 .. 400 with\n  Convention => C;",
       }   ,
   ]
,record_types:    [
       {
       name: "Mode",
       qualified_name: "SDL.Video.Displays.Mode",
       signature: "sdl.video.displays.mode",
       enclosing: "",
       is_private: false,
       documentation: "\n@field Format\n@field Width\n@field Height\n@field Refresh_Rate\n@field Driver_Data\n  TODO: Somehow make this a real type.",
       documentation_snippet: "type Mode is\n   record\n      Format       : SDL.Video.Pixel_Formats.Pixel_Format_Names;\n      Width        : C.int;\n      Height       : C.int;\n      Refresh_Rate : Refresh_Rates;\n      Driver_Data  : System.Address;\n   end record with\n  Convention => C;",
       }   ,
   ]
,access_types:    [
       {
       name: "Access_Mode",
       qualified_name: "SDL.Video.Displays.Access_Mode",
       signature: "sdl.video.displays.access_mode",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Access_Mode is access all Mode with\n  Convention => C;",
       }   ,
   ]
,}
---
