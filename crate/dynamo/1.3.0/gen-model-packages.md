---
crate: dynamo
layout: gnatdoc
gnatdoc: {
name: "Gen.Model.Packages",
qualified_name: "Gen.Model.Packages",
signature: "gen.model.packages",
enclosing: "gen.model",
is_private: false,
documentation: "------------------------------\nModel Definition\n------------------------------\nThe <b>Model_Definition</b> contains the complete model from one or\nseveral files.  It maintains a list of Ada packages that must be generated.",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Model_Definition",
       qualified_name: "Gen.Model.Packages.Model_Definition",
       signature: "gen.model.packages.model_definition",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Model_Definition is new Definition with private;",
       }   ,
       {
       name: "Package_Definition",
       qualified_name: "Gen.Model.Packages.Package_Definition",
       signature: "gen.model.packages.package_definition",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Package_Definition is new Definition with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Model_Definition_Access",
       qualified_name: "Gen.Model.Packages.Model_Definition_Access",
       signature: "gen.model.packages.model_definition_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Model_Definition_Access is access all Model_Definition'Class;",
       }   ,
       {
       name: "Package_Definition_Access",
       qualified_name: "Gen.Model.Packages.Package_Definition_Access",
       signature: "gen.model.packages.package_definition_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Package_Definition_Access is access all Package_Definition'Class;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Package_Cursor",
       qualified_name: "Gen.Model.Packages.Package_Cursor",
       signature: "gen.model.packages.package_cursor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Package_Cursor is Package_Map.Cursor;",
       }   ,
   ]
,}
---
