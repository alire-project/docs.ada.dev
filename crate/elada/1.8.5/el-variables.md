---
crate: elada
layout: gnatdoc
gnatdoc: {
name: "EL.Variables",
qualified_name: "EL.Variables",
signature: "el.variables",
enclosing: "el",
is_private: false,
documentation: "\nThe expression context provides information to resolve runtime\ninformation when evaluating an expression.  The context provides\na resolver whose role is to find variables given their name.",
documentation_snippet: "",
interface_types:    [
       {
       name: "Variable_Mapper",
       qualified_name: "EL.Variables.Variable_Mapper",
       signature: "el.variables.variable_mapper",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Variable_Mapper is interface;",
       }   ,
   ]
,access_types:    [
       {
       name: "Variable_Mapper_Access",
       qualified_name: "EL.Variables.Variable_Mapper_Access",
       signature: "el.variables.variable_mapper_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Variable_Mapper_Access is access all Variable_Mapper'Class;",
       }   ,
   ]
,}
---
