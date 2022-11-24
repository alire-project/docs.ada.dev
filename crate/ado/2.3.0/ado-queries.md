---
crate: ado
layout: gnatdoc
gnatdoc: {
name: "ADO.Queries",
qualified_name: "ADO.Queries",
signature: "ado.queries",
enclosing: "ado",
is_private: false,
documentation: "Exception raised when a query does not exist or is empty.",
documentation_snippet: "",
simple_types:    [
       {
       name: "File_Index",
       qualified_name: "ADO.Queries.File_Index",
       signature: "ado.queries.file_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type File_Index is new Natural;",
       }   ,
       {
       name: "Query_Definition",
       qualified_name: "ADO.Queries.Query_Definition",
       signature: "ado.queries.query_definition",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Query_Definition is limited private;",
       }   ,
       {
       name: "Query_File",
       qualified_name: "ADO.Queries.Query_File",
       signature: "ado.queries.query_file",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Query_File is limited private;",
       }   ,
       {
       name: "Query_Index",
       qualified_name: "ADO.Queries.Query_Index",
       signature: "ado.queries.query_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Query_Index is new Natural;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Context",
       qualified_name: "ADO.Queries.Context",
       signature: "ado.queries.context",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Context is new ADO.SQL.Query with private;",
       }   ,
       {
       name: "Query_Manager",
       qualified_name: "ADO.Queries.Query_Manager",
       signature: "ado.queries.query_manager",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Query_Manager is limited new Ada.Finalization.Limited_Controlled with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Query_Definition_Access",
       qualified_name: "ADO.Queries.Query_Definition_Access",
       signature: "ado.queries.query_definition_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Query_Definition_Access is access all Query_Definition;",
       }   ,
       {
       name: "Query_File_Access",
       qualified_name: "ADO.Queries.Query_File_Access",
       signature: "ado.queries.query_file_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Query_File_Access is access all Query_File;",
       }   ,
       {
       name: "Query_Manager_Access",
       qualified_name: "ADO.Queries.Query_Manager_Access",
       signature: "ado.queries.query_manager_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Query_Manager_Access is access all Query_Manager;",
       }   ,
       {
       name: "Static_Loader_Access",
       qualified_name: "ADO.Queries.Static_Loader_Access",
       signature: "ado.queries.static_loader_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Static_Loader_Access is\n  access function (Name : in String) return access constant String;",
       }   ,
   ]
,}
---
