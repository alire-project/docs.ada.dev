---
crate: dynamo
layout: gnatdoc
gnatdoc: {
name: "Gen.Model.Tables",
qualified_name: "Gen.Model.Tables",
signature: "gen.model.tables",
enclosing: "gen.model",
is_private: false,
documentation: "---------------------------------------------------------------------\n  gen-model-tables -- Database table model representation\n  Copyright (C) 2009 - 2022 Stephane Carrez\n  Written by Stephane Carrez (Stephane.Carrez@gmail.com)\n\n  Licensed under the Apache License, Version 2.0 (the \"License\");\n  you may not use this file except in compliance with the License.\n  You may obtain a copy of the License at\n\n      http://www.apache.org/licenses/LICENSE-2.0\n\n  Unless required by applicable law or agreed to in writing, software\n  distributed under the License is distributed on an \"AS IS\" BASIS,\n  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n  See the License for the specific language governing permissions and\n  limitations under the License.\n---------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Dependency_Type",
       qualified_name: "Gen.Model.Tables.Dependency_Type",
       signature: "gen.model.tables.dependency_type",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum NONE\n@enum FORWARD\n@enum BACKWARD\n  CIRCULAR is not yet managed.",
       documentation_snippet: "type Dependency_Type is (NONE, FORWARD, BACKWARD);",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Association_Definition",
       qualified_name: "Gen.Model.Tables.Association_Definition",
       signature: "gen.model.tables.association_definition",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Association_Definition is new Column_Definition with private;",
       }   ,
       {
       name: "Column_Definition",
       qualified_name: "Gen.Model.Tables.Column_Definition",
       signature: "gen.model.tables.column_definition",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Column_Definition is new Definition with record\n   Number   : Natural := 0;\n   Table    : Table_Definition_Access;\n   Bean     : UBO.Object;\n   Type_Name : UString;\n   Sql_Type  : UString;\n   Sql_Name   : UString;\n   Sql_Length : Positive := 255;\n   Not_Null : Boolean := False;\n   Unique    : Boolean := False;\n   Is_Version : Boolean := False;\n   Is_Key : Boolean := False;\n   Is_Readable  : Boolean := True;\n   Is_Inserted  : Boolean := True;\n   Is_Updated   : Boolean := True;\n   Is_Auditable : Boolean := False;\n   Use_Foreign_Key_Type : Boolean := False;\n   Generator    : UBO.Object;\n   Type_Mapping : Gen.Model.Mappings.Mapping_Definition_Access;\nend record;",
       }   ,
       {
       name: "Table_Definition",
       qualified_name: "Gen.Model.Tables.Table_Definition",
       signature: "gen.model.tables.table_definition",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Table_Definition is new Mappings.Mapping_Definition with record\n   Members          : aliased Column_List.List_Definition;\n   Members_Bean     : UBO.Object;\n   Auditables       : aliased Column_List.List_Definition;\n   Auditables_Bean  : UBO.Object;\n   Operations       : aliased Operation_List.List_Definition;\n   Operations_Bean  : UBO.Object;\n   Parent           : Table_Definition_Access;\n   Parent_Name      : UString;\n   Package_Def      : Gen.Model.Packages.Package_Definition_Access;\n   Type_Name        : UString;\n   Pkg_Name         : UString;\n   Table_Name       : UString;\n   Version_Column   : Column_Definition_Access;\n   Id_Column        : Column_Definition_Access;\n   Key_Count        : Natural := 0;\n   Has_Associations : Boolean := False;\n   Dependencies     : Table_Vectors.Vector;\n   Has_List         : Boolean := True;\n   Has_Mark         : Boolean := False;\n   Is_Limited       : Boolean := False;\n   Is_Serializable  : Boolean := False;\n   Is_Auditable     : Boolean := False;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Association_Definition_Access",
       qualified_name: "Gen.Model.Tables.Association_Definition_Access",
       signature: "gen.model.tables.association_definition_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Association_Definition_Access is access all Association_Definition'Class;",
       }   ,
       {
       name: "Column_Definition_Access",
       qualified_name: "Gen.Model.Tables.Column_Definition_Access",
       signature: "gen.model.tables.column_definition_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Column_Definition_Access is access all Column_Definition'Class;",
       }   ,
       {
       name: "Table_Definition_Access",
       qualified_name: "Gen.Model.Tables.Table_Definition_Access",
       signature: "gen.model.tables.table_definition_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Table_Definition_Access is access all Table_Definition'Class;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Table_Cursor",
       qualified_name: "Gen.Model.Tables.Table_Cursor",
       signature: "gen.model.tables.table_cursor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Table_Cursor is Table_Map.Cursor;",
       }   ,
   ]
,}
---
