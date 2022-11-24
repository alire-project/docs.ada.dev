---
crate: iterators
layout: gnatdoc
gnatdoc: {
name: "Iterators.From.Elements",
qualified_name: "Iterators.From.Elements",
signature: "iterators.from.elements",
enclosing: "iterators.from",
is_private: false,
documentation: "When instantiating from an element type, we get full control of further\ninstances and we can also mix container types.\n\n@formal Any_Element",
documentation_snippet: "",
subtypes:    [
       {
       name: "Iterator",
       qualified_name: "Iterators.From.Elements.Iterator",
       signature: "iterators.from.elements.iterator",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Iterator is Iterators.Iterator;",
       }   ,
       {
       name: "Operator",
       qualified_name: "Iterators.From.Elements.Operator",
       signature: "iterators.from.elements.operator",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Operator is Operators.Operator;",
       }   ,
       {
       name: "Sequence",
       qualified_name: "Iterators.From.Elements.Sequence",
       signature: "iterators.from.elements.sequence",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Sequence is Operators.Chain;",
       }   ,
   ]
,}
---
