---
crate: gnoga
layout: gnatdoc
gnatdoc: {
name: "Gnoga.Server.Database.MySQL",
qualified_name: "Gnoga.Server.Database.MySQL",
signature: "gnoga.server.database.mysql",
enclosing: "gnoga.server.database",
is_private: false,
documentation: "You will need to add linker options for MySQL. This can be done as part\nof gpr files, command line or even something like:\n pragma Linker_Options (\"-lmysqlclient\");",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Connection",
       qualified_name: "Gnoga.Server.Database.MySQL.Connection",
       signature: "gnoga.server.database.mysql.connection",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Connection is new Gnoga.Server.Database.Connection with private;",
       }   ,
       {
       name: "Recordset",
       qualified_name: "Gnoga.Server.Database.MySQL.Recordset",
       signature: "gnoga.server.database.mysql.recordset",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Recordset (Server_ID : MySQL_ID) is new Gnoga.Server.Database.Recordset with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Connection_Access",
       qualified_name: "Gnoga.Server.Database.MySQL.Connection_Access",
       signature: "gnoga.server.database.mysql.connection_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Connection_Access is access all Connection'Class;",
       }   ,
       {
       name: "MySQL_ID",
       qualified_name: "Gnoga.Server.Database.MySQL.MySQL_ID",
       signature: "gnoga.server.database.mysql.mysql_id",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type MySQL_ID is access all Integer;",
       }   ,
   ]
,}
---
