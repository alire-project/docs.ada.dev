---
crate: rxada
layout: gnatdoc
gnatdoc: {
name: "Rx.Impl.Transformers",
qualified_name: "Rx.Impl.Transformers",
signature: "rx.impl.transformers",
enclosing: "rx.impl",
is_private: false,
documentation: "",
documentation_snippet: "",
packages:    [
       {
       name: "Linkers",
       qualified_name: "Rx.Impl.Transformers.Linkers",
       signature: "rx.impl.transformers.linkers",
       enclosing: "rx.impl.transformers",
       is_private: false,
       documentation: "",
       documentation_snippet: "",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Operator",
       qualified_name: "Rx.Impl.Transformers.Operator",
       signature: "rx.impl.transformers.operator",
       enclosing: "",
       is_private: false,
       documentation: "This is the fundamental type that bridges observables y observers doing something along the way\nOverride the Observer/Subscriber inherited methods in new operators",
       documentation_snippet: "type Operator is new\n  Links.Downstream and\n  Into.Contracts.Observable and\n  From.Contracts.Observer and\n  From.Contracts.subscriber\nwith private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "From_Observable",
       qualified_name: "Rx.Impl.Transformers.From_Observable",
       signature: "rx.impl.transformers.from_observable",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype From_Observable is From.Observable'Class;",
       }   ,
       {
       name: "Into_Observable",
       qualified_name: "Rx.Impl.Transformers.Into_Observable",
       signature: "rx.impl.transformers.into_observable",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Into_Observable is Into.Observable'Class;",
       }   ,
   ]
,}
---
