---
crate: rxada
layout: gnatdoc
gnatdoc: {
name: "Rx",
qualified_name: "Rx",
signature: "rx",
enclosing: "",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Merge_Policies",
       qualified_name: "Rx.Merge_Policies",
       signature: "rx.merge_policies",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum Merge\n  Just relay as they come\n@enum Sequence\n  Force sequencing of observables\n@enum Switch\n  Drop from any previous observable, use only last one",
       documentation_snippet: "type Merge_Policies is\n  (Merge, 	-\n   Sequence,\n   Switch);",
       }   ,
       {
       name: "Rx_Event_Kinds",
       qualified_name: "Rx.Rx_Event_Kinds",
       signature: "rx.rx_event_kinds",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Rx_Event_Kinds is\n  (On_Next,\n   On_Complete,\n   On_Error);",
       }   ,
   ]
,record_types:    [
       {
       name: "Rx_Nothing",
       qualified_name: "Rx.Rx_Nothing",
       signature: "rx.rx_nothing",
       enclosing: "",
       is_private: false,
       documentation: "Some observables are used for notification purposes, with values of no importance",
       documentation_snippet: "type    Rx_Nothing is null record;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Rx_Float",
       qualified_name: "Rx.Rx_Float",
       signature: "rx.rx_float",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Rx_Float   is Long_Long_Float;",
       }   ,
       {
       name: "Rx_Integer",
       qualified_name: "Rx.Rx_Integer",
       signature: "rx.rx_integer",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Rx_Integer  is Long_Long_Integer;",
       }   ,
       {
       name: "Rx_Natural",
       qualified_name: "Rx.Rx_Natural",
       signature: "rx.rx_natural",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Rx_Natural  is Rx_Integer range 0 .. Rx_Integer'Last;",
       }   ,
       {
       name: "Rx_Positive",
       qualified_name: "Rx.Rx_Positive",
       signature: "rx.rx_positive",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Rx_Positive is Rx_Integer range 1 .. Rx_Integer'Last;",
       }   ,
       {
       name: "Rx_String",
       qualified_name: "Rx.Rx_String",
       signature: "rx.rx_string",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Rx_String  is String;",
       }   ,
   ]
,}
---
