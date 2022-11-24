---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Containers.Indefinite_Matrix2d",
qualified_name: "Agpl.Containers.Indefinite_Matrix2d",
signature: "agpl.containers.indefinite_matrix2d",
enclosing: "agpl.containers",
is_private: false,
documentation: "This is a sparse 2D matrix\nCare has been taken to make this type as efficient as possible given\nthe Ada.Containers it internally uses.\nThis type is *not* thread-safe.\n\n@formal Index\n@formal Value\n@formal \"<\"",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Matrix",
       qualified_name: "Agpl.Containers.Indefinite_Matrix2d.Matrix",
       signature: "agpl.containers.indefinite_matrix2d.matrix",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Matrix is tagged private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Index_Vector",
       qualified_name: "Agpl.Containers.Indefinite_Matrix2d.Index_Vector",
       signature: "agpl.containers.indefinite_matrix2d.index_vector",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Index_Vector is Index_Vectors.Vector;",
       }   ,
   ]
,}
---
