---
crate: gnoga
layout: gnatdoc
gnatdoc: {
name: "Gnoga.Server.Database.SQLite",
qualified_name: "Gnoga.Server.Database.SQLite",
signature: "gnoga.server.database.sqlite",
enclosing: "gnoga.server.database",
is_private: false,
documentation: "You will need to add linker options for SQLite. This can be done as part\nof gpr files, command line or even something like:\n  pragma Linker_Options (\"-lsqlite3\");",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Connection",
       qualified_name: "Gnoga.Server.Database.SQLite.Connection",
       signature: "gnoga.server.database.sqlite.connection",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Connection is new Gnoga.Server.Database.Connection with private;",
       }   ,
       {
       name: "Recordset",
       qualified_name: "Gnoga.Server.Database.SQLite.Recordset",
       signature: "gnoga.server.database.sqlite.recordset",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Recordset (Server_ID : SQLite_ID) is new Gnoga.Server.Database.Recordset with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Connection_Access",
       qualified_name: "Gnoga.Server.Database.SQLite.Connection_Access",
       signature: "gnoga.server.database.sqlite.connection_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Connection_Access is access all Connection'Class;",
       }   ,
       {
       name: "SQLite_ID",
       qualified_name: "Gnoga.Server.Database.SQLite.SQLite_ID",
       signature: "gnoga.server.database.sqlite.sqlite_id",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SQLite_ID is access all Integer;",
       }   ,
   ]
,}
---
