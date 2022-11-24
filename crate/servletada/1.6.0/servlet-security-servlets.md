---
crate: servletada
layout: gnatdoc
gnatdoc: {
name: "Servlet.Security.Servlets",
qualified_name: "Servlet.Security.Servlets",
signature: "servlet.security.servlets",
enclosing: "servlet.security",
is_private: false,
documentation: "------------------------------\nOpenID Servlet\n------------------------------\nThe <b>Openid_Servlet</b> is the OpenID root servlet for OpenID 2.0 authentication.\nIt is defined to provide a common basis for the authentication and verification servlets.",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Openid_Servlet",
       qualified_name: "Servlet.Security.Servlets.Openid_Servlet",
       signature: "servlet.security.servlets.openid_servlet",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Openid_Servlet is abstract new Servlet.Core.Servlet and Auth.Parameters with private;",
       }   ,
       {
       name: "Request_Auth_Servlet",
       qualified_name: "Servlet.Security.Servlets.Request_Auth_Servlet",
       signature: "servlet.security.servlets.request_auth_servlet",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Request_Auth_Servlet is new Openid_Servlet with private;",
       }   ,
       {
       name: "Verify_Auth_Servlet",
       qualified_name: "Servlet.Security.Servlets.Verify_Auth_Servlet",
       signature: "servlet.security.servlets.verify_auth_servlet",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Verify_Auth_Servlet is new Openid_Servlet with private;",
       }   ,
   ]
,}
---
