---
crate: lace
layout: gnatdoc
gnatdoc: {
name: "lace.Observer",
qualified_name: "lace.Observer",
signature: "lace.observer",
enclosing: "lace",
is_private: false,
documentation: "",
documentation_snippet: "",
array_types:    [
       {
       name: "fast_Views",
       qualified_name: "lace.Observer.fast_Views",
       signature: "lace.observer.fast_views",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type fast_Views is array (Positive range <>) of fast_View;",
       }   ,
       {
       name: "Views",
       qualified_name: "lace.Observer.Views",
       signature: "lace.observer.views",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Views is array (Positive range <>) of View;",
       }   ,
   ]
,interface_types:    [
       {
       name: "Item",
       qualified_name: "lace.Observer.Item",
       signature: "lace.observer.item",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Item  is limited interface;",
       }   ,
   ]
,access_types:    [
       {
       name: "fast_View",
       qualified_name: "lace.Observer.fast_View",
       signature: "lace.observer.fast_view",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type fast_View  is access all Item'Class with Asynchronous;",
       }   ,
       {
       name: "View",
       qualified_name: "lace.Observer.View",
       signature: "lace.observer.view",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type View  is access all Item'Class;",
       }   ,
   ]
,}
---
