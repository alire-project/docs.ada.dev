---
crate: ado
layout: gnatdoc
gnatdoc: {
name: "ADO.SQL",
qualified_name: "ADO.SQL",
signature: "ado.sql",
enclosing: "ado",
is_private: false,
documentation: "--------------------\nBuffer\n--------------------\nThe <b>Buffer</b> type allows to build easily an SQL statement.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Buffer",
       qualified_name: "ADO.SQL.Buffer",
       signature: "ado.sql.buffer",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Buffer is private;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Query",
       qualified_name: "ADO.SQL.Query",
       signature: "ado.sql.query",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Query is new ADO.Parameters.List with record\n   SQL    : Buffer;\n   Filter : Buffer;\n   Join   : Buffer;\nend record;",
       }   ,
       {
       name: "Update_Query",
       qualified_name: "ADO.SQL.Update_Query",
       signature: "ado.sql.update_query",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Update_Query is new Query with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Buffer_Access",
       qualified_name: "ADO.SQL.Buffer_Access",
       signature: "ado.sql.buffer_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Buffer_Access is access all Buffer;",
       }   ,
       {
       name: "Query_Access",
       qualified_name: "ADO.SQL.Query_Access",
       signature: "ado.sql.query_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Query_Access is access all Query'Class;",
       }   ,
       {
       name: "Update_Query_Access",
       qualified_name: "ADO.SQL.Update_Query_Access",
       signature: "ado.sql.update_query_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Update_Query_Access is access all Update_Query'Class;",
       }   ,
   ]
,}
---
