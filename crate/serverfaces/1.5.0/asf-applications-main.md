---
crate: serverfaces
layout: gnatdoc
gnatdoc: {
name: "ASF.Applications.Main",
qualified_name: "ASF.Applications.Main",
signature: "asf.applications.main",
enclosing: "asf.applications",
is_private: false,
documentation: "------------------------------\nFactory for creation of lifecycle, view handler\n------------------------------",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Application",
       qualified_name: "ASF.Applications.Main.Application",
       signature: "asf.applications.main.application",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Application is new ASF.Servlets.Servlet_Registry\n  and ASF.Events.Faces.Actions.Action_Listener with private;",
       }   ,
       {
       name: "Application_Factory",
       qualified_name: "ASF.Applications.Main.Application_Factory",
       signature: "asf.applications.main.application_factory",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Application_Factory is tagged limited private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Application_Access",
       qualified_name: "ASF.Applications.Main.Application_Access",
       signature: "asf.applications.main.application_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Application_Access is access all Application'Class;",
       }   ,
   ]
,}
---
