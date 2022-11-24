---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Asl.Semaphore.Counting",
qualified_name: "Asl.Semaphore.Counting",
signature: "asl.semaphore.counting",
enclosing: "asl.semaphore",
is_private: false,
documentation: "A standard counting semaphore.  The initial count is specified when the\nsemaphore is declared.  The Take operation will block is the count is\nzero, otherwise Take will decremenet the count.  Give will always\nincrement the count.",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Object",
       qualified_name: "Asl.Semaphore.Counting.Object",
       signature: "asl.semaphore.counting.object",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Object (Initial_Count : Natural) is\n  new Asl.Semaphore.Object with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Object_Ptr",
       qualified_name: "Asl.Semaphore.Counting.Object_Ptr",
       signature: "asl.semaphore.counting.object_ptr",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Object_Ptr is access all Object;",
       }   ,
   ]
,}
---
