---
crate: openglada
layout: gnatdoc
gnatdoc: {
name: "GL.Types.Colors",
qualified_name: "GL.Types.Colors",
signature: "gl.types.colors",
enclosing: "gl.types",
is_private: false,
documentation: "part of OpenGLAda, (c) 2017 Felix Krause\nreleased under the terms of the MIT license, see the file \"COPYING\"",
documentation_snippet: "",
simple_types:    [
       {
       name: "Color_Index",
       qualified_name: "GL.Types.Colors.Color_Index",
       signature: "gl.types.colors.color_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Color_Index is (R, G, B, A);",
       }   ,
   ]
,array_types:    [
       {
       name: "Basic_Color",
       qualified_name: "GL.Types.Colors.Basic_Color",
       signature: "gl.types.colors.basic_color",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Basic_Color is array (Basic_Color_Index) of Component;",
       }   ,
       {
       name: "Basic_Color_Array",
       qualified_name: "GL.Types.Colors.Basic_Color_Array",
       signature: "gl.types.colors.basic_color_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Basic_Color_Array is array (Size range <>) of aliased Basic_Color;",
       }   ,
       {
       name: "Color",
       qualified_name: "GL.Types.Colors.Color",
       signature: "gl.types.colors.color",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Color is array (Color_Index) of aliased Component;",
       }   ,
       {
       name: "Color_Array",
       qualified_name: "GL.Types.Colors.Color_Array",
       signature: "gl.types.colors.color_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Color_Array is array (Size range <>) of aliased Color;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Basic_Color_Index",
       qualified_name: "GL.Types.Colors.Basic_Color_Index",
       signature: "gl.types.colors.basic_color_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Basic_Color_Index is Color_Index range R .. B;",
       }   ,
       {
       name: "Component",
       qualified_name: "GL.Types.Colors.Component",
       signature: "gl.types.colors.component",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Component is Single range 0.0 .. 1.0;",
       }   ,
   ]
,}
---
