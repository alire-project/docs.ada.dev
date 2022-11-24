---
crate: ayacc
layout: gnatdoc
gnatdoc: {
name: "STR_Pack",
qualified_name: "STR_Pack",
signature: "str_pack",
enclosing: "",
is_private: false,
documentation: "This package contains the type declarations and procedures\nfor the minimal string minipulation needed by ayacc.",
documentation_snippet: "",
simple_types:    [
       {
       name: "STR",
       qualified_name: "STR_Pack.STR",
       signature: "str_pack.str",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type STR(Maximum_Length : Index) is limited private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Index",
       qualified_name: "STR_Pack.Index",
       signature: "str_pack.index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Index is Integer range 0 .. Maximum;",
       }   ,
   ]
,constants:    [
       {
       name: "Maximum",
       qualified_name: "STR_Pack.Maximum",
       signature: "str_pack.maximum",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Maximum : constant := 1024;",
       }   ,
   ]
,}
---
