---
crate: security
layout: gnatdoc
gnatdoc: {
name: "Security.Auth",
qualified_name: "Security.Auth",
signature: "security.auth",
enclosing: "security",
is_private: false,
documentation: "Use an authentication server implementing OpenID 2.0.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Association",
       qualified_name: "Security.Auth.Association",
       signature: "security.auth.association",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Association is private;",
       }   ,
       {
       name: "Auth_Result",
       qualified_name: "Security.Auth.Auth_Result",
       signature: "security.auth.auth_result",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Auth_Result is (AUTHENTICATED, CANCEL, SETUP_NEEDED, UNKNOWN, INVALID_SIGNATURE);",
       }   ,
       {
       name: "Authentication",
       qualified_name: "Security.Auth.Authentication",
       signature: "security.auth.authentication",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Authentication is private;",
       }   ,
       {
       name: "End_Point",
       qualified_name: "Security.Auth.End_Point",
       signature: "security.auth.end_point",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type End_Point is private;",
       }   ,
   ]
,interface_types:    [
       {
       name: "Parameters",
       qualified_name: "Security.Auth.Parameters",
       signature: "security.auth.parameters",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Parameters is limited interface;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Manager",
       qualified_name: "Security.Auth.Manager",
       signature: "security.auth.manager",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Manager is tagged limited private;",
       }   ,
       {
       name: "Principal",
       qualified_name: "Security.Auth.Principal",
       signature: "security.auth.principal",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Principal is new Security.Principal with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Factory_Access",
       qualified_name: "Security.Auth.Factory_Access",
       signature: "security.auth.factory_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Factory_Access is not\n  null access function (Provider : in String) return Manager_Access;",
       }   ,
       {
       name: "Manager_Access",
       qualified_name: "Security.Auth.Manager_Access",
       signature: "security.auth.manager_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Manager_Access is access all Manager'Class;",
       }   ,
       {
       name: "Principal_Access",
       qualified_name: "Security.Auth.Principal_Access",
       signature: "security.auth.principal_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Principal_Access is access all Principal'Class;",
       }   ,
   ]
,constants:    [
       {
       name: "PROVIDER_FACEBOOK",
       qualified_name: "Security.Auth.PROVIDER_FACEBOOK",
       signature: "security.auth.provider_facebook",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "PROVIDER_FACEBOOK : constant String := \"facebook\";",
       }   ,
       {
       name: "PROVIDER_GITHUB",
       qualified_name: "Security.Auth.PROVIDER_GITHUB",
       signature: "security.auth.provider_github",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "PROVIDER_GITHUB : constant String := \"github\";",
       }   ,
       {
       name: "PROVIDER_GOOGLE_PLUS",
       qualified_name: "Security.Auth.PROVIDER_GOOGLE_PLUS",
       signature: "security.auth.provider_google_plus",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "PROVIDER_GOOGLE_PLUS : constant String := \"google-plus\";",
       }   ,
       {
       name: "PROVIDER_OPENID",
       qualified_name: "Security.Auth.PROVIDER_OPENID",
       signature: "security.auth.provider_openid",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "PROVIDER_OPENID   : constant String := \"openid\";",
       }   ,
       {
       name: "PROVIDER_YAHOO",
       qualified_name: "Security.Auth.PROVIDER_YAHOO",
       signature: "security.auth.provider_yahoo",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "PROVIDER_YAHOO : constant String := \"yahoo\";",
       }   ,
   ]
,}
---
