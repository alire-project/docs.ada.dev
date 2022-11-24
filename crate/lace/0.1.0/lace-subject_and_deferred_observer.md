---
crate: lace
layout: gnatdoc
gnatdoc: {
name: "lace.Subject_and_deferred_Observer",
qualified_name: "lace.Subject_and_deferred_Observer",
signature: "lace.subject_and_deferred_observer",
enclosing: "lace",
is_private: false,
documentation: "",
documentation_snippet: "",
packages:    [
       {
       name: "Forge",
       qualified_name: "lace.Subject_and_deferred_Observer.Forge",
       signature: "lace.subject_and_deferred_observer.forge",
       enclosing: "lace.subject_and_deferred_observer",
       is_private: false,
       documentation: "",
       documentation_snippet: "",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Item",
       qualified_name: "lace.Subject_and_deferred_Observer.Item",
       signature: "lace.subject_and_deferred_observer.item",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Item is limited new lace.Any.limited_item\n                     and lace.Subject    .item\n                     and lace.Observer   .item with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "View",
       qualified_name: "lace.Subject_and_deferred_Observer.View",
       signature: "lace.subject_and_deferred_observer.view",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type View is access all Item'Class;",
       }   ,
   ]
,}
---
