---
crate: avrada_rts
layout: gnatdoc
gnatdoc: {
name: "Interfaces.C",
qualified_name: "Interfaces.C",
signature: "interfaces.c",
enclosing: "interfaces",
is_private: false,
documentation: "Declaration's based on C's <limits.h>",
documentation_snippet: "",
simple_types:    [
       {
       name: "C_float",
       qualified_name: "Interfaces.C.C_float",
       signature: "interfaces.c.c_float",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type C_float     is new Float;",
       }   ,
       {
       name: "char",
       qualified_name: "Interfaces.C.char",
       signature: "interfaces.c.char",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type char is new Character;",
       }   ,
       {
       name: "double",
       qualified_name: "Interfaces.C.double",
       signature: "interfaces.c.double",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type double      is new Standard.Long_Float;",
       }   ,
       {
       name: "int",
       qualified_name: "Interfaces.C.int",
       signature: "interfaces.c.int",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type int   is new Integer;",
       }   ,
       {
       name: "long",
       qualified_name: "Interfaces.C.long",
       signature: "interfaces.c.long",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type long  is new Long_Integer;",
       }   ,
       {
       name: "long_double",
       qualified_name: "Interfaces.C.long_double",
       signature: "interfaces.c.long_double",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type long_double is new Standard.Long_Long_Float;",
       }   ,
       {
       name: "ptrdiff_t",
       qualified_name: "Interfaces.C.ptrdiff_t",
       signature: "interfaces.c.ptrdiff_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type ptrdiff_t is\n  range -(2 ** (Standard'Address_Size - Integer'(1))) ..\n        +(2 ** (Standard'Address_Size - Integer'(1)) - 1);",
       }   ,
       {
       name: "short",
       qualified_name: "Interfaces.C.short",
       signature: "interfaces.c.short",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type short is new Short_Integer;",
       }   ,
       {
       name: "signed_char",
       qualified_name: "Interfaces.C.signed_char",
       signature: "interfaces.c.signed_char",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type signed_char is range SCHAR_MIN .. SCHAR_MAX;",
       }   ,
       {
       name: "size_t",
       qualified_name: "Interfaces.C.size_t",
       signature: "interfaces.c.size_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type size_t is mod 2 ** Standard'Address_Size;",
       }   ,
       {
       name: "unsigned",
       qualified_name: "Interfaces.C.unsigned",
       signature: "interfaces.c.unsigned",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type unsigned       is mod 2 ** int'Size;",
       }   ,
       {
       name: "unsigned_char",
       qualified_name: "Interfaces.C.unsigned_char",
       signature: "interfaces.c.unsigned_char",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type unsigned_char is mod (UCHAR_MAX + 1);",
       }   ,
       {
       name: "unsigned_long",
       qualified_name: "Interfaces.C.unsigned_long",
       signature: "interfaces.c.unsigned_long",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type unsigned_long  is mod 2 ** long'Size;",
       }   ,
       {
       name: "unsigned_short",
       qualified_name: "Interfaces.C.unsigned_short",
       signature: "interfaces.c.unsigned_short",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type unsigned_short is mod 2 ** short'Size;",
       }   ,
   ]
,array_types:    [
       {
       name: "char_array",
       qualified_name: "Interfaces.C.char_array",
       signature: "interfaces.c.char_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type char_array is array (size_t range <>) of aliased char;",
       }   ,
   ]
,subtypes:    [
       {
       name: "plain_char",
       qualified_name: "Interfaces.C.plain_char",
       signature: "interfaces.c.plain_char",
       enclosing: "",
       is_private: false,
       documentation: "??? should be parameterized",
       documentation_snippet: "subtype plain_char is unsigned_char;",
       }   ,
   ]
,constants:    [
       {
       name: "CHAR_BIT",
       qualified_name: "Interfaces.C.CHAR_BIT",
       signature: "interfaces.c.char_bit",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "CHAR_BIT  : constant := 8;",
       }   ,
       {
       name: "nul",
       qualified_name: "Interfaces.C.nul",
       signature: "interfaces.c.nul",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "nul : constant char := char'First;",
       }   ,
       {
       name: "SCHAR_MAX",
       qualified_name: "Interfaces.C.SCHAR_MAX",
       signature: "interfaces.c.schar_max",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "SCHAR_MAX : constant := 127;",
       }   ,
       {
       name: "SCHAR_MIN",
       qualified_name: "Interfaces.C.SCHAR_MIN",
       signature: "interfaces.c.schar_min",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "SCHAR_MIN : constant := -128;",
       }   ,
       {
       name: "UCHAR_MAX",
       qualified_name: "Interfaces.C.UCHAR_MAX",
       signature: "interfaces.c.uchar_max",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "UCHAR_MAX : constant := 255;",
       }   ,
   ]
,}
---