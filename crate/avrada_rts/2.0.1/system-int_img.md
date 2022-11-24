---
crate: avrada_rts
layout: gnatdoc
gnatdoc: {
name: "System.Int_Img",
qualified_name: "System.Int_Img",
signature: "system.int_img",
enclosing: "system",
is_private: false,
documentation: "The function U32_Img converts an unsigned value into a text\nrepresentation.\n\nValue ist the value to be converted.\n\nBuf points to a string buffer.  The actual strings starts at\nBuf+1, leaving space for a sign.\n\nRadix is the number base in the range of 2 .. 36.\n\nThe return value is length+1 of the generated string",
documentation_snippet: "",
simple_types:    [
       {
       name: "Radix_Range",
       qualified_name: "System.Int_Img.Radix_Range",
       signature: "system.int_img.radix_range",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Radix_Range is range 2 .. 36;",
       }   ,
   ]
,}
---
