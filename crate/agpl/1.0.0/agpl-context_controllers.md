---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Context_controllers",
qualified_name: "Agpl.Context_controllers",
signature: "agpl.context_controllers",
enclosing: "agpl",
is_private: false,
documentation: "----------------------------------------------------------------------\n Object                                                             --\n----------------------------------------------------------------------\n  Declaring an object of this kind will cause the execution of the\n  Beginning and Ending code when the object is created and destroyed\n  respectively",
documentation_snippet: "",
simple_types:    [
       {
       name: "Simple_controller",
       qualified_name: "Agpl.Context_controllers.Simple_controller",
       signature: "agpl.context_controllers.simple_controller",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Simple_controller (Beginning, Ending : Code_access) is private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Code_access",
       qualified_name: "Agpl.Context_controllers.Code_access",
       signature: "agpl.context_controllers.code_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Code_access is access procedure;",
       }   ,
   ]
,}
---
