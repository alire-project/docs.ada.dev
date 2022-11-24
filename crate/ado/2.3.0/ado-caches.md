---
crate: ado
layout: gnatdoc
gnatdoc: {
name: "ADO.Caches",
qualified_name: "ADO.Caches",
signature: "ado.caches",
enclosing: "ado",
is_private: false,
documentation: "---------------------------------------------------------------------\n  ado-cache -- Simple cache management\n  Copyright (C) 2017 Stephane Carrez\n  Written by Stephane Carrez (Stephane.Carrez@gmail.com)\n\n  Licensed under the Apache License, Version 2.0 (the \"License\");\n  you may not use this file except in compliance with the License.\n  You may obtain a copy of the License at\n\n      http://www.apache.org/licenses/LICENSE-2.0\n\n  Unless required by applicable law or agreed to in writing, software\n  distributed under the License is distributed on an \"AS IS\" BASIS,\n  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n  See the License for the specific language governing permissions and\n  limitations under the License.\n---------------------------------------------------------------------",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Cache_Manager",
       qualified_name: "ADO.Caches.Cache_Manager",
       signature: "ado.caches.cache_manager",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Cache_Manager is limited new Ada.Finalization.Limited_Controlled\n  and ADO.Parameters.Expander with private;",
       }   ,
       {
       name: "Cache_Type",
       qualified_name: "ADO.Caches.Cache_Type",
       signature: "ado.caches.cache_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Cache_Type is abstract limited new Ada.Finalization.Limited_Controlled with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Cache_Manager_Access",
       qualified_name: "ADO.Caches.Cache_Manager_Access",
       signature: "ado.caches.cache_manager_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Cache_Manager_Access is access all Cache_Manager'Class;",
       }   ,
       {
       name: "Cache_Type_Access",
       qualified_name: "ADO.Caches.Cache_Type_Access",
       signature: "ado.caches.cache_type_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Cache_Type_Access is access all Cache_Type'Class;",
       }   ,
   ]
,}
---
