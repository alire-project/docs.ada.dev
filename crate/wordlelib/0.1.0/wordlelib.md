---
crate: wordlelib
layout: gnatdoc
gnatdoc: {
name: "Wordlelib",
qualified_name: "Wordlelib",
signature: "wordlelib",
enclosing: "",
is_private: false,
documentation: "Re-export parameter\n\n@formal Word_Length",
documentation_snippet: "",
simple_types:    [
       {
       name: "Guess_Kind",
       qualified_name: "Wordlelib.Guess_Kind",
       signature: "wordlelib.guess_kind",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Guess_Kind is (Hit, Missplaced, Miss);",
       }   ,
   ]
,array_types:    [
       {
       name: "Attempt_Array",
       qualified_name: "Wordlelib.Attempt_Array",
       signature: "wordlelib.attempt_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Attempt_Array is array (Positive range <>) of Word;",
       }   ,
       {
       name: "Guess_Array",
       qualified_name: "Wordlelib.Guess_Array",
       signature: "wordlelib.guess_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Guess_Array is array (Positive range <>) of Guess_Result;",
       }   ,
       {
       name: "Guess_Result",
       qualified_name: "Wordlelib.Guess_Result",
       signature: "wordlelib.guess_result",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Guess_Result is array (1 .. Word_Length) of Guess_Kind;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Game",
       qualified_name: "Wordlelib.Game",
       signature: "wordlelib.game",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Game (<>) is tagged private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Valid_Chars",
       qualified_name: "Wordlelib.Valid_Chars",
       signature: "wordlelib.valid_chars",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Valid_Chars is Character range 'A' .. 'Z';",
       }   ,
       {
       name: "Word",
       qualified_name: "Wordlelib.Word",
       signature: "wordlelib.word",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Word is String (1 .. Word_Length) with\n  Dynamic_Predicate => (for all Char of Word => Char in Valid_Chars);",
       }   ,
   ]
,constants:    [
       {
       name: "Word_Length_Used",
       qualified_name: "Wordlelib.Word_Length_Used",
       signature: "wordlelib.word_length_used",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Word_Length_Used : constant Positive := Word_Length;",
       }   ,
   ]
,}
---
