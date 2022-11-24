---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Unicode.CES.Basic_8bit",
qualified_name: "Unicode.CES.Basic_8bit",
signature: "unicode.ces.basic_8bit",
enclosing: "unicode.ces",
is_private: false,
documentation: "---------\n Types --\n---------",
documentation_snippet: "",
access_types:    [
       {
       name: "Basic_8bit_String_Access",
       qualified_name: "Unicode.CES.Basic_8bit.Basic_8bit_String_Access",
       signature: "unicode.ces.basic_8bit.basic_8bit_string_access",
       enclosing: "",
       is_private: false,
       documentation: "A heigh bit string, undefined byte-order",
       documentation_snippet: "type Basic_8bit_String_Access is access Basic_8bit_String;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Basic_8bit_String",
       qualified_name: "Unicode.CES.Basic_8bit.Basic_8bit_String",
       signature: "unicode.ces.basic_8bit.basic_8bit_string",
       enclosing: "",
       is_private: false,
       documentation: "A heigh bit string, undefined byte-order",
       documentation_snippet: "subtype Basic_8bit_String is String;",
       }   ,
   ]
,constants:    [
       {
       name: "Basic_8bit_Encoding",
       qualified_name: "Unicode.CES.Basic_8bit.Basic_8bit_Encoding",
       signature: "unicode.ces.basic_8bit.basic_8bit_encoding",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Basic_8bit_Encoding : constant Encoding_Scheme :=\n  (Read   => Read'Access,\n   Width  => Width'Access,\n   Encode => Encode_Function'(Encode'Access),\n   Length => Length'Access);",
       }   ,
   ]
,}
---
