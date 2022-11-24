---
crate: libkeccak
layout: gnatdoc
gnatdoc: {
name: "Keccak.Generic_CSHAKE",
qualified_name: "Keccak.Generic_CSHAKE",
signature: "keccak.generic_cshake",
enclosing: "keccak",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Context",
       qualified_name: "Keccak.Generic_CSHAKE.Context",
       signature: "keccak.generic_cshake.context",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Context is private;",
       }   ,
       {
       name: "States",
       qualified_name: "Keccak.Generic_CSHAKE.States",
       signature: "keccak.generic_cshake.states",
       enclosing: "",
       is_private: false,
       documentation: "The possible states for the context.\n\n@value Updating When in this state the context can be fed\nwith input data by calling the Update procedure.\n\n@value Ready_To_Extract When in this state the Update procedure can\nno longer be called (i.e. no more data can be input to the context),\nand the context is ready to generate output data.\n\n@value Extracting When in this state the context can produce output\nbytes by calling the Extract procedure.\n\n@enum Updating\n@enum Ready_To_Extract\n@enum Extracting",
       documentation_snippet: "type States is (Updating, Ready_To_Extract, Extracting);",
       }   ,
   ]
,}
---
