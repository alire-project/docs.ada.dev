---
crate: dynamo
layout: gnatdoc
gnatdoc: {
name: "Gen.Model.Stypes",
qualified_name: "Gen.Model.Stypes",
signature: "gen.model.stypes",
enclosing: "gen.model",
is_private: false,
documentation: "------------------------------\nSimple type definition\n------------------------------",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Stype_Definition",
       qualified_name: "Gen.Model.Stypes.Stype_Definition",
       signature: "gen.model.stypes.stype_definition",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Stype_Definition is new Mappings.Mapping_Definition with record\n   Package_Def    : Gen.Model.Packages.Package_Definition_Access;\n   Parent_Type    : UString;\n   Type_Name      : UString;\n   Nullable_Type  : UString;\n   Pkg_Name       : UString;\n   Sql_Type       : UString;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Stype_Definition_Access",
       qualified_name: "Gen.Model.Stypes.Stype_Definition_Access",
       signature: "gen.model.stypes.stype_definition_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Stype_Definition_Access is access all Stype_Definition'Class;",
       }   ,
   ]
,}
---
