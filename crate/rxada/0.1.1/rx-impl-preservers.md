---
crate: rxada
layout: gnatdoc
gnatdoc: {
name: "Rx.Impl.Preservers",
qualified_name: "Rx.Impl.Preservers",
signature: "rx.impl.preservers",
enclosing: "rx.impl",
is_private: false,
documentation: "Specialized Transform, but with type preservation\nA separate package is convenient to allow independent package files for this kind of operators",
documentation_snippet: "",
subtypes:    [
       {
       name: "Observable",
       qualified_name: "Rx.Impl.Preservers.Observable",
       signature: "rx.impl.preservers.observable",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Observable is Typed.Observable'Class;",
       }   ,
       {
       name: "Observer",
       qualified_name: "Rx.Impl.Preservers.Observer",
       signature: "rx.impl.preservers.observer",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Observer   is Typed.Observer'Class;",
       }   ,
       {
       name: "Operator",
       qualified_name: "Rx.Impl.Preservers.Operator",
       signature: "rx.impl.preservers.operator",
       enclosing: "",
       is_private: false,
       documentation: "Specialization of the Transformer type",
       documentation_snippet: "subtype Operator is Transform.Operator;",
       }   ,
       {
       name: "T",
       qualified_name: "Rx.Impl.Preservers.T",
       signature: "rx.impl.preservers.t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype T          is Typed.Type_Traits.T;",
       }   ,
   ]
,}
---
