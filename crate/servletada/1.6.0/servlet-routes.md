---
crate: servletada
layout: gnatdoc
gnatdoc: {
name: "Servlet.Routes",
qualified_name: "Servlet.Routes",
signature: "servlet.routes",
enclosing: "servlet",
is_private: false,
documentation: "---------------------------------------------------------------------\n  servlet-routes -- Request routing\n  Copyright (C) 2015, 2016, 2017, 2019, 2021 Stephane Carrez\n  Written by Stephane Carrez (Stephane.Carrez@gmail.com)\n\n  Licensed under the Apache License, Version 2.0 (the \"License\");\n  you may not use this file except in compliance with the License.\n  You may obtain a copy of the License at\n\n      http://www.apache.org/licenses/LICENSE-2.0\n\n  Unless required by applicable law or agreed to in writing, software\n  distributed under the License is distributed on an \"AS IS\" BASIS,\n  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n  See the License for the specific language governing permissions and\n  limitations under the License.\n---------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Path_Mode",
       qualified_name: "Servlet.Routes.Path_Mode",
       signature: "servlet.routes.path_mode",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Path_Mode is (FULL, PREFIX, SUFFIX);",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Route_Context_Type",
       qualified_name: "Servlet.Routes.Route_Context_Type",
       signature: "servlet.routes.route_context_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Route_Context_Type is tagged limited private;",
       }   ,
       {
       name: "Route_Type",
       qualified_name: "Servlet.Routes.Route_Type",
       signature: "servlet.routes.route_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Route_Type is abstract new Util.Refs.Ref_Entity with null record;",
       }   ,
       {
       name: "Router_Type",
       qualified_name: "Servlet.Routes.Router_Type",
       signature: "servlet.routes.router_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Router_Type is new Ada.Finalization.Limited_Controlled with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Route_Type_Access",
       qualified_name: "Servlet.Routes.Route_Type_Access",
       signature: "servlet.routes.route_type_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Route_Type_Access is access all Route_Type'Class;",
       }   ,
       {
       name: "Router_Type_Access",
       qualified_name: "Servlet.Routes.Router_Type_Access",
       signature: "servlet.routes.router_type_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Router_Type_Access is access all Router_Type'Class;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Route_Type_Accessor",
       qualified_name: "Servlet.Routes.Route_Type_Accessor",
       signature: "servlet.routes.route_type_accessor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Route_Type_Accessor is Route_Type_Refs.Element_Accessor;",
       }   ,
       {
       name: "Route_Type_Ref",
       qualified_name: "Servlet.Routes.Route_Type_Ref",
       signature: "servlet.routes.route_type_ref",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Route_Type_Ref is Route_Type_Refs.Ref;",
       }   ,
   ]
,}
---
