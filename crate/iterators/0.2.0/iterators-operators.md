---
crate: iterators
layout: gnatdoc
gnatdoc: {
name: "Iterators.Operators",
qualified_name: "Iterators.Operators",
signature: "iterators.operators",
enclosing: "iterators",
is_private: false,
documentation: "Operators are chainable functions (monads) that take an iterator and\nreturn another iterator. The ones in this package transform the type\nthey take into the one they generate. Thus, using any of these operators\nproduces a read-only sequence, since the root container cursor cannot be\npreserved.",
documentation_snippet: "",
packages:    [
       {
       name: "Linking",
       qualified_name: "Iterators.Operators.Linking",
       signature: "iterators.operators.linking",
       enclosing: "iterators.operators",
       is_private: false,
       documentation: "-----------\n Linking --\n-----------",
       documentation_snippet: "",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Chain",
       qualified_name: "Iterators.Operators.Chain",
       signature: "iterators.operators.chain",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Chain is new Into.Iterator with private;",
       }   ,
       {
       name: "Operator",
       qualified_name: "Iterators.Operators.Operator",
       signature: "iterators.operators.operator",
       enclosing: "",
       is_private: false,
       documentation: "Operators that transform from one type into another.",
       documentation_snippet: "type Operator is abstract new Into.Iterator with private;",
       }   ,
   ]
,}
---
