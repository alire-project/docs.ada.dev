---
crate: lace_swig
layout: gnatdoc
gnatdoc: {
name: "Swig",
qualified_name: "Swig",
signature: "swig",
enclosing: "",
is_private: false,
documentation: "Elementary types.",
documentation_snippet: "",
simple_types:    [
       {
       name: "intptr_t",
       qualified_name: "Swig.intptr_t",
       signature: "swig.intptr_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type    intptr_t              is range -(2 ** (Standard'Address_Size - Integer'(1))) .. +(2 ** (Standard'Address_Size - Integer'(1)) - 1);",
       }   ,
       {
       name: "uintptr_t",
       qualified_name: "Swig.uintptr_t",
       signature: "swig.uintptr_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type   uintptr_t              is mod 2 ** Standard'Address_Size;",
       }   ,
       {
       name: "unsigned_long_Long",
       qualified_name: "Swig.unsigned_long_Long",
       signature: "swig.unsigned_long_long",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type    unsigned_long_Long    is mod 2 ** 64;",
       }   ,
   ]
,array_types:    [
       {
       name: "bool_Array",
       qualified_name: "Swig.bool_Array",
       signature: "swig.bool_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type bool_Array               is array (interfaces.c.size_t range <>) of aliased swig.bool;",
       }   ,
       {
       name: "double_Array",
       qualified_name: "Swig.double_Array",
       signature: "swig.double_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type double_Array             is array (interfaces.c.size_t range <>) of aliased interfaces.c.Double;",
       }   ,
       {
       name: "float_Array",
       qualified_name: "Swig.float_Array",
       signature: "swig.float_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type float_Array              is array (interfaces.c.size_t range <>) of aliased interfaces.c.c_Float;",
       }   ,
       {
       name: "int16_t_Array",
       qualified_name: "Swig.int16_t_Array",
       signature: "swig.int16_t_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type int16_t_Array            is array (interfaces.c.size_t range <>) of aliased swig.int16_t;",
       }   ,
       {
       name: "int32_t_Array",
       qualified_name: "Swig.int32_t_Array",
       signature: "swig.int32_t_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type int32_t_Array            is array (interfaces.c.size_t range <>) of aliased swig.int32_t;",
       }   ,
       {
       name: "int64_t_Array",
       qualified_name: "Swig.int64_t_Array",
       signature: "swig.int64_t_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type int64_t_Array            is array (interfaces.c.size_t range <>) of aliased swig.int64_t;",
       }   ,
       {
       name: "int8_t_Array",
       qualified_name: "Swig.int8_t_Array",
       signature: "swig.int8_t_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type int8_t_Array             is array (interfaces.c.size_t range <>) of aliased swig.int8_t;",
       }   ,
       {
       name: "int_Array",
       qualified_name: "Swig.int_Array",
       signature: "swig.int_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type int_Array                is array (interfaces.c.size_t range <>) of aliased interfaces.c.Int;",
       }   ,
       {
       name: "long_Array",
       qualified_name: "Swig.long_Array",
       signature: "swig.long_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type long_Array               is array (interfaces.c.size_t range <>) of aliased interfaces.c.Long;",
       }   ,
       {
       name: "long_double_Array",
       qualified_name: "Swig.long_double_Array",
       signature: "swig.long_double_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type long_double_Array        is array (interfaces.c.size_t range <>) of aliased interfaces.c.long_Double;",
       }   ,
       {
       name: "long_long_Array",
       qualified_name: "Swig.long_long_Array",
       signature: "swig.long_long_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type long_long_Array          is array (interfaces.c.size_t range <>) of aliased swig.long_Long;",
       }   ,
       {
       name: "short_Array",
       qualified_name: "Swig.short_Array",
       signature: "swig.short_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type short_Array              is array (interfaces.c.size_t range <>) of aliased interfaces.c.Short;",
       }   ,
       {
       name: "signed_char_Array",
       qualified_name: "Swig.signed_char_Array",
       signature: "swig.signed_char_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type signed_char_Array        is array (interfaces.c.size_t range <>) of aliased interfaces.c.signed_Char;",
       }   ,
       {
       name: "size_t_Array",
       qualified_name: "Swig.size_t_Array",
       signature: "swig.size_t_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type size_t_Array             is array (interfaces.c.size_t range <>) of aliased interfaces.c.Size_t;",
       }   ,
       {
       name: "uint16_t_Array",
       qualified_name: "Swig.uint16_t_Array",
       signature: "swig.uint16_t_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type uint16_t_Array           is array (interfaces.c.size_t range <>) of aliased swig.uint16_t;",
       }   ,
       {
       name: "uint32_t_Array",
       qualified_name: "Swig.uint32_t_Array",
       signature: "swig.uint32_t_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type uint32_t_Array           is array (interfaces.c.size_t range <>) of aliased swig.uint32_t;",
       }   ,
       {
       name: "uint64_t_Array",
       qualified_name: "Swig.uint64_t_Array",
       signature: "swig.uint64_t_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type uint64_t_Array           is array (interfaces.c.size_t range <>) of aliased swig.uint64_t;",
       }   ,
       {
       name: "uint8_t_Array",
       qualified_name: "Swig.uint8_t_Array",
       signature: "swig.uint8_t_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type uint8_t_Array            is array (interfaces.c.size_t range <>) of aliased swig.uint8_t;",
       }   ,
       {
       name: "unsigned_Array",
       qualified_name: "Swig.unsigned_Array",
       signature: "swig.unsigned_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type unsigned_Array           is array (interfaces.c.size_t range <>) of aliased interfaces.c.Unsigned;",
       }   ,
       {
       name: "unsigned_char_Array",
       qualified_name: "Swig.unsigned_char_Array",
       signature: "swig.unsigned_char_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type unsigned_char_Array      is array (interfaces.c.size_t range <>) of aliased interfaces.c.unsigned_Char;",
       }   ,
       {
       name: "unsigned_long_Array",
       qualified_name: "Swig.unsigned_long_Array",
       signature: "swig.unsigned_long_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type unsigned_long_Array      is array (interfaces.c.size_t range <>) of aliased interfaces.c.unsigned_Long;",
       }   ,
       {
       name: "unsigned_long_long_Array",
       qualified_name: "Swig.unsigned_long_long_Array",
       signature: "swig.unsigned_long_long_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type unsigned_long_long_Array is array (interfaces.c.size_t range <>) of aliased swig.unsigned_long_Long;",
       }   ,
       {
       name: "unsigned_short_Array",
       qualified_name: "Swig.unsigned_short_Array",
       signature: "swig.unsigned_short_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type unsigned_short_Array     is array (interfaces.c.size_t range <>) of aliased interfaces.c.unsigned_Short;",
       }   ,
       {
       name: "void_ptr_Array",
       qualified_name: "Swig.void_ptr_Array",
       signature: "swig.void_ptr_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type void_ptr_Array           is array (interfaces.c.size_t range <>) of aliased swig.void_ptr;",
       }   ,
   ]
,subtypes:    [
       {
       name: "bool",
       qualified_name: "Swig.bool",
       signature: "swig.bool",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype bool                  is interfaces.c.plain_char;",
       }   ,
       {
       name: "incomplete_class",
       qualified_name: "Swig.incomplete_class",
       signature: "swig.incomplete_class",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype incomplete_class      is System.Address;",
       }   ,
       {
       name: "int16_t",
       qualified_name: "Swig.int16_t",
       signature: "swig.int16_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype int16_t               is interfaces.Integer_16;",
       }   ,
       {
       name: "int32_t",
       qualified_name: "Swig.int32_t",
       signature: "swig.int32_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype int32_t               is interfaces.Integer_32;",
       }   ,
       {
       name: "int64_t",
       qualified_name: "Swig.int64_t",
       signature: "swig.int64_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype int64_t               is interfaces.Integer_64;",
       }   ,
       {
       name: "int8_t",
       qualified_name: "Swig.int8_t",
       signature: "swig.int8_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype int8_t                is interfaces.Integer_8;",
       }   ,
       {
       name: "long_Long",
       qualified_name: "Swig.long_Long",
       signature: "swig.long_long",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype long_Long             is long_long_Integer;",
       }   ,
       {
       name: "opaque_structure",
       qualified_name: "Swig.opaque_structure",
       signature: "swig.opaque_structure",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype opaque_structure      is System.Address;",
       }   ,
       {
       name: "uint16_t",
       qualified_name: "Swig.uint16_t",
       signature: "swig.uint16_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype uint16_t              is interfaces.unSigned_16;",
       }   ,
       {
       name: "uint32_t",
       qualified_name: "Swig.uint32_t",
       signature: "swig.uint32_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype uint32_t              is interfaces.unSigned_32;",
       }   ,
       {
       name: "uint64_t",
       qualified_name: "Swig.uint64_t",
       signature: "swig.uint64_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype uint64_t              is interfaces.unSigned_64;",
       }   ,
       {
       name: "uint8_t",
       qualified_name: "Swig.uint8_t",
       signature: "swig.uint8_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype uint8_t               is interfaces.unSigned_8;",
       }   ,
       {
       name: "void",
       qualified_name: "Swig.void",
       signature: "swig.void",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype void                  is System.Address;",
       }   ,
       {
       name: "void_ptr",
       qualified_name: "Swig.void_ptr",
       signature: "swig.void_ptr",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype void_ptr              is System.Address;",
       }   ,
   ]
,}
---