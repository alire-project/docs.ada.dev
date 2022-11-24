---
crate: serverfaces
layout: gnatdoc
gnatdoc: {
name: "ASF.Navigations",
qualified_name: "ASF.Navigations",
signature: "asf.navigations",
enclosing: "asf",
is_private: false,
documentation: "------------------------------\nNavigation Handler\n------------------------------",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Navigation_Case",
       qualified_name: "ASF.Navigations.Navigation_Case",
       signature: "asf.navigations.navigation_case",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Navigation_Case is abstract tagged limited private;",
       }   ,
       {
       name: "Navigation_Handler",
       qualified_name: "ASF.Navigations.Navigation_Handler",
       signature: "asf.navigations.navigation_handler",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Navigation_Handler is new Ada.Finalization.Limited_Controlled with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Navigation_Access",
       qualified_name: "ASF.Navigations.Navigation_Access",
       signature: "asf.navigations.navigation_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Navigation_Access is access all Navigation_Case'Class;",
       }   ,
       {
       name: "Navigation_Handler_Access",
       qualified_name: "ASF.Navigations.Navigation_Handler_Access",
       signature: "asf.navigations.navigation_handler_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Navigation_Handler_Access is access all Navigation_Handler'Class;",
       }   ,
   ]
,}
---
