---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Unicode.CES",
qualified_name: "Unicode.CES",
signature: "unicode.ces",
enclosing: "unicode",
is_private: false,
documentation: "-----------------\n Byte sequence --\n-----------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Bom_Type",
       qualified_name: "Unicode.CES.Bom_Type",
       signature: "unicode.ces.bom_type",
       enclosing: "",
       is_private: false,
       documentation: "the type of encoding used for a string, that can be deduced from the\nBOM.\n\n@enum Utf8_All\n  Utf8-encoding\n@enum Utf16_LE\n  Utf16 little-endian encoding\n@enum Utf16_BE\n  Utf16 big-endian encoding\n@enum Utf32_LE\n  Utf32 little-endian encoding\n@enum Utf32_BE\n  Utf32 big-endian encoding\n@enum Ucs4_BE\n  UCS-4, big endian machine (1234 order)\n@enum Ucs4_LE\n  UCS-4, little endian machine (4321 order)\n@enum Ucs4_2143\n  UCS-4, unusual byte order (2143 order)\n@enum Ucs4_3412\n  UCS-4, unusual byte order (3412 order)\n@enum Unknown\n  Unknown, assumed to be ASCII compatible",
       documentation_snippet: "type Bom_Type is\n  (Utf8_All,\n   Utf16_LE,\n   Utf16_BE,\n   Utf32_LE,\n   Utf32_BE,\n   Ucs4_BE,\n   Ucs4_LE,\n   Ucs4_2143,\n   Ucs4_3412,\n   Unknown);",
       }   ,
       {
       name: "Byte_Order",
       qualified_name: "Unicode.CES.Byte_Order",
       signature: "unicode.ces.byte_order",
       enclosing: "",
       is_private: false,
       documentation: "Order of bytes in word machines.\n\n@enum High_Byte_First\n@enum Low_Byte_First",
       documentation_snippet: "type Byte_Order is (High_Byte_First, Low_Byte_First);",
       }   ,
   ]
,record_types:    [
       {
       name: "Encoding_Scheme",
       qualified_name: "Unicode.CES.Encoding_Scheme",
       signature: "unicode.ces.encoding_scheme",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Encoding_Scheme is record\n   Read            : Read_Function;\n   Width           : Width_Function;\n   Encode          : Encode_Function;\n   Length          : Length_Function;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Byte_Sequence_Access",
       qualified_name: "Unicode.CES.Byte_Sequence_Access",
       signature: "unicode.ces.byte_sequence_access",
       enclosing: "",
       is_private: false,
       documentation: "A sequence of bytes. The encoding is unknown.",
       documentation_snippet: "type Byte_Sequence_Access is access all Byte_Sequence;",
       }   ,
       {
       name: "Encode_Function",
       qualified_name: "Unicode.CES.Encode_Function",
       signature: "unicode.ces.encode_function",
       enclosing: "",
       is_private: false,
       documentation: "This function converts Char to the appropriate byte sequence that\nrepresents it in the specific encoding.\nThe byte sequence is stored in Output, starting at Index + 1. On exit,\nIndex is left on the last character set in Output.\n\n@param Char\n@param Output\n@param Index",
       documentation_snippet: "type Encode_Function is access\n  procedure (Char   : Unicode_Char;\n             Output : in out Byte_Sequence;\n             Index  : in out Natural);",
       }   ,
       {
       name: "Length_Function",
       qualified_name: "Unicode.CES.Length_Function",
       signature: "unicode.ces.length_function",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Length_Function is access\n  function (Str : Byte_Sequence) return Natural;",
       }   ,
       {
       name: "Read_Function",
       qualified_name: "Unicode.CES.Read_Function",
       signature: "unicode.ces.read_function",
       enclosing: "",
       is_private: false,
       documentation: "This function returns the character at position Index in the byte\nsequence Str, and moves Index to the start of the next character.\n\n@param Str\n@param Index\n@param Char",
       documentation_snippet: "type Read_Function is access\n  procedure (Str   : Byte_Sequence;\n             Index : in out Positive;\n             Char  : out Unicode_Char);",
       }   ,
       {
       name: "Width_Function",
       qualified_name: "Unicode.CES.Width_Function",
       signature: "unicode.ces.width_function",
       enclosing: "",
       is_private: false,
       documentation: "This function returns the number of bytes that encode Char in the\nspecific encoding scheme.\n\n@param Char\n\n@return",
       documentation_snippet: "type Width_Function is access\n  function (Char : Unicode.Unicode_Char) return Natural;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Bom_Type_Utf16",
       qualified_name: "Unicode.CES.Bom_Type_Utf16",
       signature: "unicode.ces.bom_type_utf16",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Bom_Type_Utf16 is Bom_Type range Utf16_LE .. Utf16_BE;",
       }   ,
       {
       name: "Bom_Type_Utf32",
       qualified_name: "Unicode.CES.Bom_Type_Utf32",
       signature: "unicode.ces.bom_type_utf32",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Bom_Type_Utf32 is Bom_Type range Utf32_LE .. Utf32_BE;",
       }   ,
       {
       name: "Byte_Sequence",
       qualified_name: "Unicode.CES.Byte_Sequence",
       signature: "unicode.ces.byte_sequence",
       enclosing: "",
       is_private: false,
       documentation: "A sequence of bytes. The encoding is unknown.",
       documentation_snippet: "subtype Byte_Sequence is String;",
       }   ,
   ]
,constants:    [
       {
       name: "Default_Byte_Order",
       qualified_name: "Unicode.CES.Default_Byte_Order",
       signature: "unicode.ces.default_byte_order",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Default_Byte_Order : constant Byte_Order := Low_Byte_First;",
       }   ,
   ]
,}
---
