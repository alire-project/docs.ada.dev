---
crate: servletada
layout: gnatdoc
gnatdoc: {
name: "Servlet.Routes.Servlets.Rest",
qualified_name: "Servlet.Routes.Servlets.Rest",
signature: "servlet.routes.servlets.rest",
enclosing: "servlet.routes.servlets",
is_private: false,
documentation: "",
documentation_snippet: "",
array_types:    [
       {
       name: "Descriptor_Array",
       qualified_name: "Servlet.Routes.Servlets.Rest.Descriptor_Array",
       signature: "servlet.routes.servlets.rest.descriptor_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Descriptor_Array is array (Servlet.Rest.Method_Type) of Servlet.Rest.Descriptor_Access;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "API_Route_Type",
       qualified_name: "Servlet.Routes.Servlets.Rest.API_Route_Type",
       signature: "servlet.routes.servlets.rest.api_route_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type API_Route_Type is new Servlet.Routes.Servlets.Servlet_Route_Type with record\n   Descriptors : Descriptor_Array;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "API_Route_Type_Access",
       qualified_name: "Servlet.Routes.Servlets.Rest.API_Route_Type_Access",
       signature: "servlet.routes.servlets.rest.api_route_type_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type API_Route_Type_Access is access all API_Route_Type'Class;",
       }   ,
   ]
,}
---
