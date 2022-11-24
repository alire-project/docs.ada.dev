---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Unicode.CCS",
qualified_name: "Unicode.CCS",
signature: "unicode.ccs",
enclosing: "unicode",
is_private: false,
documentation: "Each of the child package shall have two public functions with\nthe following profile:\n  function Convert (Char : Unicode_Char) return Unicode_Char\nthat converts from a code point representing an abstract character in\nthe specific encoding to the code point for the same character in\nUnicode, or reverse",
documentation_snippet: "",
record_types:    [
       {
       name: "Character_Set",
       qualified_name: "Unicode.CCS.Character_Set",
       signature: "unicode.ccs.character_set",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Character_Set is record\n   To_Unicode : Conversion_Function;\n   To_CS      : Conversion_Function;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Conversion_Function",
       qualified_name: "Unicode.CCS.Conversion_Function",
       signature: "unicode.ccs.conversion_function",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Conversion_Function is access\n  function (Char : Unicode_Char) return Unicode_Char;",
       }   ,
   ]
,constants:    [
       {
       name: "Unicode_Character_Set",
       qualified_name: "Unicode.CCS.Unicode_Character_Set",
       signature: "unicode.ccs.unicode_character_set",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Unicode_Character_Set : constant Character_Set :=\n  (To_Unicode => Identity'Access,\n   To_Cs      => Identity'Access);",
       }   ,
   ]
,}
---
