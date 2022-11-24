---
crate: openglada
layout: gnatdoc
gnatdoc: {
name: "GL.Matrices",
qualified_name: "GL.Matrices",
signature: "gl.matrices",
enclosing: "gl",
is_private: false,
documentation: "this matrix is column-major (i.e. the first index defines the column,\nthe second index defines the row).\nthis is important for interoperability with GLSL.\n\n@formal Index_Type\n@formal Element_Type\n@formal \"+\"\n@formal \"-\"\n@formal \"-\"\n@formal \"*\"\n   not needed currently\n  with function \"/\" (Left, Right : Element_Type) return Element_Type is <>;\n@formal Vector_Type",
documentation_snippet: "",
array_types:    [
       {
       name: "Matrix",
       qualified_name: "GL.Matrices.Matrix",
       signature: "gl.matrices.matrix",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Matrix is array (Index_Type, Index_Type) of aliased Element_Type;",
       }   ,
   ]
,}
---
