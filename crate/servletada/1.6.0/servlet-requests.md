---
crate: servletada
layout: gnatdoc
gnatdoc: {
name: "Servlet.Requests",
qualified_name: "Servlet.Requests",
signature: "servlet.requests",
enclosing: "servlet",
is_private: false,
documentation: "",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Request",
       qualified_name: "Servlet.Requests.Request",
       signature: "servlet.requests.request",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Request is abstract new Ada.Finalization.Limited_Controlled with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Request_Access",
       qualified_name: "Servlet.Requests.Request_Access",
       signature: "servlet.requests.request_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Request_Access is access all Request'Class;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Quality_Type",
       qualified_name: "Servlet.Requests.Quality_Type",
       signature: "servlet.requests.quality_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Quality_Type is Util.Http.Headers.Quality_Type;",
       }   ,
   ]
,}
---
