---
crate: serverfaces
layout: gnatdoc
gnatdoc: {
name: "ASF.Contexts.Exceptions",
qualified_name: "ASF.Contexts.Exceptions",
signature: "asf.contexts.exceptions",
enclosing: "asf.contexts",
is_private: false,
documentation: "Message used when an exception without a message is raised.",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Exception_Handler",
       qualified_name: "ASF.Contexts.Exceptions.Exception_Handler",
       signature: "asf.contexts.exceptions.exception_handler",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Exception_Handler is new Ada.Finalization.Limited_Controlled with private;",
       }   ,
       {
       name: "Exception_Queue",
       qualified_name: "ASF.Contexts.Exceptions.Exception_Queue",
       signature: "asf.contexts.exceptions.exception_queue",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Exception_Queue is new Ada.Finalization.Limited_Controlled with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Exception_Handler_Access",
       qualified_name: "ASF.Contexts.Exceptions.Exception_Handler_Access",
       signature: "asf.contexts.exceptions.exception_handler_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Exception_Handler_Access is access all Exception_Handler'Class;",
       }   ,
   ]
,constants:    [
       {
       name: "EXCEPTION_MESSAGE_BASIC_ID",
       qualified_name: "ASF.Contexts.Exceptions.EXCEPTION_MESSAGE_BASIC_ID",
       signature: "asf.contexts.exceptions.exception_message_basic_id",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "EXCEPTION_MESSAGE_BASIC_ID    : constant String := \"asf.exceptions.unexpected.basic\";",
       }   ,
       {
       name: "EXCEPTION_MESSAGE_EXTENDED_ID",
       qualified_name: "ASF.Contexts.Exceptions.EXCEPTION_MESSAGE_EXTENDED_ID",
       signature: "asf.contexts.exceptions.exception_message_extended_id",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "EXCEPTION_MESSAGE_EXTENDED_ID : constant String := \"asf.exceptions.unexpected.extended\";",
       }   ,
   ]
,}
---
