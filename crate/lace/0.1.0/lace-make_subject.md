---
crate: lace
layout: gnatdoc
gnatdoc: {
name: "lace.make_Subject",
qualified_name: "lace.make_Subject",
signature: "lace.make_subject",
enclosing: "lace",
is_private: false,
documentation: "",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Item",
       qualified_name: "lace.make_Subject.Item",
       signature: "lace.make_subject.item",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Item is abstract limited new T\n                              and Subject.item with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "View",
       qualified_name: "lace.make_Subject.View",
       signature: "lace.make_subject.view",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type View is access all Item'Class;",
       }   ,
   ]
,}
---
