---
crate: libkeccak
layout: gnatdoc
gnatdoc: {
name: "Keccak.Padding",
qualified_name: "Keccak.Padding",
signature: "keccak.padding",
enclosing: "keccak",
is_private: false,
documentation: "-------------\n  Pad1*01  --\n-------------\n  These padding rules append a 1 bit, followed by zero or more 0 bits,\n  and ending with a final 1 bit.",
documentation_snippet: "",
constants:    [
       {
       name: "Pad101_Min_Bits",
       qualified_name: "Keccak.Padding.Pad101_Min_Bits",
       signature: "keccak.padding.pad101_min_bits",
       enclosing: "",
       is_private: false,
       documentation: "The pad10*1 rule appends at least 2 bits",
       documentation_snippet: "Pad101_Min_Bits : constant := 2;",
       }   ,
       {
       name: "Pad10_Min_Bits",
       qualified_name: "Keccak.Padding.Pad10_Min_Bits",
       signature: "keccak.padding.pad10_min_bits",
       enclosing: "",
       is_private: false,
       documentation: "The pad10*1 rule appends at least 2 bits",
       documentation_snippet: "Pad10_Min_Bits : constant := 2;",
       }   ,
   ]
,}
---
