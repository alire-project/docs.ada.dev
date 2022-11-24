---
crate: libkeccak
layout: gnatdoc
gnatdoc: {
name: "Keccak.Generic_Parallel_Hash",
qualified_name: "Keccak.Generic_Parallel_Hash",
signature: "keccak.generic_parallel_hash",
enclosing: "keccak",
is_private: false,
documentation: "Assertions to check that the correct parallel instances have\nbeen provided.\n\n@formal CV_Size_Bytes\n  Length of the Chaining Values, in bytes.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Byte_Count",
       qualified_name: "Keccak.Generic_Parallel_Hash.Byte_Count",
       signature: "keccak.generic_parallel_hash.byte_count",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Byte_Count is new Long_Long_Integer\nrange 0 .. Long_Long_Integer'Last;",
       }   ,
       {
       name: "Context",
       qualified_name: "Keccak.Generic_Parallel_Hash.Context",
       signature: "keccak.generic_parallel_hash.context",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Context is private;",
       }   ,
       {
       name: "States",
       qualified_name: "Keccak.Generic_Parallel_Hash.States",
       signature: "keccak.generic_parallel_hash.states",
       enclosing: "",
       is_private: false,
       documentation: "@value Updating When in this state additional data can be input into the\n  ParallelHash context.\n\n@value Extracting When in this state, the ParallelHash context can generate\n  output bytes by calling the Extract procedure.\n\n@value Finished When in this state the context is finished and no more data\n  can be input or output.\n\n@enum Updating\n@enum Extracting\n@enum Finished",
       documentation_snippet: "type States is (Updating, Extracting, Finished);",
       }   ,
   ]
,subtypes:    [
       {
       name: "Block_Size_Number",
       qualified_name: "Keccak.Generic_Parallel_Hash.Block_Size_Number",
       signature: "keccak.generic_parallel_hash.block_size_number",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Block_Size_Number is Positive range 1 .. Positive'Last / 8;",
       }   ,
   ]
,}
---
