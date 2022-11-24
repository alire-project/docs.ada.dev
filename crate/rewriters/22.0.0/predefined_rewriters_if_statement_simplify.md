---
crate: rewriters
layout: gnatdoc
gnatdoc: {
name: "Predefined_Rewriters_If_Statement_Simplify",
qualified_name: "Predefined_Rewriters_If_Statement_Simplify",
signature: "predefined_rewriters_if_statement_simplify",
enclosing: "",
is_private: false,
documentation: "TODO:\nUse Is_Negation function to capture\nall patterns in which the two branches can be swapped\nin a single pattern.",
documentation_snippet: "",
constants:    [
       {
       name: "Rewriter_If_False_Stmt",
       qualified_name: "Predefined_Rewriters_If_Statement_Simplify.Rewriter_If_False_Stmt",
       signature: "predefined_rewriters_if_statement_simplify.rewriter_if_false_stmt",
       enclosing: "",
       is_private: false,
       documentation: "Warning: by removing $M_Stmts_True; some with/use clauses\n         might become obsolete and the compiler will\n         produce warnings!",
       documentation_snippet: "Rewriter_If_False_Stmt : aliased constant Rewriter_Find_And_Replace :=\n  Make_Rewriter_Find_And_Replace\n    (Make_Pattern\n       (\"if false then $M_Stmts_True; else $M_Stmts_False; end if;\",\n        If_Stmt_Rule),\n     Make_Pattern (\"$M_Stmts_False;\", Stmts_Rule));",
       }   ,
       {
       name: "Rewriter_If_Identical_Branches_Stmt",
       qualified_name: "Predefined_Rewriters_If_Statement_Simplify.Rewriter_If_Identical_Branches_Stmt",
       signature: "predefined_rewriters_if_statement_simplify.rewriter_if_identical_branches_stmt",
       enclosing: "",
       is_private: false,
       documentation: "We can't rewrite when $S_Expr has a side effect,\nbecause it would change the behaviour of the program.",
       documentation_snippet: "Rewriter_If_Identical_Branches_Stmt :\n  aliased constant Rewriter_Find_And_Replace :=\n  Make_Rewriter_Find_And_Replace\n    (Make_Pattern\n       (\"if $S_Expr then $M_Stmts; else $M_Stmts; end if;\",\n        If_Stmt_Rule),\n     Make_Pattern (\"$M_Stmts;\", Stmt_Rule),\n     Make_Match_Accepter_Function_Access\n       (Accept_Expr_No_Side_Effects'Access));",
       }   ,
       {
       name: "Rewriter_If_Negation_Condition_Stmt",
       qualified_name: "Predefined_Rewriters_If_Statement_Simplify.Rewriter_If_Negation_Condition_Stmt",
       signature: "predefined_rewriters_if_statement_simplify.rewriter_if_negation_condition_stmt",
       enclosing: "",
       is_private: false,
       documentation: "Rewrite only when else branch is NOT empty\n\nThe resulting code might still be simplified using\n* Not\n* Minimal Parenthesis",
       documentation_snippet: "Rewriter_If_Negation_Condition_Stmt :\n  aliased constant Rewriter_Find_And_Replace :=\n  Make_Rewriter_Find_And_Replace\n    (Make_Pattern\n       (\"if $S_Cond then $M_Stmts_True; \" &\n        \"else $S_Stmt_False; $M_Stmts_False; end if;\",\n        If_Stmt_Rule),\n     Make_Pattern\n       (\"if not ($S_Cond) then $S_Stmt_False; $M_Stmts_False; \" &\n        \"else $M_Stmts_True; end if;\",\n        If_Stmt_Rule),\n     Make_Match_Accepter_Function_Access\n       (Accept_Cond_Is_Negation'Access));",
       }   ,
       {
       name: "Rewriter_If_True_Stmt",
       qualified_name: "Predefined_Rewriters_If_Statement_Simplify.Rewriter_If_True_Stmt",
       signature: "predefined_rewriters_if_statement_simplify.rewriter_if_true_stmt",
       enclosing: "",
       is_private: false,
       documentation: "Warning: by removing $M_Stmts_False; some with/use clauses\n         might become obsolete and the compiler will\n         produce warnings!",
       documentation_snippet: "Rewriter_If_True_Stmt : aliased constant Rewriter_Find_And_Replace :=\n  Make_Rewriter_Find_And_Replace\n    (Make_Pattern\n       (\"if true then $M_Stmts_True; else $M_Stmts_False; end if;\",\n        If_Stmt_Rule),\n     Make_Pattern (\"$M_Stmts_True;\", Stmts_Rule));",
       }   ,
       {
       name: "Rewriter_Null_Else_Branch",
       qualified_name: "Predefined_Rewriters_If_Statement_Simplify.Rewriter_Null_Else_Branch",
       signature: "predefined_rewriters_if_statement_simplify.rewriter_null_else_branch",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Rewriter_Null_Else_Branch : aliased constant Rewriter_Find_And_Replace :=\n  Make_Rewriter_Find_And_Replace\n    (Make_Pattern\n       (\"if $S_Cond then $M_Stmts; else null; end if;\", If_Stmt_Rule),\n     Make_Pattern (\"if $S_Cond then $M_Stmts; end if;\", If_Stmt_Rule));",
       }   ,
       {
       name: "Rewriter_Null_Then_Branch",
       qualified_name: "Predefined_Rewriters_If_Statement_Simplify.Rewriter_Null_Then_Branch",
       signature: "predefined_rewriters_if_statement_simplify.rewriter_null_then_branch",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Rewriter_Null_Then_Branch : aliased constant Rewriter_Find_And_Replace :=\n  Make_Rewriter_Find_And_Replace\n    (Make_Pattern\n       (\"if $S_Cond then null; else $S_Stmt; $M_Stmts; end if;\",\n        If_Stmt_Rule),\n     Make_Pattern\n       (\"if not ($S_Cond) then $S_Stmt; $M_Stmts; end if;\",\n        If_Stmt_Rule));",
       }   ,
       {
       name: "Rewriter_Use_Elsif",
       qualified_name: "Predefined_Rewriters_If_Statement_Simplify.Rewriter_Use_Elsif",
       signature: "predefined_rewriters_if_statement_simplify.rewriter_use_elsif",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Rewriter_Use_Elsif : aliased constant Rewriter_Find_And_Replace :=\n  Make_Rewriter_Find_And_Replace\n    (Make_Pattern\n       (\"if $S_Cond1 then $M_Stmts_True1; else \" &\n        \"if $S_Cond2 then $M_Stmts_True2; else $M_Stmts_False2; end if; \"\n        &\n        \"end if;\",\n        If_Stmt_Rule),\n     Make_Pattern\n       (\"if $S_Cond1 then $M_Stmts_True1; \" &\n        \"elsif $S_Cond2 then $M_Stmts_True2; else $M_Stmts_False2;\" &\n        \"end if;\",\n        If_Stmt_Rule));",
       }   ,
   ]
,}
---
