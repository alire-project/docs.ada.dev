---
crate: clic
layout: gnatdoc
gnatdoc: {
name: "CLIC.User_Input",
qualified_name: "CLIC.User_Input",
signature: "clic.user_input",
enclosing: "clic",
is_private: false,
documentation: "-----------------\n Interactivity --\n-----------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Answer_Kind",
       qualified_name: "CLIC.User_Input.Answer_Kind",
       signature: "clic.user_input.answer_kind",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Answer_Kind is (Yes, No, Always);",
       }   ,
   ]
,array_types:    [
       {
       name: "Answer_Set",
       qualified_name: "CLIC.User_Input.Answer_Set",
       signature: "clic.user_input.answer_set",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Answer_Set is array (Answer_Kind) of Boolean;",
       }   ,
   ]
,record_types:    [
       {
       name: "Answer_With_Input",
       qualified_name: "CLIC.User_Input.Answer_With_Input",
       signature: "clic.user_input.answer_with_input",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Answer_With_Input (Length : Natural) is record\n   Input  : String (1 .. Length);\n   Answer : Answer_Kind;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "String_Validation_Access",
       qualified_name: "CLIC.User_Input.String_Validation_Access",
       signature: "clic.user_input.string_validation_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type String_Validation_Access is\n  access function (Str : String) return Boolean;",
       }   ,
   ]
,variables:    [
       {
       name: "Not_Interactive",
       qualified_name: "CLIC.User_Input.Not_Interactive",
       signature: "clic.user_input.not_interactive",
       enclosing: "",
       is_private: false,
       documentation: "When not Interactive, instead of asking the user something, use default.",
       documentation_snippet: "Not_Interactive : aliased Boolean := False;",
       }   ,
   ]
,}
---
