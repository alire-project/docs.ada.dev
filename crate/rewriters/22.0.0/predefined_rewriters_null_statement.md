---
crate: rewriters
layout: gnatdoc
gnatdoc: {
name: "Predefined_Rewriters_Null_Statement",
qualified_name: "Predefined_Rewriters_Null_Statement",
signature: "predefined_rewriters_null_statement",
enclosing: "",
is_private: false,
documentation: "",
documentation_snippet: "",
constants:    [
       {
       name: "Rewriter_Unnecessary_Null_Stmt",
       qualified_name: "Predefined_Rewriters_Null_Statement.Rewriter_Unnecessary_Null_Stmt",
       signature: "predefined_rewriters_null_statement.rewriter_unnecessary_null_stmt",
       enclosing: "",
       is_private: false,
       documentation: "TODO: do we also need the swapped version? i.e. \"null; $S_Stmts;\"",
       documentation_snippet: "Rewriter_Unnecessary_Null_Stmt :\n  aliased constant Rewriter_Find_And_Replace :=\n  Make_Rewriter_Find_And_Replace\n    (Make_Pattern (\"$S_Stmt; null;\", Stmts_Rule),\n     Make_Pattern (\"$S_Stmt;\", Stmt_Rule));",
       }   ,
   ]
,}
---
