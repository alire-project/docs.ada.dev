---
crate: libkeccak
layout: gnatdoc
gnatdoc: {
name: "Keccak.Generic_Tuple_Hash",
qualified_name: "Keccak.Generic_Tuple_Hash",
signature: "keccak.generic_tuple_hash",
enclosing: "keccak",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Context",
       qualified_name: "Keccak.Generic_Tuple_Hash.Context",
       signature: "keccak.generic_tuple_hash.context",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Context is private;",
       }   ,
       {
       name: "States",
       qualified_name: "Keccak.Generic_Tuple_Hash.States",
       signature: "keccak.generic_tuple_hash.states",
       enclosing: "",
       is_private: false,
       documentation: "@value Updating When in this state additional data can be input into the\n  TupleHash context.\n\n@value Extracting When in this state, the TupleHash context can generate\n  output bytes by calling the Extract procedure.\n\n@value Finished When in this state the context is finished and no more data\n  can be input or output.\n\n@enum Updating\n@enum Extracting\n@enum Finished",
       documentation_snippet: "type States is (Updating, Extracting, Finished);",
       }   ,
   ]
,}
---
