---
crate: felix
layout: gnatdoc
gnatdoc: {
name: "Standard_Text",
qualified_name: "Standard_Text",
signature: "standard_text",
enclosing: "",
is_private: false,
documentation: "----------------------------------------------------------------------------\n  Copyright (c) 2021, Lev Kujawski.\n\n  Permission is hereby granted, free of charge, to any person obtaining a\n  copy of this software and associated documentation files (the \"Software\")\n  to deal in the Software without restriction, including without limitation\n  the rights to use, copy, modify, merge, publish, distribute, sublicense,\n  and sell copies of the Software, and to permit persons to whom the\n  Software is furnished to do so.\n\n  THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL\n  THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING\n  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER\n  DEALINGS IN THE SOFTWARE.\n\n  SPDX-License-Identifier: MIT-0\n\n  File:          stantext.ads (Ada Package Specification)\n  Language:      Ada (1995) [1]\n  Author:        Lev Kujawski\n  Description:   Type-safe printf() emulation for string localization\n\n  References:\n  [1] Information technology - Programming languages - Ada,\n      ISO/IEC 8652:1995(E), 15 Feb. 1995.\n----------------------------------------------------------------------------\n\n  Standard_Text utilizes the C library's printf family of functions to\n  guarantee that output will match that of C programs using the standard\n  library.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Element_T",
       qualified_name: "Standard_Text.Element_T",
       signature: "standard_text.element_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Element_T (<>) is limited private;",
       }   ,
       {
       name: "Modifier_T",
       qualified_name: "Standard_Text.Modifier_T",
       signature: "standard_text.modifier_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Modifier_T (<>) is limited private;",
       }   ,
       {
       name: "Text_T",
       qualified_name: "Standard_Text.Text_T",
       signature: "standard_text.text_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Text_T (<>) is limited private;",
       }   ,
   ]
,}
---
