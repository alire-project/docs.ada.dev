---
crate: dcf
layout: gnatdoc
gnatdoc: {
name: "DCF",
qualified_name: "DCF",
signature: "dcf",
enclosing: "",
is_private: false,
documentation: "SPDX-License-Identifier: MIT\n\nCopyright (c) 2019 onox <denkpadje@gmail.com>\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files (the \"Software\"), to deal\nin the Software without restriction, including without limitation the rights\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is\nfurnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in\nall copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN\nTHE SOFTWARE.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Integer_64",
       qualified_name: "DCF.Integer_64",
       signature: "dcf.integer_64",
       enclosing: "",
       is_private: false,
       documentation: "Based on C99 long long int",
       documentation_snippet: "type Integer_64 is range -(2 ** 63) .. +(2 ** 63 - 1);",
       }   ,
       {
       name: "Unsigned_16",
       qualified_name: "DCF.Unsigned_16",
       signature: "dcf.unsigned_16",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Unsigned_16 is mod 2 ** 16\n  with Size => 16;",
       }   ,
       {
       name: "Unsigned_32",
       qualified_name: "DCF.Unsigned_32",
       signature: "dcf.unsigned_32",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Unsigned_32 is mod 2 ** 32\n  with Size => 32;",
       }   ,
       {
       name: "Unsigned_8",
       qualified_name: "DCF.Unsigned_8",
       signature: "dcf.unsigned_8",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Unsigned_8 is mod 2 ** 8\n  with Size => 8;",
       }   ,
   ]
,}
---
