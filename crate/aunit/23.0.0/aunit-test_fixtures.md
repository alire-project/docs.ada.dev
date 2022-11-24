---
crate: aunit
layout: gnatdoc
gnatdoc: {
name: "AUnit.Test_Fixtures",
qualified_name: "AUnit.Test_Fixtures",
signature: "aunit.test_fixtures",
enclosing: "aunit",
is_private: false,
documentation: "<description>\nA Test_Fixture is used to provide a common environment for a set of test\ncases.\n\nTo define a test case from a test fixture, see AUnit.Test_Caller.\n\nEach test runs in its own fixture so there can be no side effects among\ntest runs.\n\nHere is an example:\n\n<code>\npackage Math_Test is\n   Type Test is new AUnit.Test_Fixtures.Test_Fixture with record\n      M_Value1 : Integer;\n      M_Value2 : Integer;\n   end record;\n\n   procedure Set_Up (T : in out Test);\n\n   procedure Test_Addition (T : in out Test);\n\nend Math_Test;\n\npackage body Math_Test is\n\n   procedure Set_Up (T : in out Test) is\n   begin\n      T.M_Value1 := 2;\n      T.M_Value2 := 3;\n   end Set_Up;\n\n   procedure Test_Addition (T : in out Test) is\n   begin\n      Assert (T.M_Value1 + T.M_Value2 = 5,\n              \"Incorrect addition for integers\");\n   end Test_Addition;\n\nend Math_Test;\n</code>\n</description>",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Test_Fixture",
       qualified_name: "AUnit.Test_Fixtures.Test_Fixture",
       signature: "aunit.test_fixtures.test_fixture",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Test_Fixture is new AUnit.Assertions.Test with private;",
       }   ,
   ]
,}
---
