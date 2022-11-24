---
crate: security
layout: gnatdoc
gnatdoc: {
name: "Security.Policies",
qualified_name: "Security.Policies",
signature: "security.policies",
enclosing: "security",
is_private: false,
documentation: "---------------------------------------------------------------------\n  security-policies -- Security Policies\n  Copyright (C) 2010, 2011, 2012, 2015, 2018 Stephane Carrez\n  Written by Stephane Carrez (Stephane.Carrez@gmail.com)\n\n  Licensed under the Apache License, Version 2.0 (the \"License\");\n  you may not use this file except in compliance with the License.\n  You may obtain a copy of the License at\n\n      http://www.apache.org/licenses/LICENSE-2.0\n\n  Unless required by applicable law or agreed to in writing, software\n  distributed under the License is distributed on an \"AS IS\" BASIS,\n  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n  See the License for the specific language governing permissions and\n  limitations under the License.\n---------------------------------------------------------------------",
documentation_snippet: "",
packages:    [
       {
       name: "Reader_Config",
       qualified_name: "Security.Policies.Reader_Config",
       signature: "security.policies.reader_config",
       enclosing: "security.policies",
       is_private: false,
       documentation: "",
       documentation_snippet: "",
variables:           [
              {
              name: "Config",
              qualified_name: "Security.Policies.Reader_Config.Config",
              signature: "security.policies.reader_config.config",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "Config : aliased Policy_Config;",
              }          ,
          ]
,       }   ,
   ]
,simple_types:    [
       {
       name: "Policy_Index",
       qualified_name: "Security.Policies.Policy_Index",
       signature: "security.policies.policy_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Policy_Index is new Positive;",
       }   ,
   ]
,array_types:    [
       {
       name: "Controller_Access_Array",
       qualified_name: "Security.Policies.Controller_Access_Array",
       signature: "security.policies.controller_access_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Controller_Access_Array is\n  array (Permissions.Permission_Index range <>) of Controller_Access;",
       }   ,
       {
       name: "Policy_Context_Array",
       qualified_name: "Security.Policies.Policy_Context_Array",
       signature: "security.policies.policy_context_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Policy_Context_Array is\n  array (Policy_Index range <>) of Policy_Context_Access;",
       }   ,
   ]
,record_types:    [
       {
       name: "Policy_Config",
       qualified_name: "Security.Policies.Policy_Config",
       signature: "security.policies.policy_config",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Policy_Config is record\n   Id          : Natural := 0;\n   Permissions : Util.Beans.Objects.Vectors.Vector;\n   Patterns    : Util.Beans.Objects.Vectors.Vector;\n   Manager     : Policy_Manager_Access;\nend record;",
       }   ,
   ]
,interface_types:    [
       {
       name: "Policy_Context",
       qualified_name: "Security.Policies.Policy_Context",
       signature: "security.policies.policy_context",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Policy_Context is limited interface;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Policy",
       qualified_name: "Security.Policies.Policy",
       signature: "security.policies.policy",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Policy is abstract new Ada.Finalization.Limited_Controlled with private;",
       }   ,
       {
       name: "Policy_Manager",
       qualified_name: "Security.Policies.Policy_Manager",
       signature: "security.policies.policy_manager",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Policy_Manager (Max_Policies : Policy_Index) is\n  new Ada.Finalization.Limited_Controlled with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Controller_Access",
       qualified_name: "Security.Policies.Controller_Access",
       signature: "security.policies.controller_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Controller_Access is access all Security.Controllers.Controller'Class;",
       }   ,
       {
       name: "Policy_Access",
       qualified_name: "Security.Policies.Policy_Access",
       signature: "security.policies.policy_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Policy_Access is access all Policy'Class;",
       }   ,
       {
       name: "Policy_Config_Access",
       qualified_name: "Security.Policies.Policy_Config_Access",
       signature: "security.policies.policy_config_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Policy_Config_Access is access all Policy_Config;",
       }   ,
       {
       name: "Policy_Context_Access",
       qualified_name: "Security.Policies.Policy_Context_Access",
       signature: "security.policies.policy_context_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Policy_Context_Access is access all Policy_Context'Class;",
       }   ,
       {
       name: "Policy_Context_Array_Access",
       qualified_name: "Security.Policies.Policy_Context_Array_Access",
       signature: "security.policies.policy_context_array_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Policy_Context_Array_Access is access Policy_Context_Array;",
       }   ,
       {
       name: "Policy_Manager_Access",
       qualified_name: "Security.Policies.Policy_Manager_Access",
       signature: "security.policies.policy_manager_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Policy_Manager_Access is access all Policy_Manager'Class;",
       }   ,
       {
       name: "Security_Context_Access",
       qualified_name: "Security.Policies.Security_Context_Access",
       signature: "security.policies.security_context_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Security_Context_Access is access all Contexts.Security_Context'Class;",
       }   ,
   ]
,}
---
