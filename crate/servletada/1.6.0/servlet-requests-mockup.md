---
crate: servletada
layout: gnatdoc
gnatdoc: {
name: "Servlet.Requests.Mockup",
qualified_name: "Servlet.Requests.Mockup",
signature: "servlet.requests.mockup",
enclosing: "servlet.requests",
is_private: false,
documentation: "------------------------------\nRequest Mockup\n------------------------------\nThe request mockup provides additional procedures to set the request\nparameters, the URI, the peer address and other read-only values.",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Part_Request",
       qualified_name: "Servlet.Requests.Mockup.Part_Request",
       signature: "servlet.requests.mockup.part_request",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Part_Request (Count : Natural) is new Request with private;",
       }   ,
       {
       name: "Request",
       qualified_name: "Servlet.Requests.Mockup.Request",
       signature: "servlet.requests.mockup.request",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Request is new Servlet.Requests.Request with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Request_Access",
       qualified_name: "Servlet.Requests.Mockup.Request_Access",
       signature: "servlet.requests.mockup.request_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Request_Access is access all Request'Class;",
       }   ,
   ]
,}
---
