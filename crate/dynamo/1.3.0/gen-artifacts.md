---
crate: dynamo
layout: gnatdoc
gnatdoc: {
name: "Gen.Artifacts",
qualified_name: "Gen.Artifacts",
signature: "gen.artifacts",
enclosing: "gen",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Iteration_Mode",
       qualified_name: "Gen.Artifacts.Iteration_Mode",
       signature: "gen.artifacts.iteration_mode",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Iteration_Mode is (ITERATION_PACKAGE, ITERATION_TABLE);",
       }   ,
   ]
,interface_types:    [
       {
       name: "Generator",
       qualified_name: "Gen.Artifacts.Generator",
       signature: "gen.artifacts.generator",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Generator is limited interface and Util.Log.Logging;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Artifact",
       qualified_name: "Gen.Artifacts.Artifact",
       signature: "gen.artifacts.artifact",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Artifact is abstract new Ada.Finalization.Limited_Controlled with private;",
       }   ,
   ]
,}
---
