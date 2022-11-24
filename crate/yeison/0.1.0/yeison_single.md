---
crate: yeison
layout: gnatdoc
gnatdoc: {
name: "Yeison_Single",
qualified_name: "Yeison_Single",
signature: "yeison_single",
enclosing: "",
is_private: false,
documentation: "",
documentation_snippet: "",
packages:    [
       {
       name: "Operators",
       qualified_name: "Yeison_Single.Operators",
       signature: "yeison_single.operators",
       enclosing: "yeison_single",
       is_private: false,
       documentation: "",
       documentation_snippet: "",
       }   ,
   ]
,simple_types:    [
       {
       name: "Vec_Aux",
       qualified_name: "Yeison_Single.Vec_Aux",
       signature: "yeison_single.vec_aux",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Vec_Aux is private with\n  Aggregate => (Empty => Empty,\n                Add_Unnamed => Append);",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Any",
       qualified_name: "Yeison_Single.Any",
       signature: "yeison_single.any",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Any is tagged private with\n  Integer_Literal   => To_Int,\n  Real_Literal      => To_Real,\n  String_Literal    => To_String,\n  Constant_Indexing => Constant_Reference,\n  Aggregate => (Empty     => Empty,\n                Add_Named => Insert);",
       }   ,
   ]
,subtypes:    [
       {
       name: "Text",
       qualified_name: "Yeison_Single.Text",
       signature: "yeison_single.text",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Text is String;",
       }   ,
   ]
,}
---
