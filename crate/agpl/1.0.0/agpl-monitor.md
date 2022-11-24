---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Monitor",
qualified_name: "Agpl.Monitor",
signature: "agpl.monitor",
enclosing: "agpl",
is_private: false,
documentation: "Mutex with counter. A task may safely request it multiple times,\nas long as it releases it the same times",
documentation_snippet: "",
interface_types:    [
       {
       name: "Semaphore",
       qualified_name: "Agpl.Monitor.Semaphore",
       signature: "agpl.monitor.semaphore",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Semaphore is synchronized interface;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Object",
       qualified_name: "Agpl.Monitor.Object",
       signature: "agpl.monitor.object",
       enclosing: "",
       is_private: false,
       documentation: "Note that for generality purposes, if S in null no error will happen\n\n@field S",
       documentation_snippet: "type Object (S : access Semaphore'Class) is new\n  Finalization.Limited_Controlled with null record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Semaphore_Access",
       qualified_name: "Agpl.Monitor.Semaphore_Access",
       signature: "agpl.monitor.semaphore_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Semaphore_Access is access all Semaphore'Class;",
       }   ,
   ]
,}
---
