---
crate: serverfaces
layout: gnatdoc
gnatdoc: {
name: "ASF.Routes.Servlets",
qualified_name: "ASF.Routes.Servlets",
signature: "asf.routes.servlets",
enclosing: "asf.routes",
is_private: false,
documentation: "---------------------------------------------------------------------\n  asf-routes-servlets -- Servlet request routing\n  Copyright (C) 2015 Stephane Carrez\n  Written by Stephane Carrez (Stephane.Carrez@gmail.com)\n\n  Licensed under the Apache License, Version 2.0 (the \"License\");\n  you may not use this file except in compliance with the License.\n  You may obtain a copy of the License at\n\n      http://www.apache.org/licenses/LICENSE-2.0\n\n  Unless required by applicable law or agreed to in writing, software\n  distributed under the License is distributed on an \"AS IS\" BASIS,\n  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n  See the License for the specific language governing permissions and\n  limitations under the License.\n---------------------------------------------------------------------",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Proxy_Route_Type",
       qualified_name: "ASF.Routes.Servlets.Proxy_Route_Type",
       signature: "asf.routes.servlets.proxy_route_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Proxy_Route_Type is new Servlet_Route_Type with record\n   Route   : Servlet_Route_Type_Access;\nend record;",
       }   ,
       {
       name: "Servlet_Route_Type",
       qualified_name: "ASF.Routes.Servlets.Servlet_Route_Type",
       signature: "asf.routes.servlets.servlet_route_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Servlet_Route_Type is new ASF.Routes.Route_Type with record\n   Filters : ASF.Filters.Filter_List_Access;\n   Servlet : ASF.Servlets.Servlet_Access;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Proxy_Route_Type_Access",
       qualified_name: "ASF.Routes.Servlets.Proxy_Route_Type_Access",
       signature: "asf.routes.servlets.proxy_route_type_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Proxy_Route_Type_Access is access all Proxy_Route_Type'Class;",
       }   ,
       {
       name: "Servlet_Route_Type_Access",
       qualified_name: "ASF.Routes.Servlets.Servlet_Route_Type_Access",
       signature: "asf.routes.servlets.servlet_route_type_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Servlet_Route_Type_Access is access all Servlet_Route_Type'Class;",
       }   ,
   ]
,}
---
