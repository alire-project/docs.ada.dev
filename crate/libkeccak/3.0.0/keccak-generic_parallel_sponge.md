---
crate: libkeccak
layout: gnatdoc
gnatdoc: {
name: "Keccak.Generic_Parallel_Sponge",
qualified_name: "Keccak.Generic_Parallel_Sponge",
signature: "keccak.generic_parallel_sponge",
enclosing: "keccak",
is_private: false,
documentation: "\n@formal State_Size\n  Size in bits of the underlying permutation state.\n  E.g. for Keccak-f[1600] this should be set to 1600.\n@formal State_Type\n  Type of the parallel permutation state.\n@formal Parallelism\n  Number of parallel instances provided by State_Type.\n@formal Init\n  Initializes the parallel permutation states.\n@formal Permute_All\n  Applies the permutation function to each state in parallel.\n@formal XOR_Bits_Into_State_Separate\n  XOR bits into a specific instance of the permutation state.\n@formal XOR_Bits_Into_State_All\n@formal Extract_Bytes\n  Extracts a bytes of output from the state\n@formal Pad\n  Apply the padding rule to a block of data.\n@formal Min_Padding_Bits\n  Minimum number of padding bits appended to the message.\n  \n  E.g. for pad10*1 there are a minimum of 2 padding bits (two '1' bits).",
documentation_snippet: "",
simple_types:    [
       {
       name: "Context",
       qualified_name: "Keccak.Generic_Parallel_Sponge.Context",
       signature: "keccak.generic_parallel_sponge.context",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Context (Capacity : Positive) is private;",
       }   ,
       {
       name: "States",
       qualified_name: "Keccak.Generic_Parallel_Sponge.States",
       signature: "keccak.generic_parallel_sponge.states",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type States is (Absorbing, Squeezing, Finished);",
       }   ,
   ]
,subtypes:    [
       {
       name: "Rate_Bits_Number",
       qualified_name: "Keccak.Generic_Parallel_Sponge.Rate_Bits_Number",
       signature: "keccak.generic_parallel_sponge.rate_bits_number",
       enclosing: "",
       is_private: false,
       documentation: "Number representing the Rate (in bits).\n\nThe Rate must be a positive integer, and less than the size of the\nstate (i.e. there must be at least 1 bit of \"capacity\"). Furthermore,\nthis implementation restricts the Rate to a multiple of 8 bits.",
       documentation_snippet: "subtype Rate_Bits_Number is Positive range 1 .. State_Size - 1\n  with Dynamic_Predicate => Rate_Bits_Number mod 8 = 0;",
       }   ,
   ]
,constants:    [
       {
       name: "Block_Size_Bits",
       qualified_name: "Keccak.Generic_Parallel_Sponge.Block_Size_Bits",
       signature: "keccak.generic_parallel_sponge.block_size_bits",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Block_Size_Bits        : constant Positive := State_Size;",
       }   ,
       {
       name: "Num_Parallel_Instances",
       qualified_name: "Keccak.Generic_Parallel_Sponge.Num_Parallel_Instances",
       signature: "keccak.generic_parallel_sponge.num_parallel_instances",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Num_Parallel_Instances : constant Positive := Parallelism;",
       }   ,
   ]
,}
---
