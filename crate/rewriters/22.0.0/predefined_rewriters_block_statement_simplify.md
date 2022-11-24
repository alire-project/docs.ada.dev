---
crate: rewriters
layout: gnatdoc
gnatdoc: {
name: "Predefined_Rewriters_Block_Statement_Simplify",
qualified_name: "Predefined_Rewriters_Block_Statement_Simplify",
signature: "predefined_rewriters_block_statement_simplify",
enclosing: "",
is_private: false,
documentation: "",
documentation_snippet: "",
constants:    [
       {
       name: "Rewriter_Declare_And_Overwrite",
       qualified_name: "Predefined_Rewriters_Block_Statement_Simplify.Rewriter_Declare_And_Overwrite",
       signature: "predefined_rewriters_block_statement_simplify.rewriter_declare_and_overwrite",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Rewriter_Declare_And_Overwrite :\n  aliased constant Rewriter_Find_And_Replace :=\n  Make_Rewriter_Find_And_Replace\n    (Make_Pattern\n       (\"declare $S_Var : $S_Type := $S_Val_False; \" &\n        \"begin if $S_Cond then $S_Var := $S_Val_True; end if; \" &\n        \"$M_Stmts; end;\",\n        Block_Stmt_Rule),\n     Make_Pattern\n       (\"declare $S_Var : $S_Type := \" &\n        \"(if $S_Cond then $S_Val_True else $S_Val_False); \" &\n        \"begin $M_Stmts; end;\",\n        Block_Stmt_Rule),\n     Make_Match_Accepter_Function_Access (Accept_Variable'Access));",
       }   ,
       {
       name: "Rewriter_Return_Expression",
       qualified_name: "Predefined_Rewriters_Block_Statement_Simplify.Rewriter_Return_Expression",
       signature: "predefined_rewriters_block_statement_simplify.rewriter_return_expression",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Rewriter_Return_Expression :\n  aliased constant Rewriter_Find_And_Replace :=\n  Make_Rewriter_Find_And_Replace\n    (Make_Pattern\n       (\"declare $S_Var : constant $S_Type := $S_Expr; \" &\n        \"begin return $S_Var; end;\",\n        Block_Stmt_Rule),\n     Make_Pattern (\"return $S_Expr;\", Return_Stmt_Rule));",
       }   ,
   ]
,}
---
