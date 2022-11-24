---
crate: libkeccak
layout: gnatdoc
gnatdoc: {
name: "Keccak.Generic_Parallel_CSHAKE",
qualified_name: "Keccak.Generic_Parallel_CSHAKE",
signature: "keccak.generic_parallel_cshake",
enclosing: "keccak",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Context",
       qualified_name: "Keccak.Generic_Parallel_CSHAKE.Context",
       signature: "keccak.generic_parallel_cshake.context",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Context is private;",
       }   ,
       {
       name: "States",
       qualified_name: "Keccak.Generic_Parallel_CSHAKE.States",
       signature: "keccak.generic_parallel_cshake.states",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type States is (Updating, Extracting, Finished);",
       }   ,
   ]
,subtypes:    [
       {
       name: "Rate_Bits_Number",
       qualified_name: "Keccak.Generic_Parallel_CSHAKE.Rate_Bits_Number",
       signature: "keccak.generic_parallel_cshake.rate_bits_number",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Rate_Bits_Number is XOF.Rate_Bits_Number;",
       }   ,
   ]
,constants:    [
       {
       name: "Num_Parallel_Instances",
       qualified_name: "Keccak.Generic_Parallel_CSHAKE.Num_Parallel_Instances",
       signature: "keccak.generic_parallel_cshake.num_parallel_instances",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Num_Parallel_Instances : constant Positive := XOF.Num_Parallel_Instances;",
       }   ,
   ]
,}
---
