---
crate: libkeccak
layout: gnatdoc
gnatdoc: {
name: "Keccak.Generic_Parallel_XOF",
qualified_name: "Keccak.Generic_Parallel_XOF",
signature: "keccak.generic_parallel_xof",
enclosing: "keccak",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Context",
       qualified_name: "Keccak.Generic_Parallel_XOF.Context",
       signature: "keccak.generic_parallel_xof.context",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Context is private;",
       }   ,
       {
       name: "States",
       qualified_name: "Keccak.Generic_Parallel_XOF.States",
       signature: "keccak.generic_parallel_xof.states",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type States is (Updating, Extracting, Finished);",
       }   ,
   ]
,subtypes:    [
       {
       name: "Rate_Bits_Number",
       qualified_name: "Keccak.Generic_Parallel_XOF.Rate_Bits_Number",
       signature: "keccak.generic_parallel_xof.rate_bits_number",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Rate_Bits_Number is XOF_Sponge.Rate_Bits_Number;",
       }   ,
   ]
,constants:    [
       {
       name: "Num_Parallel_Instances",
       qualified_name: "Keccak.Generic_Parallel_XOF.Num_Parallel_Instances",
       signature: "keccak.generic_parallel_xof.num_parallel_instances",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Num_Parallel_Instances : constant Positive := XOF_Sponge.Num_Parallel_Instances;",
       }   ,
   ]
,}
---
