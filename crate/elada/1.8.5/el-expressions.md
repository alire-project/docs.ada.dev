---
crate: elada
layout: gnatdoc
gnatdoc: {
name: "EL.Expressions",
qualified_name: "EL.Expressions",
signature: "el.expressions",
enclosing: "el",
is_private: false,
documentation: "Exception raised when parsing an invalid expression.",
documentation_snippet: "",
record_types:    [
       {
       name: "Method_Info",
       qualified_name: "EL.Expressions.Method_Info",
       signature: "el.expressions.method_info",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Method_Info is record\n   Object  : EL.Objects.Object;\n   Binding : Util.Beans.Methods.Method_Binding_Access;\nend record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Expression",
       qualified_name: "EL.Expressions.Expression",
       signature: "el.expressions.expression",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Expression is new Ada.Finalization.Controlled with private;",
       }   ,
       {
       name: "Method_Expression",
       qualified_name: "EL.Expressions.Method_Expression",
       signature: "el.expressions.method_expression",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Method_Expression is new EL.Expressions.Expression with private;",
       }   ,
       {
       name: "Value_Expression",
       qualified_name: "EL.Expressions.Value_Expression",
       signature: "el.expressions.value_expression",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Value_Expression is new Expression with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Expression_Access",
       qualified_name: "EL.Expressions.Expression_Access",
       signature: "el.expressions.expression_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Expression_Access is access all Expression'Class;",
       }   ,
       {
       name: "Value_Expression_Access",
       qualified_name: "EL.Expressions.Value_Expression_Access",
       signature: "el.expressions.value_expression_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Value_Expression_Access is access all Value_Expression'Class;",
       }   ,
   ]
,}
---
