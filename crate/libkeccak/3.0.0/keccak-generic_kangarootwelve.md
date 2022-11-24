---
crate: libkeccak
layout: gnatdoc
gnatdoc: {
name: "Keccak.Generic_KangarooTwelve",
qualified_name: "Keccak.Generic_KangarooTwelve",
signature: "keccak.generic_kangarootwelve",
enclosing: "keccak",
is_private: false,
documentation: "Assertions to check that the correct parallel instances have\nbeen provided.\n\n@formal CV_Size_Bytes\n  The size of each chaining value (CV) in bytes.\n  This is set to 256 bits (32 bytes) for KangarooTwelve\n  and 512 bits (64 bytes) for MarsupilamiFourteen.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Byte_Count",
       qualified_name: "Keccak.Generic_KangarooTwelve.Byte_Count",
       signature: "keccak.generic_kangarootwelve.byte_count",
       enclosing: "",
       is_private: false,
       documentation: "Represents a quantity of bytes.",
       documentation_snippet: "type Byte_Count is new Long_Long_Integer range 0 .. Long_Long_Integer'Last;",
       }   ,
       {
       name: "Context",
       qualified_name: "Keccak.Generic_KangarooTwelve.Context",
       signature: "keccak.generic_kangarootwelve.context",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Context is private;",
       }   ,
       {
       name: "States",
       qualified_name: "Keccak.Generic_KangarooTwelve.States",
       signature: "keccak.generic_kangarootwelve.states",
       enclosing: "",
       is_private: false,
       documentation: "The possible states for the context.\n\n@value Updating When in this state the context can be fed\nwith input data by calling the Update procedure.\n\n@value Ready_To_Extract When in this state the Update procedure can\nno longer be called (i.e. no more data can be input to the context),\nand the context is ready to generate output data.\n\n@value Extracting When in this state the context can produce output\nbytes by calling the Extract procedure.\n\n@enum Updating\n@enum Ready_To_Extract\n@enum Extracting",
       documentation_snippet: "type States is (Updating, Ready_To_Extract, Extracting);",
       }   ,
   ]
,constants:    [
       {
       name: "Block_Size_Bytes",
       qualified_name: "Keccak.Generic_KangarooTwelve.Block_Size_Bytes",
       signature: "keccak.generic_kangarootwelve.block_size_bytes",
       enclosing: "",
       is_private: false,
       documentation: "Size of each parallel block.\nThis is set to 8 kiB in the K12 documentation.",
       documentation_snippet: "Block_Size_Bytes : constant := 8192;",
       }   ,
   ]
,}
---
