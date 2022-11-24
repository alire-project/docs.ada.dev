---
crate: semantic_versioning
layout: gnatdoc
gnatdoc: {
name: "Semantic_Versioning.Basic",
qualified_name: "Semantic_Versioning.Basic",
signature: "semantic_versioning.basic",
enclosing: "semantic_versioning",
is_private: false,
documentation: "Collections of versions (usually a compatible subset). These basic sets\nonly allow \"and\" conditions.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Conditions",
       qualified_name: "Semantic_Versioning.Basic.Conditions",
       signature: "semantic_versioning.basic.conditions",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Conditions is\n  (At_Least, At_Most, Exactly, Except, Within_Major, Within_Minor);",
       }   ,
       {
       name: "Restriction",
       qualified_name: "Semantic_Versioning.Basic.Restriction",
       signature: "semantic_versioning.basic.restriction",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Restriction is private;",
       }   ,
   ]
,record_types:    [
       {
       name: "Result",
       qualified_name: "Semantic_Versioning.Basic.Result",
       signature: "semantic_versioning.basic.result",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Result (Valid  : Boolean;\n             Length : Natural) is\n   record\n      case Valid is\n         when True  => Set   : Version_Set;\n         when False => Error : String (1 .. Length);\n      end case;\n   end record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Version_Set",
       qualified_name: "Semantic_Versioning.Basic.Version_Set",
       signature: "semantic_versioning.basic.version_set",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Version_Set is tagged private;",
       }   ,
   ]
,constants:    [
       {
       name: "Any",
       qualified_name: "Semantic_Versioning.Basic.Any",
       signature: "semantic_versioning.basic.any",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Any : constant Version_Set;",
       }   ,
   ]
,}
---
