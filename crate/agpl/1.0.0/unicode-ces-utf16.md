---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Unicode.CES.Utf16",
qualified_name: "Unicode.CES.Utf16",
signature: "unicode.ces.utf16",
enclosing: "unicode.ces",
is_private: false,
documentation: "---------\n Types --\n---------",
documentation_snippet: "",
access_types:    [
       {
       name: "Utf16_LE_String_Access",
       qualified_name: "Unicode.CES.Utf16.Utf16_LE_String_Access",
       signature: "unicode.ces.utf16.utf16_le_string_access",
       enclosing: "",
       is_private: false,
       documentation: "Similar, but with little-endian byte-order",
       documentation_snippet: "type Utf16_LE_String_Access is access Utf16_LE_String;",
       }   ,
       {
       name: "Utf16_String_Access",
       qualified_name: "Unicode.CES.Utf16.Utf16_String_Access",
       signature: "unicode.ces.utf16.utf16_string_access",
       enclosing: "",
       is_private: false,
       documentation: "A UTF16-encoded string, undefined byte-order",
       documentation_snippet: "type Utf16_String_Access is access Utf16_String;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Utf16_BE_String",
       qualified_name: "Unicode.CES.Utf16.Utf16_BE_String",
       signature: "unicode.ces.utf16.utf16_be_string",
       enclosing: "",
       is_private: false,
       documentation: "Similar, but with big-endian byte-order",
       documentation_snippet: "subtype Utf16_BE_String is Utf16_String;",
       }   ,
       {
       name: "Utf16_LE_String",
       qualified_name: "Unicode.CES.Utf16.Utf16_LE_String",
       signature: "unicode.ces.utf16.utf16_le_string",
       enclosing: "",
       is_private: false,
       documentation: "Similar, but with little-endian byte-order",
       documentation_snippet: "subtype Utf16_LE_String is Utf16_String;",
       }   ,
       {
       name: "Utf16_String",
       qualified_name: "Unicode.CES.Utf16.Utf16_String",
       signature: "unicode.ces.utf16.utf16_string",
       enclosing: "",
       is_private: false,
       documentation: "A UTF16-encoded string, undefined byte-order",
       documentation_snippet: "subtype Utf16_String is String;",
       }   ,
   ]
,constants:    [
       {
       name: "Utf16_BE_Encoding",
       qualified_name: "Unicode.CES.Utf16.Utf16_BE_Encoding",
       signature: "unicode.ces.utf16.utf16_be_encoding",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Utf16_BE_Encoding : constant Encoding_Scheme :=\n  (Read   => Read_BE'Access,\n   Width  => Width'Access,\n   Encode => Encode_Function'(Encode_BE'Access),\n   Length => Length'Access);",
       }   ,
       {
       name: "Utf16_LE_Encoding",
       qualified_name: "Unicode.CES.Utf16.Utf16_LE_Encoding",
       signature: "unicode.ces.utf16.utf16_le_encoding",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Utf16_LE_Encoding : constant Encoding_Scheme :=\n  (Read   => Read'Access,\n   Width  => Width'Access,\n   Encode => Encode_Function'(Encode'Access),\n   Length => Length'Access);",
       }   ,
   ]
,}
---
