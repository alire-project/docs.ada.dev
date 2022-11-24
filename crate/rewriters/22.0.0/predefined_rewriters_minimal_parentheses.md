---
crate: rewriters
layout: gnatdoc
gnatdoc: {
name: "Predefined_Rewriters_Minimal_Parentheses",
qualified_name: "Predefined_Rewriters_Minimal_Parentheses",
signature: "predefined_rewriters_minimal_parentheses",
enclosing: "",
is_private: false,
documentation: "Unfortunately gnatpp does not deal with parentheses.\nChange enhancement submitted to AdaCore\nhttps://gt3-prod-1.adacore.com/#/tickets/UA07-043\n\nPoor man's solution to remove as many parentheses as possible",
documentation_snippet: "",
constants:    [
       {
       name: "Rewriter_Minimal_Parentheses",
       qualified_name: "Predefined_Rewriters_Minimal_Parentheses.Rewriter_Minimal_Parentheses",
       signature: "predefined_rewriters_minimal_parentheses.rewriter_minimal_parentheses",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Rewriter_Minimal_Parentheses :\n  aliased constant Rewriter_Find_And_Replace :=\n  Make_Rewriter_Find_And_Replace\n    (Make_Pattern (\"($S_Expr)\", Expr_Rule),\n     Make_Pattern (\"$S_Expr\", Expr_Rule),\n     Make_Match_Accepter_Function_Access\n       (Accept_No_Parentheses'Access));",
       }   ,
   ]
,}
---
