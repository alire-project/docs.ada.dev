---
crate: mathpaqs
layout: gnatdoc
gnatdoc: {
name: "Frac_euclid",
qualified_name: "Frac_euclid",
signature: "frac_euclid",
enclosing: "",
is_private: false,
documentation: "----------------------------------------------------------------------------\n  File:            frac_euclid.ads\n  Description:     Generic package, gives back the field of quotients of an\n                     euclidean ring (i.e. a ring with division; this allows\n                     for *reduction* of fractions)\n  Date/version:    22-Dec-1996\n  Author:          Gautier de Montmollin\n                   http://gautiersblog.blogspot.com/\n----------------------------------------------------------------------------\n\n@formal ring_elt\n  ring element type\n@formal zero\n  0 and 1 elements\n@formal one\n  0 and 1 elements\n@formal \"-\"\n  unary oper.\n@formal \"+\"\n  binary oper.\n@formal \"-\"\n@formal \"*\"\n@formal \"/\"\n  returns the quotient:  a= b*q + r\n  q:quotient, r:rest",
documentation_snippet: "",
record_types:    [
       {
       name: "frac_elt",
       qualified_name: "Frac_euclid.frac_elt",
       signature: "frac_euclid.frac_elt",
       enclosing: "",
       is_private: false,
       documentation: "\n@field a\n@field b\n  define fraction",
       documentation_snippet: "type frac_elt is record a,b:ring_elt; end record;",
       }   ,
   ]
,constants:    [
       {
       name: "frac_0",
       qualified_name: "Frac_euclid.frac_0",
       signature: "frac_euclid.frac_0",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "frac_0: constant frac_elt:= (zero,one);",
       }   ,
       {
       name: "frac_1",
       qualified_name: "Frac_euclid.frac_1",
       signature: "frac_euclid.frac_1",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "frac_1: constant frac_elt:= (one,one);",
       }   ,
   ]
,variables:    [
       {
       name: "auto_reduce",
       qualified_name: "Frac_euclid.auto_reduce",
       signature: "frac_euclid.auto_reduce",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "auto_reduce: Boolean:= True;",
       }   ,
       {
       name: "reduce_in_add",
       qualified_name: "Frac_euclid.reduce_in_add",
       signature: "frac_euclid.reduce_in_add",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "reduce_in_add: Boolean:= True;",
       }   ,
   ]
,}
---
