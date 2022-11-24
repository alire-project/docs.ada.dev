---
crate: libkeccak
layout: gnatdoc
gnatdoc: {
name: "Keccak.Types",
qualified_name: "Keccak.Types",
signature: "keccak.types",
enclosing: "keccak",
is_private: false,
documentation: "-----------------------------------------------------------------------------\n  This package defines common types used throughout the various packages\n  in the library.\n-----------------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Unsigned_1",
       qualified_name: "Keccak.Types.Unsigned_1",
       signature: "keccak.types.unsigned_1",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Unsigned_1 is mod 2**1 with Size => 1;",
       }   ,
       {
       name: "Unsigned_2",
       qualified_name: "Keccak.Types.Unsigned_2",
       signature: "keccak.types.unsigned_2",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Unsigned_2 is mod 2**2 with Size => 2;",
       }   ,
       {
       name: "Unsigned_4",
       qualified_name: "Keccak.Types.Unsigned_4",
       signature: "keccak.types.unsigned_4",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Unsigned_4 is mod 2**4 with Size => 4;",
       }   ,
   ]
,array_types:    [
       {
       name: "Byte_Array",
       qualified_name: "Keccak.Types.Byte_Array",
       signature: "keccak.types.byte_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Byte_Array is array (Index_Number range <>) of Byte\n  with Component_Size => 8;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Byte",
       qualified_name: "Keccak.Types.Byte",
       signature: "keccak.types.byte",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Byte is Interfaces.Unsigned_8\n  with Object_Size => 8;",
       }   ,
       {
       name: "Index_Number",
       qualified_name: "Keccak.Types.Index_Number",
       signature: "keccak.types.index_number",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Index_Number is Natural range 0 .. Natural'Last - 1;",
       }   ,
   ]
,constants:    [
       {
       name: "Null_Byte_Array",
       qualified_name: "Keccak.Types.Null_Byte_Array",
       signature: "keccak.types.null_byte_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Null_Byte_Array : constant Byte_Array (1 .. 0) := (others => 0);",
       }   ,
   ]
,}
---
