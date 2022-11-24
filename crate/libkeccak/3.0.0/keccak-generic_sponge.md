---
crate: libkeccak
layout: gnatdoc
gnatdoc: {
name: "Keccak.Generic_Sponge",
qualified_name: "Keccak.Generic_Sponge",
signature: "keccak.generic_sponge",
enclosing: "keccak",
is_private: false,
documentation: "-----------------------------------------------------------------------------\n  Copyright (c) 2019, Daniel King\n  All rights reserved.\n\n  Redistribution and use in source and binary forms, with or without\n  modification, are permitted provided that the following conditions are met:\n      * Redistributions of source code must retain the above copyright\n        notice, this list of conditions and the following disclaimer.\n      * Redistributions in binary form must reproduce the above copyright\n        notice, this list of conditions and the following disclaimer in the\n        documentation and/or other materials provided with the distribution.\n      * The name of the copyright holder may not be used to endorse or promote\n        Products derived from this software without specific prior written\n        permission.\n\n  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS \"AS IS\"\n  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE\n  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE\n  ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER BE LIABLE FOR ANY\n  DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES\n  (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;\n  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND\n  ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT\n  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF\n  THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.\n-----------------------------------------------------------------------------\n\n@formal State_Size_Bits\n  Type for the internal state.\n@formal State_Type\n  Procedure to initialize the state\n@formal Init_State\n  Procedure to permute the state\n@formal Permute\n  Procedure to XOR bits into the internal state.\n@formal XOR_Bits_Into_State\n  Extracts a block of output from the state\n@formal Extract_Data\n  Padding rule\n@formal Pad",
documentation_snippet: "",
simple_types:    [
       {
       name: "Context",
       qualified_name: "Keccak.Generic_Sponge.Context",
       signature: "keccak.generic_sponge.context",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Context is private;",
       }   ,
       {
       name: "States",
       qualified_name: "Keccak.Generic_Sponge.States",
       signature: "keccak.generic_sponge.states",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type States is (Absorbing, Squeezing);",
       }   ,
   ]
,subtypes:    [
       {
       name: "Rate_Bits_Number",
       qualified_name: "Keccak.Generic_Sponge.Rate_Bits_Number",
       signature: "keccak.generic_sponge.rate_bits_number",
       enclosing: "",
       is_private: false,
       documentation: "Number representing the Rate (in bits).\n\nThe Rate must be a positive integer, and less than the size of the\nstate (i.e. there must be at least 1 bit of \"capacity\"). Furthermore,\nthis implementation restricts the Rate to a multiple of 8 bits.",
       documentation_snippet: "subtype Rate_Bits_Number is Positive range 1 .. State_Size_Bits - 1\n  with Dynamic_Predicate => Rate_Bits_Number mod 8 = 0;",
       }   ,
   ]
,constants:    [
       {
       name: "Block_Size_Bits",
       qualified_name: "Keccak.Generic_Sponge.Block_Size_Bits",
       signature: "keccak.generic_sponge.block_size_bits",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Block_Size_Bits : constant Positive := State_Size_Bits;",
       }   ,
   ]
,}
---
