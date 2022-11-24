---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Containers.Naked_Vectors",
qualified_name: "Agpl.Containers.Naked_Vectors",
signature: "agpl.containers.naked_vectors",
enclosing: "agpl.containers",
is_private: false,
documentation: "Package for unbounded vectors, integer-indexed\nSimilar to the one in the standard library, but exposes the internal vector.\nSo it's a bit unsafer, but also eficienter.\n\n@formal Item_type\n@formal Initial_size\n@formal Grow_factor",
documentation_snippet: "",
simple_types:    [
       {
       name: "Sides",
       qualified_name: "Agpl.Containers.Naked_Vectors.Sides",
       signature: "agpl.containers.naked_vectors.sides",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Sides is (Start, Ending);",
       }   ,
   ]
,array_types:    [
       {
       name: "Item_array",
       qualified_name: "Agpl.Containers.Naked_Vectors.Item_array",
       signature: "agpl.containers.naked_vectors.item_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Item_array is array (Integer range <>) of Item_type;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Object",
       qualified_name: "Agpl.Containers.Naked_Vectors.Object",
       signature: "agpl.containers.naked_vectors.object",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Object (First : Integer) is new Proto_object with private;",
       }   ,
       {
       name: "Proto_object",
       qualified_name: "Agpl.Containers.Naked_Vectors.Proto_object",
       signature: "agpl.containers.naked_vectors.proto_object",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Proto_object (First : Integer) is new Finalization.Controlled with\n   record\n      Vector : Item_array_access;\n   end record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Item_array_access",
       qualified_name: "Agpl.Containers.Naked_Vectors.Item_array_access",
       signature: "agpl.containers.naked_vectors.item_array_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Item_array_access is access all Item_array;",
       }   ,
   ]
,}
---
