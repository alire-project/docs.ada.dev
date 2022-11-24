---
crate: serverfaces
layout: gnatdoc
gnatdoc: {
name: "ASF.Validators.Texts",
qualified_name: "ASF.Validators.Texts",
signature: "asf.validators.texts",
enclosing: "asf.validators",
is_private: false,
documentation: "",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Length_Validator",
       qualified_name: "ASF.Validators.Texts.Length_Validator",
       signature: "asf.validators.texts.length_validator",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Length_Validator is new Validator with private;",
       }   ,
       {
       name: "Regex_Validator",
       qualified_name: "ASF.Validators.Texts.Regex_Validator",
       signature: "asf.validators.texts.regex_validator",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Regex_Validator (Size : GNAT.Regpat.Program_Size) is new Validator with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Length_Validator_Access",
       qualified_name: "ASF.Validators.Texts.Length_Validator_Access",
       signature: "asf.validators.texts.length_validator_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Length_Validator_Access is access all Length_Validator'Class;",
       }   ,
       {
       name: "Regex_Validator_Access",
       qualified_name: "ASF.Validators.Texts.Regex_Validator_Access",
       signature: "asf.validators.texts.regex_validator_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Regex_Validator_Access is access all Regex_Validator'Class;",
       }   ,
   ]
,constants:    [
       {
       name: "MAXIMUM_MESSAGE_ID",
       qualified_name: "ASF.Validators.Texts.MAXIMUM_MESSAGE_ID",
       signature: "asf.validators.texts.maximum_message_id",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "MAXIMUM_MESSAGE_ID : constant String := \"asf.validators.length.maximum\";",
       }   ,
       {
       name: "MINIMUM_MESSAGE_ID",
       qualified_name: "ASF.Validators.Texts.MINIMUM_MESSAGE_ID",
       signature: "asf.validators.texts.minimum_message_id",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "MINIMUM_MESSAGE_ID : constant String := \"asf.validators.length.minimum\";",
       }   ,
       {
       name: "REGEX_MESSAGE_ID",
       qualified_name: "ASF.Validators.Texts.REGEX_MESSAGE_ID",
       signature: "asf.validators.texts.regex_message_id",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "REGEX_MESSAGE_ID   : constant String := \"asf.validators.regex\";",
       }   ,
   ]
,}
---
