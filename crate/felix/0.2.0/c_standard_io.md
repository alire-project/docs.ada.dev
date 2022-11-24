---
crate: felix
layout: gnatdoc
gnatdoc: {
name: "C_Standard_IO",
qualified_name: "C_Standard_IO",
signature: "c_standard_io",
enclosing: "",
is_private: false,
documentation: "----------------------------------------------------------------------------\n  Copyright (c) 2021, Lev Kujawski.\n\n  Permission is hereby granted, free of charge, to any person obtaining a\n  copy of this software and associated documentation files (the \"Software\")\n  to deal in the Software without restriction, including without limitation\n  the rights to use, copy, modify, merge, publish, distribute, sublicense,\n  and sell copies of the Software, and to permit persons to whom the\n  Software is furnished to do so.\n\n  THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL\n  THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING\n  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER\n  DEALINGS IN THE SOFTWARE.\n\n  SPDX-License-Identifier: MIT-0\n\n  File:          cstandio.ads (Ada Package Specification)\n  Language:      Ada (1987) [1]\n  Author:        Lev Kujawski\n  Description:   C Standard Input/Output (stdio.h) interface for Ada\n\n  References:\n  [1] Programming languages - Ada, ISO/IEC 8652:1987, 15 Jun. 1987.\n----------------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "File_Mode_T",
       qualified_name: "C_Standard_IO.File_Mode_T",
       signature: "c_standard_io.file_mode_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type File_Mode_T is (Read, Write, Read_Write);",
       }   ,
       {
       name: "File_T",
       qualified_name: "C_Standard_IO.File_T",
       signature: "c_standard_io.file_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type File_T is limited private;",
       }   ,
   ]
,}
---
