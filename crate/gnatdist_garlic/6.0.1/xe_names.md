---
crate: gnatdist_garlic
layout: gnatdoc
gnatdoc: {
name: "XE_Names",
qualified_name: "XE_Names",
signature: "xe_names",
enclosing: "",
is_private: false,
documentation: "This package contains routines for handling the names table. The table\nis used to store character strings for identifiers and operator symbols,\nas well as other string values such as unit names and file names.",
documentation_snippet: "",
variables:    [
       {
       name: "Name_Buffer",
       qualified_name: "XE_Names.Name_Buffer",
       signature: "xe_names.name_buffer",
       enclosing: "",
       is_private: false,
       documentation: "This buffer is used to set the name to be stored in the table for the\nName_Find call, and to retrieve the name for the Get_Name_String call.\nThe plus 1 in the length allows for cases of adding ASCII.NUL. The\n16K here is intended to be an infinite value that ensures that we\nnever overflow the buffer (names this long are too absurd to worry!)",
       documentation_snippet: "Name_Buffer : String (1 .. 16 * 1024);",
       }   ,
       {
       name: "Name_Len",
       qualified_name: "XE_Names.Name_Len",
       signature: "xe_names.name_len",
       enclosing: "",
       is_private: false,
       documentation: "Length of name stored in Name_Buffer. Used as an input parameter for\nName_Find, and as an output value by Get_Name_String, or Write_Name.",
       documentation_snippet: "Name_Len : Natural;",
       }   ,
   ]
,}
---
