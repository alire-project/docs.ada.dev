---
crate: libadalang
layout: gnatdoc
gnatdoc: {
name: "Libadalang.Expr_Eval",
qualified_name: "Libadalang.Expr_Eval",
signature: "libadalang.expr_eval",
enclosing: "libadalang",
is_private: false,
documentation: "\nCopyright (C) 2014-2022, AdaCore\nSPDX-License-Identifier: Apache-2.0",
documentation_snippet: "",
simple_types:    [
       {
       name: "Expr_Kind",
       qualified_name: "Libadalang.Expr_Eval.Expr_Kind",
       signature: "libadalang.expr_eval.expr_kind",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Expr_Kind is (Enum_Lit, Int, Real, String_Lit);",
       }   ,
   ]
,record_types:    [
       {
       name: "Eval_Result",
       qualified_name: "Libadalang.Expr_Eval.Eval_Result",
       signature: "libadalang.expr_eval.eval_result",
       enclosing: "",
       is_private: false,
       documentation: "This data type represents the result of the evaluation of an expression\n\n@field Kind\n@field Expr_Type\n@field Enum_Result\n@field Int_Result\n@field Real_Result\n@field String_Result",
       documentation_snippet: "type Eval_Result (Kind : Expr_Kind := Int) is limited record\n   Expr_Type : LAL.Base_Type_Decl;\n   case Kind is\n      when Enum_Lit =>\n         Enum_Result : LAL.Enum_Literal_Decl;\n      when Int =>\n         Int_Result : Big_Integer;\n      when Real =>\n         Real_Result : Rational;\n      when String_Lit =>\n         String_Result : Unbounded_Text_Type;\n   end case;\nend record;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Big_Integer",
       qualified_name: "Libadalang.Expr_Eval.Big_Integer",
       signature: "libadalang.expr_eval.big_integer",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Big_Integer is GNATCOLL.GMP.Integers.Big_Integer;",
       }   ,
       {
       name: "Double",
       qualified_name: "Libadalang.Expr_Eval.Double",
       signature: "libadalang.expr_eval.double",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Double is GNATCOLL.GMP.Double;",
       }   ,
       {
       name: "Rational",
       qualified_name: "Libadalang.Expr_Eval.Rational",
       signature: "libadalang.expr_eval.rational",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Rational is GNATCOLL.GMP.Rational_Numbers.Rational;",
       }   ,
   ]
,}
---
