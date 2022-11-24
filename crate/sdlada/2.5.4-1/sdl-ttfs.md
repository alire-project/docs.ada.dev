---
crate: sdlada
layout: gnatdoc
gnatdoc: {
name: "SDL.TTFs",
qualified_name: "SDL.TTFs",
signature: "sdl.ttfs",
enclosing: "sdl",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Font_Faces",
       qualified_name: "SDL.TTFs.Font_Faces",
       signature: "sdl.ttfs.font_faces",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Font_Faces is range 0 .. C.long'Last with\n  Size       => C.long'Size,\n  Convention => C;",
       }   ,
       {
       name: "Font_Hints",
       qualified_name: "SDL.TTFs.Font_Hints",
       signature: "sdl.ttfs.font_hints",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Font_Hints is (Normal, Light, Mono, None) with\n  Convention => C;",
       }   ,
       {
       name: "Font_Measurements",
       qualified_name: "SDL.TTFs.Font_Measurements",
       signature: "sdl.ttfs.font_measurements",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Font_Measurements is range 0 .. C.int'Last with\n  Size       => C.int'Size,\n  Convention => C;",
       }   ,
       {
       name: "Font_Outlines",
       qualified_name: "SDL.TTFs.Font_Outlines",
       signature: "sdl.ttfs.font_outlines",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Font_Outlines is range 0 .. C.int'Last with\n  Size       => C.int'Size,\n  Convention => C;",
       }   ,
       {
       name: "Font_Styles",
       qualified_name: "SDL.TTFs.Font_Styles",
       signature: "sdl.ttfs.font_styles",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Font_Styles is mod 2 ** 32 with\n  Convention => C;",
       }   ,
       {
       name: "Point_Sizes",
       qualified_name: "SDL.TTFs.Point_Sizes",
       signature: "sdl.ttfs.point_sizes",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Point_Sizes is new C.int;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Fonts",
       qualified_name: "SDL.TTFs.Fonts",
       signature: "sdl.ttfs.fonts",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Fonts is new Ada.Finalization.Controlled with private;",
       }   ,
   ]
,constants:    [
       {
       name: "Null_Font",
       qualified_name: "SDL.TTFs.Null_Font",
       signature: "sdl.ttfs.null_font",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Null_Font : constant Fonts;",
       }   ,
       {
       name: "Outlines_Off",
       qualified_name: "SDL.TTFs.Outlines_Off",
       signature: "sdl.ttfs.outlines_off",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Outlines_Off : constant Font_Outlines := Font_Outlines'First;",
       }   ,
       {
       name: "Style_Bold",
       qualified_name: "SDL.TTFs.Style_Bold",
       signature: "sdl.ttfs.style_bold",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Style_Bold           : constant Font_Styles := 16#0000_0001#;",
       }   ,
       {
       name: "Style_Italic",
       qualified_name: "SDL.TTFs.Style_Italic",
       signature: "sdl.ttfs.style_italic",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Style_Italic         : constant Font_Styles := 16#0000_0002#;",
       }   ,
       {
       name: "Style_Normal",
       qualified_name: "SDL.TTFs.Style_Normal",
       signature: "sdl.ttfs.style_normal",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Style_Normal         : constant Font_Styles := 16#0000_0000#;",
       }   ,
       {
       name: "Style_Strike_Through",
       qualified_name: "SDL.TTFs.Style_Strike_Through",
       signature: "sdl.ttfs.style_strike_through",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Style_Strike_Through : constant Font_Styles := 16#0000_0008#;",
       }   ,
       {
       name: "Style_Underline",
       qualified_name: "SDL.TTFs.Style_Underline",
       signature: "sdl.ttfs.style_underline",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Style_Underline      : constant Font_Styles := 16#0000_0004#;",
       }   ,
   ]
,}
---