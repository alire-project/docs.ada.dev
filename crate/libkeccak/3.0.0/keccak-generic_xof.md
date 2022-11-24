---
crate: libkeccak
layout: gnatdoc
gnatdoc: {
name: "Keccak.Generic_XOF",
qualified_name: "Keccak.Generic_XOF",
signature: "keccak.generic_xof",
enclosing: "keccak",
is_private: false,
documentation: "Import common types from Keccak.Types to avoid users of the\npackage to be dependent on Keccak.Types.\n\n@formal Capacity\n  Sponge capacity in bits.\n  \n  This must be a multiple of 8, and must be smaller than the state size.\n@formal Suffix\n@formal Suffix_Size\n@formal Permutation_Initial_Value\n  An optional inital value for the permutation state.\n  \n  If non-empty, this data block will be written to the permutation state\n  and then the permutation function will be applied. Otherwise, the\n  permutation state will be zero-initialised.\n  \n  The length of this parameter cannot exceed the permutation state size.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Context",
       qualified_name: "Keccak.Generic_XOF.Context",
       signature: "keccak.generic_xof.context",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Context is private;",
       }   ,
       {
       name: "States",
       qualified_name: "Keccak.Generic_XOF.States",
       signature: "keccak.generic_xof.states",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type States is (Updating, Ready_To_Extract, Extracting);",
       }   ,
   ]
,subtypes:    [
       {
       name: "Byte",
       qualified_name: "Keccak.Generic_XOF.Byte",
       signature: "keccak.generic_xof.byte",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Byte is Keccak.Types.Byte;",
       }   ,
       {
       name: "Byte_Array",
       qualified_name: "Keccak.Generic_XOF.Byte_Array",
       signature: "keccak.generic_xof.byte_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Byte_Array   is Keccak.Types.Byte_Array;",
       }   ,
       {
       name: "Index_Number",
       qualified_name: "Keccak.Generic_XOF.Index_Number",
       signature: "keccak.generic_xof.index_number",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Index_Number is Keccak.Types.Index_Number;",
       }   ,
       {
       name: "Rate_Bits_Number",
       qualified_name: "Keccak.Generic_XOF.Rate_Bits_Number",
       signature: "keccak.generic_xof.rate_bits_number",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Rate_Bits_Number is XOF_Sponge.Rate_Bits_Number;",
       }   ,
   ]
,}
---
