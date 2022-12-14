---
crate: sdlada
layout: gnatdoc
gnatdoc: {
name: "SDL.Log",
qualified_name: "SDL.Log",
signature: "sdl.log",
enclosing: "sdl",
is_private: false,
documentation: "Messages longer than Max_Length will be truncated.\nTODO: Import this from a C constant set from SDL_MAX_LOG_MESSAGE.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Categories",
       qualified_name: "SDL.Log.Categories",
       signature: "sdl.log.categories",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Categories is range 0 .. 2 ** 32;",
       }   ,
       {
       name: "Priorities",
       qualified_name: "SDL.Log.Priorities",
       signature: "sdl.log.priorities",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Priorities is (Verbose, Debug, Info, Warn, Error, Critical) with\n  Convention => C;",
       }   ,
   ]
,record_types:    [
       {
       name: "Root_User_Data",
       qualified_name: "SDL.Log.Root_User_Data",
       signature: "sdl.log.root_user_data",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Root_User_Data is tagged null record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Output_Callback",
       qualified_name: "SDL.Log.Output_Callback",
       signature: "sdl.log.output_callback",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Output_Callback is access procedure\n  (User_Data : in Root_User_Data'Class;\n   Category  : in Categories;\n   Priority  : in Priorities;\n   Message   : in String);",
       }   ,
   ]
,subtypes:    [
       {
       name: "Custom_Categories",
       qualified_name: "SDL.Log.Custom_Categories",
       signature: "sdl.log.custom_categories",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Custom_Categories is Categories range Reserved_Last .. Categories'Last;",
       }   ,
   ]
,constants:    [
       {
       name: "Application",
       qualified_name: "SDL.Log.Application",
       signature: "sdl.log.application",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Application    : constant Categories := 0;",
       }   ,
       {
       name: "Assert",
       qualified_name: "SDL.Log.Assert",
       signature: "sdl.log.assert",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Assert         : constant Categories := 2;",
       }   ,
       {
       name: "Audio",
       qualified_name: "SDL.Log.Audio",
       signature: "sdl.log.audio",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Audio          : constant Categories := 4;",
       }   ,
       {
       name: "Errors",
       qualified_name: "SDL.Log.Errors",
       signature: "sdl.log.errors",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Errors         : constant Categories := 1;",
       }   ,
       {
       name: "Input",
       qualified_name: "SDL.Log.Input",
       signature: "sdl.log.input",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Input          : constant Categories := 7;",
       }   ,
       {
       name: "Max_Length",
       qualified_name: "SDL.Log.Max_Length",
       signature: "sdl.log.max_length",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Max_Length : constant Integer := 4096;",
       }   ,
       {
       name: "Render",
       qualified_name: "SDL.Log.Render",
       signature: "sdl.log.render",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Render         : constant Categories := 6;",
       }   ,
       {
       name: "Reserved_First",
       qualified_name: "SDL.Log.Reserved_First",
       signature: "sdl.log.reserved_first",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Reserved_First : constant Categories := 9;",
       }   ,
       {
       name: "Reserved_Last",
       qualified_name: "SDL.Log.Reserved_Last",
       signature: "sdl.log.reserved_last",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Reserved_Last  : constant Categories := 18;",
       }   ,
       {
       name: "System",
       qualified_name: "SDL.Log.System",
       signature: "sdl.log.system",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "System         : constant Categories := 3;",
       }   ,
       {
       name: "Test",
       qualified_name: "SDL.Log.Test",
       signature: "sdl.log.test",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Test           : constant Categories := 8;",
       }   ,
       {
       name: "Video",
       qualified_name: "SDL.Log.Video",
       signature: "sdl.log.video",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Video          : constant Categories := 5;",
       }   ,
   ]
,}
---
