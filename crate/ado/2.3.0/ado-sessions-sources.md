---
crate: ado
layout: gnatdoc
gnatdoc: {
name: "ADO.Sessions.Sources",
qualified_name: "ADO.Sessions.Sources",
signature: "ado.sessions.sources",
enclosing: "ado.sessions",
is_private: false,
documentation: "------------------------------\nThe database connection source\n------------------------------\nThe <b>DataSource</b> is the factory for getting a connection to the database.\nIt contains the configuration properties to define which database driver must\nbe used and which connection parameters the driver has to use to establish\nthe connection.",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Data_Source",
       qualified_name: "ADO.Sessions.Sources.Data_Source",
       signature: "ado.sessions.sources.data_source",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Data_Source is new ADO.Connections.Configuration with private;",
       }   ,
       {
       name: "Replicated_DataSource",
       qualified_name: "ADO.Sessions.Sources.Replicated_DataSource",
       signature: "ado.sessions.sources.replicated_datasource",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Replicated_DataSource is new Data_Source with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Data_Source_Access",
       qualified_name: "ADO.Sessions.Sources.Data_Source_Access",
       signature: "ado.sessions.sources.data_source_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Data_Source_Access is access all Data_Source'Class;",
       }   ,
       {
       name: "Replicated_DataSource_Access",
       qualified_name: "ADO.Sessions.Sources.Replicated_DataSource_Access",
       signature: "ado.sessions.sources.replicated_datasource_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Replicated_DataSource_Access is access all Replicated_DataSource'Class;",
       }   ,
   ]
,}
---
