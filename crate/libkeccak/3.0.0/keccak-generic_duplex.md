---
crate: libkeccak
layout: gnatdoc
gnatdoc: {
name: "Keccak.Generic_Duplex",
qualified_name: "Keccak.Generic_Duplex",
signature: "keccak.generic_duplex",
enclosing: "keccak",
is_private: false,
documentation: "-----------------------------------------------------------------------------\n  Copyright (c) 2019, Daniel King\n  All rights reserved.\n\n  Redistribution and use in source and binary forms, with or without\n  modification, are permitted provided that the following conditions are met:\n      * Redistributions of source code must retain the above copyright\n        notice, this list of conditions and the following disclaimer.\n      * Redistributions in binary form must reproduce the above copyright\n        notice, this list of conditions and the following disclaimer in the\n        documentation and/or other materials provided with the distribution.\n      * The name of the copyright holder may not be used to endorse or promote\n        Products derived from this software without specific prior written\n        permission.\n\n  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS \"AS IS\"\n  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE\n  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE\n  ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER BE LIABLE FOR ANY\n  DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES\n  (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;\n  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND\n  ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT\n  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF\n  THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.\n-----------------------------------------------------------------------------\n\n@formal State_Size_Bits\n  Type for the Duplex state (e.g. this could be a Keccak[1600] state).\n@formal State_Type\n  Procedure to initialize the state.\n@formal Init_State\n  Procedure to permute the state.\n@formal Permute\n  Procedure to XOR bits into the generic state.\n@formal XOR_Bits_Into_State\n  Procedure to copy bytes from the generic state.\n@formal Extract_Bits\n  Procedure to apply the padding rule to a block of bytes.\n@formal Pad\n  The minimum number of bits that are added to the message  by the padding\n  rule. The duplex constructon ensures that this amount of bits is free\n  in the block before the padding is applied.\n@formal Min_Padding_Bits\n  @summary\n  Generic implementation of the Duplex cryptographic construction.\n  \n  @description\n  The duplex construction is a cryptographic scheme defined in the\n  specification \"Cryptographic Sponge Functions\" from authors of Keccak.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Context",
       qualified_name: "Keccak.Generic_Duplex.Context",
       signature: "keccak.generic_duplex.context",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Context is private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Rate_Number",
       qualified_name: "Keccak.Generic_Duplex.Rate_Number",
       signature: "keccak.generic_duplex.rate_number",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Rate_Number is Positive range 1 + Min_Padding_Bits .. State_Size_Bits - 1;",
       }   ,
   ]
,}
---
