---
crate: avrada_rts
layout: gnatdoc
gnatdoc: {
name: "System.Parameters",
qualified_name: "System.Parameters",
signature: "system.parameters",
enclosing: "system",
is_private: false,
documentation: "type Size_Type is new Integer;",
documentation_snippet: "",
simple_types:    [
       {
       name: "Size_Type",
       qualified_name: "System.Parameters.Size_Type",
       signature: "system.parameters.size_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Size_Type is range\n  -(2 ** (Integer'(Standard'Address_Size) - 1)) ..\n  +(2 ** (Integer'(Standard'Address_Size) - 1)) - 1;",
       }   ,
   ]
,constants:    [
       {
       name: "Runtime_Default_Sec_Stack_Size",
       qualified_name: "System.Parameters.Runtime_Default_Sec_Stack_Size",
       signature: "system.parameters.runtime_default_sec_stack_size",
       enclosing: "",
       is_private: false,
       documentation: "The run-time chosen default size for secondary stacks that may be\noverridden by the user with the use of binder -D switch.\nThe GCC-9 binder generates references.",
       documentation_snippet: "Runtime_Default_Sec_Stack_Size : constant Size_Type := 256;",
       }   ,
       {
       name: "Unspecified_Size",
       qualified_name: "System.Parameters.Unspecified_Size",
       signature: "system.parameters.unspecified_size",
       enclosing: "",
       is_private: false,
       documentation: "Type used to provide task storage size to runtime",
       documentation_snippet: "Unspecified_Size : constant Size_Type := Size_Type'First;",
       }   ,
   ]
,}
---
