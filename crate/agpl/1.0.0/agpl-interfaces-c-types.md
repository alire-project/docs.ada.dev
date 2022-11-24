---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Interfaces.C.Types",
qualified_name: "Agpl.Interfaces.C.Types",
signature: "agpl.interfaces.c.types",
enclosing: "agpl.interfaces.c",
is_private: false,
documentation: "Types for interfacing with C/C++ commonly used across AGPL",
documentation_snippet: "",
simple_types:    [
       {
       name: "Agpl_Bool",
       qualified_name: "Agpl.Interfaces.C.Types.Agpl_Bool",
       signature: "agpl.interfaces.c.types.agpl_bool",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Agpl_Bool        is new Ic.Int;",
       }   ,
       {
       name: "Double",
       qualified_name: "Agpl.Interfaces.C.Types.Double",
       signature: "agpl.interfaces.c.types.double",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Double           is new Ic.Double;",
       }   ,
       {
       name: "Int",
       qualified_name: "Agpl.Interfaces.C.Types.Int",
       signature: "agpl.interfaces.c.types.int",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Int              is new Ic.Int;",
       }   ,
       {
       name: "Return_Code",
       qualified_name: "Agpl.Interfaces.C.Types.Return_Code",
       signature: "agpl.interfaces.c.types.return_code",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Return_Code      is new Ic.Int;",
       }   ,
       {
       name: "Void",
       qualified_name: "Agpl.Interfaces.C.Types.Void",
       signature: "agpl.interfaces.c.types.void",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Void is private;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Cstring",
       qualified_name: "Agpl.Interfaces.C.Types.Cstring",
       signature: "agpl.interfaces.c.types.cstring",
       enclosing: "",
       is_private: false,
       documentation: "A controlled layer over chars_ptr",
       documentation_snippet: "type Cstring is tagged private;",
       }   ,
       {
       name: "Void_Ptr_Limited",
       qualified_name: "Agpl.Interfaces.C.Types.Void_Ptr_Limited",
       signature: "agpl.interfaces.c.types.void_ptr_limited",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Void_Ptr_Limited is new Ada.Finalization.Limited_Controlled with record\n   Ptr : Void_Ptr;\nend record;",
       }   ,
       {
       name: "Void_Ptr_Nonlimited",
       qualified_name: "Agpl.Interfaces.C.Types.Void_Ptr_Nonlimited",
       signature: "agpl.interfaces.c.types.void_ptr_nonlimited",
       enclosing: "",
       is_private: false,
       documentation: "Note that default copy is a shallow copy!!!\n\n@field Ptr",
       documentation_snippet: "type Void_Ptr_Nonlimited is new Ada.Finalization.Controlled with record\n   Ptr : Void_Ptr;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Void_Ptr",
       qualified_name: "Agpl.Interfaces.C.Types.Void_Ptr",
       signature: "agpl.interfaces.c.types.void_ptr",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Void_Ptr is access all Void;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Char_Array",
       qualified_name: "Agpl.Interfaces.C.Types.Char_Array",
       signature: "agpl.interfaces.c.types.char_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Char_Array    is Ic.Char_Array;",
       }   ,
       {
       name: "Chars_Ptr",
       qualified_name: "Agpl.Interfaces.C.Types.Chars_Ptr",
       signature: "agpl.interfaces.c.types.chars_ptr",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Chars_Ptr     is Ic.Strings.Chars_Ptr;",
       }   ,
   ]
,constants:    [
       {
       name: "False",
       qualified_name: "Agpl.Interfaces.C.Types.False",
       signature: "agpl.interfaces.c.types.false",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "False : constant Agpl_Bool := 0;",
       }   ,
       {
       name: "Return_Err",
       qualified_name: "Agpl.Interfaces.C.Types.Return_Err",
       signature: "agpl.interfaces.c.types.return_err",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Return_Err : constant Return_Code := 1;",
       }   ,
       {
       name: "Return_Ok",
       qualified_name: "Agpl.Interfaces.C.Types.Return_Ok",
       signature: "agpl.interfaces.c.types.return_ok",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Return_Ok  : constant Return_Code := 0;",
       }   ,
       {
       name: "True",
       qualified_name: "Agpl.Interfaces.C.Types.True",
       signature: "agpl.interfaces.c.types.true",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "True  : constant Agpl_Bool := 1;",
       }   ,
   ]
,}
---
