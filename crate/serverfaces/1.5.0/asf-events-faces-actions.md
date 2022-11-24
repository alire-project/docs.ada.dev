---
crate: serverfaces
layout: gnatdoc
gnatdoc: {
name: "ASF.Events.Faces.Actions",
qualified_name: "ASF.Events.Faces.Actions",
signature: "asf.events.faces.actions",
enclosing: "asf.events.faces",
is_private: false,
documentation: "---------------------------------------------------------------------\n  asf-events-faces-actions -- Actions Events\n  Copyright (C) 2010, 2011, 2012, 2013 Stephane Carrez\n  Written by Stephane Carrez (Stephane.Carrez@gmail.com)\n\n  Licensed under the Apache License, Version 2.0 (the \"License\");\n  you may not use this file except in compliance with the License.\n  You may obtain a copy of the License at\n\n      http://www.apache.org/licenses/LICENSE-2.0\n\n  Unless required by applicable law or agreed to in writing, software\n  distributed under the License is distributed on an \"AS IS\" BASIS,\n  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n  See the License for the specific language governing permissions and\n  limitations under the License.\n---------------------------------------------------------------------",
documentation_snippet: "",
interface_types:    [
       {
       name: "Action_Listener",
       qualified_name: "ASF.Events.Faces.Actions.Action_Listener",
       signature: "asf.events.faces.actions.action_listener",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Action_Listener is limited interface and Util.Events.Event_Listener;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Action_Event",
       qualified_name: "ASF.Events.Faces.Actions.Action_Event",
       signature: "asf.events.faces.actions.action_event",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Action_Event is new Faces_Event with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Action_Event_Access",
       qualified_name: "ASF.Events.Faces.Actions.Action_Event_Access",
       signature: "asf.events.faces.actions.action_event_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Action_Event_Access is access all Action_Event'Class;",
       }   ,
       {
       name: "Action_Listener_Access",
       qualified_name: "ASF.Events.Faces.Actions.Action_Listener_Access",
       signature: "asf.events.faces.actions.action_listener_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Action_Listener_Access is access all Action_Listener'Class;",
       }   ,
   ]
,}
---
