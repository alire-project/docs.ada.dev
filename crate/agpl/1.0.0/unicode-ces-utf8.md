---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Unicode.CES.Utf8",
qualified_name: "Unicode.CES.Utf8",
signature: "unicode.ces.utf8",
enclosing: "unicode.ces",
is_private: false,
documentation: "---------\n Types --\n---------",
documentation_snippet: "",
access_types:    [
       {
       name: "Utf8_String_Access",
       qualified_name: "Unicode.CES.Utf8.Utf8_String_Access",
       signature: "unicode.ces.utf8.utf8_string_access",
       enclosing: "",
       is_private: false,
       documentation: "An UTF8-encoded string.",
       documentation_snippet: "type Utf8_String_Access is access all Utf8_String;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Utf8_String",
       qualified_name: "Unicode.CES.Utf8.Utf8_String",
       signature: "unicode.ces.utf8.utf8_string",
       enclosing: "",
       is_private: false,
       documentation: "An UTF8-encoded string.",
       documentation_snippet: "subtype Utf8_String is String;",
       }   ,
   ]
,constants:    [
       {
       name: "Utf8_Encoding",
       qualified_name: "Unicode.CES.Utf8.Utf8_Encoding",
       signature: "unicode.ces.utf8.utf8_encoding",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Utf8_Encoding : constant Encoding_Scheme :=\n  (Read   => Read'Access,\n   Width  => Width'Access,\n   Encode => Encode_Function'(Encode'Access),\n   Length => Length'Access);",
       }   ,
   ]
,}
---
