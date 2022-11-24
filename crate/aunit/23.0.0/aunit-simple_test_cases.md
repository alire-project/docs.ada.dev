---
crate: aunit
layout: gnatdoc
gnatdoc: {
name: "AUnit.Simple_Test_Cases",
qualified_name: "AUnit.Simple_Test_Cases",
signature: "aunit.simple_test_cases",
enclosing: "aunit",
is_private: false,
documentation: "This type is used to implement a simple test case: define a derived type\nthat overrides the Run_Test and Name methods.\n\nYou don't usually need to use that type, but Test_Fixture/Test_Caller\nor Test_Case instead.",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Test_Case",
       qualified_name: "AUnit.Simple_Test_Cases.Test_Case",
       signature: "aunit.simple_test_cases.test_case",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Test_Case is abstract new AUnit.Assertions.Test with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Test_Case_Access",
       qualified_name: "AUnit.Simple_Test_Cases.Test_Case_Access",
       signature: "aunit.simple_test_cases.test_case_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Test_Case_Access is access all Test_Case'Class;",
       }   ,
   ]
,}
---
