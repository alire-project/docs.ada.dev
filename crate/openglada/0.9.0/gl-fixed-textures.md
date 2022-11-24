---
crate: openglada
layout: gnatdoc
gnatdoc: {
name: "GL.Fixed.Textures",
qualified_name: "GL.Fixed.Textures",
signature: "gl.fixed.textures",
enclosing: "gl.fixed",
is_private: false,
documentation: "part of OpenGLAda, (c) 2017 Felix Krause\nreleased under the terms of the MIT license, see the file \"COPYING\"",
documentation_snippet: "",
simple_types:    [
       {
       name: "Combine_Function",
       qualified_name: "GL.Fixed.Textures.Combine_Function",
       signature: "gl.fixed.textures.combine_function",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Combine_Function is (Add, Replace, Modulate, Subtract, Add_Signed,\n                          Interpolate, Dot3_RGB, Dot3_RGBA);",
       }   ,
       {
       name: "Source_Index",
       qualified_name: "GL.Fixed.Textures.Source_Index",
       signature: "gl.fixed.textures.source_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Source_Index is range 0 .. 2;",
       }   ,
       {
       name: "Source_Kind",
       qualified_name: "GL.Fixed.Textures.Source_Kind",
       signature: "gl.fixed.textures.source_kind",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Source_Kind is (Texture, Constant_Src, Primary_Color, Previous);",
       }   ,
       {
       name: "Texture_Function",
       qualified_name: "GL.Fixed.Textures.Texture_Function",
       signature: "gl.fixed.textures.texture_function",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Texture_Function is (Add, Blend, Replace, Modulate, Decal, Combine);",
       }   ,
   ]
,subtypes:    [
       {
       name: "Alpha_Combine_Function",
       qualified_name: "GL.Fixed.Textures.Alpha_Combine_Function",
       signature: "gl.fixed.textures.alpha_combine_function",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Alpha_Combine_Function is Combine_Function range Add .. Interpolate;",
       }   ,
       {
       name: "Scaling_Factor",
       qualified_name: "GL.Fixed.Textures.Scaling_Factor",
       signature: "gl.fixed.textures.scaling_factor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Scaling_Factor is Double range 1.0 .. 4.0;",
       }   ,
   ]
,}
---
