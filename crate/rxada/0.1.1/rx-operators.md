---
crate: rxada
layout: gnatdoc
gnatdoc: {
name: "Rx.Operators",
qualified_name: "Rx.Operators",
signature: "rx.operators",
enclosing: "rx",
is_private: false,
documentation: "This package seems unnecessary but by separating it from Transform we can too separate each operator\nimplementation classes in its own packages, just like with Typed/Observables hierarchy.",
documentation_snippet: "",
packages:    [
       {
       name: "Counters",
       qualified_name: "Rx.Operators.Counters",
       signature: "rx.operators.counters",
       enclosing: "rx.operators",
       is_private: false,
       documentation: "------------\n Counters --\n------------\n\n@formal Succ\n@formal Default_Initial_Count",
       documentation_snippet: "",
       }   ,
       {
       name: "Linkers",
       qualified_name: "Rx.Operators.Linkers",
       signature: "rx.operators.linkers",
       enclosing: "rx.operators",
       is_private: false,
       documentation: "Analog to the one in Observables",
       documentation_snippet: "",
       }   ,
   ]
,subtypes:    [
       {
       name: "Operator",
       qualified_name: "Rx.Operators.Operator",
       signature: "rx.operators.operator",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Operator Is Typed.Operator'Class;",
       }   ,
   ]
,}
---
