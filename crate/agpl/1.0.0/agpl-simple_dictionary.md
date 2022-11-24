---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Simple_Dictionary",
qualified_name: "Agpl.Simple_Dictionary",
signature: "agpl.simple_dictionary",
enclosing: "agpl",
is_private: false,
documentation: "----------------------------------------------------------------------\n Object                                                             --\n----------------------------------------------------------------------\n\n@formal Element_Type\n@formal Equal",
documentation_snippet: "",
simple_types:    [
       {
       name: "Object",
       qualified_name: "Agpl.Simple_Dictionary.Object",
       signature: "agpl.simple_dictionary.object",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Object is private;",
       }   ,
   ]
,array_types:    [
       {
       name: "Pair_Array",
       qualified_name: "Agpl.Simple_Dictionary.Pair_Array",
       signature: "agpl.simple_dictionary.pair_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Pair_Array is array (Positive range <>) of Pairs;",
       }   ,
   ]
,record_types:    [
       {
       name: "Pairs",
       qualified_name: "Agpl.Simple_Dictionary.Pairs",
       signature: "agpl.simple_dictionary.pairs",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Pairs is record\n   Key   : Ustring;\n   Value : Element_Type;\nend record;",
       }   ,
   ]
,}
---
