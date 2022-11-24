---
crate: lace
layout: gnatdoc
gnatdoc: {
name: "lace.Subject_and_instant_Observer",
qualified_name: "lace.Subject_and_instant_Observer",
signature: "lace.subject_and_instant_observer",
enclosing: "lace",
is_private: false,
documentation: "",
documentation_snippet: "",
packages:    [
       {
       name: "Forge",
       qualified_name: "lace.Subject_and_instant_Observer.Forge",
       signature: "lace.subject_and_instant_observer.forge",
       enclosing: "lace.subject_and_instant_observer",
       is_private: false,
       documentation: "",
       documentation_snippet: "",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Item",
       qualified_name: "lace.Subject_and_instant_Observer.Item",
       signature: "lace.subject_and_instant_observer.item",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Item is limited new lace.Any.limited_item\n                     and lace.Subject    .item\n                     and lace.Observer   .item with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "View",
       qualified_name: "lace.Subject_and_instant_Observer.View",
       signature: "lace.subject_and_instant_observer.view",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type View is access all Item'Class;",
       }   ,
   ]
,}
---
