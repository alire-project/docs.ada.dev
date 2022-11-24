---
crate: dynamo
layout: gnatdoc
gnatdoc: {
name: "Gen.Generator",
qualified_name: "Gen.Generator",
signature: "gen.generator",
enclosing: "gen",
is_private: false,
documentation: "---------------------------------------------------------------------\n  gen-generator -- Code Generator\n  Copyright (C) 2009, 2010, 2011, 2012, 2013, 2015, 2018, 2022 Stephane Carrez\n  Written by Stephane Carrez (Stephane.Carrez@gmail.com)\n\n  Licensed under the Apache License, Version 2.0 (the \"License\");\n  you may not use this file except in compliance with the License.\n  You may obtain a copy of the License at\n\n      http://www.apache.org/licenses/LICENSE-2.0\n\n  Unless required by applicable law or agreed to in writing, software\n  distributed under the License is distributed on an \"AS IS\" BASIS,\n  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n  See the License for the specific language governing permissions and\n  limitations under the License.\n---------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Package_Type",
       qualified_name: "Gen.Generator.Package_Type",
       signature: "gen.generator.package_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Package_Type is (PACKAGE_MODEL, PACKAGE_FORMS);",
       }   ,
   ]
,record_types:    [
       {
       name: "Mapping_File",
       qualified_name: "Gen.Generator.Mapping_File",
       signature: "gen.generator.mapping_file",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Mapping_File is record\n   Path   : UString;\n   Output : Ada.Text_IO.File_Type;\nend record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Handler",
       qualified_name: "Gen.Generator.Handler",
       signature: "gen.generator.handler",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Handler is new ASF.Applications.Main.Application and Gen.Artifacts.Generator with private;",
       }   ,
   ]
,constants:    [
       {
       name: "G_URI",
       qualified_name: "Gen.Generator.G_URI",
       signature: "gen.generator.g_uri",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "G_URI : constant String := \"http://code.google.com/p/ada-ado/generator\";",
       }   ,
   ]
,}
---
