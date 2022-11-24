---
crate: rxada
layout: gnatdoc
gnatdoc: {
name: "Rx.Tools.Semaphores",
qualified_name: "Rx.Tools.Semaphores",
signature: "rx.tools.semaphores",
enclosing: "rx.tools",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Shared",
       qualified_name: "Rx.Tools.Semaphores.Shared",
       signature: "rx.tools.semaphores.shared",
       enclosing: "",
       is_private: false,
       documentation: "A ref-counted semaphore which is initially invalid",
       documentation_snippet: "type Shared is private;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Critical_Section",
       qualified_name: "Rx.Tools.Semaphores.Critical_Section",
       signature: "rx.tools.semaphores.critical_section",
       enclosing: "",
       is_private: false,
       documentation: "Declare an instance of this type in the scope to be made exclusive\nIt automatically seizes/releases the semaphore on entering/exiting the scope of declaration\nThe mutex is copied and could be disposed of by the caller inside the critical section",
       documentation_snippet: "type Critical_Section (Mutex : access Shared) is tagged limited private;",
       }   ,
   ]
,}
---
