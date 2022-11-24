---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Types.Ustrings",
qualified_name: "Agpl.Types.Ustrings",
signature: "agpl.types.ustrings",
enclosing: "agpl.types",
is_private: false,
documentation: "----------------------------------------------------------------------\n Unbounded String Facilities                                        --\n----------------------------------------------------------------------",
documentation_snippet: "",
array_types:    [
       {
       name: "Ustring_Array",
       qualified_name: "Agpl.Types.Ustrings.Ustring_Array",
       signature: "agpl.types.ustrings.ustring_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Ustring_Array is array (Positive range <>) of Ustring;",
       }   ,
   ]
,subtypes:    [
       {
       name: "UString",
       qualified_name: "Agpl.Types.Ustrings.UString",
       signature: "agpl.types.ustrings.ustring",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype UString is ASU.Unbounded_String;",
       }   ,
   ]
,variables:    [
       {
       name: "Nul",
       qualified_name: "Agpl.Types.Ustrings.Nul",
       signature: "agpl.types.ustrings.nul",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Nul          : UString renames ASU.Null_Unbounded_String;",
       }   ,
       {
       name: "Null_Ustring",
       qualified_name: "Agpl.Types.Ustrings.Null_Ustring",
       signature: "agpl.types.ustrings.null_ustring",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Null_Ustring : UString renames ASU.Null_Unbounded_String;",
       }   ,
   ]
,}
---
