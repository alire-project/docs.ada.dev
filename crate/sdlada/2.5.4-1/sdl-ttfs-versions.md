---
crate: sdlada
layout: gnatdoc
gnatdoc: {
name: "SDL.TTFs.Versions",
qualified_name: "SDL.TTFs.Versions",
signature: "sdl.ttfs.versions",
enclosing: "sdl.ttfs",
is_private: false,
documentation: "These allow the user to determine which version of SDLAda_TTF they compiled with.",
documentation_snippet: "",
constants:    [
       {
       name: "Compiled",
       qualified_name: "SDL.TTFs.Versions.Compiled",
       signature: "sdl.ttfs.versions.compiled",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Compiled : constant SDL.Versions.Version := (Major => Compiled_Major,\n                                             Minor => Compiled_Minor,\n                                             Patch => Compiled_Patch);",
       }   ,
       {
       name: "Compiled_Major",
       qualified_name: "SDL.TTFs.Versions.Compiled_Major",
       signature: "sdl.ttfs.versions.compiled_major",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Compiled_Major : constant SDL.Versions.Version_Level with\n  Import        => True,\n  Convention    => C,\n  External_Name => \"SDL_Ada_TTF_Major_Version\";",
       }   ,
       {
       name: "Compiled_Minor",
       qualified_name: "SDL.TTFs.Versions.Compiled_Minor",
       signature: "sdl.ttfs.versions.compiled_minor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Compiled_Minor : constant SDL.Versions.Version_Level with\n  Import        => True,\n  Convention    => C,\n  External_Name => \"SDL_Ada_TTF_Minor_Version\";",
       }   ,
       {
       name: "Compiled_Patch",
       qualified_name: "SDL.TTFs.Versions.Compiled_Patch",
       signature: "sdl.ttfs.versions.compiled_patch",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Compiled_Patch : constant SDL.Versions.Version_Level with\n  Import        => True,\n  Convention    => C,\n  External_Name => \"SDL_Ada_TTF_Patch_Version\";",
       }   ,
   ]
,}
---
