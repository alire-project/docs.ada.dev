---
crate: trendy_test
layout: gnatdoc
gnatdoc: {
name: "Trendy_Test",
qualified_name: "Trendy_Test",
signature: "trendy_test",
enclosing: "",
is_private: false,
documentation: "Base class for all operations to be done on a test procedure.\n\nAn operation might not even go further in a test procedure than the\nregistration call, such as for operations to gather all of the tests.\nOperations could run the whole procedure, or data collect.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Test_Result",
       qualified_name: "Trendy_Test.Test_Result",
       signature: "trendy_test.test_result",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Test_Result is (Passed, Failed, Skipped);",
       }   ,
   ]
,array_types:    [
       {
       name: "Test_Group",
       qualified_name: "Trendy_Test.Test_Group",
       signature: "trendy_test.test_group",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Test_Group is array (Positive range <>) of Test_Procedure;",
       }   ,
   ]
,record_types:    [
       {
       name: "Test_Report",
       qualified_name: "Trendy_Test.Test_Report",
       signature: "trendy_test.test_report",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Test_Report is record\n    Name                 : Ada.Strings.Unbounded.Unbounded_String;\n    Status               : Test_Result;\n    Start_Time, End_Time : Ada.Calendar.Time;\n    Failure              : Ada.Strings.Unbounded.Unbounded_String := Ada.Strings.Unbounded.Null_Unbounded_String;\nend record;",
       }   ,
   ]
,interface_types:    [
       {
       name: "Operation",
       qualified_name: "Trendy_Test.Operation",
       signature: "trendy_test.operation",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Operation is limited interface;",
       }   ,
   ]
,access_types:    [
       {
       name: "Test_Procedure",
       qualified_name: "Trendy_Test.Test_Procedure",
       signature: "trendy_test.test_procedure",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Test_Procedure is access procedure (Op : in out Operation'Class);",
       }   ,
   ]
,}
---
