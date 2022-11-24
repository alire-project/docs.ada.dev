---
crate: yeison
layout: gnatdoc
gnatdoc: {
name: "Yeison_Multi",
qualified_name: "Yeison_Multi",
signature: "yeison_multi",
enclosing: "",
is_private: false,
documentation: "",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Any",
       qualified_name: "Yeison_Multi.Any",
       signature: "yeison_multi.any",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Any is tagged private;",
       }   ,
       {
       name: "Map",
       qualified_name: "Yeison_Multi.Map",
       signature: "yeison_multi.map",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Map is tagged private with\n  Aggregate => (Empty => Empty,\n                Add_Named => Insert);",
       }   ,
       {
       name: "Scalar",
       qualified_name: "Yeison_Multi.Scalar",
       signature: "yeison_multi.scalar",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Scalar is tagged private with\n  Integer_Literal => To_Int,\n  String_Literal => To_Str;",
       }   ,
   ]
,}
---
