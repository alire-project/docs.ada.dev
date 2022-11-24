---
crate: lace
layout: gnatdoc
gnatdoc: {
name: "lace.make_Observer",
qualified_name: "lace.make_Observer",
signature: "lace.make_observer",
enclosing: "lace",
is_private: false,
documentation: "",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Item",
       qualified_name: "lace.make_Observer.Item",
       signature: "lace.make_observer.item",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Item is abstract limited new T\n                              and Observer.item with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "View",
       qualified_name: "lace.make_Observer.View",
       signature: "lace.make_observer.view",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type View is access all Item'Class;",
       }   ,
   ]
,}
---
