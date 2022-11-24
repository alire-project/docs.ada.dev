---
crate: lace
layout: gnatdoc
gnatdoc: {
name: "lace.Subject.local",
qualified_name: "lace.Subject.local",
signature: "lace.subject.local",
enclosing: "lace.subject",
is_private: false,
documentation: "",
documentation_snippet: "",
packages:    [
       {
       name: "Forge",
       qualified_name: "lace.Subject.local.Forge",
       signature: "lace.subject.local.forge",
       enclosing: "lace.subject.local",
       is_private: false,
       documentation: "",
       documentation_snippet: "",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Item",
       qualified_name: "lace.Subject.local.Item",
       signature: "lace.subject.local.item",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Item is limited new Any.limited_item\n                     and Subject    .item with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "View",
       qualified_name: "lace.Subject.local.View",
       signature: "lace.subject.local.view",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type View is access all Item'Class;",
       }   ,
   ]
,}
---
