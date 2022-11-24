---
crate: rewriters
layout: gnatdoc
gnatdoc: {
name: "Predefined_Rewriters_Append",
qualified_name: "Predefined_Rewriters_Append",
signature: "predefined_rewriters_append",
enclosing: "",
is_private: false,
documentation: "",
documentation_snippet: "",
constants:    [
       {
       name: "Rewriter_Ampersand_Prefer_Append",
       qualified_name: "Predefined_Rewriters_Append.Rewriter_Ampersand_Prefer_Append",
       signature: "predefined_rewriters_append.rewriter_ampersand_prefer_append",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Rewriter_Ampersand_Prefer_Append :\naliased constant Rewriter_Find_And_Replace :=\n  Make_Rewriter_Find_And_Replace\n    (Make_Pattern (\"$S_Var := $S_Var & $S_Tail;\", Assignment_Stmt_Rule),\n     Make_Pattern (\"Append ($S_Var, $S_Tail);\", Call_Stmt_Rule),\n     Make_Match_Accepter_Function_Access\n       (Accept_Var_Unbounded_String'Access));",
       }   ,
       {
       name: "Rewriter_Append",
       qualified_name: "Predefined_Rewriters_Append.Rewriter_Append",
       signature: "predefined_rewriters_append.rewriter_append",
       enclosing: "",
       is_private: false,
       documentation: "Rewriter for patterns to improve the usage of the `Append` function.",
       documentation_snippet: "Rewriter_Append : aliased constant Rewriter_Sequence :=\n  Make_Rewriter_Sequence\n    (Rewriter_Ampersand_Prefer_Append & Rewriter_Append_To_Unbounded_String);",
       }   ,
       {
       name: "Rewriter_Append_To_Unbounded_String",
       qualified_name: "Predefined_Rewriters_Append.Rewriter_Append_To_Unbounded_String",
       signature: "predefined_rewriters_append.rewriter_append_to_unbounded_string",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Rewriter_Append_To_Unbounded_String :\n  aliased constant Rewriter_Find_And_Replace :=\n  Make_Rewriter_Find_And_Replace\n    (Make_Pattern\n       (\"Append ($S_Var, To_Unbounded_String ($M_Source => $S_Expr));\",\n        Call_Stmt_Rule),\n     Make_Pattern\n       (\"Append ($S_Var, $S_Expr);\", Call_Stmt_Rule),\n     Make_Match_Accepter_Function_Access\n       (Accept_Append_To_Unbounded_String'Access));",
       }   ,
   ]
,}
---
