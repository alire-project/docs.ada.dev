---
crate: ado
layout: gnatdoc
gnatdoc: {
name: "ADO.Connections",
qualified_name: "ADO.Connections",
signature: "ado.connections",
enclosing: "ado",
is_private: false,
documentation: "Raised for all errors reported by the database.",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Configuration",
       qualified_name: "ADO.Connections.Configuration",
       signature: "ado.connections.configuration",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Configuration is new ADO.Configs.Configuration with null record;",
       }   ,
       {
       name: "Database_Connection",
       qualified_name: "ADO.Connections.Database_Connection",
       signature: "ado.connections.database_connection",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Database_Connection is abstract new Util.Refs.Ref_Entity with record\n   Ident : String (1 .. 8) := (others => ' ');\nend record;",
       }   ,
       {
       name: "Driver",
       qualified_name: "ADO.Connections.Driver",
       signature: "ado.connections.driver",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Driver is abstract tagged limited private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Database_Connection_Access",
       qualified_name: "ADO.Connections.Database_Connection_Access",
       signature: "ado.connections.database_connection_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Database_Connection_Access is access all Database_Connection'Class;",
       }   ,
       {
       name: "Driver_Access",
       qualified_name: "ADO.Connections.Driver_Access",
       signature: "ado.connections.driver_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Driver_Access is access all Driver'Class;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Driver_Index",
       qualified_name: "ADO.Connections.Driver_Index",
       signature: "ado.connections.driver_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Driver_Index is ADO.Configs.Driver_Index range 1 .. ADO.Configs.Driver_Index'Last;",
       }   ,
   ]
,}
---
