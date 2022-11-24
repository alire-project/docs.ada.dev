---
crate: asfml
layout: gnatdoc
gnatdoc: {
name: "Sf.Graphics.Transform",
qualified_name: "Sf.Graphics.Transform",
signature: "sf.graphics.transform",
enclosing: "sf.graphics",
is_private: false,
documentation: "//////////////////////////////////////////////////////////\n/ @brief Encapsulate a 3x3 transform matrix\n/\n//////////////////////////////////////////////////////////",
documentation_snippet: "",
array_types:    [
       {
       name: "sfTransform_matrix_array",
       qualified_name: "Sf.Graphics.Transform.sfTransform_matrix_array",
       signature: "sf.graphics.transform.sftransform_matrix_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfTransform_matrix_array is array (0 .. 8) of aliased float;",
       }   ,
   ]
,record_types:    [
       {
       name: "sfTransform",
       qualified_name: "Sf.Graphics.Transform.sfTransform",
       signature: "sf.graphics.transform.sftransform",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfTransform is record\n   matrix : aliased sfTransform_matrix_array;\nend record;",
       }   ,
   ]
,constants:    [
       {
       name: "Identity",
       qualified_name: "Sf.Graphics.Transform.Identity",
       signature: "sf.graphics.transform.identity",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Identity : aliased constant sfTransform;",
       }   ,
   ]
,}
---
