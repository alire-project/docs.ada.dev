---
crate: rewriters
layout: gnatdoc
gnatdoc: {
name: "Predefined_Rewriters_Case_Expression_Simplify",
qualified_name: "Predefined_Rewriters_Case_Expression_Simplify",
signature: "predefined_rewriters_case_expression_simplify",
enclosing: "",
is_private: false,
documentation: "",
documentation_snippet: "",
constants:    [
       {
       name: "Rewriter_Case_Expression_Binary_With_Others",
       qualified_name: "Predefined_Rewriters_Case_Expression_Simplify.Rewriter_Case_Expression_Binary_With_Others",
       signature: "predefined_rewriters_case_expression_simplify.rewriter_case_expression_binary_with_others",
       enclosing: "",
       is_private: false,
       documentation: "Rewriter for patterns involving the case expression\nthat can be simplified.\n\nThe resulting code might still be simplified using\n* Simplify if expression",
       documentation_snippet: "Rewriter_Case_Expression_Binary_With_Others :\n  aliased constant Rewriter_Find_And_Replace :=\n  Make_Rewriter_Find_And_Replace\n    (Make_Pattern\n       (\"case $S_Expr is when $M_Values => $S_Val_In, \" &\n        \"when others => $S_Val_Out\",\n        Expr_Rule),\n     Make_Pattern\n       (\"if ($S_Expr) in $M_Values then $S_Val_In else $S_Val_Out\",\n        Expr_Rule));",
       }   ,
   ]
,}
---
