---
crate: libkeccak
layout: gnatdoc
gnatdoc: {
name: "Keccak.Generic_MonkeyDuplex",
qualified_name: "Keccak.Generic_MonkeyDuplex",
signature: "keccak.generic_monkeyduplex",
enclosing: "keccak",
is_private: false,
documentation: "-----------------------------------------------------------------------------\n  Copyright (c) 2019, Daniel King\n  All rights reserved.\n\n  Redistribution and use in source and binary forms, with or without\n  modification, are permitted provided that the following conditions are met:\n      * Redistributions of source code must retain the above copyright\n        notice, this list of conditions and the following disclaimer.\n      * Redistributions in binary form must reproduce the above copyright\n        notice, this list of conditions and the following disclaimer in the\n        documentation and/or other materials provided with the distribution.\n      * The name of the copyright holder may not be used to endorse or promote\n        Products derived from this software without specific prior written\n        permission.\n\n  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS \"AS IS\"\n  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE\n  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE\n  ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER BE LIABLE FOR ANY\n  DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES\n  (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;\n  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND\n  ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT\n  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF\n  THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.\n-----------------------------------------------------------------------------\n\n@formal State_Size_Bits\n@formal State_Type\n@formal Init_State\n@formal Permute_Start\n@formal Permute_Step\n@formal Permute_Stride\n  Procedure to XOR bits into the generic state.\n@formal XOR_Bits_Into_State\n@formal XOR_Byte_Into_State\n@formal Extract_Bits\n@formal XOR_Padding_Into_State\n@formal Min_Padding_Bits",
documentation_snippet: "",
simple_types:    [
       {
       name: "Context",
       qualified_name: "Keccak.Generic_MonkeyDuplex.Context",
       signature: "keccak.generic_monkeyduplex.context",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Context is private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Rate_Bits_Number",
       qualified_name: "Keccak.Generic_MonkeyDuplex.Rate_Bits_Number",
       signature: "keccak.generic_monkeyduplex.rate_bits_number",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Rate_Bits_Number is Positive range Min_Padding_Bits + 1 .. State_Size_Bits - 1;",
       }   ,
   ]
,}
---
