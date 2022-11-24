---
crate: libkeccak
layout: gnatdoc
gnatdoc: {
name: "Keccak.Generic_Parallel_Permutation_Parallel_Fallback",
qualified_name: "Keccak.Generic_Parallel_Permutation_Parallel_Fallback",
signature: "keccak.generic_parallel_permutation_parallel_fallback",
enclosing: "keccak",
is_private: false,
documentation: "\n@formal Permutation_State\n  Type for the parallel permutation state (e.g. Keccak-f[1600]ï¿½2).\n@formal Base_Parallelism\n  The number of parallel instances for the @Permutation_Type@.\n  \n  For example, if Permutation_State is the state for Keccak-f[1600]ï¿½4\n  then set Base_Parallelism to 4.\n@formal Parallel_Factor\n  Multiply the Base_Parallelism by this number.\n  \n  The overall number of parallel instances will be:\n     Base_Parallelism * Parallel_Factor.\n  \n  For example, if this package is instantiated with Keccak-f[1600]ï¿½4\n  and Parallel_Factor = 2, then this package will use 2x Keccak-f[1600]ï¿½4\n  to produce an overall Keccak-f[1600]ï¿½8 parallel permutation.\n@formal Init\n  Initializes the Permutation_State to all zeroes.\n@formal XOR_Bits_Into_State_Separate\n  XOR bits into each parallel state.\n@formal XOR_Bits_Into_State_All\n@formal Extract_Bytes\n  Extract bytes from each parallel state.\n@formal State_Size_Bits",
documentation_snippet: "",
simple_types:    [
       {
       name: "State_Index",
       qualified_name: "Keccak.Generic_Parallel_Permutation_Parallel_Fallback.State_Index",
       signature: "keccak.generic_parallel_permutation_parallel_fallback.state_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type State_Index is new Natural range 0 .. Num_Parallel_Instances - 1;",
       }   ,
   ]
,array_types:    [
       {
       name: "Permutation_State_Array",
       qualified_name: "Keccak.Generic_Parallel_Permutation_Parallel_Fallback.Permutation_State_Array",
       signature: "keccak.generic_parallel_permutation_parallel_fallback.permutation_state_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Permutation_State_Array is\n  array (0 .. Parallel_Factor - 1)\n  of Permutation_State;",
       }   ,
   ]
,record_types:    [
       {
       name: "Parallel_State",
       qualified_name: "Keccak.Generic_Parallel_Permutation_Parallel_Fallback.Parallel_State",
       signature: "keccak.generic_parallel_permutation_parallel_fallback.parallel_state",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Parallel_State is record\n   States : Permutation_State_Array;\nend record;",
       }   ,
   ]
,constants:    [
       {
       name: "Num_Parallel_Instances",
       qualified_name: "Keccak.Generic_Parallel_Permutation_Parallel_Fallback.Num_Parallel_Instances",
       signature: "keccak.generic_parallel_permutation_parallel_fallback.num_parallel_instances",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Num_Parallel_Instances : constant Positive := Base_Parallelism * Parallel_Factor;",
       }   ,
   ]
,}
---
