---
crate: rewriters
layout: gnatdoc
gnatdoc: {
name: "Predefined_Rewriters_Case_Statement_Simplify",
qualified_name: "Predefined_Rewriters_Case_Statement_Simplify",
signature: "predefined_rewriters_case_statement_simplify",
enclosing: "",
is_private: false,
documentation: "",
documentation_snippet: "",
constants:    [
       {
       name: "Rewriter_Case_Binary_With_Others",
       qualified_name: "Predefined_Rewriters_Case_Statement_Simplify.Rewriter_Case_Binary_With_Others",
       signature: "predefined_rewriters_case_statement_simplify.rewriter_case_binary_with_others",
       enclosing: "",
       is_private: false,
       documentation: "The resulting code might still be simplified using\n* Simplify If statement\n* Minimal Parenthesis",
       documentation_snippet: "Rewriter_Case_Binary_With_Others :\naliased constant Rewriter_Find_And_Replace :=\n  Make_Rewriter_Find_And_Replace\n    (Make_Pattern\n       (\"case $S_Expr is when $M_Values => $M_Stmts_In; \" &\n            \"when others => $M_Stmts_Out; end case;\",\n        Case_Stmt_Rule),\n     Make_Pattern\n       (\"if ($S_Expr) in $M_Values then $M_Stmts_In; \" &\n            \"else $M_Stmts_Out; end if;\",\n        If_Stmt_Rule));",
       }   ,
       {
       name: "Rewriter_Case_Identical_Branches",
       qualified_name: "Predefined_Rewriters_Case_Statement_Simplify.Rewriter_Case_Identical_Branches",
       signature: "predefined_rewriters_case_statement_simplify.rewriter_case_identical_branches",
       enclosing: "",
       is_private: false,
       documentation: "TODO: How to make a concrete pattern matching\nan arbitrary number of alternatives?\nOr at least 2..N, where N is the largest number of alternatives\nin a case statement in the code base",
       documentation_snippet: "Rewriter_Case_Identical_Branches :\naliased constant Rewriter_Find_And_Replace :=\n  Make_Rewriter_Find_And_Replace\n    (Make_Pattern\n       (\"case $S_Expr is \" & \"when $M_1_Vals => $M_Stmts;\" &\n            \"when $M_2_Vals => $M_Stmts;\" & \"end case;\",\n        Case_Stmt_Rule),\n     Make_Pattern (\"$M_Stmts;\", Stmt_Rule),\n     Make_Match_Accepter_Function_Access\n       (Accept_Expr_No_Side_Effects'Access));",
       }   ,
       {
       name: "Rewriter_Case_Single",
       qualified_name: "Predefined_Rewriters_Case_Statement_Simplify.Rewriter_Case_Single",
       signature: "predefined_rewriters_case_statement_simplify.rewriter_case_single",
       enclosing: "",
       is_private: false,
       documentation: "In case of a case statement with a single alternative\n(single when branch),\nthe condition \"($S_Expr) in $M_Values\" is True:\nAda requires and the compiler enforces that\nall possible values are included in the set of alternatives.\nWhen the evaluation of the expression has a side effect,\nwe can't leave it out.",
       documentation_snippet: "Rewriter_Case_Single : aliased constant Rewriter_Find_And_Replace :=\n  Make_Rewriter_Find_And_Replace\n    (Make_Pattern\n       (\"case $S_Expr is when $M_Values => $M_Stmts; end case;\",\n        Case_Stmt_Rule),\n     Make_Pattern (\"$M_Stmts;\", Stmt_Rule),\n     Make_Match_Accepter_Function_Access\n       (Accept_Expr_No_Side_Effects'Access));",
       }   ,
   ]
,}
---
