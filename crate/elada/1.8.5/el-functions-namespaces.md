---
crate: elada
layout: gnatdoc
gnatdoc: {
name: "EL.Functions.Namespaces",
qualified_name: "EL.Functions.Namespaces",
signature: "el.functions.namespaces",
enclosing: "el.functions",
is_private: false,
documentation: "------------------------------\nNamespace Function mapper\n------------------------------\nThe <b>NS_Function_Mapper</b> is a delegate function mapper which provides XML\nnamespace support.  The XML namespaces are registered with the <b>Set_Namespace</b>\nprocedure which records a prefix and the associated URI namespace.  When a function is\nsearched, the <b>Namespace</b> is searched in the prefix map to find the corresponding\nURI namespace.  Then, the delegated function mapper is invoked using that URI.",
documentation_snippet: "",
tagged_types:    [
       {
       name: "NS_Function_Mapper",
       qualified_name: "EL.Functions.Namespaces.NS_Function_Mapper",
       signature: "el.functions.namespaces.ns_function_mapper",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type NS_Function_Mapper is new Function_Mapper with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Function_Mapper_Access",
       qualified_name: "EL.Functions.Namespaces.Function_Mapper_Access",
       signature: "el.functions.namespaces.function_mapper_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Function_Mapper_Access is access all Function_Mapper'Class;",
       }   ,
   ]
,}
---
