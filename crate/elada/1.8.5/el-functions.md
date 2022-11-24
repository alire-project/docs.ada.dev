---
crate: elada
layout: gnatdoc
gnatdoc: {
name: "EL.Functions",
qualified_name: "EL.Functions",
signature: "el.functions",
enclosing: "el",
is_private: false,
documentation: "\nThe expression context provides information to resolve runtime\ninformation when evaluating an expression.  The context provides\na resolver whose role is to find variables given their name.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Function_Type",
       qualified_name: "EL.Functions.Function_Type",
       signature: "el.functions.function_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Function_Type is (F_1_ARG, F_2_ARG, F_3_ARG, F_4_ARG);",
       }   ,
   ]
,record_types:    [
       {
       name: "Function_Access",
       qualified_name: "EL.Functions.Function_Access",
       signature: "el.functions.function_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Function_Access (Of_Type : Function_Type := F_1_ARG) is record\n   Optimize : Boolean := True;\n   case Of_Type is\n      when F_1_ARG =>\n         Func1 : Function_1_Access;\n      when F_2_ARG =>\n         Func2 : Function_2_Access;\n      when F_3_ARG =>\n         Func3 : Function_3_Access;\n      when F_4_ARG =>\n         Func4 : Function_4_Access;\n   end case;\nend record;",
       }   ,
   ]
,interface_types:    [
       {
       name: "Function_Mapper",
       qualified_name: "EL.Functions.Function_Mapper",
       signature: "el.functions.function_mapper",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Function_Mapper is interface;",
       }   ,
   ]
,access_types:    [
       {
       name: "Function_1_Access",
       qualified_name: "EL.Functions.Function_1_Access",
       signature: "el.functions.function_1_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Function_1_Access is access function (P : Object) return Object;",
       }   ,
       {
       name: "Function_2_Access",
       qualified_name: "EL.Functions.Function_2_Access",
       signature: "el.functions.function_2_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Function_2_Access is access function (P1, P2 : Object) return Object;",
       }   ,
       {
       name: "Function_3_Access",
       qualified_name: "EL.Functions.Function_3_Access",
       signature: "el.functions.function_3_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Function_3_Access is access function (P1, P2, P3 : Object) return Object;",
       }   ,
       {
       name: "Function_4_Access",
       qualified_name: "EL.Functions.Function_4_Access",
       signature: "el.functions.function_4_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Function_4_Access is access function (P1, P2, P3, P4 : Object) return Object;",
       }   ,
       {
       name: "Function_Mapper_Access",
       qualified_name: "EL.Functions.Function_Mapper_Access",
       signature: "el.functions.function_mapper_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Function_Mapper_Access is access all Function_Mapper'Class;",
       }   ,
   ]
,}
---
