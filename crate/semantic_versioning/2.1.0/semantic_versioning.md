---
crate: semantic_versioning
layout: gnatdoc
gnatdoc: {
name: "Semantic_Versioning",
qualified_name: "Semantic_Versioning",
signature: "semantic_versioning",
enclosing: "",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Point",
       qualified_name: "Semantic_Versioning.Point",
       signature: "semantic_versioning.point",
       enclosing: "",
       is_private: false,
       documentation: "Enough to store a YYYYMMDD as a point",
       documentation_snippet: "type Point is range 0 .. 99_999_999;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Version",
       qualified_name: "Semantic_Versioning.Version",
       signature: "semantic_versioning.version",
       enclosing: "",
       is_private: false,
       documentation: "A version is a major, minor and patch number\nOptionally it may include pre-release name and build metadata, e.g.:\n1.2.0-alpha+c3423fab",
       documentation_snippet: "type Version is tagged private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Version_String",
       qualified_name: "Semantic_Versioning.Version_String",
       signature: "semantic_versioning.version_string",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Version_String is String\n  with Dynamic_Predicate => (for all S of Version_String => S /= ' ');",
       }   ,
   ]
,}
---
