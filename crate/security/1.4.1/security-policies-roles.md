---
crate: security
layout: gnatdoc
gnatdoc: {
name: "Security.Policies.Roles",
qualified_name: "Security.Policies.Roles",
signature: "security.policies.roles",
enclosing: "security.policies",
is_private: false,
documentation: "---------------------------------------------------------------------\n  security-policies-roles -- Role based policies\n  Copyright (C) 2010, 2011, 2012, 2017, 2018 Stephane Carrez\n  Written by Stephane Carrez (Stephane.Carrez@gmail.com)\n\n  Licensed under the Apache License, Version 2.0 (the \"License\");\n  you may not use this file except in compliance with the License.\n  You may obtain a copy of the License at\n\n      http://www.apache.org/licenses/LICENSE-2.0\n\n  Unless required by applicable law or agreed to in writing, software\n  distributed under the License is distributed on an \"AS IS\" BASIS,\n  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n  See the License for the specific language governing permissions and\n  limitations under the License.\n---------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Role_Type",
       qualified_name: "Security.Policies.Roles.Role_Type",
       signature: "security.policies.roles.role_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Role_Type is new Natural range 0 .. 63;",
       }   ,
   ]
,array_types:    [
       {
       name: "Role_Map",
       qualified_name: "Security.Policies.Roles.Role_Map",
       signature: "security.policies.roles.role_map",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Role_Map is array (Role_Type'Range) of Boolean;",
       }   ,
       {
       name: "Role_Name_Array",
       qualified_name: "Security.Policies.Roles.Role_Name_Array",
       signature: "security.policies.roles.role_name_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Role_Name_Array is array (Positive range <>) of Ada.Strings.Unbounded.String_Access;",
       }   ,
       {
       name: "Role_Type_Array",
       qualified_name: "Security.Policies.Roles.Role_Type_Array",
       signature: "security.policies.roles.role_type_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Role_Type_Array is array (Positive range <>) of Role_Type;",
       }   ,
   ]
,interface_types:    [
       {
       name: "Role_Principal_Context",
       qualified_name: "Security.Policies.Roles.Role_Principal_Context",
       signature: "security.policies.roles.role_principal_context",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Role_Principal_Context is limited interface;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Role_Policy",
       qualified_name: "Security.Policies.Roles.Role_Policy",
       signature: "security.policies.roles.role_policy",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Role_Policy is new Policy with private;",
       }   ,
       {
       name: "Role_Policy_Context",
       qualified_name: "Security.Policies.Roles.Role_Policy_Context",
       signature: "security.policies.roles.role_policy_context",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Role_Policy_Context is new Policy_Context with record\n   Roles : Role_Map;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Role_Policy_Access",
       qualified_name: "Security.Policies.Roles.Role_Policy_Access",
       signature: "security.policies.roles.role_policy_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Role_Policy_Access is access all Role_Policy'Class;",
       }   ,
       {
       name: "Role_Policy_Context_Access",
       qualified_name: "Security.Policies.Roles.Role_Policy_Context_Access",
       signature: "security.policies.roles.role_policy_context_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Role_Policy_Context_Access is access all Role_Policy_Context'Class;",
       }   ,
   ]
,constants:    [
       {
       name: "NAME",
       qualified_name: "Security.Policies.Roles.NAME",
       signature: "security.policies.roles.name",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "NAME : constant String := \"Role-Policy\";",
       }   ,
   ]
,}
---
