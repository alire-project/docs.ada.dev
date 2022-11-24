---
crate: hmac
layout: gnatdoc
gnatdoc: {
name: "HMAC_Generic",
qualified_name: "HMAC_Generic",
signature: "hmac_generic",
enclosing: "",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Context",
       qualified_name: "HMAC_Generic.Context",
       signature: "hmac_generic.context",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Context is private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Digest",
       qualified_name: "HMAC_Generic.Digest",
       signature: "hmac_generic.digest",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Digest is Element_Array (0 .. Digest_Length - 1);",
       }   ,
   ]
,}
---
