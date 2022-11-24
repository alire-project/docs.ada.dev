---
crate: sdlada
layout: gnatdoc
gnatdoc: {
name: "SDL.Video.Surfaces",
qualified_name: "SDL.Video.Surfaces",
signature: "sdl.video.surfaces",
enclosing: "sdl.video",
is_private: false,
documentation: "",
documentation_snippet: "",
packages:    [
       {
       name: "User_Data",
       qualified_name: "SDL.Video.Surfaces.User_Data",
       signature: "sdl.video.surfaces.user_data",
       enclosing: "sdl.video.surfaces",
       is_private: false,
       documentation: "",
       documentation_snippet: "",
       }   ,
   ]
,simple_types:    [
       {
       name: "Colour_Masks",
       qualified_name: "SDL.Video.Surfaces.Colour_Masks",
       signature: "sdl.video.surfaces.colour_masks",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Colour_Masks is mod 2 ** 32 with\n  Convention => C;",
       }   ,
       {
       name: "Internal_Surface",
       qualified_name: "SDL.Video.Surfaces.Internal_Surface",
       signature: "sdl.video.surfaces.internal_surface",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Internal_Surface is private;",
       }   ,
       {
       name: "Pixel_Depths",
       qualified_name: "SDL.Video.Surfaces.Pixel_Depths",
       signature: "sdl.video.surfaces.pixel_depths",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Pixel_Depths is new Positive with\n  Convention       => C,\n  Static_Predicate => Pixel_Depths in 1 | 2 | 4 | 8 | 12 | 15 | 16 | 24 | 32;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Surface",
       qualified_name: "SDL.Video.Surfaces.Surface",
       signature: "sdl.video.surfaces.surface",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Surface is new Ada.Finalization.Controlled with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Internal_Surface_Pointer",
       qualified_name: "SDL.Video.Surfaces.Internal_Surface_Pointer",
       signature: "sdl.video.surfaces.internal_surface_pointer",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Internal_Surface_Pointer is access Internal_Surface with\n  Convention => C;",
       }   ,
   ]
,constants:    [
       {
       name: "Null_Surface",
       qualified_name: "SDL.Video.Surfaces.Null_Surface",
       signature: "sdl.video.surfaces.null_surface",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Null_Surface : constant Surface;",
       }   ,
   ]
,}
---
