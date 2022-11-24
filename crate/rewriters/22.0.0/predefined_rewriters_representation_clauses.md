---
crate: rewriters
layout: gnatdoc
gnatdoc: {
name: "Predefined_Rewriters_Representation_Clauses",
qualified_name: "Predefined_Rewriters_Representation_Clauses",
signature: "predefined_rewriters_representation_clauses",
enclosing: "",
is_private: false,
documentation: "TODO:\nUse $M_Pragmas and check for pragmas only to\nreduce the number of patterns\n(in particular remove the special cases\n Rewriter_For_Attribute_Use_Pragma_Var and\n Rewriter_For_Attribute_Use_Pragma_All)",
documentation_snippet: "",
constants:    [
       {
       name: "Rewriter_For_Attribute_Use",
       qualified_name: "Predefined_Rewriters_Representation_Clauses.Rewriter_For_Attribute_Use",
       signature: "predefined_rewriters_representation_clauses.rewriter_for_attribute_use",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Rewriter_For_Attribute_Use :\n  aliased constant Rewriter_Find_And_Replace :=\n  Make_Rewriter_Find_And_Replace\n    (Make_Pattern\n       (\"$S_Var : $S_Type := $M_Value with $M_Aspects;\" &\n        \"for $S_Var'$S_Attribute use $S_Expr;\",\n        Basic_Decls_Rule),\n     Make_Pattern\n       (\"$S_Var : $S_Type := $M_Value \" &\n        \"with $M_Aspects, $S_Attribute => $S_Expr;\",\n        Basic_Decl_Rule));",
       }   ,
       {
       name: "Rewriter_For_Attribute_Use_Aliased",
       qualified_name: "Predefined_Rewriters_Representation_Clauses.Rewriter_For_Attribute_Use_Aliased",
       signature: "predefined_rewriters_representation_clauses.rewriter_for_attribute_use_aliased",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Rewriter_For_Attribute_Use_Aliased :\n  aliased constant Rewriter_Find_And_Replace :=\n  Make_Rewriter_Find_And_Replace\n    (Make_Pattern\n       (\"$S_Var : aliased $S_Type := $M_Value with $M_Aspects;\" &\n        \"for $S_Var'$S_Attribute use $S_Expr;\",\n        Basic_Decls_Rule),\n     Make_Pattern\n       (\"$S_Var : aliased $S_Type := $M_Value \" &\n        \"with $M_Aspects, $S_Attribute => $S_Expr;\",\n        Basic_Decl_Rule));",
       }   ,
       {
       name: "Rewriter_For_Attribute_Use_Array",
       qualified_name: "Predefined_Rewriters_Representation_Clauses.Rewriter_For_Attribute_Use_Array",
       signature: "predefined_rewriters_representation_clauses.rewriter_for_attribute_use_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Rewriter_For_Attribute_Use_Array :\n  aliased constant Rewriter_Find_And_Replace :=\n  Make_Rewriter_Find_And_Replace\n    (Make_Pattern\n       (\"$S_Var : array ($M_Ranges) of $S_Type := \" &\n        \"$M_Value with $M_Aspects;\" &\n        \"for $S_Var'$S_Attribute use $S_Expr;\",\n        Basic_Decls_Rule),\n     Make_Pattern\n       (\"$S_Var : array ($M_Ranges) of $S_Type := $M_Value \" &\n        \"with $M_Aspects, $S_Attribute => $S_Expr;\",\n        Basic_Decl_Rule));",
       }   ,
       {
       name: "Rewriter_For_Attribute_Use_Pragma_All",
       qualified_name: "Predefined_Rewriters_Representation_Clauses.Rewriter_For_Attribute_Use_Pragma_All",
       signature: "predefined_rewriters_representation_clauses.rewriter_for_attribute_use_pragma_all",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Rewriter_For_Attribute_Use_Pragma_All :\n  aliased constant Rewriter_Find_And_Replace :=\n  Make_Rewriter_Find_And_Replace\n    (Make_Pattern\n       (\"$S_Var : $S_Type := $M_Value with $M_Aspects;\" &\n        \"pragma Warnings (Off);\"\n        & \"for $S_Var'$S_Attribute use $S_Expr;\",\n        Basic_Decls_Rule),\n     Make_Pattern\n       (\"$S_Var : $S_Type := $M_Value \" &\n        \"with $M_Aspects, $S_Attribute => $S_Expr;\" &\n        \"pragma Warnings (Off);\",\n        Basic_Decls_Rule));",
       }   ,
       {
       name: "Rewriter_For_Attribute_Use_Pragma_Var",
       qualified_name: "Predefined_Rewriters_Representation_Clauses.Rewriter_For_Attribute_Use_Pragma_Var",
       signature: "predefined_rewriters_representation_clauses.rewriter_for_attribute_use_pragma_var",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Rewriter_For_Attribute_Use_Pragma_Var :\n  aliased constant Rewriter_Find_And_Replace :=\n  Make_Rewriter_Find_And_Replace\n    (Make_Pattern\n       (\"$S_Var : $S_Type := $M_Value with $M_Aspects;\" &\n        \"pragma Warnings (Off, $S_Var);\" &\n        \"for $S_Var'$S_Attribute use $S_Expr;\",\n        Basic_Decls_Rule),\n     Make_Pattern\n       (\"$S_Var : $S_Type := $M_Value \" &\n        \"with $M_Aspects, $S_Attribute => $S_Expr;\" &\n        \"pragma Warnings (Off, $S_Var);\",\n        Basic_Decls_Rule));",
       }   ,
       {
       name: "Rewriter_Representation_Clauses",
       qualified_name: "Predefined_Rewriters_Representation_Clauses.Rewriter_Representation_Clauses",
       signature: "predefined_rewriters_representation_clauses.rewriter_representation_clauses",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Rewriter_Representation_Clauses :\naliased constant Rewriter_Sequence :=\n  Make_Rewriter_Sequence\n    (Rewriter_For_Attribute_Use &\n     Rewriter_For_Attribute_Use_Aliased &\n     Rewriter_For_Attribute_Use_Array &\n     Rewriter_For_Attribute_Use_Pragma_Var &\n     Rewriter_For_Attribute_Use_Pragma_All\n    );",
       }   ,
   ]
,}
---
