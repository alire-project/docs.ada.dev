---
crate: mathpaqs
layout: gnatdoc
gnatdoc: {
name: "Frac",
qualified_name: "Frac",
signature: "frac",
enclosing: "",
is_private: false,
documentation: "----------------------------------------------------------------------------
documentation_snippet: "",
record_types:    [
       {
       name: "frac_elt",
       qualified_name: "Frac.frac_elt",
       signature: "frac.frac_elt",
       enclosing: "",
       is_private: false,
       documentation: "\n@field a\n@field b\n  define fraction
       documentation_snippet: "type frac_elt is record a,b:ring_elt; end record;",
       }   ,
   ]
,constants:    [
       {
       name: "frac_0",
       qualified_name: "Frac.frac_0",
       signature: "frac.frac_0",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "frac_0: constant frac_elt:= (zero,one);",
       }   ,
       {
       name: "frac_1",
       qualified_name: "Frac.frac_1",
       signature: "frac.frac_1",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "frac_1: constant frac_elt:= (one,one);",
       }   ,
   ]
,}
---