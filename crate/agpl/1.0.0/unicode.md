---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Unicode",
qualified_name: "Unicode",
signature: "unicode",
enclosing: "",
is_private: false,
documentation: "In the package below, all the functions Is_* are based on values defined\nin the XML standard.\nSeveral child packages are provided, that support different encoding\nforms, and can all convert from and to Utf32, which thus behaves as the\nreference.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Unicode_Char",
       qualified_name: "Unicode.Unicode_Char",
       signature: "unicode.unicode_char",
       enclosing: "",
       is_private: false,
       documentation: "A code point associated with a given character, taken in the Unicode\nrepertoire.\nNote that by design, the first 127 entries are taken in the ASCII set\nand are fully compatible. You can thus easily compare this with\nconstant characters by using Character'Pos ('.')",
       documentation_snippet: "type Unicode_Char is mod 2**32;",
       }   ,
   ]
,}
---
