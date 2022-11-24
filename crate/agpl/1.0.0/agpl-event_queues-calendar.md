---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Event_queues.Calendar",
qualified_name: "Agpl.Event_queues.Calendar",
signature: "agpl.event_queues.calendar",
enclosing: "agpl.event_queues",
is_private: false,
documentation: "Handle for an event. Can be used to cancel it:",
documentation_snippet: "",
simple_types:    [
       {
       name: "Event_type",
       qualified_name: "Agpl.Event_queues.Calendar.Event_type",
       signature: "agpl.event_queues.calendar.event_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Event_type is private;",
       }   ,
       {
       name: "Object",
       qualified_name: "Agpl.Event_queues.Calendar.Object",
       signature: "agpl.event_queues.calendar.object",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Object (Stack_size : Natural := 64 * 1024) is limited private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Object_access",
       qualified_name: "Agpl.Event_queues.Calendar.Object_access",
       signature: "agpl.event_queues.calendar.object_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Object_access is access all Object;",
       }   ,
   ]
,constants:    [
       {
       name: "End_Of_Time",
       qualified_name: "Agpl.Event_queues.Calendar.End_Of_Time",
       signature: "agpl.event_queues.calendar.end_of_time",
       enclosing: "",
       is_private: false,
       documentation: "Returned by Get_Next_Deadline when no other deadline exists.",
       documentation_snippet: "End_Of_Time : constant Time := Time_Of (Year_Number'Last, 1, 1);",
       }   ,
   ]
,}
---
