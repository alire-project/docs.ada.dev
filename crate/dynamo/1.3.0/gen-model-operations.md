---
crate: dynamo
layout: gnatdoc
gnatdoc: {
name: "Gen.Model.Operations",
qualified_name: "Gen.Model.Operations",
signature: "gen.model.operations",
enclosing: "gen.model",
is_private: false,
documentation: "---------------------------------------------------------------------\n  gen-model-operations -- Operation declarations\n  Copyright (C) 2012, 2016, 2017, 2021 Stephane Carrez\n  Written by Stephane Carrez (Stephane.Carrez@gmail.com)\n\n  Licensed under the Apache License, Version 2.0 (the \"License\");\n  you may not use this file except in compliance with the License.\n  You may obtain a copy of the License at\n\n      http://www.apache.org/licenses/LICENSE-2.0\n\n  Unless required by applicable law or agreed to in writing, software\n  distributed under the License is distributed on an \"AS IS\" BASIS,\n  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n  See the License for the specific language governing permissions and\n  limitations under the License.\n---------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Operation_Type",
       qualified_name: "Gen.Model.Operations.Operation_Type",
       signature: "gen.model.operations.operation_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Operation_Type is (UNKNOWN, ASF_ACTION, ASF_UPLOAD, AWA_EVENT);",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Operation_Definition",
       qualified_name: "Gen.Model.Operations.Operation_Definition",
       signature: "gen.model.operations.operation_definition",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Operation_Definition is new Definition with private;",
       }   ,
       {
       name: "Parameter_Definition",
       qualified_name: "Gen.Model.Operations.Parameter_Definition",
       signature: "gen.model.operations.parameter_definition",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Parameter_Definition is new Definition with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Operation_Definition_Access",
       qualified_name: "Gen.Model.Operations.Operation_Definition_Access",
       signature: "gen.model.operations.operation_definition_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Operation_Definition_Access is access all Operation_Definition'Class;",
       }   ,
       {
       name: "Parameter_Definition_Access",
       qualified_name: "Gen.Model.Operations.Parameter_Definition_Access",
       signature: "gen.model.operations.parameter_definition_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Parameter_Definition_Access is access all Parameter_Definition'Class;",
       }   ,
   ]
,}
---
