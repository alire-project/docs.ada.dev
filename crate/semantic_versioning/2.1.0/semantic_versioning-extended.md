---
crate: semantic_versioning
layout: gnatdoc
gnatdoc: {
name: "Semantic_Versioning.Extended",
qualified_name: "Semantic_Versioning.Extended",
signature: "semantic_versioning.extended",
enclosing: "semantic_versioning",
is_private: false,
documentation: "",
documentation_snippet: "",
record_types:    [
       {
       name: "Result",
       qualified_name: "Semantic_Versioning.Extended.Result",
       signature: "semantic_versioning.extended.result",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Result (Valid  : Boolean;\n             Length : Natural) is record\n   case Valid is\n      when True =>\n         Set : Version_Set;\n      when False =>\n         Error : String (1 .. Length);\n   end case;\nend record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Version_Set",
       qualified_name: "Semantic_Versioning.Extended.Version_Set",
       signature: "semantic_versioning.extended.version_set",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Version_Set is tagged private;",
       }   ,
   ]
,}
---
