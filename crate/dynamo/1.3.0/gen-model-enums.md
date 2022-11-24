---
crate: dynamo
layout: gnatdoc
gnatdoc: {
name: "Gen.Model.Enums",
qualified_name: "Gen.Model.Enums",
signature: "gen.model.enums",
enclosing: "gen.model",
is_private: false,
documentation: "---------------------------------------------------------------------\n  gen-model-enums -- Enum definitions\n  Copyright (C) 2011, 2012, 2018, 2021 Stephane Carrez\n  Written by Stephane Carrez (Stephane.Carrez@gmail.com)\n\n  Licensed under the Apache License, Version 2.0 (the \"License\");\n  you may not use this file except in compliance with the License.\n  You may obtain a copy of the License at\n\n      http://www.apache.org/licenses/LICENSE-2.0\n\n  Unless required by applicable law or agreed to in writing, software\n  distributed under the License is distributed on an \"AS IS\" BASIS,\n  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n  See the License for the specific language governing permissions and\n  limitations under the License.\n---------------------------------------------------------------------",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Enum_Definition",
       qualified_name: "Gen.Model.Enums.Enum_Definition",
       signature: "gen.model.enums.enum_definition",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Enum_Definition is new Mappings.Mapping_Definition with record\n   Values         : aliased Value_List.List_Definition;\n   Values_Bean    : UBO.Object;\n   Package_Def    : Gen.Model.Packages.Package_Definition_Access;\n   Type_Name      : UString;\n   Nullable_Type  : UString;\n   Pkg_Name       : UString;\n   Sql_Type       : UString;\nend record;",
       }   ,
       {
       name: "Value_Definition",
       qualified_name: "Gen.Model.Enums.Value_Definition",
       signature: "gen.model.enums.value_definition",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Value_Definition is new Definition with record\n   Number : Natural := 0;\n   Enum   : Enum_Definition_Access;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Enum_Definition_Access",
       qualified_name: "Gen.Model.Enums.Enum_Definition_Access",
       signature: "gen.model.enums.enum_definition_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Enum_Definition_Access is access all Enum_Definition'Class;",
       }   ,
       {
       name: "Value_Definition_Access",
       qualified_name: "Gen.Model.Enums.Value_Definition_Access",
       signature: "gen.model.enums.value_definition_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Value_Definition_Access is access all Value_Definition'Class;",
       }   ,
   ]
,}
---
