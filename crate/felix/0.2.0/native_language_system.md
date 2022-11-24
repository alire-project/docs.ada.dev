---
crate: felix
layout: gnatdoc
gnatdoc: {
name: "Native_Language_System",
qualified_name: "Native_Language_System",
signature: "native_language_system",
enclosing: "",
is_private: false,
documentation: "----------------------------------------------------------------------------\n  Copyright (c) 2021, Lev Kujawski.\n\n  Permission is hereby granted, free of charge, to any person obtaining a\n  copy of this software and associated documentation files (the \"Software\")\n  to deal in the Software without restriction, including without limitation\n  the rights to use, copy, modify, merge, publish, distribute, sublicense,\n  and sell copies of the Software, and to permit persons to whom the\n  Software is furnished to do so.\n\n  THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL\n  THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING\n  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER\n  DEALINGS IN THE SOFTWARE.\n\n  SPDX-License-Identifier: MIT-0\n\n  File:          nalansys.ads (Ada Package Specification)\n  Language:      Ada (1987) [1]\n  Author:        Lev Kujawski\n  Description:   X/Open Native Language System [2] interface for Ada\n\n  References:\n  [1] Programming languages - Ada, ISO/IEC 8652:1987, 15 Jun. 1987.\n  [2] X/Open, Internationalisation Guide Version 2, G304, Jul. 1993.\n----------------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Catalog_T",
       qualified_name: "Native_Language_System.Catalog_T",
       signature: "native_language_system.catalog_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Catalog_T is limited private;",
       }   ,
       {
       name: "Category_T",
       qualified_name: "Native_Language_System.Category_T",
       signature: "native_language_system.category_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Category_T is (LC_ALL,\n                    LC_COLLATE,\n                    LC_CTYPE,\n                    LC_MESSAGES,\n                    LC_MONETARY,\n                    LC_NUMERIC,\n                    LC_TIME);",
       }   ,
       {
       name: "Locale_T",
       qualified_name: "Native_Language_System.Locale_T",
       signature: "native_language_system.locale_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Locale_T is limited private;",
       }   ,
   ]
,}
---
