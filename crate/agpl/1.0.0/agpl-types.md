---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Types",
qualified_name: "Agpl.Types",
signature: "agpl.types",
enclosing: "agpl",
is_private: false,
documentation: "Types of general use across Agpl",
documentation_snippet: "",
simple_types:    [
       {
       name: "Data_Rate",
       qualified_name: "Agpl.Types.Data_Rate",
       signature: "agpl.types.data_rate",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Data_Rate is new Float;",
       }   ,
       {
       name: "Unsigned_8",
       qualified_name: "Agpl.Types.Unsigned_8",
       signature: "agpl.types.unsigned_8",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Unsigned_8 is new Interfaces.Unsigned_8;",
       }   ,
       {
       name: "Utf8String",
       qualified_name: "Agpl.Types.Utf8String",
       signature: "agpl.types.utf8string",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Utf8String is new String;",
       }   ,
   ]
,array_types:    [
       {
       name: "Natural_Array",
       qualified_name: "Agpl.Types.Natural_Array",
       signature: "agpl.types.natural_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Natural_Array is array (Positive range <>) of Natural;",
       }   ,
       {
       name: "Rgb_array",
       qualified_name: "Agpl.Types.Rgb_array",
       signature: "agpl.types.rgb_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Rgb_array is array (Integer range <>) of Rgb_triplet;",
       }   ,
   ]
,record_types:    [
       {
       name: "Rgb_triplet",
       qualified_name: "Agpl.Types.Rgb_triplet",
       signature: "agpl.types.rgb_triplet",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Rgb_triplet is record\n   R, G, B : Unsigned_8;\nend record;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Hex_Character",
       qualified_name: "Agpl.Types.Hex_Character",
       signature: "agpl.types.hex_character",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Hex_Character is String (1 .. 2);",
       }   ,
   ]
,}
---
