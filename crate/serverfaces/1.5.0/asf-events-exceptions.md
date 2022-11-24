---
crate: serverfaces
layout: gnatdoc
gnatdoc: {
name: "ASF.Events.Exceptions",
qualified_name: "ASF.Events.Exceptions",
signature: "asf.events.exceptions",
enclosing: "asf.events",
is_private: false,
documentation: "------------------------------\nException event\n------------------------------\nThe <b>Exception_Event</b> represents an exception that is raised while processing\na request.  If is posted by the ASF framework when an unhandled exception is caught.\nAn application can also publish such event when necessary.\n\nAfter each lifecycle phase, the exception handler is invoked to process the\n<b>Exception_Event</b> that have been queued.",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Exception_Event",
       qualified_name: "ASF.Events.Exceptions.Exception_Event",
       signature: "asf.events.exceptions.exception_event",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Exception_Event is new Util.Events.Event with record\n   Ex : Ada.Exceptions.Exception_Occurrence;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Exception_Event_Access",
       qualified_name: "ASF.Events.Exceptions.Exception_Event_Access",
       signature: "asf.events.exceptions.exception_event_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Exception_Event_Access is access all Exception_Event'Class;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Exception_Event_Cursor",
       qualified_name: "ASF.Events.Exceptions.Exception_Event_Cursor",
       signature: "asf.events.exceptions.exception_event_cursor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Exception_Event_Cursor is Event_Vectors.Cursor;",
       }   ,
       {
       name: "Exception_Event_Vector",
       qualified_name: "ASF.Events.Exceptions.Exception_Event_Vector",
       signature: "asf.events.exceptions.exception_event_vector",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Exception_Event_Vector is Event_Vectors.Vector;",
       }   ,
   ]
,}
---
