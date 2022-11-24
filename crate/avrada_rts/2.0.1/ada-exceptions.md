---
crate: avrada_rts
layout: gnatdoc
gnatdoc: {
name: "Ada.Exceptions",
qualified_name: "Ada.Exceptions",
signature: "ada.exceptions",
enclosing: "ada",
is_private: false,
documentation: "This version of Ada.Exceptions is a simplified version for use in\nAVR-Ada.  It supports simplified exception handling without\nexception propagation, i.e. restriction No_Exception_Propagation\nis set.\n\nYou also have to define __gnat_last_chance_handler somewhere in\nyour code as the typical binder generated last-chance-handler is\nstripped in AVR-Ada.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Exception_Id",
       qualified_name: "Ada.Exceptions.Exception_Id",
       signature: "ada.exceptions.exception_id",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Exception_Id is private;",
       }   ,
   ]
,constants:    [
       {
       name: "Null_Id",
       qualified_name: "Ada.Exceptions.Null_Id",
       signature: "ada.exceptions.null_id",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Null_Id : constant Exception_Id;",
       }   ,
   ]
,}
---
