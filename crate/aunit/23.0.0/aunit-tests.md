---
crate: aunit
layout: gnatdoc
gnatdoc: {
name: "AUnit.Tests",
qualified_name: "AUnit.Tests",
signature: "aunit.tests",
enclosing: "aunit",
is_private: false,
documentation: "Base Test Case or Test Suite\n\nThis base type allows composition of both test cases and sub-suites into a\ntest suite (Composite pattern)",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Test",
       qualified_name: "AUnit.Tests.Test",
       signature: "aunit.tests.test",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Test is abstract tagged limited private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Test_Access",
       qualified_name: "AUnit.Tests.Test_Access",
       signature: "aunit.tests.test_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Test_Access is access all Test'Class;",
       }   ,
   ]
,}
---
