---
crate: blake2s
layout: gnatdoc
gnatdoc: {
name: "BLAKE2S",
qualified_name: "BLAKE2S",
signature: "blake2s",
enclosing: "",
is_private: false,
documentation: "----------------------------------------------------------------------------\n  Copyright (c) 2021, Lev Kujawski.\n\n  Permission is hereby granted, free of charge, to any person obtaining a\n  copy of this software and associated documentation files (the \"Software\")\n  to deal in the Software without restriction, including without limitation\n  the rights to use, copy, modify, merge, publish, distribute, sublicense,\n  and sell copies of the Software, and to permit persons to whom the\n  Software is furnished to do so.\n\n  THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL\n  THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING\n  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER\n  DEALINGS IN THE SOFTWARE.\n\n  SPDX-License-Identifier: MIT-0\n\n  File:          blake2s.ads (Ada Package Specification)\n  Language:      SPARK83 [1] subset of Ada (1987) [2]\n  Author:        Lev Kujawski\n  Description:   Implementation of the BLAKE2s hash function [3]\n\n  References:\n  [1] SPARK Team, SPARK83 - The SPADE Ada83 Kernel, Altran Praxis, 17 Oct.\n      2011.\n  [2] Programming languages - Ada, ISO/IEC 8652:1987, 15 Jun. 1987.\n  [3] M-J. Saarinen and J-P. Aumasson, \"The BLAKE2 Cryptographic Hash and\n      Message Authentication Code (MAC),\" RFC 7693, Nov. 2015.\n----------------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Status_T",
       qualified_name: "BLAKE2S.Status_T",
       signature: "blake2s.status_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Status_T is (Success, Failure);",
       }   ,
       {
       name: "T",
       qualified_name: "BLAKE2S.T",
       signature: "blake2s.t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type T is private;",
       }   ,
   ]
,array_types:    [
       {
       name: "Digest_T",
       qualified_name: "BLAKE2S.Digest_T",
       signature: "blake2s.digest_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Digest_T is array (Digest_Index_T range <>) of Octets.T;",
       }   ,
       {
       name: "Key_T",
       qualified_name: "BLAKE2S.Key_T",
       signature: "blake2s.key_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Key_T is array (Key_Index_T range <>) of Octets.T;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Digest_Default_T",
       qualified_name: "BLAKE2S.Digest_Default_T",
       signature: "blake2s.digest_default_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Digest_Default_T is Digest_T (Digest_Index_T);",
       }   ,
       {
       name: "Digest_Index_T",
       qualified_name: "BLAKE2S.Digest_Index_T",
       signature: "blake2s.digest_index_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Digest_Index_T is Positive\n  range Positive'First .. Digest_Length_Default;",
       }   ,
       {
       name: "Key_Default_T",
       qualified_name: "BLAKE2S.Key_Default_T",
       signature: "blake2s.key_default_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Key_Default_T is Key_T (Key_Index_T);",
       }   ,
       {
       name: "Key_Index_T",
       qualified_name: "BLAKE2S.Key_Index_T",
       signature: "blake2s.key_index_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Key_Index_T is Positive\n  range Positive'First .. Key_Length_Default;",
       }   ,
   ]
,constants:    [
       {
       name: "Digest_Length_Default",
       qualified_name: "BLAKE2S.Digest_Length_Default",
       signature: "blake2s.digest_length_default",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Digest_Length_Default : constant := 32;",
       }   ,
       {
       name: "Key_Length_Default",
       qualified_name: "BLAKE2S.Key_Length_Default",
       signature: "blake2s.key_length_default",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Key_Length_Default : constant := 32;",
       }   ,
   ]
,}
---
