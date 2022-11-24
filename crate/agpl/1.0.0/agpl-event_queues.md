---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Event_queues",
qualified_name: "Agpl.Event_queues",
signature: "agpl.event_queues",
enclosing: "agpl",
is_private: false,
documentation: "This type can be extended to match any required context",
documentation_snippet: "",
simple_types:    [
       {
       name: "Master_States",
       qualified_name: "Agpl.Event_queues.Master_States",
       signature: "agpl.event_queues.master_states",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Master_States is (Waiting_Worker, Waiting_Deadline, Executing, Idle, Ready);",
       }   ,
       {
       name: "Worker_States",
       qualified_name: "Agpl.Event_queues.Worker_States",
       signature: "agpl.event_queues.worker_states",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Worker_States is (Waiting, Executing);",
       }   ,
   ]
,record_types:    [
       {
       name: "Context_type",
       qualified_name: "Agpl.Event_queues.Context_type",
       signature: "agpl.event_queues.context_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Context_type is tagged null record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Action_Procedure",
       qualified_name: "Agpl.Event_queues.Action_Procedure",
       signature: "agpl.event_queues.action_procedure",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Action_Procedure is access procedure (Context : Context_Type'Class);",
       }   ,
   ]
,}
---
