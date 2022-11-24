---
crate: langkit_support
layout: gnatdoc
gnatdoc: {
name: "Langkit_Support.Internal",
qualified_name: "Langkit_Support.Internal",
signature: "langkit_support.internal",
enclosing: "langkit_support",
is_private: false,
documentation: "\nCopyright (C) 2014-2022, AdaCore\nSPDX-License-Identifier: Apache-2.0",
documentation_snippet: "",
array_types:    [
       {
       name: "Token_Kind_Name_Array",
       qualified_name: "Langkit_Support.Internal.Token_Kind_Name_Array",
       signature: "langkit_support.internal.token_kind_name_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Token_Kind_Name_Array is\n  array (Token_Kind_Index range <>) of Text_Access;",
       }   ,
   ]
,access_types:    [
       {
       name: "Debug_String_Access",
       qualified_name: "Langkit_Support.Internal.Debug_String_Access",
       signature: "langkit_support.internal.debug_string_access",
       enclosing: "",
       is_private: false,
       documentation: "Reference to a statically allocated String. Used in descriptor tables\nwhenever we need to provide string for debug (compatible with\nAda.Text_IO).",
       documentation_snippet: "type Debug_String_Access is not null access constant String;",
       }   ,
       {
       name: "Text_Access",
       qualified_name: "Langkit_Support.Internal.Text_Access",
       signature: "langkit_support.internal.text_access",
       enclosing: "",
       is_private: false,
       documentation: "Reference to a static Unicode string. Used in descriptor tables whenever\nwe need to provide a name.",
       documentation_snippet: "type Text_Access is not null access constant Text_Type;",
       }   ,
       {
       name: "Token_Kind_Name_Array_Access",
       qualified_name: "Langkit_Support.Internal.Token_Kind_Name_Array_Access",
       signature: "langkit_support.internal.token_kind_name_array_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Token_Kind_Name_Array_Access is\n  not null access constant Token_Kind_Name_Array;",
       }   ,
   ]
,}
---
