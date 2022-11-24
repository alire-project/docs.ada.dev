---
crate: libkeccak
layout: gnatdoc
gnatdoc: {
name: "Keccak.Generic_KeccakF",
qualified_name: "Keccak.Generic_KeccakF",
signature: "keccak.generic_keccakf",
enclosing: "keccak",
is_private: false,
documentation: "-----------------------------------------------------------------------------\n  Copyright (c) 2019, Daniel King\n  All rights reserved.\n\n  Redistribution and use in source and binary forms, with or without\n  modification, are permitted provided that the following conditions are met:\n      * Redistributions of source code must retain the above copyright\n        notice, this list of conditions and the following disclaimer.\n      * Redistributions in binary form must reproduce the above copyright\n        notice, this list of conditions and the following disclaimer in the\n        documentation and/or other materials provided with the distribution.\n      * The name of the copyright holder may not be used to endorse or promote\n        Products derived from this software without specific prior written\n        permission.\n\n  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS \"AS IS\"\n  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE\n  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE\n  ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER BE LIABLE FOR ANY\n  DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES\n  (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;\n  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND\n  ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT\n  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF\n  THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.\n-----------------------------------------------------------------------------\n\n@formal Lane_Size_Log\n  Modular type for a lane of the Keccak state.\n  \n  Lane_Type'Modulus must be equal to 2**(2**Lane_Size_Log).\n  For example, when Lane_Size_Log=6 Lane_Type must be a 64-bit\n  mod type (2**Lane_Size_Log = 64 when Lane_Size_Log = 6).\n@formal Lane_Type",
documentation_snippet: "",
simple_types:    [
       {
       name: "Lane_Complemented_State",
       qualified_name: "Keccak.Generic_KeccakF.Lane_Complemented_State",
       signature: "keccak.generic_keccakf.lane_complemented_state",
       enclosing: "",
       is_private: false,
       documentation: "State type used for the lane complementing implementation.\n\nA distinct type is used here to prevent confusion in using the wrong\nsubprograms with the wrong type, as specific implementations are needed\nto handle the lane complemented Keccak-f state.",
       documentation_snippet: "type Lane_Complemented_State is private;",
       }   ,
       {
       name: "Round_Index",
       qualified_name: "Keccak.Generic_KeccakF.Round_Index",
       signature: "keccak.generic_keccakf.round_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Round_Index is new Natural range 0 .. 23;",
       }   ,
       {
       name: "State",
       qualified_name: "Keccak.Generic_KeccakF.State",
       signature: "keccak.generic_keccakf.state",
       enclosing: "",
       is_private: false,
       documentation: "Keccak-f[B] state, where B is the state size in bits (e.g. 1600 bits).",
       documentation_snippet: "type State is private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Round_Count",
       qualified_name: "Keccak.Generic_KeccakF.Round_Count",
       signature: "keccak.generic_keccakf.round_count",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Round_Count is Positive range 1 .. 24;",
       }   ,
   ]
,constants:    [
       {
       name: "Lane_Size_Bits",
       qualified_name: "Keccak.Generic_KeccakF.Lane_Size_Bits",
       signature: "keccak.generic_keccakf.lane_size_bits",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Lane_Size_Bits  : constant Positive := 2**Lane_Size_Log;",
       }   ,
       {
       name: "State_Size_Bits",
       qualified_name: "Keccak.Generic_KeccakF.State_Size_Bits",
       signature: "keccak.generic_keccakf.state_size_bits",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "State_Size_Bits : constant Positive := Lane_Size_Bits * 25;",
       }   ,
   ]
,}
---
