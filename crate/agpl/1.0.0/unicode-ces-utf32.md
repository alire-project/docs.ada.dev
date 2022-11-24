---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Unicode.CES.Utf32",
qualified_name: "Unicode.CES.Utf32",
signature: "unicode.ces.utf32",
enclosing: "unicode.ces",
is_private: false,
documentation: "---------\n Types --\n---------",
documentation_snippet: "",
access_types:    [
       {
       name: "Utf32_LE_String_Access",
       qualified_name: "Unicode.CES.Utf32.Utf32_LE_String_Access",
       signature: "unicode.ces.utf32.utf32_le_string_access",
       enclosing: "",
       is_private: false,
       documentation: "A Utf32-encoded, little-endian string.",
       documentation_snippet: "type Utf32_LE_String_Access is access Utf32_LE_String;",
       }   ,
       {
       name: "Utf32_String_Access",
       qualified_name: "Unicode.CES.Utf32.Utf32_String_Access",
       signature: "unicode.ces.utf32.utf32_string_access",
       enclosing: "",
       is_private: false,
       documentation: "A UTF32-encoded string. Byte-order is unspecified",
       documentation_snippet: "type Utf32_String_Access is access Utf32_String;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Utf32_BE_String",
       qualified_name: "Unicode.CES.Utf32.Utf32_BE_String",
       signature: "unicode.ces.utf32.utf32_be_string",
       enclosing: "",
       is_private: false,
       documentation: "A Utf32-encoded, big-endian string.",
       documentation_snippet: "subtype Utf32_BE_String is Utf32_String;",
       }   ,
       {
       name: "Utf32_LE_String",
       qualified_name: "Unicode.CES.Utf32.Utf32_LE_String",
       signature: "unicode.ces.utf32.utf32_le_string",
       enclosing: "",
       is_private: false,
       documentation: "A Utf32-encoded, little-endian string.",
       documentation_snippet: "subtype Utf32_LE_String is Utf32_String;",
       }   ,
       {
       name: "Utf32_String",
       qualified_name: "Unicode.CES.Utf32.Utf32_String",
       signature: "unicode.ces.utf32.utf32_string",
       enclosing: "",
       is_private: false,
       documentation: "A UTF32-encoded string. Byte-order is unspecified",
       documentation_snippet: "subtype Utf32_String is String;",
       }   ,
   ]
,constants:    [
       {
       name: "Utf32_BE_Encoding",
       qualified_name: "Unicode.CES.Utf32.Utf32_BE_Encoding",
       signature: "unicode.ces.utf32.utf32_be_encoding",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Utf32_BE_Encoding : constant Encoding_Scheme :=\n  (Read   => Read_BE'Access,\n   Width  => Width'Access,\n   Encode => Encode_Function'(Encode_BE'Access),\n   Length => Length'Access);",
       }   ,
       {
       name: "Utf32_Char_Width",
       qualified_name: "Unicode.CES.Utf32.Utf32_Char_Width",
       signature: "unicode.ces.utf32.utf32_char_width",
       enclosing: "",
       is_private: false,
       documentation: "Number of bytes used to represent every character in Utf32",
       documentation_snippet: "Utf32_Char_Width : constant := 4;",
       }   ,
       {
       name: "Utf32_LE_Encoding",
       qualified_name: "Unicode.CES.Utf32.Utf32_LE_Encoding",
       signature: "unicode.ces.utf32.utf32_le_encoding",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Utf32_LE_Encoding : constant Encoding_Scheme :=\n  (Read   => Read'Access,\n   Width  => Width'Access,\n   Encode => Encode_Function'(Encode'Access),\n   Length => Length'Access);",
       }   ,
   ]
,}
---
