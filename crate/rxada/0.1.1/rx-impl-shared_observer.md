---
crate: rxada
layout: gnatdoc
gnatdoc: {
name: "Rx.Impl.Shared_Observer",
qualified_name: "Rx.Impl.Shared_Observer",
signature: "rx.impl.shared_observer",
enclosing: "rx.impl",
is_private: false,
documentation: "",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Observer",
       qualified_name: "Rx.Impl.Shared_Observer.Observer",
       signature: "rx.impl.shared_observer.observer",
       enclosing: "",
       is_private: false,
       documentation: "In essence this is a carcass for a pointed to observer.\nThis way, both threads using it access the same actual Observer.\nDeallocation is properly done in On_Complete /On_Error",
       documentation_snippet: "type Observer is new Typed.Contracts.Observer with private;",
       }   ,
   ]
,}
---
