---
crate: asfml
layout: gnatdoc
gnatdoc: {
name: "Sf.Window.VideoMode",
qualified_name: "Sf.Window.VideoMode",
signature: "sf.window.videomode",
enclosing: "sf.window",
is_private: false,
documentation: "//////////////////////////////////////////////////////////\n/ @brief sfVideoMode defines a video mode (width, height, bpp, frequency)\n/        and provides functions for getting modes supported\n/        by the display device\n/\n//////////////////////////////////////////////////////////\n/< Video mode width, in pixels\n/< Video mode height, in pixels\n/< Video mode pixel depth, in bits per pixels",
documentation_snippet: "",
record_types:    [
       {
       name: "sfVideoMode",
       qualified_name: "Sf.Window.VideoMode.sfVideoMode",
       signature: "sf.window.videomode.sfvideomode",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfVideoMode is record\n   width : aliased sfUint32;\n   height : aliased sfUint32;\n   bitsPerPixel : aliased sfUint32;\nend record;",
       }   ,
   ]
,}
---
