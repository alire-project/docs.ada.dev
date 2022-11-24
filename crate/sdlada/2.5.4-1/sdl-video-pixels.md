---
crate: sdlada
layout: gnatdoc
gnatdoc: {
name: "SDL.Video.Pixels",
qualified_name: "SDL.Video.Pixels",
signature: "sdl.video.pixels",
enclosing: "sdl.video",
is_private: false,
documentation: "",
documentation_snippet: "",
packages:    [
       {
       name: "Texture_Data",
       qualified_name: "SDL.Video.Pixels.Texture_Data",
       signature: "sdl.video.pixels.texture_data",
       enclosing: "sdl.video.pixels",
       is_private: false,
       documentation: "",
       documentation_snippet: "",
subtypes:           [
              {
              name: "Pointer",
              qualified_name: "SDL.Video.Pixels.Texture_Data.Pointer",
              signature: "sdl.video.pixels.texture_data.pointer",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "subtype Pointer is Texture_Data_1D.Pointer;",
              }          ,
          ]
,       }   ,
   ]
,simple_types:    [
       {
       name: "Pitches",
       qualified_name: "SDL.Video.Pixels.Pitches",
       signature: "sdl.video.pixels.pitches",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Pitches is new C.int with\n  Size       => 32,\n  Convention => C;",
       }   ,
   ]
,array_types:    [
       {
       name: "ARGB_8888_Array",
       qualified_name: "SDL.Video.Pixels.ARGB_8888_Array",
       signature: "sdl.video.pixels.argb_8888_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type ARGB_8888_Array is array (SDL.Dimension range <>) of aliased ARGB_8888;",
       }   ,
   ]
,record_types:    [
       {
       name: "ARGB_8888",
       qualified_name: "SDL.Video.Pixels.ARGB_8888",
       signature: "sdl.video.pixels.argb_8888",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type ARGB_8888 is\n   record\n      Alpha : SDL.Video.Palettes.Colour_Component;\n      Red   : SDL.Video.Palettes.Colour_Component;\n      Green : SDL.Video.Palettes.Colour_Component;\n      Blue  : SDL.Video.Palettes.Colour_Component;\n   end record with\n  Size       => 32,\n  Convention => C;",
       }   ,
   ]
,}
---
