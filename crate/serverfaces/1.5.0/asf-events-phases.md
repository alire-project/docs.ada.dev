---
crate: serverfaces
layout: gnatdoc
gnatdoc: {
name: "ASF.Events.Phases",
qualified_name: "ASF.Events.Phases",
signature: "asf.events.phases",
enclosing: "asf.events",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Phase_Type",
       qualified_name: "ASF.Events.Phases.Phase_Type",
       signature: "asf.events.phases.phase_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Phase_Type is (ANY_PHASE,\n                    RESTORE_VIEW,\n                    APPLY_REQUEST_VALUES,\n                    PROCESS_VALIDATION,\n                    UPDATE_MODEL_VALUES,\n                    INVOKE_APPLICATION,\n                    RENDER_RESPONSE);",
       }   ,
   ]
,interface_types:    [
       {
       name: "Phase_Listener",
       qualified_name: "ASF.Events.Phases.Phase_Listener",
       signature: "asf.events.phases.phase_listener",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Phase_Listener is limited interface and Util.Events.Event_Listener;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Phase_Event",
       qualified_name: "ASF.Events.Phases.Phase_Event",
       signature: "asf.events.phases.phase_event",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Phase_Event (Phase : Phase_Type) is new Util.Events.Event with null record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Phase_Listener_Access",
       qualified_name: "ASF.Events.Phases.Phase_Listener_Access",
       signature: "asf.events.phases.phase_listener_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Phase_Listener_Access is access all Phase_Listener'Class;",
       }   ,
   ]
,}
---
