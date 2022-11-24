---
crate: sparknacl
layout: gnatdoc
gnatdoc: {
name: "SPARKNaCl.Stream",
qualified_name: "SPARKNaCl.Stream",
signature: "sparknacl.stream",
enclosing: "sparknacl",
is_private: false,
documentation: "Distinct from Bytes_32, but both inherit Equal,\nRandom_Bytes, and Sanitize primitive operations.",
documentation_snippet: "",
simple_types:    [
       {
       name: "HSalsa20_Nonce",
       qualified_name: "SPARKNaCl.Stream.HSalsa20_Nonce",
       signature: "sparknacl.stream.hsalsa20_nonce",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type HSalsa20_Nonce is new Bytes_24;",
       }   ,
       {
       name: "Salsa20_Nonce",
       qualified_name: "SPARKNaCl.Stream.Salsa20_Nonce",
       signature: "sparknacl.stream.salsa20_nonce",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Salsa20_Nonce  is new Bytes_8;",
       }   ,
   ]
,}
---
