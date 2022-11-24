---
crate: libkeccak
layout: gnatdoc
gnatdoc: {
name: "Keccak.Generic_Hash",
qualified_name: "Keccak.Generic_Hash",
signature: "keccak.generic_hash",
enclosing: "keccak",
is_private: false,
documentation: "Import common types from Keccak.Types to avoid users of the\npackage to be dependent on Keccak.Types.\n\n@formal Digest_Size\n  Output digest size in bits. E.g. for SHA3-256 Digest_Size=256\n@formal Capacity\n  The capacity of the hash. By default the capacity is twice the digest size.\n  \n  The Rate is calculated as Hash_Sponge.State_Size - Capacity, and the value\n  for the capacity must be chosen so that the rate is a multiple of 8.\n@formal Suffix\n  Up to 8 bits that are appended to the message before padding bits.\n  \n  The least significant bit is the first bit that is appended.\n@formal Suffix_Size\n  The number of bits in the Suffix to append. This must be a value\n  in the range 0 .. 8.\n@formal Permutation_Initial_Value\n  An optional inital value for the permutation state.\n  \n  If non-empty, this data block will be written to the permutation state\n  and then the permutation function will be applied. Otherwise, the\n  permutation state will be zero-initialised.\n  \n  The length of this parameter cannot exceed the permutation state size.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Context",
       qualified_name: "Keccak.Generic_Hash.Context",
       signature: "keccak.generic_hash.context",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Context is private;",
       }   ,
       {
       name: "States",
       qualified_name: "Keccak.Generic_Hash.States",
       signature: "keccak.generic_hash.states",
       enclosing: "",
       is_private: false,
       documentation: "The possible states for the context.\n\n@value Updating When in this state the context can be fed\nwith input data by calling the Update procedure.\n\n@value Ready_To_Finish When in this state the Update procedure can\nno longer be called (i.e. no more data can be input to the context),\nand the context is ready to compute the final hash value.\n\n@value Finished When in this state the final hash value has been computed\nand the context can not be used further. However, the context could be\nre-initialized and used again for a new hash computation.\n\n@enum Updating\n@enum Ready_To_Finish\n@enum Finished",
       documentation_snippet: "type States is (Updating, Ready_To_Finish, Finished);",
       }   ,
   ]
,subtypes:    [
       {
       name: "Byte",
       qualified_name: "Keccak.Generic_Hash.Byte",
       signature: "keccak.generic_hash.byte",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Byte is Keccak.Types.Byte;",
       }   ,
       {
       name: "Byte_Array",
       qualified_name: "Keccak.Generic_Hash.Byte_Array",
       signature: "keccak.generic_hash.byte_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Byte_Array   is Keccak.Types.Byte_Array;",
       }   ,
       {
       name: "Digest_Index",
       qualified_name: "Keccak.Generic_Hash.Digest_Index",
       signature: "keccak.generic_hash.digest_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Digest_Index is Keccak.Types.Index_Number\nrange 0 .. (Keccak.Types.Index_Number (Digest_Size) / 8) - 1;",
       }   ,
       {
       name: "Digest_Type",
       qualified_name: "Keccak.Generic_Hash.Digest_Type",
       signature: "keccak.generic_hash.digest_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Digest_Type is Keccak.Types.Byte_Array (Digest_Index);",
       }   ,
       {
       name: "Index_Number",
       qualified_name: "Keccak.Generic_Hash.Index_Number",
       signature: "keccak.generic_hash.index_number",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Index_Number is Keccak.Types.Index_Number;",
       }   ,
       {
       name: "Rate_Bits_Number",
       qualified_name: "Keccak.Generic_Hash.Rate_Bits_Number",
       signature: "keccak.generic_hash.rate_bits_number",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Rate_Bits_Number is Hash_Sponge.Rate_Bits_Number;",
       }   ,
   ]
,}
---
