---
crate: serverfaces
layout: gnatdoc
gnatdoc: {
name: "ASF.Security.Filters",
qualified_name: "ASF.Security.Filters",
signature: "asf.security.filters",
enclosing: "asf.security",
is_private: false,
documentation: "---------------------------------------------------------------------\n  security-filters -- Security filter\n  Copyright (C) 2011, 2012, 2015, 2018 Stephane Carrez\n  Written by Stephane Carrez (Stephane.Carrez@gmail.com)\n\n  Licensed under the Apache License, Version 2.0 (the \"License\");\n  you may not use this file except in compliance with the License.\n  You may obtain a copy of the License at\n\n      http://www.apache.org/licenses/LICENSE-2.0\n\n  Unless required by applicable law or agreed to in writing, software\n  distributed under the License is distributed on an \"AS IS\" BASIS,\n  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n  See the License for the specific language governing permissions and\n  limitations under the License.\n---------------------------------------------------------------------",
documentation_snippet: "",
subtypes:    [
       {
       name: "Auth_Filter",
       qualified_name: "ASF.Security.Filters.Auth_Filter",
       signature: "asf.security.filters.auth_filter",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Auth_Filter is Servlet.Security.Filters.Auth_Filter;",
       }   ,
   ]
,constants:    [
       {
       name: "AID_COOKIE",
       qualified_name: "ASF.Security.Filters.AID_COOKIE",
       signature: "asf.security.filters.aid_cookie",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "AID_COOKIE : constant String := \"AID\";",
       }   ,
       {
       name: "SID_COOKIE",
       qualified_name: "ASF.Security.Filters.SID_COOKIE",
       signature: "asf.security.filters.sid_cookie",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "SID_COOKIE : constant String := \"SID\";",
       }   ,
   ]
,}
---
