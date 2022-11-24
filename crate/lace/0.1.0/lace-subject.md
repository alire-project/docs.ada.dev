---
crate: lace
layout: gnatdoc
gnatdoc: {
name: "lace.Subject",
qualified_name: "lace.Subject",
signature: "lace.subject",
enclosing: "lace",
is_private: false,
documentation: "",
documentation_snippet: "",
array_types:    [
       {
       name: "fast_Views",
       qualified_name: "lace.Subject.fast_Views",
       signature: "lace.subject.fast_views",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type fast_Views is array (Positive range <>) of fast_View;",
       }   ,
       {
       name: "Observer_views",
       qualified_name: "lace.Subject.Observer_views",
       signature: "lace.subject.observer_views",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Observer_views is array (Positive range <>) of Observer.view;",
       }   ,
       {
       name: "Views",
       qualified_name: "lace.Subject.Views",
       signature: "lace.subject.views",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Views is array (Positive range <>) of View;",
       }   ,
   ]
,interface_types:    [
       {
       name: "Item",
       qualified_name: "lace.Subject.Item",
       signature: "lace.subject.item",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Item  is limited interface;",
       }   ,
   ]
,access_types:    [
       {
       name: "fast_View",
       qualified_name: "lace.Subject.fast_View",
       signature: "lace.subject.fast_view",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type fast_View  is access all Item'Class with Asynchronous;",
       }   ,
       {
       name: "View",
       qualified_name: "lace.Subject.View",
       signature: "lace.subject.view",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type View  is access all Item'Class;",
       }   ,
   ]
,}
---
