---
crate: rewriters
layout: gnatdoc
gnatdoc: {
name: "Predefined_Rewriters_Prefer_If_Expression",
qualified_name: "Predefined_Rewriters_Prefer_If_Expression",
signature: "predefined_rewriters_prefer_if_expression",
enclosing: "",
is_private: false,
documentation: "TODO: Don't prefer If Expression when one of\nthe placeholders $S_Val_True and $S_Val_False\nare already if expressions or case expressions",
documentation_snippet: "",
constants:    [
       {
       name: "Rewriter_If_Expression",
       qualified_name: "Predefined_Rewriters_Prefer_If_Expression.Rewriter_If_Expression",
       signature: "predefined_rewriters_prefer_if_expression.rewriter_if_expression",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Rewriter_If_Expression : aliased constant Rewriter_Sequence :=\n  Make_Rewriter_Sequence\n    (Rewriter_If_Stmt_Subprogram_Single_Diffent_Argument &\n     Rewriter_If_Stmt_Assignment & Rewriter_If_Stmt_Return &\n     Rewriter_If_Stmt_Return_Stmt);",
       }   ,
       {
       name: "Rewriter_If_Stmt_Assignment",
       qualified_name: "Predefined_Rewriters_Prefer_If_Expression.Rewriter_If_Stmt_Assignment",
       signature: "predefined_rewriters_prefer_if_expression.rewriter_if_stmt_assignment",
       enclosing: "",
       is_private: false,
       documentation: "TODO: add check that nested if expressions &\n      case expressions are prevented",
       documentation_snippet: "Rewriter_If_Stmt_Assignment : aliased constant Rewriter_Find_And_Replace :=\n  Make_Rewriter_Find_And_Replace\n    (Make_Pattern\n       (\"if $S_Cond then\" & \" $S_Var := $S_Val_True;\" & \"else\" &\n        \" $S_Var := $S_Val_False;\" & \"end if;\",\n        If_Stmt_Rule),\n     Make_Pattern\n       (\"$S_Var := (if $S_Cond then $S_Val_True else $S_Val_False);\",\n        Stmt_Rule));",
       }   ,
       {
       name: "Rewriter_If_Stmt_Return",
       qualified_name: "Predefined_Rewriters_Prefer_If_Expression.Rewriter_If_Stmt_Return",
       signature: "predefined_rewriters_prefer_if_expression.rewriter_if_stmt_return",
       enclosing: "",
       is_private: false,
       documentation: "TODO: add check that nested if expressions &\n      case expressions are prevented",
       documentation_snippet: "Rewriter_If_Stmt_Return : aliased constant Rewriter_Find_And_Replace :=\n  Make_Rewriter_Find_And_Replace\n    (Make_Pattern\n       (\"if $S_Cond then return $S_Expr_True; \" &\n        \"else return $S_Expr_False; end if;\",\n        If_Stmt_Rule),\n     Make_Pattern\n       (\"return (if $S_Cond then $S_Expr_True else $S_Expr_False);\",\n        Return_Stmt_Rule));",
       }   ,
       {
       name: "Rewriter_If_Stmt_Return_Stmt",
       qualified_name: "Predefined_Rewriters_Prefer_If_Expression.Rewriter_If_Stmt_Return_Stmt",
       signature: "predefined_rewriters_prefer_if_expression.rewriter_if_stmt_return_stmt",
       enclosing: "",
       is_private: false,
       documentation: "TODO: add check that nested if expressions &\n      case expressions are prevented",
       documentation_snippet: "Rewriter_If_Stmt_Return_Stmt : aliased constant Rewriter_Find_And_Replace :=\n  Make_Rewriter_Find_And_Replace\n    (Make_Pattern\n       (\"if $S_Cond then return $S_Expr_True; end if; \" &\n        \"return $S_Expr_False;\",\n        Stmts_Rule),\n     Make_Pattern\n       (\"return (if $S_Cond then $S_Expr_True else $S_Expr_False);\",\n        Return_Stmt_Rule));",
       }   ,
       {
       name: "Rewriter_If_Stmt_Subprogram_Single_Diffent_Argument",
       qualified_name: "Predefined_Rewriters_Prefer_If_Expression.Rewriter_If_Stmt_Subprogram_Single_Diffent_Argument",
       signature: "predefined_rewriters_prefer_if_expression.rewriter_if_stmt_subprogram_single_diffent_argument",
       enclosing: "",
       is_private: false,
       documentation: "Note that our current implementation doesn't handle this pattern\nas one might expect, since we have not implemented multi matching.\nSo, any match in the current implementation will have\nan empty list for $M_Args_Before.\nMulti matching has recently been added to the C++ version\nof the rejuvenation library\n\nTODO: add check that nested if expressions &\n      case expressions are prevented",
       documentation_snippet: "Rewriter_If_Stmt_Subprogram_Single_Diffent_Argument :\n  aliased constant Rewriter_Find_And_Replace :=\n  Make_Rewriter_Find_And_Replace\n    (Make_Pattern\n       (\"if $S_Cond then \" &\n        \"$S_Subp ($M_Args_Before, $M_Name => $S_Val_True, $M_Args_After);\" &\n        \"else \" &\n        \"$S_Subp ($M_Args_Before, $M_Name => $S_Val_False, $M_Args_After);\" &\n        \"end if;\",\n        If_Stmt_Rule),\n     Make_Pattern\n       (\"$S_Subp ($M_Args_Before,\" &\n        \"$M_Name => (if $S_Cond then $S_Val_True else $S_Val_False),\" &\n        \"$M_Args_After);\",\n        Call_Stmt_Rule),\n     Make_Match_Accepter_Function_Access (Accept_All_Independent'Access));",
       }   ,
   ]
,}
---
