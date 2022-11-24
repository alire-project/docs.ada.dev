---
crate: sdlada
layout: gnatdoc
gnatdoc: {
name: "SDL.Images.Versions",
qualified_name: "SDL.Images.Versions",
signature: "sdl.images.versions",
enclosing: "sdl.images",
is_private: false,
documentation: "These allow the user to determine which version of SDLAda_Image they compiled with.",
documentation_snippet: "",
constants:    [
       {
       name: "Compiled",
       qualified_name: "SDL.Images.Versions.Compiled",
       signature: "sdl.images.versions.compiled",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Compiled : constant SDL.Versions.Version := (Major => Compiled_Major,\n                                             Minor => Compiled_Minor,\n                                             Patch => Compiled_Patch);",
       }   ,
       {
       name: "Compiled_Major",
       qualified_name: "SDL.Images.Versions.Compiled_Major",
       signature: "sdl.images.versions.compiled_major",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Compiled_Major : constant SDL.Versions.Version_Level with\n  Import        => True,\n  Convention    => C,\n  External_Name => \"SDL_Ada_Image_Major_Version\";",
       }   ,
       {
       name: "Compiled_Minor",
       qualified_name: "SDL.Images.Versions.Compiled_Minor",
       signature: "sdl.images.versions.compiled_minor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Compiled_Minor : constant SDL.Versions.Version_Level with\n  Import        => True,\n  Convention    => C,\n  External_Name => \"SDL_Ada_Image_Minor_Version\";",
       }   ,
       {
       name: "Compiled_Patch",
       qualified_name: "SDL.Images.Versions.Compiled_Patch",
       signature: "sdl.images.versions.compiled_patch",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Compiled_Patch : constant SDL.Versions.Version_Level with\n  Import        => True,\n  Convention    => C,\n  External_Name => \"SDL_Ada_Image_Patch_Version\";",
       }   ,
   ]
,}
---
