---
crate: libkeccak
layout: gnatdoc
gnatdoc: {
name: "Keccak.Generic_Parallel_Permutation_Serial_Fallback",
qualified_name: "Keccak.Generic_Parallel_Permutation_Serial_Fallback",
signature: "keccak.generic_parallel_permutation_serial_fallback",
enclosing: "keccak",
is_private: false,
documentation: "\n@formal Permutation_State\n@formal Init\n@formal XOR_Bits_Into_State\n@formal Extract_Bytes\n@formal State_Size_Bits\n  State size of the permutation in bits.\n  \n  E.g. for Keccak-f[1600] set State_Size_Bits to 1600.\n@formal Parallelism\n  Specifies the number of simulated parallel instances.",
documentation_snippet: "",
array_types:    [
       {
       name: "Permutation_State_Array",
       qualified_name: "Keccak.Generic_Parallel_Permutation_Serial_Fallback.Permutation_State_Array",
       signature: "keccak.generic_parallel_permutation_serial_fallback.permutation_state_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Permutation_State_Array is array (0 .. Parallelism - 1) of Permutation_State;",
       }   ,
   ]
,record_types:    [
       {
       name: "Parallel_State",
       qualified_name: "Keccak.Generic_Parallel_Permutation_Serial_Fallback.Parallel_State",
       signature: "keccak.generic_parallel_permutation_serial_fallback.parallel_state",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Parallel_State is record\n   States : Permutation_State_Array;\nend record;",
       }   ,
   ]
,constants:    [
       {
       name: "Num_Parallel_Instances",
       qualified_name: "Keccak.Generic_Parallel_Permutation_Serial_Fallback.Num_Parallel_Instances",
       signature: "keccak.generic_parallel_permutation_serial_fallback.num_parallel_instances",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Num_Parallel_Instances : constant Positive := Parallelism;",
       }   ,
   ]
,}
---
