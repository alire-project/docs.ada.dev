---
crate: rewriters
layout: gnatdoc
gnatdoc: {
name: "Predefined_Rewriters_Declaration_Simplify",
qualified_name: "Predefined_Rewriters_Declaration_Simplify",
signature: "predefined_rewriters_declaration_simplify",
enclosing: "",
is_private: false,
documentation: "",
documentation_snippet: "",
constants:    [
       {
       name: "Rewriter_Declarations_Combine",
       qualified_name: "Predefined_Rewriters_Declaration_Simplify.Rewriter_Declarations_Combine",
       signature: "predefined_rewriters_declaration_simplify.rewriter_declarations_combine",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Rewriter_Declarations_Combine : aliased constant Rewriter_Repeat :=\n  Make_Rewriter_Repeat (Rewriter_Declarations_Combine_Step);",
       }   ,
       {
       name: "Rewriter_Declarations_Combine_Step",
       qualified_name: "Predefined_Rewriters_Declaration_Simplify.Rewriter_Declarations_Combine_Step",
       signature: "predefined_rewriters_declaration_simplify.rewriter_declarations_combine_step",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Rewriter_Declarations_Combine_Step :\n  aliased constant Rewriter_Find_And_Replace :=\n  Make_Rewriter_Find_And_Replace\n    (Make_Pattern\n       (\"$M_X : $S_Type := $M_Expr;\" & \"$M_Y : $S_Type := $M_Expr;\",\n        Basic_Decls_Rule),\n     Make_Pattern (\"$M_X, $M_Y : $S_Type := $M_Expr;\", Basic_Decl_Rule),\n     Make_Match_Accepter_Function_Access\n       (Accept_Expr_No_Side_Effects'Access));",
       }   ,
   ]
,}
---
