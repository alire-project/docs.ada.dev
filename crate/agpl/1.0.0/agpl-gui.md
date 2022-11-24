---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Gui",
qualified_name: "Agpl.Gui",
signature: "agpl.gui",
enclosing: "agpl",
is_private: false,
documentation: "",
documentation_snippet: "",
interface_types:    [
       {
       name: "Event",
       qualified_name: "Agpl.Gui.Event",
       signature: "agpl.gui.event",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Event is interface;",
       }   ,
       {
       name: "Event_Handler",
       qualified_name: "Agpl.Gui.Event_Handler",
       signature: "agpl.gui.event_handler",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Event_Handler is interface;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Clicked",
       qualified_name: "Agpl.Gui.Clicked",
       signature: "agpl.gui.clicked",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Clicked is new Event with record\n   Data_X, Data_Y : Float;\nend record;",
       }   ,
   ]
,}
---
