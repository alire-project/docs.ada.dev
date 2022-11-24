---
crate: minirest
layout: gnatdoc
gnatdoc: {
name: "Minirest",
qualified_name: "Minirest",
signature: "minirest",
enclosing: "",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Parameters",
       qualified_name: "Minirest.Parameters",
       signature: "minirest.parameters",
       enclosing: "",
       is_private: false,
       documentation: "A collection of arguments of type key + value",
       documentation_snippet: "type Parameters is private;",
       }   ,
       {
       name: "Status_Kinds",
       qualified_name: "Minirest.Status_Kinds",
       signature: "minirest.status_kinds",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum Informative\n  1xx\n@enum Success\n  2xx\n@enum Redirect\n  3xx\n@enum Client_Error\n  4xx\n@enum Server_Error\n  5xx",
       documentation_snippet: "type Status_Kinds is (Informative,\n                      Success,\n                      Redirect,\n                      Client_Error,\n                      Server_Error);",
       }   ,
   ]
,record_types:    [
       {
       name: "Response",
       qualified_name: "Minirest.Response",
       signature: "minirest.response",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Response (Status : Status_Kinds; Status_Length : Natural) is tagged\n   record\n      Status_Line : String (1 .. Status_Length);\n      Status_Code : Positive range 100 .. 599;\n      Raw_Headers : AAA.Strings.Vector;\n      Headers     : AAA.Strings.Map;\n      Content     : AAA.Strings.Vector;\n   end record;",
       }   ,
   ]
,constants:    [
       {
       name: "No_Arguments",
       qualified_name: "Minirest.No_Arguments",
       signature: "minirest.no_arguments",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Arguments : constant Parameters;",
       }   ,
   ]
,}
---
