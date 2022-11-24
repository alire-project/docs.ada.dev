---
crate: openglada
layout: gnatdoc
gnatdoc: {
name: "GL",
qualified_name: "GL",
signature: "gl",
enclosing: "",
is_private: false,
documentation: "part of OpenGLAda, (c) 2017 Felix Krause\nreleased under the terms of the MIT license, see the file \"COPYING\"",
documentation_snippet: "",
simple_types:    [
       {
       name: "Index_Homogeneous",
       qualified_name: "GL.Index_Homogeneous",
       signature: "gl.index_homogeneous",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Index_Homogeneous is (X, Y, Z, W);",
       }   ,
   ]
,subtypes:    [
       {
       name: "Index_2D",
       qualified_name: "GL.Index_2D",
       signature: "gl.index_2d",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Index_2D is Index_Homogeneous range X .. Y;",
       }   ,
       {
       name: "Index_3D",
       qualified_name: "GL.Index_3D",
       signature: "gl.index_3d",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Index_3D is Index_Homogeneous range X .. Z;",
       }   ,
   ]
,}
---
