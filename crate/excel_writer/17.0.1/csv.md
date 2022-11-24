---
crate: excel_writer
layout: gnatdoc
gnatdoc: {
name: "CSV",
qualified_name: "CSV",
signature: "csv",
enclosing: "",
is_private: false,
documentation: "Freeware, author: J-P. Rosen, http://www.adalog.fr/",
documentation_snippet: "",
array_types:    [
       {
       name: "Fields_Bounds",
       qualified_name: "CSV.Fields_Bounds",
       signature: "csv.fields_bounds",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Fields_Bounds is array (Positive range <>) of Bounds;",
       }   ,
   ]
,record_types:    [
       {
       name: "Bounds",
       qualified_name: "CSV.Bounds",
       signature: "csv.bounds",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Bounds is\n   record\n      Start : Positive;\n      Stop  : Natural;\n   end record;",
       }   ,
   ]
,}
---
