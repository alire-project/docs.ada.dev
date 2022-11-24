---
crate: security
layout: gnatdoc
gnatdoc: {
name: "Security.Policies.URLs",
qualified_name: "Security.Policies.URLs",
signature: "security.policies.urls",
enclosing: "security.policies",
is_private: false,
documentation: "---------------------------------------------------------------------\n  security-policies-urls -- URL security policy\n  Copyright (C) 2010, 2011, 2012, 2017, 2018, 2019 Stephane Carrez\n  Written by Stephane Carrez (Stephane.Carrez@gmail.com)\n\n  Licensed under the Apache License, Version 2.0 (the \"License\");\n  you may not use this file except in compliance with the License.\n  You may obtain a copy of the License at\n\n      http://www.apache.org/licenses/LICENSE-2.0\n\n  Unless required by applicable law or agreed to in writing, software\n  distributed under the License is distributed on an \"AS IS\" BASIS,\n  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n  See the License for the specific language governing permissions and\n  limitations under the License.\n---------------------------------------------------------------------",
documentation_snippet: "",
tagged_types:    [
       {
       name: "URL_Permission",
       qualified_name: "Security.Policies.URLs.URL_Permission",
       signature: "security.policies.urls.url_permission",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type URL_Permission (Len : Natural) is new Permissions.Permission (P_URL.Permission) with record\n   URL : String (1 .. Len);\nend record;",
       }   ,
       {
       name: "URL_Policy",
       qualified_name: "Security.Policies.URLs.URL_Policy",
       signature: "security.policies.urls.url_policy",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type URL_Policy is new Policy with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "URL_Policy_Access",
       qualified_name: "Security.Policies.URLs.URL_Policy_Access",
       signature: "security.policies.urls.url_policy_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type URL_Policy_Access is access all URL_Policy'Class;",
       }   ,
   ]
,constants:    [
       {
       name: "NAME",
       qualified_name: "Security.Policies.URLs.NAME",
       signature: "security.policies.urls.name",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "NAME : constant String := \"URL-Policy\";",
       }   ,
   ]
,}
---
