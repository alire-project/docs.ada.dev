---
crate: sdlada
layout: gnatdoc
gnatdoc: {
name: "SDL.Video.Rectangles",
qualified_name: "SDL.Video.Rectangles",
signature: "sdl.video.rectangles",
enclosing: "sdl.video",
is_private: false,
documentation: "",
documentation_snippet: "",
array_types:    [
       {
       name: "Line_Arrays",
       qualified_name: "SDL.Video.Rectangles.Line_Arrays",
       signature: "sdl.video.rectangles.line_arrays",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Line_Arrays is array (C.size_t range <>) of aliased Line_Segment with\n  Convention => C;",
       }   ,
       {
       name: "Point_Arrays",
       qualified_name: "SDL.Video.Rectangles.Point_Arrays",
       signature: "sdl.video.rectangles.point_arrays",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Point_Arrays is array (C.size_t range <>) of aliased Point with\n  Convention => C;",
       }   ,
       {
       name: "Rectangle_Arrays",
       qualified_name: "SDL.Video.Rectangles.Rectangle_Arrays",
       signature: "sdl.video.rectangles.rectangle_arrays",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Rectangle_Arrays is array (C.size_t range <>) of aliased Rectangle with\n  Convention => C;",
       }   ,
       {
       name: "Size_Arrays",
       qualified_name: "SDL.Video.Rectangles.Size_Arrays",
       signature: "sdl.video.rectangles.size_arrays",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Size_Arrays is array (C.size_t range <>) of aliased SDL.Sizes with\n  Convention => C;",
       }   ,
   ]
,record_types:    [
       {
       name: "Line_Segment",
       qualified_name: "SDL.Video.Rectangles.Line_Segment",
       signature: "sdl.video.rectangles.line_segment",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Line_Segment is\n   record\n      Start  : SDL.Coordinates;\n      Finish : SDL.Coordinates;\n   end record with\n  Convention => C;",
       }   ,
       {
       name: "Rectangle",
       qualified_name: "SDL.Video.Rectangles.Rectangle",
       signature: "sdl.video.rectangles.rectangle",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Rectangle is\n   record\n      X      : SDL.Coordinate;\n      Y      : SDL.Coordinate;\n      Width  : SDL.Natural_Dimension;\n      Height : SDL.Natural_Dimension;\n   end record with\n  Convention => C;",
       }   ,
   ]
,access_types:    [
       {
       name: "Rectangle_Access",
       qualified_name: "SDL.Video.Rectangles.Rectangle_Access",
       signature: "sdl.video.rectangles.rectangle_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Rectangle_Access is access all Rectangle with\n  Convention => C;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Point",
       qualified_name: "SDL.Video.Rectangles.Point",
       signature: "sdl.video.rectangles.point",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Point is SDL.Coordinates;",
       }   ,
   ]
,constants:    [
       {
       name: "Null_Rectangle",
       qualified_name: "SDL.Video.Rectangles.Null_Rectangle",
       signature: "sdl.video.rectangles.null_rectangle",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Null_Rectangle : constant Rectangle := (others => 0);",
       }   ,
   ]
,}
---
