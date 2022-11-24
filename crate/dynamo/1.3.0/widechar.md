---
crate: dynamo
layout: gnatdoc
gnatdoc: {
name: "Widechar",
qualified_name: "Widechar",
signature: "widechar",
enclosing: "",
is_private: false,
documentation: "Subprograms for manipulation of wide character sequences. Note that in\nthis package, wide character and wide wide character are not distinguished\nsince this package is basically concerned with syntactic notions, and it\ndeals with Char_Code values, rather than values of actual Ada types.",
documentation_snippet: "",
variables:    [
       {
       name: "Wide_Char_Byte_Count",
       qualified_name: "Widechar.Wide_Char_Byte_Count",
       signature: "widechar.wide_char_byte_count",
       enclosing: "",
       is_private: false,
       documentation: "This value is incremented whenever Scan_Wide or Skip_Wide is called.\nThe amount added is the length of the wide character sequence minus\none. This means that the count that accumulates here represents the\ndifference between the length in characters and the length in bytes.\nThis is used for checking the line length in characters.",
       documentation_snippet: "Wide_Char_Byte_Count : Nat := 0;",
       }   ,
   ]
,}
---
