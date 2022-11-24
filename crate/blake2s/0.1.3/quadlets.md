---
crate: blake2s
layout: gnatdoc
gnatdoc: {
name: "Quadlets",
qualified_name: "Quadlets",
signature: "quadlets",
enclosing: "",
is_private: false,
documentation: "----------------------------------------------------------------------------\n  Copyright (c) 2021, Lev Kujawski.\n\n  Permission is hereby granted, free of charge, to any person obtaining a\n  copy of this software and associated documentation files (the \"Software\")\n  to deal in the Software without restriction, including without limitation\n  the rights to use, copy, modify, merge, publish, distribute, sublicense,\n  and sell copies of the Software, and to permit persons to whom the\n  Software is furnished to do so.\n\n  THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL\n  THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING\n  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER\n  DEALINGS IN THE SOFTWARE.\n\n  SPDX-License-Identifier: MIT-0\n\n  File:          quadlets.ads (Ada Package Specification)\n  Language:      SPARK83 [1] subset of Ada (1987) [2]\n  Author:        Lev Kujawski\n  Description:   Specification of the Quadlets type and related subprograms\n\n  References:\n  [1] SPARK Team, SPARK83 - The SPADE Ada83 Kernel, Altran Praxis, 17 Oct.\n      2011.\n  [2] Programming languages - Ada, ISO/IEC 8652:1987, 15 Jun. 1987.\n----------------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "T",
       qualified_name: "Quadlets.T",
       signature: "quadlets.t",
       enclosing: "",
       is_private: false,
       documentation: "# assert T'Base is Long_Integer;",
       documentation_snippet: "type T is range 0 .. 4294967295;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Bit_Count_T",
       qualified_name: "Quadlets.Bit_Count_T",
       signature: "quadlets.bit_count_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Bit_Count_T is Natural range 0 .. Bits - 1;",
       }   ,
       {
       name: "Octet_Index_T",
       qualified_name: "Quadlets.Octet_Index_T",
       signature: "quadlets.octet_index_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Octet_Index_T is Natural range 0 .. 3;",
       }   ,
   ]
,constants:    [
       {
       name: "Bits",
       qualified_name: "Quadlets.Bits",
       signature: "quadlets.bits",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Bits : constant := 32;",
       }   ,
   ]
,}
---
