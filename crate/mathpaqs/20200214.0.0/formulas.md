---
crate: mathpaqs
layout: gnatdoc
gnatdoc: {
name: "Formulas",
qualified_name: "Formulas",
signature: "formulas",
enclosing: "",
is_private: false,
documentation: "TO DO:\n  - implement user functions\n  - (never-ending) improve Simplify (see misses at Test_Formulas)\n\n@formal Real\n  Payload can be a helper for user variables.\n  For instance, formulas can be associated to different objects where\n  user variables may have different values.\n@formal Payload_type\n@formal Evaluate_variable",
documentation_snippet: "",
simple_types:    [
       {
       name: "Output_style",
       qualified_name: "Formulas.Output_style",
       signature: "formulas.output_style",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum normal\n  Normal is infix, should be the closest to the parsed formula\n@enum bracketed\n  Like normal, but displays a {} around every parse tree node",
       documentation_snippet: "type Output_style is (\n  normal,\n  bracketed\n);",
       }   ,
   ]
,array_types:    [
       {
       name: "Character_Set",
       qualified_name: "Formulas.Character_Set",
       signature: "formulas.character_set",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Character_Set is array (Character) of Boolean;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Formula",
       qualified_name: "Formulas.Formula",
       signature: "formulas.formula",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Formula is tagged private;",
       }   ,
   ]
,access_types:    [
       {
       name: "List_proc",
       qualified_name: "Formulas.List_proc",
       signature: "formulas.list_proc",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type List_proc is access procedure (name : String; parameters : Natural);",
       }   ,
   ]
,constants:    [
       {
       name: "following_character",
       qualified_name: "Formulas.following_character",
       signature: "formulas.following_character",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "following_character  : constant Character_Set :=\n  ('a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' | '$' | '.' => True, others => False);",
       }   ,
       {
       name: "letters",
       qualified_name: "Formulas.letters",
       signature: "formulas.letters",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "letters  : constant Character_Set :=\n  ('a' .. 'z' | 'A' .. 'Z' => True, others => False);",
       }   ,
   ]
,}
---
