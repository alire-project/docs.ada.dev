---
crate: dynamo
layout: gnatdoc
gnatdoc: {
name: "Gen.Model.Mappings",
qualified_name: "Gen.Model.Mappings",
signature: "gen.model.mappings",
enclosing: "gen.model",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Basic_Type",
       qualified_name: "Gen.Model.Mappings.Basic_Type",
       signature: "gen.model.mappings.basic_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Basic_Type is (T_BOOLEAN,\n                    T_INTEGER,\n                    T_DATE,\n                    T_ENUM,\n                    T_IDENTIFIER,\n                    T_STRING,\n                    T_FLOAT,\n                    T_BLOB,\n                    T_ENTITY_TYPE,\n                    T_BEAN,\n                    T_TABLE);",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Mapping_Definition",
       qualified_name: "Gen.Model.Mappings.Mapping_Definition",
       signature: "gen.model.mappings.mapping_definition",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Mapping_Definition is new Definition with record\n   Target        : UString;\n   Kind          : Basic_Type := T_INTEGER;\n   Allow_Null    : Mapping_Definition_Access;\n   Nullable      : Boolean := False;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Mapping_Definition_Access",
       qualified_name: "Gen.Model.Mappings.Mapping_Definition_Access",
       signature: "gen.model.mappings.mapping_definition_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Mapping_Definition_Access is access all Mapping_Definition'Class;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Cursor",
       qualified_name: "Gen.Model.Mappings.Cursor",
       signature: "gen.model.mappings.cursor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Cursor is Mapping_Maps.Cursor;",
       }   ,
       {
       name: "Map",
       qualified_name: "Gen.Model.Mappings.Map",
       signature: "gen.model.mappings.map",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Map is Mapping_Maps.Map;",
       }   ,
   ]
,constants:    [
       {
       name: "ADA_MAPPING",
       qualified_name: "Gen.Model.Mappings.ADA_MAPPING",
       signature: "gen.model.mappings.ada_mapping",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "ADA_MAPPING    : constant String := \"Ada05\";",
       }   ,
       {
       name: "MySQL_MAPPING",
       qualified_name: "Gen.Model.Mappings.MySQL_MAPPING",
       signature: "gen.model.mappings.mysql_mapping",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "MySQL_MAPPING  : constant String := \"MySQL\";",
       }   ,
       {
       name: "Postgresql_MAPPING",
       qualified_name: "Gen.Model.Mappings.Postgresql_MAPPING",
       signature: "gen.model.mappings.postgresql_mapping",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Postgresql_MAPPING : constant String := \"Postgresql\";",
       }   ,
       {
       name: "SQLite_MAPPING",
       qualified_name: "Gen.Model.Mappings.SQLite_MAPPING",
       signature: "gen.model.mappings.sqlite_mapping",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "SQLite_MAPPING : constant String := \"SQLite\";",
       }   ,
   ]
,}
---
