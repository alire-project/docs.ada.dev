---
crate: cobs
layout: gnatdoc
gnatdoc: {
name: "Generic_COBS",
qualified_name: "Generic_COBS",
signature: "generic_cobs",
enclosing: "",
is_private: false,
documentation: "-----------------------------------------------------------------------------\n  Copyright (c) 2020 Daniel King\n\n  Permission is hereby granted, free of charge, to any person obtaining a\n  copy of this software and associated documentation files (the \"Software\"),\n  to deal in the Software without restriction, including without limitation\n  the rights to use, copy, modify, merge, publish, distribute, sublicense,\n  and/or sell copies of the Software, and to permit persons to whom the\n  Software is furnished to do so, subject to the following conditions:\n\n  The above copyright notice and this permission notice shall be included in\n  all copies or substantial portions of the Software.\n\n  THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING\n  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER\n  DEALINGS IN THE SOFTWARE.\n-----------------------------------------------------------------------------\n\n@formal Byte\n@formal Index\n@formal Byte_Count\n@formal Byte_Array",
documentation_snippet: "",
subtypes:    [
       {
       name: "Positive_Byte_Count",
       qualified_name: "Generic_COBS.Positive_Byte_Count",
       signature: "generic_cobs.positive_byte_count",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Positive_Byte_Count is Byte_Count range 1 .. Byte_Count'Last;",
       }   ,
   ]
,constants:    [
       {
       name: "Frame_Delimiter",
       qualified_name: "Generic_COBS.Frame_Delimiter",
       signature: "generic_cobs.frame_delimiter",
       enclosing: "",
       is_private: false,
       documentation: "COBS uses 0 as the frame delimiter byte.",
       documentation_snippet: "Frame_Delimiter : constant Byte := 0;",
       }   ,
   ]
,}
---
