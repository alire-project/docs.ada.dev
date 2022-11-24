---
crate: security
layout: gnatdoc
gnatdoc: {
name: "Security.OAuth.Clients",
qualified_name: "Security.OAuth.Clients",
signature: "security.oauth.clients",
enclosing: "security.oauth",
is_private: false,
documentation: "Note: OAuth 1.0 could be implemented but since it's being deprecated\nit's not worth doing it.",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Access_Token",
       qualified_name: "Security.OAuth.Clients.Access_Token",
       signature: "security.oauth.clients.access_token",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Access_Token (Len : Natural) is new Security.Principal with private;",
       }   ,
       {
       name: "Application",
       qualified_name: "Security.OAuth.Clients.Application",
       signature: "security.oauth.clients.application",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Application is new Security.OAuth.Application with private;",
       }   ,
       {
       name: "Grant_Type",
       qualified_name: "Security.OAuth.Clients.Grant_Type",
       signature: "security.oauth.clients.grant_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Grant_Type is new Security.Principal with private;",
       }   ,
       {
       name: "OpenID_Token",
       qualified_name: "Security.OAuth.Clients.OpenID_Token",
       signature: "security.oauth.clients.openid_token",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type OpenID_Token (Len, Id_Len, Refresh_Len : Natural) is new Access_Token with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Access_Token_Access",
       qualified_name: "Security.OAuth.Clients.Access_Token_Access",
       signature: "security.oauth.clients.access_token_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Access_Token_Access is access all Access_Token'Class;",
       }   ,
       {
       name: "OpenID_Token_Access",
       qualified_name: "Security.OAuth.Clients.OpenID_Token_Access",
       signature: "security.oauth.clients.openid_token_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type OpenID_Token_Access is access all OpenID_Token'Class;",
       }   ,
   ]
,}
---
