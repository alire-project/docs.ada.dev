---
crate: dynamo
layout: gnatdoc
gnatdoc: {
name: "Text",
qualified_name: "Text",
signature: "text",
enclosing: "",
is_private: false,
documentation: "this package defines a reference-counted string pointer type. it is used\nfor all YAML data entities and relieves the user from the need to\nmanually dispose events created by the parser.\n\ntypically, YAML content strings are deallocated in the same order as they\nare allocated. this knowledge is built into a storage pool for efficient\nmemory usage and to avoid fragmentation.\n\nto be able to efficiently interface with C, this package allocates its\nstrings so that they can directly be passed on to C without the need to\ncopy any data. Use the subroutines Export and Delete_Exported to get\nC-compatible string values from a Reference. these subroutines also\ntake care of reference counting for values exposed to C. this means that\nafter exporting a value, you *must* eventually call Delete_Exported in\norder for the value to be freed.\n\nHINT: this package makes use of compiler implementation details and may\nnot work with other compilers. however, since there currently are no\nAda 2012 compilers but GNAT, this is not considered a problem.",
documentation_snippet: "",
access_types:    [
       {
       name: "UTF_8_String_Access",
       qualified_name: "Text.UTF_8_String_Access",
       signature: "text.utf_8_string_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type UTF_8_String_Access is access UTF_8_String;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Constant_Instance",
       qualified_name: "Text.Constant_Instance",
       signature: "text.constant_instance",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Constant_Instance is Reference;",
       }   ,
       {
       name: "Pool_Offset",
       qualified_name: "Text.Pool_Offset",
       signature: "text.pool_offset",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Pool_Offset is System.Storage_Elements.Storage_Offset\nrange 0 .. System.Storage_Elements.Storage_Offset (Integer'Last);",
       }   ,
       {
       name: "Reference",
       qualified_name: "Text.Reference",
       signature: "text.reference",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Reference is Ada.Strings.Unbounded.Unbounded_String;",
       }   ,
       {
       name: "UTF_8_String",
       qualified_name: "Text.UTF_8_String",
       signature: "text.utf_8_string",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype UTF_8_String is Ada.Strings.UTF_Encoding.UTF_8_String;",
       }   ,
   ]
,constants:    [
       {
       name: "Empty",
       qualified_name: "Text.Empty",
       signature: "text.empty",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Empty : constant Reference;",
       }   ,
   ]
,}
---
