---
crate: servletada
layout: gnatdoc
gnatdoc: {
name: "Servlet.Rest",
qualified_name: "Servlet.Rest",
signature: "servlet.rest",
enclosing: "servlet",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Method_Type",
       qualified_name: "Servlet.Rest.Method_Type",
       signature: "servlet.rest.method_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Method_Type is (GET, HEAD, POST, PUT, DELETE, TRACE, CONNECT, OPTIONS, PATCH);",
       }   ,
       {
       name: "Stream_Type",
       qualified_name: "Servlet.Rest.Stream_Type",
       signature: "servlet.rest.stream_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Stream_Type is (JSON, XML, FORM, RAW);",
       }   ,
   ]
,array_types:    [
       {
       name: "Stream_Modes",
       qualified_name: "Servlet.Rest.Stream_Modes",
       signature: "servlet.rest.stream_modes",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Stream_Modes is array (Stream_Type) of Boolean;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Descriptor",
       qualified_name: "Servlet.Rest.Descriptor",
       signature: "servlet.rest.descriptor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Descriptor is abstract tagged limited private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Descriptor_Access",
       qualified_name: "Servlet.Rest.Descriptor_Access",
       signature: "servlet.rest.descriptor_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Descriptor_Access is access all Descriptor'Class;",
       }   ,
       {
       name: "Operation_Access",
       qualified_name: "Servlet.Rest.Operation_Access",
       signature: "servlet.rest.operation_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Operation_Access is\n   access procedure (Req    : in out Servlet.Rest.Request'Class;\n                     Reply  : in out Servlet.Rest.Response'Class;\n                     Stream : in out Servlet.Rest.Output_Stream'Class);",
       }   ,
   ]
,subtypes:    [
       {
       name: "Mime_Access",
       qualified_name: "Servlet.Rest.Mime_Access",
       signature: "servlet.rest.mime_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Mime_Access is Util.Http.Mimes.Mime_Access;",
       }   ,
       {
       name: "Mime_List",
       qualified_name: "Servlet.Rest.Mime_List",
       signature: "servlet.rest.mime_list",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Mime_List is Util.Http.Mimes.Mime_List;",
       }   ,
       {
       name: "Mime_List_Access",
       qualified_name: "Servlet.Rest.Mime_List_Access",
       signature: "servlet.rest.mime_list_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Mime_List_Access is Util.Http.Mimes.Mime_List_Access;",
       }   ,
       {
       name: "Output_Stream",
       qualified_name: "Servlet.Rest.Output_Stream",
       signature: "servlet.rest.output_stream",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Output_Stream is Util.Serialize.IO.Output_Stream;",
       }   ,
       {
       name: "Request",
       qualified_name: "Servlet.Rest.Request",
       signature: "servlet.rest.request",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Request is Servlet.Requests.Request;",
       }   ,
       {
       name: "Response",
       qualified_name: "Servlet.Rest.Response",
       signature: "servlet.rest.response",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Response is Servlet.Responses.Response;",
       }   ,
   ]
,}
---
