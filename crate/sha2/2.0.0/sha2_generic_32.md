---
crate: sha2
layout: gnatdoc
gnatdoc: {
name: "SHA2_Generic_32",
qualified_name: "SHA2_Generic_32",
signature: "sha2_generic_32",
enclosing: "",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Context",
       qualified_name: "SHA2_Generic_32.Context",
       signature: "sha2_generic_32.context",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Context is private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Digest",
       qualified_name: "SHA2_Generic_32.Digest",
       signature: "sha2_generic_32.digest",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Digest is Element_Array (0 .. Digest_Length - 1);",
       }   ,
   ]
,constants:    [
       {
       name: "Block_Length",
       qualified_name: "SHA2_Generic_32.Block_Length",
       signature: "sha2_generic_32.block_length",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Block_Length  : constant Index := 64;",
       }   ,
       {
       name: "Digest_Length",
       qualified_name: "SHA2_Generic_32.Digest_Length",
       signature: "sha2_generic_32.digest_length",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Digest_Length : constant Index := Length;",
       }   ,
   ]
,}
---
