---
crate: security
layout: gnatdoc
gnatdoc: {
name: "Security.Controllers.Roles",
qualified_name: "Security.Controllers.Roles",
signature: "security.controllers.roles",
enclosing: "security.controllers",
is_private: false,
documentation: "------------------------------\nSecurity Controller\n------------------------------\nThe <b>Role_Controller</b> implements a simple role based permissions check.\nThe permission is granted if the user has the role defined by the controller.",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Role_Controller",
       qualified_name: "Security.Controllers.Roles.Role_Controller",
       signature: "security.controllers.roles.role_controller",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Role_Controller (Count : Positive) is limited new Controller with record\n   Roles : Policies.Roles.Role_Type_Array (1 .. Count);\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Role_Controller_Access",
       qualified_name: "Security.Controllers.Roles.Role_Controller_Access",
       signature: "security.controllers.roles.role_controller_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Role_Controller_Access is access all Role_Controller'Class;",
       }   ,
   ]
,}
---
