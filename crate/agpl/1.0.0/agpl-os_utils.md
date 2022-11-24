---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Os_Utils",
qualified_name: "Agpl.Os_Utils",
signature: "agpl.os_utils",
enclosing: "agpl",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Address_Kinds",
       qualified_name: "Agpl.Os_Utils.Address_Kinds",
       signature: "agpl.os_utils.address_kinds",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Address_Kinds is (Malformed, Local, Internal, Public);",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Address_Vector",
       qualified_name: "Agpl.Os_Utils.Address_Vector",
       signature: "agpl.os_utils.address_vector",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Address_Vector is\n  new Agpl.Containers.String_Vectors.Vector with null record;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Address_Cursor",
       qualified_name: "Agpl.Os_Utils.Address_Cursor",
       signature: "agpl.os_utils.address_cursor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Address_Cursor is Agpl.Containers.String_Vectors.Cursor;",
       }   ,
   ]
,}
---
