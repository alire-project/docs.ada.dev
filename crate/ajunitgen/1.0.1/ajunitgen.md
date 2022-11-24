---
crate: ajunitgen
layout: gnatdoc
gnatdoc: {
name: "AJUnitGen",
qualified_name: "AJUnitGen",
signature: "ajunitgen",
enclosing: "",
is_private: false,
documentation: "Simple package to generate JUnit-compatible XML reports ",
documentation_snippet: "",
simple_types:    [
       {
       name: "Outcomes",
       qualified_name: "AJUnitGen.Outcomes",
       signature: "ajunitgen.outcomes",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Outcomes is (Pass, Error, Fail, Skip);",
       }   ,
       {
       name: "Test_Case",
       qualified_name: "AJUnitGen.Test_Case",
       signature: "ajunitgen.test_case",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Test_Case (<>) is private;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Collection",
       qualified_name: "AJUnitGen.Collection",
       signature: "ajunitgen.collection",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Collection is tagged private;",
       }   ,
       {
       name: "Test_Suite",
       qualified_name: "AJUnitGen.Test_Suite",
       signature: "ajunitgen.test_suite",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Test_Suite (<>) is tagged private;",
       }   ,
   ]
,}
---
