---
crate: sdlada
layout: gnatdoc
gnatdoc: {
name: "SDL.Versions",
qualified_name: "SDL.Versions",
signature: "sdl.versions",
enclosing: "sdl",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Revision_Level",
       qualified_name: "SDL.Versions.Revision_Level",
       signature: "sdl.versions.revision_level",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Revision_Level is mod 2 ** 32;",
       }   ,
       {
       name: "Version_Level",
       qualified_name: "SDL.Versions.Version_Level",
       signature: "sdl.versions.version_level",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Version_Level is mod 2 ** 8 with\n  Size       => 8,\n  Convention => C;",
       }   ,
   ]
,record_types:    [
       {
       name: "Version",
       qualified_name: "SDL.Versions.Version",
       signature: "sdl.versions.version",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Version is\n   record\n      Major : Version_Level;\n      Minor : Version_Level;\n      Patch : Version_Level;\n   end record with\n  Convention => C;",
       }   ,
   ]
,constants:    [
       {
       name: "Compiled_Major",
       qualified_name: "SDL.Versions.Compiled_Major",
       signature: "sdl.versions.compiled_major",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Compiled_Major : constant Version_Level with\n  Import        => True,\n  Convention    => C,\n  External_Name => \"SDL_Ada_Major_Version\";",
       }   ,
       {
       name: "Compiled_Minor",
       qualified_name: "SDL.Versions.Compiled_Minor",
       signature: "sdl.versions.compiled_minor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Compiled_Minor : constant Version_Level with\n  Import        => True,\n  Convention    => C,\n  External_Name => \"SDL_Ada_Minor_Version\";",
       }   ,
       {
       name: "Compiled_Patch",
       qualified_name: "SDL.Versions.Compiled_Patch",
       signature: "sdl.versions.compiled_patch",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Compiled_Patch : constant Version_Level with\n  Import        => True,\n  Convention    => C,\n  External_Name => \"SDL_Ada_Patch_Version\";",
       }   ,
   ]
,}
---
