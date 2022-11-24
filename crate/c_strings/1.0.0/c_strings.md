---
crate: c_strings
layout: gnatdoc
gnatdoc: {
name: "C_Strings",
qualified_name: "C_Strings",
signature: "c_strings",
enclosing: "",
is_private: false,
documentation: "Intended use: in calls to C subprograms that expect a pointer to char,\n  which -fada-dump-spec translates as Chars_Ptr, do:\n  Call_To_C (C_Strings.To_C (\"whatever\").To_Ptr);",
documentation_snippet: "",
tagged_types:    [
       {
       name: "C_String",
       qualified_name: "C_Strings.C_String",
       signature: "c_strings.c_string",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type C_String (<>) is tagged limited private;",
       }   ,
   ]
,variables:    [
       {
       name: "Null_Ptr",
       qualified_name: "C_Strings.Null_Ptr",
       signature: "c_strings.null_ptr",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Null_Ptr : CS.Chars_Ptr renames CS.Null_Ptr;",
       }   ,
   ]
,}
---
