---
crate: langkit_support
layout: gnatdoc
gnatdoc: {
name: "Langkit_Support.Types",
qualified_name: "Langkit_Support.Types",
signature: "langkit_support.types",
enclosing: "langkit_support",
is_private: false,
documentation: "Provide miscellaneous types to Langkit-generated libraries",
documentation_snippet: "",
simple_types:    [
       {
       name: "Comparison_Relation",
       qualified_name: "Langkit_Support.Types.Comparison_Relation",
       signature: "langkit_support.types.comparison_relation",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Comparison_Relation is\n  (Less_Than, Less_Or_Equal, Greater_Than, Greater_Or_Equal);",
       }   ,
       {
       name: "Version_Number",
       qualified_name: "Langkit_Support.Types.Version_Number",
       signature: "langkit_support.types.version_number",
       enclosing: "",
       is_private: false,
       documentation: "Number associated to a resource. This number is supposed to be unique\nfor some class of resource. For instance unique in all analysis contexts\na process creates.",
       documentation_snippet: "type Version_Number is new Interfaces.Unsigned_64;",
       }   ,
   ]
,}
---
