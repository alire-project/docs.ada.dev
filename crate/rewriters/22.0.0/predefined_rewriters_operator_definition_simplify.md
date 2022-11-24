---
crate: rewriters
layout: gnatdoc
gnatdoc: {
name: "Predefined_Rewriters_Operator_Definition_Simplify",
qualified_name: "Predefined_Rewriters_Operator_Definition_Simplify",
signature: "predefined_rewriters_operator_definition_simplify",
enclosing: "",
is_private: false,
documentation: "",
documentation_snippet: "",
constants:    [
       {
       name: "Rewriter_Definition_Different",
       qualified_name: "Predefined_Rewriters_Operator_Definition_Simplify.Rewriter_Definition_Different",
       signature: "predefined_rewriters_operator_definition_simplify.rewriter_definition_different",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Rewriter_Definition_Different :\n  aliased constant Rewriter_Find_And_Replace :=\n  Make_Rewriter_Find_And_Replace\n    (Make_Pattern (\"$S_Expr /= $S_Expr\", Expr_Rule),\n     Make_Pattern (\"false\", Expr_Rule),\n     Make_Match_Accepter_Function_Access\n       (Accept_Expr_No_Side_Effects'Access));",
       }   ,
       {
       name: "Rewriter_Definition_Divide",
       qualified_name: "Predefined_Rewriters_Operator_Definition_Simplify.Rewriter_Definition_Divide",
       signature: "predefined_rewriters_operator_definition_simplify.rewriter_definition_divide",
       enclosing: "",
       is_private: false,
       documentation: "TODO can it be correct for integers & float at the same time?",
       documentation_snippet: "Rewriter_Definition_Divide : aliased constant Rewriter_Find_And_Replace :=\n  Make_Rewriter_Find_And_Replace\n    (Make_Pattern (\"$S_Expr / $S_Expr\", Expr_Rule),\n     Make_Pattern (\"1\", Expr_Rule),\n     Make_Match_Accepter_Function_Access\n       (Accept_Integer_No_Side_Effects'Access));",
       }   ,
       {
       name: "Rewriter_Definition_Equal",
       qualified_name: "Predefined_Rewriters_Operator_Definition_Simplify.Rewriter_Definition_Equal",
       signature: "predefined_rewriters_operator_definition_simplify.rewriter_definition_equal",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Rewriter_Definition_Equal : aliased constant Rewriter_Find_And_Replace :=\n  Make_Rewriter_Find_And_Replace\n    (Make_Pattern (\"$S_Expr = $S_Expr\", Expr_Rule),\n     Make_Pattern (\"true\", Expr_Rule),\n     Make_Match_Accepter_Function_Access\n       (Accept_Expr_No_Side_Effects'Access));",
       }   ,
       {
       name: "Rewriter_Definition_Minus",
       qualified_name: "Predefined_Rewriters_Operator_Definition_Simplify.Rewriter_Definition_Minus",
       signature: "predefined_rewriters_operator_definition_simplify.rewriter_definition_minus",
       enclosing: "",
       is_private: false,
       documentation: "TODO can it be correct for integers & float at the same time?",
       documentation_snippet: "Rewriter_Definition_Minus : aliased constant Rewriter_Find_And_Replace :=\n  Make_Rewriter_Find_And_Replace\n    (Make_Pattern (\"$S_Expr - $S_Expr\", Expr_Rule),\n     Make_Pattern (\"0\", Expr_Rule),\n     Make_Match_Accepter_Function_Access\n       (Accept_Integer_No_Side_Effects'Access));",
       }   ,
       {
       name: "Rewriter_Definition_Modulo",
       qualified_name: "Predefined_Rewriters_Operator_Definition_Simplify.Rewriter_Definition_Modulo",
       signature: "predefined_rewriters_operator_definition_simplify.rewriter_definition_modulo",
       enclosing: "",
       is_private: false,
       documentation: "TODO: can mod be overloaded or is it only defined for integer types?",
       documentation_snippet: "Rewriter_Definition_Modulo : aliased constant Rewriter_Find_And_Replace :=\n  Make_Rewriter_Find_And_Replace\n    (Make_Pattern (\"$S_Expr mod $S_Expr\", Expr_Rule),\n     Make_Pattern (\"0\", Expr_Rule),\n     Make_Match_Accepter_Function_Access\n       (Accept_Expr_No_Side_Effects'Access));",
       }   ,
       {
       name: "Rewriter_Definition_Remainder",
       qualified_name: "Predefined_Rewriters_Operator_Definition_Simplify.Rewriter_Definition_Remainder",
       signature: "predefined_rewriters_operator_definition_simplify.rewriter_definition_remainder",
       enclosing: "",
       is_private: false,
       documentation: "TODO: can rem be overloaded or is it only defined for integer types?",
       documentation_snippet: "Rewriter_Definition_Remainder :\n  aliased constant Rewriter_Find_And_Replace :=\n  Make_Rewriter_Find_And_Replace\n    (Make_Pattern (\"$S_Expr rem $S_Expr\", Expr_Rule),\n     Make_Pattern (\"0\", Expr_Rule),\n     Make_Match_Accepter_Function_Access\n       (Accept_Expr_No_Side_Effects'Access));",
       }   ,
   ]
,}
---
