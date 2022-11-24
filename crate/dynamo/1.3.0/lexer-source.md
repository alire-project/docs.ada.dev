---
crate: dynamo
layout: gnatdoc
gnatdoc: {
name: "Lexer.Source",
qualified_name: "Lexer.Source",
signature: "lexer.source",
enclosing: "lexer",
is_private: false,
documentation: "a Source is anything that provides a character stream. Sources are always\nsingle-use objects; the lexer takes ownership of sources and deallocates\nthem.",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Instance",
       qualified_name: "Lexer.Source.Instance",
       signature: "lexer.source.instance",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Instance is abstract new Ada.Finalization.Limited_Controlled with\n  null record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Pointer",
       qualified_name: "Lexer.Source.Pointer",
       signature: "lexer.source.pointer",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Pointer is access all Instance'Class;",
       }   ,
   ]
,}
---
