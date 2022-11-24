---
crate: avrada_rts
layout: gnatdoc
gnatdoc: {
name: "System.Secondary_Stack",
qualified_name: "System.Secondary_Stack",
signature: "system.secondary_stack",
enclosing: "system",
is_private: false,
documentation: "Version for use in HI-E mode",
documentation_snippet: "",
simple_types:    [
       {
       name: "Mark_Id",
       qualified_name: "System.Secondary_Stack.Mark_Id",
       signature: "system.secondary_stack.mark_id",
       enclosing: "",
       is_private: false,
       documentation: "Type used to mark the stack for mark/release processing",
       documentation_snippet: "type Mark_Id is private;",
       }   ,
       {
       name: "SS_Stack",
       qualified_name: "System.Secondary_Stack.SS_Stack",
       signature: "system.secondary_stack.ss_stack",
       enclosing: "",
       is_private: false,
       documentation: "Data structure for secondary stacks",
       documentation_snippet: "type SS_Stack (Size : SP.Size_Type) is private;",
       }   ,
   ]
,access_types:    [
       {
       name: "SS_Stack_Ptr",
       qualified_name: "System.Secondary_Stack.SS_Stack_Ptr",
       signature: "system.secondary_stack.ss_stack_ptr",
       enclosing: "",
       is_private: false,
       documentation: "Pointer to secondary stack objects",
       documentation_snippet: "type SS_Stack_Ptr is access all SS_Stack;",
       }   ,
   ]
,}
---
