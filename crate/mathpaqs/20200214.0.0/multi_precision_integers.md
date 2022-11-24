---
crate: mathpaqs
layout: gnatdoc
gnatdoc: {
name: "Multi_precision_integers",
qualified_name: "Multi_precision_integers",
signature: "multi_precision_integers",
enclosing: "",
is_private: false,
documentation: "Integers for array indexing --",
documentation_snippet: "",
simple_types:    [
       {
       name: "Multi_int",
       qualified_name: "Multi_precision_integers.Multi_int",
       signature: "multi_precision_integers.multi_int",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Multi_int (n: Index_int) is private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Basic_int",
       qualified_name: "Multi_precision_integers.Basic_int",
       signature: "multi_precision_integers.basic_int",
       enclosing: "",
       is_private: false,
       documentation: "the \"normal\" signed integer",
       documentation_snippet: "subtype Basic_int is Integer;",
       }   ,
       {
       name: "Index_int",
       qualified_name: "Multi_precision_integers.Index_int",
       signature: "multi_precision_integers.index_int",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Index_int is Integer;",
       }   ,
   ]
,constants:    [
       {
       name: "Debug",
       qualified_name: "Multi_precision_integers.Debug",
       signature: "multi_precision_integers.debug",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Debug : constant Boolean:= False;",
       }   ,
   ]
,}
---
