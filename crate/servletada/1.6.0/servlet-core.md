---
crate: servletada
layout: gnatdoc
gnatdoc: {
name: "Servlet.Core",
qualified_name: "Servlet.Core",
signature: "servlet.core",
enclosing: "servlet",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Filter_Chain",
       qualified_name: "Servlet.Core.Filter_Chain",
       signature: "servlet.core.filter_chain",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Filter_Chain is limited private;",
       }   ,
       {
       name: "Filter_Config",
       qualified_name: "Servlet.Core.Filter_Config",
       signature: "servlet.core.filter_config",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Filter_Config is private;",
       }   ,
       {
       name: "Request_Dispatcher",
       qualified_name: "Servlet.Core.Request_Dispatcher",
       signature: "servlet.core.request_dispatcher",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Request_Dispatcher is limited private;",
       }   ,
       {
       name: "Status_Type",
       qualified_name: "Servlet.Core.Status_Type",
       signature: "servlet.core.status_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Status_Type is (Ready, Disabled, Started, Suspended, Stopped);",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Servlet",
       qualified_name: "Servlet.Core.Servlet",
       signature: "servlet.core.servlet",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Servlet is tagged limited private;",
       }   ,
       {
       name: "Servlet_Registry",
       qualified_name: "Servlet.Core.Servlet_Registry",
       signature: "servlet.core.servlet_registry",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Servlet_Registry is new Servlet.Sessions.Factory.Session_Factory with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Filter_Access",
       qualified_name: "Servlet.Core.Filter_Access",
       signature: "servlet.core.filter_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Filter_Access is access all Servlet.Filters.Filter'Class;",
       }   ,
       {
       name: "Filter_List_Access",
       qualified_name: "Servlet.Core.Filter_List_Access",
       signature: "servlet.core.filter_list_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Filter_List_Access is access all Servlet.Filters.Filter_List;",
       }   ,
       {
       name: "Servlet_Access",
       qualified_name: "Servlet.Core.Servlet_Access",
       signature: "servlet.core.servlet_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Servlet_Access is access all Servlet'Class;",
       }   ,
       {
       name: "Servlet_Registry_Access",
       qualified_name: "Servlet.Core.Servlet_Registry_Access",
       signature: "servlet.core.servlet_registry_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Servlet_Registry_Access is access all Servlet_Registry'Class;",
       }   ,
   ]
,}
---
