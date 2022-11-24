---
crate: rewriters
layout: gnatdoc
gnatdoc: {
name: "Predefined_Rewriters_Operator_Definition_Equivalence",
qualified_name: "Predefined_Rewriters_Operator_Definition_Equivalence",
signature: "predefined_rewriters_operator_definition_equivalence",
enclosing: "",
is_private: false,
documentation: "",
documentation_snippet: "",
constants:    [
       {
       name: "Rewriter_Double",
       qualified_name: "Predefined_Rewriters_Operator_Definition_Equivalence.Rewriter_Double",
       signature: "predefined_rewriters_operator_definition_equivalence.rewriter_double",
       enclosing: "",
       is_private: false,
       documentation: "Rewriter makes performance faster,\nespecially when expression consumes a lot of time.\n\nWe don't rewrite in case of side effects:\ne.g. suppose the function f has a side effect.\nf(3) + f(3) triggers side effects twice\nwhile 2 * (f(3)) triggers side effects only once\nHowever how important is the side effect?\nMight be perfectly acceptable to log only once\nthat f is entered, and f returns!\n\nThe resulting code might still be simplified using\n* Minimal Parenthesis",
       documentation_snippet: "Rewriter_Double : aliased constant Rewriter_Find_And_Replace :=\n  Make_Rewriter_Find_And_Replace\n    (Make_Pattern (\"$S_Expr + $S_Expr\", Expr_Rule),\n     Make_Pattern (\"2 * ($S_Expr)\", Expr_Rule),\n     Make_Match_Accepter_Function_Access\n       (Accept_Expr_No_Side_Effects'Access));",
       }   ,
   ]
,}
---
