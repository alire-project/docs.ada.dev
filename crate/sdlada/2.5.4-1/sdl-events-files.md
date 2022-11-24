---
crate: sdlada
layout: gnatdoc
gnatdoc: {
name: "SDL.Events.Files",
qualified_name: "SDL.Events.Files",
signature: "sdl.events.files",
enclosing: "sdl.events",
is_private: false,
documentation: "Drag and drop events.",
documentation_snippet: "",
record_types:    [
       {
       name: "Drop_Events",
       qualified_name: "SDL.Events.Files.Drop_Events",
       signature: "sdl.events.files.drop_events",
       enclosing: "",
       is_private: false,
       documentation: "\n@field Event_Type\n  Will be set to Drop_File.\n@field Time_Stamp\n@field File_Name\n  User *must* call Free on this.",
       documentation_snippet: "type Drop_Events is\n   record\n      Event_Type : Event_Types;\n      Time_Stamp : Time_Stamps;\n      File_Name  : Interfaces.C.Strings.chars_ptr;\n   end record with\n  Convention => C;",
       }   ,
   ]
,constants:    [
       {
       name: "Drop_File",
       qualified_name: "SDL.Events.Files.Drop_File",
       signature: "sdl.events.files.drop_file",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Drop_File : constant Event_Types := 16#0000_1000#;",
       }   ,
   ]
,}
---
