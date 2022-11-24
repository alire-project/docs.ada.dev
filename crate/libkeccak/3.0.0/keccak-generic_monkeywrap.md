---
crate: libkeccak
layout: gnatdoc
gnatdoc: {
name: "Keccak.Generic_MonkeyWrap",
qualified_name: "Keccak.Generic_MonkeyWrap",
signature: "keccak.generic_monkeywrap",
enclosing: "keccak",
is_private: false,
documentation: "-----------------------------------------------------------------------------\n  Copyright (c) 2019, Daniel King\n  All rights reserved.\n\n  Redistribution and use in source and binary forms, with or without\n  modification, are permitted provided that the following conditions are met:\n      * Redistributions of source code must retain the above copyright\n        notice, this list of conditions and the following disclaimer.\n      * Redistributions in binary form must reproduce the above copyright\n        notice, this list of conditions and the following disclaimer in the\n        documentation and/or other materials provided with the distribution.\n      * The name of the copyright holder may not be used to endorse or promote\n        Products derived from this software without specific prior written\n        permission.\n\n  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS \"AS IS\"\n  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE\n  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE\n  ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER BE LIABLE FOR ANY\n  DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES\n  (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;\n  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND\n  ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT\n  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF\n  THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.\n-----------------------------------------------------------------------------\n\n@formal Block_Size_Bytes",
documentation_snippet: "",
simple_types:    [
       {
       name: "Context",
       qualified_name: "Keccak.Generic_MonkeyWrap.Context",
       signature: "keccak.generic_monkeywrap.context",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Context is private;",
       }   ,
       {
       name: "State",
       qualified_name: "Keccak.Generic_MonkeyWrap.State",
       signature: "keccak.generic_monkeywrap.state",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type State is (Auth_Data,\n               Encrypting,\n               Extracting_Tag,\n               Decrypting,\n               Verifying_Tag);",
       }   ,
   ]
,constants:    [
       {
       name: "Max_Block_Size_Bits",
       qualified_name: "Keccak.Generic_MonkeyWrap.Max_Block_Size_Bits",
       signature: "keccak.generic_monkeywrap.max_block_size_bits",
       enclosing: "",
       is_private: false,
       documentation: "MonkeyWrap specification requires: 0 < p <= b - 4\n\nI.e. the block size does not exceed state size - 4 bits\n(2 bits padding, 2 bits domain separation).\n\nE.g. for Keccak-p[1600] this is 1600 - 4 = 1596",
       documentation_snippet: "Max_Block_Size_Bits : constant Positive := Max_Rate_Bits - 2;",
       }   ,
       {
       name: "Max_Key_Size_Bits",
       qualified_name: "Keccak.Generic_MonkeyWrap.Max_Key_Size_Bits",
       signature: "keccak.generic_monkeywrap.max_key_size_bits",
       enclosing: "",
       is_private: false,
       documentation: "The size of the key must fit in the underlying permutation's block size,\nminus 18 bits.\n\nSee Section 5.1 of the Ketje v2 specification.",
       documentation_snippet: "Max_Key_Size_Bits : constant Positive := MonkeyDuplex.State_Size_Bits - 18;",
       }   ,
       {
       name: "Max_Rate_Bits",
       qualified_name: "Keccak.Generic_MonkeyWrap.Max_Rate_Bits",
       signature: "keccak.generic_monkeywrap.max_rate_bits",
       enclosing: "",
       is_private: false,
       documentation: "Maximum possible rate of the underlying MonkeyDuplex.\n\nE.g. for Keccak-p[1600] this is 1600 - 2 = 1598",
       documentation_snippet: "Max_Rate_Bits : constant Positive :=\n  MonkeyDuplex.State_Size_Bits - MonkeyDuplex.Min_Padding_Bits;",
       }   ,
   ]
,}
---
