---
crate: ayacc
layout: gnatdoc
gnatdoc: {
name: "Lists",
qualified_name: "Lists",
signature: "lists",
enclosing: "",
is_private: false,
documentation: "| This package provides singly linked lists with elements of type\n| ItemType, where ItemType is specified by a generic parameter.\n\n@formal Itemtype\n  | This is the data being manipulated.\n@formal Equal\n  | This allows the user to define\n  | equality on ItemType.  For instance\n  | if ItemType is an abstract type\n  | then equality is defined in terms of\n  | the abstract type.  If this function\n  | is not provided equality defaults to\n  | =.",
documentation_snippet: "",
simple_types:    [
       {
       name: "List",
       qualified_name: "Lists.List",
       signature: "lists.list",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type List is private;",
       }   ,
       {
       name: "Listiter",
       qualified_name: "Lists.Listiter",
       signature: "lists.listiter",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Listiter is private;",
       }   ,
   ]
,}
---
