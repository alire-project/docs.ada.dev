---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Tasking.Throttle",
qualified_name: "Agpl.Tasking.Throttle",
signature: "agpl.tasking.throttle",
enclosing: "agpl.tasking",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Budgets",
       qualified_name: "Agpl.Tasking.Throttle.Budgets",
       signature: "agpl.tasking.throttle.budgets",
       enclosing: "",
       is_private: false,
       documentation: "Percent of CPU allowed\n By default, this object has 100% budget.",
       documentation_snippet: "type Budgets is range 1 .. 100;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Object",
       qualified_name: "Agpl.Tasking.Throttle.Object",
       signature: "agpl.tasking.throttle.object",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Object is abstract tagged private;",
       }   ,
   ]
,constants:    [
       {
       name: "Log_Section",
       qualified_name: "Agpl.Tasking.Throttle.Log_Section",
       signature: "agpl.tasking.throttle.log_section",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Log_Section : constant String := \"agpl.tasking.throttle\";",
       }   ,
   ]
,}
---
