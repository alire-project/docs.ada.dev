---
crate: security
layout: gnatdoc
gnatdoc: {
name: "Security.Controllers.URLs",
qualified_name: "Security.Controllers.URLs",
signature: "security.controllers.urls",
enclosing: "security.controllers",
is_private: false,
documentation: "------------------------------\nSecurity Controller\n------------------------------\nThe <b>URL_Controller</b> implements the permission check for URL permissions.\nIt uses the URL policy manager to verify the permission.",
documentation_snippet: "",
tagged_types:    [
       {
       name: "URL_Controller",
       qualified_name: "Security.Controllers.URLs.URL_Controller",
       signature: "security.controllers.urls.url_controller",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type URL_Controller is limited new Controller with record\n   Manager : Security.Policies.URLs.URL_Policy_Access;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "URL_Controller_Access",
       qualified_name: "Security.Controllers.URLs.URL_Controller_Access",
       signature: "security.controllers.urls.url_controller_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type URL_Controller_Access is access all URL_Controller'Class;",
       }   ,
   ]
,}
---
