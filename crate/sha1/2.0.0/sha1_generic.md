---
crate: sha1
layout: gnatdoc
gnatdoc: {
name: "SHA1_Generic",
qualified_name: "SHA1_Generic",
signature: "sha1_generic",
enclosing: "",
is_private: false,
documentation: "@summary\nGeneric Secure Hash Algorithm 1 implementation in Ada\n\n@description\nThis package provides implementation of SHA1 algorithm and operates on\na generic Element_Array type, which represents an array of bytes.\n\n@formal Element\n  Element represents one byte of data\n@formal Index\n  Index type of the Element_Array\n@formal Element_Array\n  An array of bytes",
documentation_snippet: "",
simple_types:    [
       {
       name: "Context",
       qualified_name: "SHA1_Generic.Context",
       signature: "sha1_generic.context",
       enclosing: "",
       is_private: false,
       documentation: "Algorithm context, holds all of the necessary internal data. Always\ninitialized with correct data, calling Initialize() functions is not\nrequired but is strongly advised.",
       documentation_snippet: "type Context is private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Digest",
       qualified_name: "SHA1_Generic.Digest",
       signature: "sha1_generic.digest",
       enclosing: "",
       is_private: false,
       documentation: "Type representing the result of a hash function",
       documentation_snippet: "subtype Digest is Element_Array (0 .. Digest_Length - 1);",
       }   ,
   ]
,constants:    [
       {
       name: "Block_Length",
       qualified_name: "SHA1_Generic.Block_Length",
       signature: "sha1_generic.block_length",
       enclosing: "",
       is_private: false,
       documentation: "Block length (in bytes), not very useful for the end user",
       documentation_snippet: "Block_Length : constant Index := 64;",
       }   ,
       {
       name: "Digest_Length",
       qualified_name: "SHA1_Generic.Digest_Length",
       signature: "sha1_generic.digest_length",
       enclosing: "",
       is_private: false,
       documentation: "Length (in bytes) of the hash result",
       documentation_snippet: "Digest_Length : constant Index := 20;",
       }   ,
   ]
,}
---
