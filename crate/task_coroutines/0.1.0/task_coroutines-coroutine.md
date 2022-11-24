---
crate: task_coroutines
layout: gnatdoc
gnatdoc: {
name: "Task_Coroutines.Coroutine",
qualified_name: "Task_Coroutines.Coroutine",
signature: "task_coroutines.coroutine",
enclosing: "task_coroutines",
is_private: false,
documentation: "",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Inner_Control",
       qualified_name: "Task_Coroutines.Coroutine.Inner_Control",
       signature: "task_coroutines.coroutine.inner_control",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Inner_Control\nis tagged limited private;",
       }   ,
       {
       name: "Instance",
       qualified_name: "Task_Coroutines.Coroutine.Instance",
       signature: "task_coroutines.coroutine.instance",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Instance\nis tagged limited private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Coro_Proc",
       qualified_name: "Task_Coroutines.Coroutine.Coro_Proc",
       signature: "task_coroutines.coroutine.coro_proc",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Coro_Proc is access procedure (Ctrl : in out Inner_Control'Class);",
       }   ,
   ]
,}
---
