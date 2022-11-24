---
crate: avrada_rts
layout: gnatdoc
gnatdoc: {
name: "System.Memory",
qualified_name: "System.Memory",
signature: "system.memory",
enclosing: "system",
is_private: false,
documentation: "This unit may be used directly from an application program by providing\nan appropriate WITH, and the interface can be expected to remain stable.",
documentation_snippet: "",
simple_types:    [
       {
       name: "size_t",
       qualified_name: "System.Memory.size_t",
       signature: "system.memory.size_t",
       enclosing: "",
       is_private: false,
       documentation: "Note: the reason we redefine this here instead of using the\ndefinition in Interfaces.C is that we do not want to drag in\nall of Interfaces.C just because System.Memory is used.",
       documentation_snippet: "type size_t is mod 2 ** Standard'Address_Size;",
       }   ,
   ]
,}
---
