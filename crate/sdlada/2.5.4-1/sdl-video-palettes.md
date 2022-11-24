---
crate: sdlada
layout: gnatdoc
gnatdoc: {
name: "SDL.Video.Palettes",
qualified_name: "SDL.Video.Palettes",
signature: "sdl.video.palettes",
enclosing: "sdl.video",
is_private: false,
documentation: "------------------------------------------------------------------------------------------------------------------\n  Copyright (c) 2013-2020, Luke A. Guest\n\n  This software is provided 'as-is', without any express or implied\n  warranty. In no event will the authors be held liable for any damages\n  arising from the use of this software.\n\n  Permission is granted to anyone to use this software for any purpose,\n  including commercial applications, and to alter it and redistribute it\n  freely, subject to the following restrictions:\n\n     1. The origin of this software must not be misrepresented; you must not\n     claim that you wrote the original software. If you use this software\n     in a product, an acknowledgment in the product documentation would be\n     appreciated but is not required.\n\n     2. Altered source versions must be plainly marked as such, and must not be\n     misrepresented as being the original software.\n\n     3. This notice may not be removed or altered from any source\n     distribution.\n------------------------------------------------------------------------------------------------------------------\n  SDL.Video.Palettes\n\n  Palettes, colours and various conversions.\n------------------------------------------------------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Colour_Component",
       qualified_name: "SDL.Video.Palettes.Colour_Component",
       signature: "sdl.video.palettes.colour_component",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Colour_Component is range 0 .. 255 with\n  Size       => 8,\n  Convention => C;",
       }   ,
       {
       name: "Cursor",
       qualified_name: "SDL.Video.Palettes.Cursor",
       signature: "sdl.video.palettes.cursor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Cursor is private;",
       }   ,
   ]
,record_types:    [
       {
       name: "Colour",
       qualified_name: "SDL.Video.Palettes.Colour",
       signature: "sdl.video.palettes.colour",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Colour is\n   record\n      Red   : Colour_Component := Colour_Component'First;\n      Green : Colour_Component := Colour_Component'First;\n      Blue  : Colour_Component := Colour_Component'First;\n      Alpha : Colour_Component := Colour_Component'First;\n   end record with\n  Convention => C_Pass_by_Copy,\n  Size       => Colour_Component'Size * 4;",
       }   ,
       {
       name: "RGB_Colour",
       qualified_name: "SDL.Video.Palettes.RGB_Colour",
       signature: "sdl.video.palettes.rgb_colour",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type RGB_Colour is\n   record\n      Red   : Colour_Component := Colour_Component'First;\n      Green : Colour_Component := Colour_Component'First;\n      Blue  : Colour_Component := Colour_Component'First;\n   end record with\n  Convention => C_Pass_by_Copy,\n  Size       => Colour_Component'Size * 4;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Palette",
       qualified_name: "SDL.Video.Palettes.Palette",
       signature: "sdl.video.palettes.palette",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Palette is tagged limited private with\n  Default_Iterator  => Iterate,\n  Iterator_Element  => Colour,\n  Constant_Indexing => Constant_Reference;",
       }   ,
   ]
,access_types:    [
       {
       name: "Palette_Access",
       qualified_name: "SDL.Video.Palettes.Palette_Access",
       signature: "sdl.video.palettes.palette_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Palette_Access is access Palette;",
       }   ,
   ]
,constants:    [
       {
       name: "Empty_Palette",
       qualified_name: "SDL.Video.Palettes.Empty_Palette",
       signature: "sdl.video.palettes.empty_palette",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Empty_Palette : constant Palette;",
       }   ,
       {
       name: "No_Element",
       qualified_name: "SDL.Video.Palettes.No_Element",
       signature: "sdl.video.palettes.no_element",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Element : constant Cursor;",
       }   ,
       {
       name: "Null_Colour",
       qualified_name: "SDL.Video.Palettes.Null_Colour",
       signature: "sdl.video.palettes.null_colour",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Null_Colour : constant Colour := (others => <>);",
       }   ,
       {
       name: "Null_RGB_Colour",
       qualified_name: "SDL.Video.Palettes.Null_RGB_Colour",
       signature: "sdl.video.palettes.null_rgb_colour",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Null_RGB_Colour : constant RGB_Colour := (others => <>);",
       }   ,
   ]
,}
---
