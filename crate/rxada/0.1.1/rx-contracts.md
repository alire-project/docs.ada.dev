---
crate: rxada
layout: gnatdoc
gnatdoc: {
name: "Rx.Contracts",
qualified_name: "Rx.Contracts",
signature: "rx.contracts",
enclosing: "rx",
is_private: false,
documentation: "------------\n Observer --\n------------\n\n@formal T",
documentation_snippet: "",
interface_types:    [
       {
       name: "Observable",
       qualified_name: "Rx.Contracts.Observable",
       signature: "rx.contracts.observable",
       enclosing: "",
       is_private: false,
       documentation: "Someone capable of producing data to which an observer can subscribe",
       documentation_snippet: "type Observable is interface;",
       }   ,
       {
       name: "Observer",
       qualified_name: "Rx.Contracts.Observer",
       signature: "rx.contracts.observer",
       enclosing: "",
       is_private: false,
       documentation: "Someone interested in receiving data",
       documentation_snippet: "type Observer is interface;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Sink",
       qualified_name: "Rx.Contracts.Sink",
       signature: "rx.contracts.sink",
       enclosing: "",
       is_private: false,
       documentation: "A sink is someone who requested a subscription and consumes data,\nas opposed to an operator that passes data along.",
       documentation_snippet: "type Sink is abstract new Observer and Subscribers.Subscriber with private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Subscriber",
       qualified_name: "Rx.Contracts.Subscriber",
       signature: "rx.contracts.subscriber",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Subscriber is Subscribers.Subscriber;",
       }   ,
   ]
,}
---
