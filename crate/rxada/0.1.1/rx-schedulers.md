---
crate: rxada
layout: gnatdoc
gnatdoc: {
name: "Rx.Schedulers",
qualified_name: "Rx.Schedulers",
signature: "rx.schedulers",
enclosing: "rx",
is_private: false,
documentation: "Note: there's is never, in the current implementation, reclaiming of created threads.\nSo you might try to be conservative (i.e. use Idle_Thread instead of New_Thread).\nNew_Thread may be justified in setup stages where you are reserving threads for tasks.",
documentation_snippet: "",
interface_types:    [
       {
       name: "Pool",
       qualified_name: "Rx.Schedulers.Pool",
       signature: "rx.schedulers.pool",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Pool is limited interface;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Scheduler",
       qualified_name: "Rx.Schedulers.Scheduler",
       signature: "rx.schedulers.scheduler",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Scheduler is tagged private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Pool_Access",
       qualified_name: "Rx.Schedulers.Pool_Access",
       signature: "rx.schedulers.pool_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Pool_Access is access all Pool'Class;",
       }   ,
       {
       name: "Thread",
       qualified_name: "Rx.Schedulers.Thread",
       signature: "rx.schedulers.thread",
       enclosing: "",
       is_private: false,
       documentation: "An actual scheduler thread",
       documentation_snippet: "type Thread is access all Rx.Dispatchers.Dispatcher'Class;",
       }   ,
       {
       name: "Thread_Allocator",
       qualified_name: "Rx.Schedulers.Thread_Allocator",
       signature: "rx.schedulers.thread_allocator",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Thread_Allocator is access function return Thread;",
       }   ,
   ]
,}
---
