---
crate: aunit
layout: gnatdoc
gnatdoc: {
name: "AUnit",
qualified_name: "AUnit",
signature: "aunit",
enclosing: "",
is_private: false,
documentation: "Test Suite Framework",
documentation_snippet: "",
simple_types:    [
       {
       name: "Status",
       qualified_name: "AUnit.Status",
       signature: "aunit.status",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Status is (Success, Failure);",
       }   ,
   ]
,access_types:    [
       {
       name: "Message_String",
       qualified_name: "AUnit.Message_String",
       signature: "aunit.message_string",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Message_String is access String;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Test_String",
       qualified_name: "AUnit.Test_String",
       signature: "aunit.test_string",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Test_String is Message_String;",
       }   ,
   ]
,}
---
