---
crate: dynamo
layout: gnatdoc
gnatdoc: {
name: "Gen.Model.Projects",
qualified_name: "Gen.Model.Projects",
signature: "gen.model.projects",
enclosing: "gen.model",
is_private: false,
documentation: "---------------------------------------------------------------------\n  gen-model-projects -- Projects meta data\n  Copyright (C) 2011, 2012, 2013, 2014, 2017, 2018, 2021 Stephane Carrez\n  Written by Stephane Carrez (Stephane.Carrez@gmail.com)\n\n  Licensed under the Apache License, Version 2.0 (the \"License\");\n  you may not use this file except in compliance with the License.\n  You may obtain a copy of the License at\n\n      http://www.apache.org/licenses/LICENSE-2.0\n\n  Unless required by applicable law or agreed to in writing, software\n  distributed under the License is distributed on an \"AS IS\" BASIS,\n  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n  See the License for the specific language governing permissions and\n  limitations under the License.\n---------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Dependency_Type",
       qualified_name: "Gen.Model.Projects.Dependency_Type",
       signature: "gen.model.projects.dependency_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Dependency_Type is (NONE, DIRECT, INDIRECT, BOTH);",
       }   ,
   ]
,record_types:    [
       {
       name: "Project_Reference",
       qualified_name: "Gen.Model.Projects.Project_Reference",
       signature: "gen.model.projects.project_reference",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Project_Reference is record\n   Project : Project_Definition_Access := null;\n   Name    : UString;\n   Kind    : Dependency_Type := NONE;\nend record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Project_Definition",
       qualified_name: "Gen.Model.Projects.Project_Definition",
       signature: "gen.model.projects.project_definition",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Project_Definition is new Definition with record\n   Path    : UString;\n   Props   : Util.Properties.Manager;\n   Modules : Project_Vectors.Vector;\n   Root          : Project_Definition_Access := null;\n   Dependencies  : Project_Vectors.Vector;\n   Project_Files : Gen.Utils.GNAT.Project_Info_Vectors.Vector;\n   Dynamo_Files  : Gen.Utils.String_List.Vector;\n   Recursive_Scan : Boolean := False;\n   Recursing      : Boolean := False;\n   Depend_Scan    : Boolean := False;\n   Is_Plugin      : Boolean := False;\n   Use_Mysql      : Boolean := True;\n   Use_Sqlite     : Boolean := True;\n   Use_Postgresql : Boolean := True;\nend record;",
       }   ,
       {
       name: "Root_Project_Definition",
       qualified_name: "Gen.Model.Projects.Root_Project_Definition",
       signature: "gen.model.projects.root_project_definition",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Root_Project_Definition is new Project_Definition with record\n   Projects    : Project_Vectors.Vector;\n   Install_Dir : UString;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Project_Definition_Access",
       qualified_name: "Gen.Model.Projects.Project_Definition_Access",
       signature: "gen.model.projects.project_definition_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Project_Definition_Access is access all Project_Definition'Class;",
       }   ,
   ]
,}
---
