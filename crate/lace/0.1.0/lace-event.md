---
crate: lace
layout: gnatdoc
gnatdoc: {
name: "lace.Event",
qualified_name: "lace.Event",
signature: "lace.event",
enclosing: "lace",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Kind",
       qualified_name: "lace.Event.Kind",
       signature: "lace.event.kind",
       enclosing: "",
       is_private: false,
       documentation: "\nUniquely identifies each derived event class.\n\nEach derived event class will have its own Kind.\n\nMaps to the extended name of 'ada.Tags.Tag_type' value of each derived\nevent class (see 'Conversions' section in 'lace.Event.utility').",
       documentation_snippet: "type Kind is new String;",
       }   ,
   ]
,record_types:    [
       {
       name: "Item",
       qualified_name: "lace.Event.Item",
       signature: "lace.event.item",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Item is tagged null record;",
       }   ,
   ]
,subtypes:    [
       {
       name: "observer_Name",
       qualified_name: "lace.Event.observer_Name",
       signature: "lace.event.observer_name",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype observer_Name is String;",
       }   ,
       {
       name: "subject_Name",
       qualified_name: "lace.Event.subject_Name",
       signature: "lace.event.subject_name",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype  subject_Name is String;",
       }   ,
   ]
,constants:    [
       {
       name: "null_Event",
       qualified_name: "lace.Event.null_Event",
       signature: "lace.event.null_event",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "null_Event : constant Event.item;",
       }   ,
   ]
,}
---
