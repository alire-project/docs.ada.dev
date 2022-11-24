---
crate: aunit
layout: gnatdoc
gnatdoc: {
name: "AUnit.Test_Caller",
qualified_name: "AUnit.Test_Caller",
signature: "aunit.test_caller",
enclosing: "aunit",
is_private: false,
documentation: "<description>\nA Test caller provides access to a test case type based on a test fixture.\nTest callers are useful when you want to run individual test or add it to\na suite.\nTest callers invoke only one Test (i.e. test method) on one Fixture of a\nAUnit.Test_Fixtures.Test_Fixture.\n\nHere is an example:\n\n<code>\npackage Math_Test is\n   Type Test is new AUnit.Test_Fixtures.Test_Fixture with record\n      M_Value1 : Integer;\n      M_Value2 : Integer;\n   end record;\n\n   procedure Set_Up (T : in out Test);\n\n   procedure Test_Addition (T : in out Test);\n   procedure Test_Subtraction (T : in out Test);\n\nend Math_Test;\n\nfunction Suite return AUnit.Test_Suites.Test_Suite_Access is\n   package Caller is new AUnit.Test_Caller (Math_Test.Test);\n   The_Suite       : AUnit.Test_Suites.Test_Suite_Access :=\n                       new AUnit.Test_Suites.Test_Suite;\nbegin\n   The_Suite.Add_Test\n    (Caller.Create (\"Test Addition on integers\",\n                    Math_Test.Test_Addition'Access));\n   The_Suite.Add_Test\n    (Caller.Create (\"Test Subtraction on integers\",\n                    Math_Test.Test_Subtraction'Access));\n   return The_Suite;\nend Suite;\n</code>\n</description>\n\n@formal Test_Fixture",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Test_Case",
       qualified_name: "AUnit.Test_Caller.Test_Case",
       signature: "aunit.test_caller.test_case",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Test_Case is new AUnit.Simple_Test_Cases.Test_Case with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Test_Case_Access",
       qualified_name: "AUnit.Test_Caller.Test_Case_Access",
       signature: "aunit.test_caller.test_case_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Test_Case_Access is access all Test_Case'Class;",
       }   ,
       {
       name: "Test_Method",
       qualified_name: "AUnit.Test_Caller.Test_Method",
       signature: "aunit.test_caller.test_method",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Test_Method is access procedure (Test : in out Test_Fixture);",
       }   ,
   ]
,}
---
