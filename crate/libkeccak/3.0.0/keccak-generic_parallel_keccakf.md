---
crate: libkeccak
layout: gnatdoc
gnatdoc: {
name: "Keccak.Generic_Parallel_KeccakF",
qualified_name: "Keccak.Generic_Parallel_KeccakF",
signature: "keccak.generic_parallel_keccakf",
enclosing: "keccak",
is_private: false,
documentation: "\n@formal Lane_Size_Log\n  The binary logarithm of the lane size.\n  \n  This determines the Keccak-f state size. Allowed values are:\n  * Lane_Size_Log = 3 => 8-bit lanes,  Keccak-f[200]\n  * Lane_Size_Log = 4 => 16-bit lanes, Keccak-f[400]\n  * Lane_Size_Log = 5 => 32-bit lanes, Keccak-f[800]\n  * Lane_Size_Log = 6 => 64-bit lanes, Keccak-f[1600]\n@formal Lane_Type\n  Lane type e.g. Unsigned_64.\n@formal VXXI_Index\n  Index type into the vector component.\n@formal VXXI\n  Vector type.\n@formal VXXI_View\n  A view of the vector type, permitting individual access to each vector\n  component.\n@formal Vector_Width\n  Number of vector to components to actually use.\n  \n  Usually, this would be set to the actual number of vector components\n  (e.g. 4 for a 4x 32-bit vector). However, you may use a smaller number\n  if you don't want to use the full vector width. For example, you could\n  set Vector_Width to 2 with a 4x 32-bit vector type, to obtain 2x\n  parallelism (the upper 2 vector components would not be used).\n@formal Load\n@formal Store\n@formal \"xor\"\n  Calculates A xor State_Size_Bits per vector component.\n@formal Rotate_Left\n  Calculates Rotate_Left(A) per vector component.\n@formal And_Not\n  Calculates State_Size_Bits and (not A) per vector component.\n@formal Shift_Left\n@formal Shift_Right",
documentation_snippet: "",
simple_types:    [
       {
       name: "Parallel_State",
       qualified_name: "Keccak.Generic_Parallel_KeccakF.Parallel_State",
       signature: "keccak.generic_parallel_keccakf.parallel_state",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Parallel_State is private;",
       }   ,
       {
       name: "Round_Index",
       qualified_name: "Keccak.Generic_Parallel_KeccakF.Round_Index",
       signature: "keccak.generic_parallel_keccakf.round_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Round_Index is range 0 .. 23;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Round_Count",
       qualified_name: "Keccak.Generic_Parallel_KeccakF.Round_Count",
       signature: "keccak.generic_parallel_keccakf.round_count",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Round_Count is Positive range 1 .. 24;",
       }   ,
   ]
,constants:    [
       {
       name: "Initialized_State",
       qualified_name: "Keccak.Generic_Parallel_KeccakF.Initialized_State",
       signature: "keccak.generic_parallel_keccakf.initialized_state",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Initialized_State : constant Parallel_State;",
       }   ,
       {
       name: "Lane_Size_Bits",
       qualified_name: "Keccak.Generic_Parallel_KeccakF.Lane_Size_Bits",
       signature: "keccak.generic_parallel_keccakf.lane_size_bits",
       enclosing: "",
       is_private: false,
       documentation: "Lane size (in bits, i.e. 8, 16, 32, or 64)",
       documentation_snippet: "Lane_Size_Bits : constant Positive := 2**Lane_Size_Log;",
       }   ,
       {
       name: "Num_Parallel_Instances",
       qualified_name: "Keccak.Generic_Parallel_KeccakF.Num_Parallel_Instances",
       signature: "keccak.generic_parallel_keccakf.num_parallel_instances",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Num_Parallel_Instances : constant Positive := Vector_Width;",
       }   ,
       {
       name: "State_Size_Bits",
       qualified_name: "Keccak.Generic_Parallel_KeccakF.State_Size_Bits",
       signature: "keccak.generic_parallel_keccakf.state_size_bits",
       enclosing: "",
       is_private: false,
       documentation: "Keccak-f state size (in bits).",
       documentation_snippet: "State_Size_Bits : constant Positive := Lane_Size_Bits * 25;",
       }   ,
   ]
,}
---
