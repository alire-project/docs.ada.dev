---
crate: ado
layout: gnatdoc
gnatdoc: {
name: "ADO.Schemas",
qualified_name: "ADO.Schemas",
signature: "ado.schemas",
enclosing: "ado",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Column_Cursor",
       qualified_name: "ADO.Schemas.Column_Cursor",
       signature: "ado.schemas.column_cursor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Column_Cursor is private;",
       }   ,
       {
       name: "Column_Definition",
       qualified_name: "ADO.Schemas.Column_Definition",
       signature: "ado.schemas.column_definition",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Column_Definition is private;",
       }   ,
       {
       name: "Column_Index",
       qualified_name: "ADO.Schemas.Column_Index",
       signature: "ado.schemas.column_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Column_Index is new Natural range 0 .. ADO.Configs.MAX_COLUMNS;",
       }   ,
       {
       name: "Column_Type",
       qualified_name: "ADO.Schemas.Column_Type",
       signature: "ado.schemas.column_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Column_Type is\n  (\n   T_UNKNOWN,\n   T_BOOLEAN,\n   T_TINYINT,\n   T_SMALLINT,\n   T_INTEGER,\n   T_LONG_INTEGER,\n   T_FLOAT,\n   T_DOUBLE,\n   T_DECIMAL,\n   T_ENUM,\n   T_SET,\n   T_TIME,\n   T_YEAR,\n   T_DATE,\n   T_DATE_TIME,\n   T_TIMESTAMP,\n   T_CHAR,\n   T_VARCHAR,\n   T_BLOB,\n   T_NULL\n  );",
       }   ,
       {
       name: "Schema_Definition",
       qualified_name: "ADO.Schemas.Schema_Definition",
       signature: "ado.schemas.schema_definition",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Schema_Definition is limited private;",
       }   ,
       {
       name: "Table_Cursor",
       qualified_name: "ADO.Schemas.Table_Cursor",
       signature: "ado.schemas.table_cursor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Table_Cursor is private;",
       }   ,
       {
       name: "Table_Definition",
       qualified_name: "ADO.Schemas.Table_Definition",
       signature: "ado.schemas.table_definition",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Table_Definition is private;",
       }   ,
   ]
,array_types:    [
       {
       name: "Member_Names",
       qualified_name: "ADO.Schemas.Member_Names",
       signature: "ado.schemas.member_names",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Member_Names is array (Column_Index range <>) of Util.Strings.Name_Access;",
       }   ,
   ]
,record_types:    [
       {
       name: "Class_Mapping",
       qualified_name: "ADO.Schemas.Class_Mapping",
       signature: "ado.schemas.class_mapping",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Class_Mapping (Count : Column_Index)\nis tagged limited record\n   Table     : Util.Strings.Name_Access;\n   Members   : Member_Names (1 .. Count);\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Class_Mapping_Access",
       qualified_name: "ADO.Schemas.Class_Mapping_Access",
       signature: "ado.schemas.class_mapping_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Class_Mapping_Access is access constant Class_Mapping'Class;",
       }   ,
   ]
,}
---
