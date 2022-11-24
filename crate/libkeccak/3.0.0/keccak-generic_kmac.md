---
crate: libkeccak
layout: gnatdoc
gnatdoc: {
name: "Keccak.Generic_KMAC",
qualified_name: "Keccak.Generic_KMAC",
signature: "keccak.generic_kmac",
enclosing: "keccak",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Context",
       qualified_name: "Keccak.Generic_KMAC.Context",
       signature: "keccak.generic_kmac.context",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Context is private;",
       }   ,
       {
       name: "States",
       qualified_name: "Keccak.Generic_KMAC.States",
       signature: "keccak.generic_kmac.states",
       enclosing: "",
       is_private: false,
       documentation: "@value Updating When in this state additional data can be input into the\n  KMAC context.\n\n@value Extracting When in this state, the KMAC context can generate\n  output bytes by calling the Extract procedure.\n\n@value Finished When in this state the context is finished and no more data\n  can be input or output.\n\n@enum Updating\n@enum Extracting\n@enum Finished",
       documentation_snippet: "type States is (Updating, Extracting, Finished);",
       }   ,
   ]
,}
---
