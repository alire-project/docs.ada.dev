---
crate: rewriters
layout: gnatdoc
gnatdoc: {
name: "Predefined_Rewriters_If_Statement_Distribution",
qualified_name: "Predefined_Rewriters_If_Statement_Distribution",
signature: "predefined_rewriters_if_statement_distribution",
enclosing: "",
is_private: false,
documentation: "",
documentation_snippet: "",
constants:    [
       {
       name: "Rewriter_If_Stmt_Identical_Tail",
       qualified_name: "Predefined_Rewriters_If_Statement_Distribution.Rewriter_If_Stmt_Identical_Tail",
       signature: "predefined_rewriters_if_statement_distribution.rewriter_if_stmt_identical_tail",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Rewriter_If_Stmt_Identical_Tail :\n  aliased constant Rewriter_Find_And_Replace :=\n  Make_Rewriter_Find_And_Replace\n    (Make_Pattern\n       (\"if $S_Cond then $M_Stmts_True; $S_Stmt; \" &\n        \"else $M_Stmts_False; $S_Stmt; end if;\",\n        If_Stmt_Rule),\n     Make_Pattern\n       (\"if $S_Cond then $M_Stmts_True; \" &\n        \"else $M_Stmts_False; end if; $S_Stmt;\",\n        Stmts_Rule));",
       }   ,
       {
       name: "Rewriter_If_Stmt_Identical_Tails",
       qualified_name: "Predefined_Rewriters_If_Statement_Distribution.Rewriter_If_Stmt_Identical_Tails",
       signature: "predefined_rewriters_if_statement_distribution.rewriter_if_stmt_identical_tails",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Rewriter_If_Stmt_Identical_Tails :\naliased constant Rewriter_Repeat :=\n  Make_Rewriter_Repeat (Rewriter_If_Stmt_Identical_Tail);",
       }   ,
   ]
,}
---
