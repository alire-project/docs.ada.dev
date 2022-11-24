---
crate: openapi
layout: gnatdoc
gnatdoc: {
name: "OpenAPI.Clients",
qualified_name: "OpenAPI.Clients",
signature: "openapi.clients",
enclosing: "openapi",
is_private: false,
documentation: "Exception raised when an API was not found.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Operation_Type",
       qualified_name: "OpenAPI.Clients.Operation_Type",
       signature: "openapi.clients.operation_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Operation_Type is (HEAD, GET, POST, PUT, DELETE, OPTIONS, PATCH);",
       }   ,
       {
       name: "Stream_Accessor",
       qualified_name: "OpenAPI.Clients.Stream_Accessor",
       signature: "openapi.clients.stream_accessor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Stream_Accessor (Stream : access OpenAPI.Streams.Output_Stream'Class) is private\nwith Implicit_Dereference => Stream;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Client_Type",
       qualified_name: "OpenAPI.Clients.Client_Type",
       signature: "openapi.clients.client_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Client_Type is new Util.Http.Clients.Client with private;",
       }   ,
       {
       name: "Request_Type",
       qualified_name: "OpenAPI.Clients.Request_Type",
       signature: "openapi.clients.request_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Request_Type is tagged limited private;",
       }   ,
       {
       name: "URI_Type",
       qualified_name: "OpenAPI.Clients.URI_Type",
       signature: "openapi.clients.uri_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type URI_Type is tagged private;",
       }   ,
   ]
,}
---
