---
crate: hangman
layout: gnatdoc
gnatdoc: {
name: "hangman",
qualified_name: "hangman",
signature: "hangman",
enclosing: "",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "List_Type",
       qualified_name: "hangman.List_Type",
       signature: "hangman.list_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type List_Type is private;",
       }   ,
   ]
,array_types:    [
       {
       name: "alpha",
       qualified_name: "hangman.alpha",
       signature: "hangman.alpha",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Type alpha is Array (Positive range <>) of Character;",
       }   ,
       {
       name: "ManArray",
       qualified_name: "hangman.ManArray",
       signature: "hangman.manarray",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Type ManArray is Array (1..11) of Line;",
       }   ,
       {
       name: "SArray",
       qualified_name: "hangman.SArray",
       signature: "hangman.sarray",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Type SArray is Array (Positive range <>) of Character;",
       }   ,
   ]
,record_types:    [
       {
       name: "SType",
       qualified_name: "hangman.SType",
       signature: "hangman.stype",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Type SType (Size: Positive) is	record\n	Top : Natural := 0;\n    Store : SArray (1..Size);\nEnd record;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Line",
       qualified_name: "hangman.Line",
       signature: "hangman.line",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Subtype Line is String(1..18);",
       }   ,
       {
       name: "rng",
       qualified_name: "hangman.rng",
       signature: "hangman.rng",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype rng is positive range 1 .. 100;",
       }   ,
   ]
,}
---
