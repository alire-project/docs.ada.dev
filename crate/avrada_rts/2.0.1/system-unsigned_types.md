---
crate: avrada_rts
layout: gnatdoc
gnatdoc: {
name: "System.Unsigned_Types",
qualified_name: "System.Unsigned_Types",
signature: "system.unsigned_types",
enclosing: "system",
is_private: false,
documentation: "This package contains definitions of standard unsigned types that\ncorrespond in size to the standard signed types declared in Standard.\nand (unlike the types in Interfaces) have corresponding names. It\nalso contains some related definitions for other specialized types\nused by the compiler in connection with packed array types.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Bits_1",
       qualified_name: "System.Unsigned_Types.Bits_1",
       signature: "system.unsigned_types.bits_1",
       enclosing: "",
       is_private: false,
       documentation: "Types used for packed array conversions",
       documentation_snippet: "type Bits_1 is mod 2**1;",
       }   ,
       {
       name: "Bits_2",
       qualified_name: "System.Unsigned_Types.Bits_2",
       signature: "system.unsigned_types.bits_2",
       enclosing: "",
       is_private: false,
       documentation: "Types used for packed array conversions",
       documentation_snippet: "type Bits_2 is mod 2**2;",
       }   ,
       {
       name: "Bits_4",
       qualified_name: "System.Unsigned_Types.Bits_4",
       signature: "system.unsigned_types.bits_4",
       enclosing: "",
       is_private: false,
       documentation: "Types used for packed array conversions",
       documentation_snippet: "type Bits_4 is mod 2**4;",
       }   ,
       {
       name: "Float_Unsigned",
       qualified_name: "System.Unsigned_Types.Float_Unsigned",
       signature: "system.unsigned_types.float_unsigned",
       enclosing: "",
       is_private: false,
       documentation: "Used in the implementation of Is_Negative intrinsic (see Exp_Intr)",
       documentation_snippet: "type Float_Unsigned       is mod 2 ** Float'Size;",
       }   ,
       {
       name: "Long_Long_Unsigned",
       qualified_name: "System.Unsigned_Types.Long_Long_Unsigned",
       signature: "system.unsigned_types.long_long_unsigned",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Long_Long_Unsigned   is mod 2 ** Long_Long_Integer'Size;",
       }   ,
       {
       name: "Long_Unsigned",
       qualified_name: "System.Unsigned_Types.Long_Unsigned",
       signature: "system.unsigned_types.long_unsigned",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Long_Unsigned        is mod 2 ** Long_Integer'Size;",
       }   ,
       {
       name: "Packed_Byte",
       qualified_name: "System.Unsigned_Types.Packed_Byte",
       signature: "system.unsigned_types.packed_byte",
       enclosing: "",
       is_private: false,
       documentation: "Component type for Packed_Bytes array",
       documentation_snippet: "type Packed_Byte is mod 2 ** 8;",
       }   ,
       {
       name: "Packed_Bytes2",
       qualified_name: "System.Unsigned_Types.Packed_Bytes2",
       signature: "system.unsigned_types.packed_bytes2",
       enclosing: "",
       is_private: false,
       documentation: "for Packed_Bytes2'Alignment use 2;",
       documentation_snippet: "type Packed_Bytes2 is new Packed_Bytes1;",
       }   ,
       {
       name: "Packed_Bytes4",
       qualified_name: "System.Unsigned_Types.Packed_Bytes4",
       signature: "system.unsigned_types.packed_bytes4",
       enclosing: "",
       is_private: false,
       documentation: "This is the type used to implement packed arrays where an alignment\nof 4 (if possible) is helpful for maximum efficiency of the get and\nset routines in the corresponding library unit. This is true of all\ncomponent sizes that are divisible by 4 (other than powers of 2, which\nare either handled by direct masking or not packed at all). In such\ncases the clusters can be assumed to be 4-byte aligned if the array\nis aligned (see System.Pack_12 in file s-pack12 as an example).",
       documentation_snippet: "type Packed_Bytes4 is new Packed_Bytes1;",
       }   ,
       {
       name: "Short_Short_Unsigned",
       qualified_name: "System.Unsigned_Types.Short_Short_Unsigned",
       signature: "system.unsigned_types.short_short_unsigned",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Short_Short_Unsigned is mod 2 ** Short_Short_Integer'Size;",
       }   ,
       {
       name: "Short_Unsigned",
       qualified_name: "System.Unsigned_Types.Short_Unsigned",
       signature: "system.unsigned_types.short_unsigned",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Short_Unsigned       is mod 2 ** Short_Integer'Size;",
       }   ,
       {
       name: "Unsigned",
       qualified_name: "System.Unsigned_Types.Unsigned",
       signature: "system.unsigned_types.unsigned",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Unsigned             is mod 2 ** Integer'Size;",
       }   ,
   ]
,array_types:    [
       {
       name: "Packed_Bytes1",
       qualified_name: "System.Unsigned_Types.Packed_Bytes1",
       signature: "system.unsigned_types.packed_bytes1",
       enclosing: "",
       is_private: false,
       documentation: "This is the type used to implement packed arrays where no alignment\nis required. This includes the cases of 1,2,4 (where we use direct\nmasking operations), and all odd component sizes (where the clusters\nare not aligned anyway, see, e.g. System.Pack_07 in file s-pack07\nfor details.",
       documentation_snippet: "type Packed_Bytes1 is array (Natural range <>) of Packed_Byte;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Bytes_F",
       qualified_name: "System.Unsigned_Types.Bytes_F",
       signature: "system.unsigned_types.bytes_f",
       enclosing: "",
       is_private: false,
       documentation: "Type used in implementation of Is_Negative intrinsic (see Exp_Intr)",
       documentation_snippet: "subtype Bytes_F is Packed_Bytes4 (1 .. Float'Size / 8);",
       }   ,
   ]
,}
---
