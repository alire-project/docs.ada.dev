---
crate: rewriters
layout: gnatdoc
gnatdoc: {
name: "Predefined_Rewriters_Prefer_Short_Circuit",
qualified_name: "Predefined_Rewriters_Prefer_Short_Circuit",
signature: "predefined_rewriters_prefer_short_circuit",
enclosing: "",
is_private: false,
documentation: "Use short circuit form of logical operators\nRewrite only occurs when behaviour is identical",
documentation_snippet: "",
constants:    [
       {
       name: "Rewriter_And_Then",
       qualified_name: "Predefined_Rewriters_Prefer_Short_Circuit.Rewriter_And_Then",
       signature: "predefined_rewriters_prefer_short_circuit.rewriter_and_then",
       enclosing: "",
       is_private: false,
       documentation: "Use short circuit form of logical `and` operator",
       documentation_snippet: "Rewriter_And_Then : aliased constant Rewriter_Find_And_Replace :=\n  Make_Rewriter_Find_And_Replace\n    (Make_Pattern (\"$S_Left and $S_Right\", Expr_Rule),\n     Make_Pattern (\"$S_Left and then $S_Right\", Expr_Rule),\n     Make_Match_Accepter_Function_Access\n       (Accept_Right_Boolean_No_Side_Effects'Access));",
       }   ,
       {
       name: "Rewriter_Or_Else",
       qualified_name: "Predefined_Rewriters_Prefer_Short_Circuit.Rewriter_Or_Else",
       signature: "predefined_rewriters_prefer_short_circuit.rewriter_or_else",
       enclosing: "",
       is_private: false,
       documentation: "Use short circuit form of logical `or` operator",
       documentation_snippet: "Rewriter_Or_Else : aliased constant Rewriter_Find_And_Replace :=\n  Make_Rewriter_Find_And_Replace\n    (Make_Pattern (\"$S_Left or $S_Right\", Expr_Rule),\n     Make_Pattern (\"$S_Left or else $S_Right\", Expr_Rule),\n     Make_Match_Accepter_Function_Access\n       (Accept_Right_Boolean_No_Side_Effects'Access));",
       }   ,
   ]
,}
---
