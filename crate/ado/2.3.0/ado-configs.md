---
crate: ado
layout: gnatdoc
gnatdoc: {
name: "ADO.Configs",
qualified_name: "ADO.Configs",
signature: "ado.configs",
enclosing: "ado",
is_private: false,
documentation: "Configuration property to control the search paths to load XML queries.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Driver_Index",
       qualified_name: "ADO.Configs.Driver_Index",
       signature: "ado.configs.driver_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Driver_Index is new Natural range 0 .. MAX_DRIVERS;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Configuration",
       qualified_name: "ADO.Configs.Configuration",
       signature: "ado.configs.configuration",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Configuration is new Ada.Finalization.Controlled with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Configuration_Access",
       qualified_name: "ADO.Configs.Configuration_Access",
       signature: "ado.configs.configuration_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Configuration_Access is access all Configuration'Class;",
       }   ,
   ]
,constants:    [
       {
       name: "DYNAMIC_DRIVER_LOAD",
       qualified_name: "ADO.Configs.DYNAMIC_DRIVER_LOAD",
       signature: "ado.configs.dynamic_driver_load",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "DYNAMIC_DRIVER_LOAD : constant String := \"ado.drivers.load\";",
       }   ,
       {
       name: "MAX_COLUMNS",
       qualified_name: "ADO.Configs.MAX_COLUMNS",
       signature: "ado.configs.max_columns",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "MAX_COLUMNS : constant := 2000;",
       }   ,
       {
       name: "MAX_DRIVERS",
       qualified_name: "ADO.Configs.MAX_DRIVERS",
       signature: "ado.configs.max_drivers",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "MAX_DRIVERS : constant := 4;",
       }   ,
       {
       name: "NO_ENTITY_LOAD",
       qualified_name: "ADO.Configs.NO_ENTITY_LOAD",
       signature: "ado.configs.no_entity_load",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "NO_ENTITY_LOAD : constant String := \"ado.entities.ignore\";",
       }   ,
       {
       name: "QUERY_LOAD_CONFIG",
       qualified_name: "ADO.Configs.QUERY_LOAD_CONFIG",
       signature: "ado.configs.query_load_config",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "QUERY_LOAD_CONFIG  : constant String := \"ado.queries.load\";",
       }   ,
       {
       name: "QUERY_PATHS_CONFIG",
       qualified_name: "ADO.Configs.QUERY_PATHS_CONFIG",
       signature: "ado.configs.query_paths_config",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "QUERY_PATHS_CONFIG : constant String := \"ado.queries.paths\";",
       }   ,
   ]
,}
---
