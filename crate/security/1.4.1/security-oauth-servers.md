---
crate: security
layout: gnatdoc
gnatdoc: {
name: "Security.OAuth.Servers",
qualified_name: "Security.OAuth.Servers",
signature: "security.oauth.servers",
enclosing: "security.oauth",
is_private: false,
documentation: "Minimum length for the server private key (160 bits min length).\n(See NIST Special Publication 800-107)",
documentation_snippet: "",
simple_types:    [
       {
       name: "Grant_Kind",
       qualified_name: "Security.OAuth.Servers.Grant_Kind",
       signature: "security.oauth.servers.grant_kind",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Grant_Kind is (No_Grant, Access_Grant, Code_Grant,\n                    Implicit_Grant, Password_Grant, Credential_Grant,\n                    Extension_Grant);",
       }   ,
       {
       name: "Grant_Status",
       qualified_name: "Security.OAuth.Servers.Grant_Status",
       signature: "security.oauth.servers.grant_status",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Grant_Status is (Invalid_Grant, Expired_Grant, Revoked_Grant,\n                      Stealed_Grant, Valid_Grant);",
       }   ,
   ]
,record_types:    [
       {
       name: "Grant_Type",
       qualified_name: "Security.OAuth.Servers.Grant_Type",
       signature: "security.oauth.servers.grant_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Grant_Type is record\n   Request : Grant_Kind := No_Grant;\n   Status  : Grant_Status := Invalid_Grant;\n   Token   : Ada.Strings.Unbounded.Unbounded_String;\n   Expires : Ada.Calendar.Time;\n   Expires_In : Duration := 0.0;\n   Auth    : Principal_Access;\n   Error   : Util.Strings.Name_Access;\nend record;",
       }   ,
   ]
,interface_types:    [
       {
       name: "Application_Manager",
       qualified_name: "Security.OAuth.Servers.Application_Manager",
       signature: "security.oauth.servers.application_manager",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Application_Manager is limited interface;",
       }   ,
       {
       name: "Principal",
       qualified_name: "Security.OAuth.Servers.Principal",
       signature: "security.oauth.servers.principal",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Principal is limited interface and Security.Principal;",
       }   ,
       {
       name: "Realm_Manager",
       qualified_name: "Security.OAuth.Servers.Realm_Manager",
       signature: "security.oauth.servers.realm_manager",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Realm_Manager is limited interface;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Application",
       qualified_name: "Security.OAuth.Servers.Application",
       signature: "security.oauth.servers.application",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Application is new Security.OAuth.Application with private;",
       }   ,
       {
       name: "Auth_Manager",
       qualified_name: "Security.OAuth.Servers.Auth_Manager",
       signature: "security.oauth.servers.auth_manager",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Auth_Manager is tagged limited private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Application_Manager_Access",
       qualified_name: "Security.OAuth.Servers.Application_Manager_Access",
       signature: "security.oauth.servers.application_manager_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Application_Manager_Access is access all Application_Manager'Class;",
       }   ,
       {
       name: "Auth_Manager_Access",
       qualified_name: "Security.OAuth.Servers.Auth_Manager_Access",
       signature: "security.oauth.servers.auth_manager_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Auth_Manager_Access is access all Auth_Manager'Class;",
       }   ,
       {
       name: "Principal_Access",
       qualified_name: "Security.OAuth.Servers.Principal_Access",
       signature: "security.oauth.servers.principal_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Principal_Access is access all Principal'Class;",
       }   ,
       {
       name: "Realm_Manager_Access",
       qualified_name: "Security.OAuth.Servers.Realm_Manager_Access",
       signature: "security.oauth.servers.realm_manager_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Realm_Manager_Access is access all Realm_Manager'Class;",
       }   ,
   ]
,constants:    [
       {
       name: "MIN_KEY_LENGTH",
       qualified_name: "Security.OAuth.Servers.MIN_KEY_LENGTH",
       signature: "security.oauth.servers.min_key_length",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "MIN_KEY_LENGTH : constant Positive := 20;",
       }   ,
   ]
,}
---
