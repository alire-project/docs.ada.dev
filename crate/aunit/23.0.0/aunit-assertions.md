---
crate: aunit
layout: gnatdoc
gnatdoc: {
name: "AUnit.Assertions",
qualified_name: "AUnit.Assertions",
signature: "aunit.assertions",
enclosing: "aunit",
is_private: false,
documentation: "<description>\nThis package provides the Assert methods used by the user to verify test\nresults.\nThose methods are used to report errors within AUnit tests when a result\ndoes not match an expected value.\n</description>",
documentation_snippet: "",
simple_types:    [
       {
       name: "Failure_Iter",
       qualified_name: "AUnit.Assertions.Failure_Iter",
       signature: "aunit.assertions.failure_iter",
       enclosing: "",
       is_private: false,
       documentation: "Iterator used to retrieve failures.",
       documentation_snippet: "type Failure_Iter is private;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Test",
       qualified_name: "AUnit.Assertions.Test",
       signature: "aunit.assertions.test",
       enclosing: "",
       is_private: false,
       documentation: "Test is used as root type for all Test cases, but also for Test fixtures\nThis allows easy access to all Assert procedures from user tests.",
       documentation_snippet: "type Test is abstract new AUnit.Tests.Test with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Test_Access",
       qualified_name: "AUnit.Assertions.Test_Access",
       signature: "aunit.assertions.test_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Test_Access is access all Test'Class;",
       }   ,
       {
       name: "Throwing_Exception_Proc",
       qualified_name: "AUnit.Assertions.Throwing_Exception_Proc",
       signature: "aunit.assertions.throwing_exception_proc",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Throwing_Exception_Proc is access procedure;",
       }   ,
   ]
,}
---
